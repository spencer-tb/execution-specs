#!/usr/bin/env python3
"""
Patch existing generated test files to add post-state assertions.

Reads each test_*.py file in tests/static/state_tests/, extracts the filler
path from @pytest.mark.ported_from, loads the filler's expect[].result from
git history, and replaces ``post = {}`` with proper Account assertions.

Usage:
    uv run python scripts/patch_post_assertions.py [--dry-run] [--single FILE]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from fixture_to_python import (
    COINBASE_ADDRESS,
    _format_storage_from_result,
    _parse_result_int,
    bytecode_to_op_string,
    format_balance,
    format_int,
    generate_post_value_string,
    load_filler_expect_results,
    load_filler_tx_dimensions,
    post_value_uses_op,
    resolve_expect_for_case,
)

# ---------------------------------------------------------------------------
# Parsing existing test files
# ---------------------------------------------------------------------------

_PORTED_FROM_RE = re.compile(
    r'@pytest\.mark\.ported_from\(\s*\[\s*"([^"]+)"'
)
_ADDR_VAR_RE = re.compile(
    r'^\s+(\w+)\s*=\s*Address\("(0x[0-9a-fA-F]+)"\)', re.MULTILINE
)
_PARAMETRIZE_RE = re.compile(
    r'@pytest\.mark\.parametrize\(\s*\n\s*"([^"]+)"', re.MULTILINE
)


def extract_filler_path(content: str) -> str | None:
    """Extract filler path from @pytest.mark.ported_from."""
    m = _PORTED_FROM_RE.search(content)
    return m.group(1) if m else None


def extract_addr_vars(content: str) -> dict[str, str]:
    """Extract address -> variable name mapping from test file."""
    result: dict[str, str] = {}
    for m in _ADDR_VAR_RE.finditer(content):
        var_name = m.group(1)
        addr = m.group(2).lower()
        result[addr] = var_name
    return result


def is_multi_case(content: str) -> bool:
    """Check if the test is parametrized (multi-case)."""
    return "@pytest.mark.parametrize(" in content


def extract_parametrize_case_count(content: str) -> int:
    """Count the number of parametrize cases."""
    # Find the parametrize values list
    m = re.search(
        r"@pytest\.mark\.parametrize\([^[]*\[\s*(.*?)\s*\],",
        content,
        re.DOTALL,
    )
    if not m:
        return 1
    # Count entries (each non-empty line with a value or pytest.param)
    block = m.group(1)
    # Count lines that start with a value/tuple/pytest.param
    entries = re.findall(r"(?:pytest\.param\(|^\s*\(|^\s*[\"'\d{])", block, re.MULTILINE)
    return max(len(entries), 1)


def extract_param_names(content: str) -> list[str]:
    """Extract parametrize parameter names."""
    m = _PARAMETRIZE_RE.search(content)
    if not m:
        return []
    return [n.strip() for n in m.group(1).split(",")]


# ---------------------------------------------------------------------------
# Post-state generation (reused from fixture_to_python)
# ---------------------------------------------------------------------------


def generate_post_lines(
    result: dict[str, dict],
    addr_vars: dict[str, str],
) -> list[str]:
    """Generate post = {...} lines from filler expect result.

    Returns list of strings (each a complete line).
    """
    lines = ["    post = {"]
    has_entries = False
    for addr, fields in sorted(result.items()):
        if addr.lower() == COINBASE_ADDRESS:
            continue
        var = addr_vars.get(addr.lower(), f'Address("{addr}")')

        if "shouldnotexist" in fields:
            lines.append(f"        {var}: Account.NONEXISTENT,")
            has_entries = True
            continue

        parts = []
        if "storage" in fields:
            parts.append(
                f"storage={_format_storage_from_result(fields['storage'])}"
            )
        if "nonce" in fields:
            parts.append(f"nonce={_parse_result_int(fields['nonce'])}")
        if "balance" in fields:
            val = _parse_result_int(fields["balance"])
            parts.append(f"balance={format_balance(val)}")
        if "code" in fields:
            code_hex = str(fields["code"])
            if code_hex in ("0x", ""):
                parts.append('code=b""')
            else:
                op_str = bytecode_to_op_string(code_hex)
                if op_str is not None:
                    parts.append(f"code={op_str}")
                else:
                    raw = code_hex[2:] if code_hex.startswith("0x") else code_hex
                    parts.append(f'code=bytes.fromhex("{raw}")')

        if parts:
            parts_str = ", ".join(parts)
            single = f"        {var}: Account({parts_str}),"
            if len(single) <= 100 and "\n" not in parts_str:
                lines.append(single)
            else:
                lines.append(f"        {var}: Account(")
                for p in parts:
                    lines.append(f"            {p},")
                lines.append("        ),")
            has_entries = True
    lines.append("    }")
    if not has_entries:
        return ["    post = {}"]
    return lines


# ---------------------------------------------------------------------------
# Multi-case handling
# ---------------------------------------------------------------------------


def case_index_to_dgv(
    i: int,
    num_data: int,
    num_gas: int,
    num_value: int,
) -> tuple[int, int, int]:
    """Map flat case index to (d, g, v) using fixture compiler ordering.

    Ordering: data outermost, gas middle, value innermost.
    """
    d = i // (num_gas * num_value)
    g = (i // num_value) % num_gas
    v = i % num_value
    return (d, g, v)


def compute_multi_case_post(
    expect_entries: list[dict],
    num_cases: int,
    addr_vars: dict[str, str],
    dimensions: tuple[int, int, int] | None = None,
) -> tuple[str, list[str] | None, str | None, str | None]:
    """Compute post assertion strategy for multi-case tests.

    Returns:
        (post_type, expected_storages, storage_var, storage_addr)
        post_type: "shared" | "parametrize" | "fallback"
    """
    # Check if all entries share same result or use wildcard indexes
    all_results = [e.get("result", {}) for e in expect_entries]
    all_same = len(all_results) > 0 and all(
        r == all_results[0] for r in all_results
    )
    all_wildcard = all(
        e.get("indexes", {}).get("data", -1) == -1
        and e.get("indexes", {}).get("gas", -1) == -1
        and e.get("indexes", {}).get("value", -1) == -1
        for e in expect_entries
    )

    if (all_same or all_wildcard) and all_results:
        return "shared", None, None, None

    # Determine dimensions for d,g,v mapping
    if dimensions is None:
        dims = (num_cases, 1, 1)  # Assume data-only
    else:
        nd, ng, nv = dimensions
        if nd * ng * nv == num_cases:
            dims = dimensions
        else:
            dims = (num_cases, 1, 1)  # Fallback

    # Check if only storage differs per case
    only_storage = True
    case_results: list[dict | None] = []
    for i in range(num_cases):
        d, g, v = case_index_to_dgv(i, *dims)
        r = resolve_expect_for_case(expect_entries, d, g, v)
        case_results.append(r)
        if r:
            for a, fields in r.items():
                if a.lower() == COINBASE_ADDRESS:
                    continue
                non_storage = {
                    k for k in fields
                    if k != "storage" and not k.startswith("//")
                }
                if non_storage:
                    only_storage = False

    if only_storage and any(case_results):
        storage_addr = None
        expected_storages: list[str] = []
        for r in case_results:
            if r is None:
                expected_storages.append("{}")
                continue
            found = False
            for a, fields in r.items():
                if a.lower() == COINBASE_ADDRESS:
                    continue
                if "storage" in fields:
                    storage_addr = a
                    expected_storages.append(
                        _format_storage_from_result(fields["storage"])
                    )
                    found = True
                    break
            if not found:
                expected_storages.append("{}")

        if storage_addr:
            storage_var = addr_vars.get(
                storage_addr.lower(),
                f'Address("{storage_addr}")',
            )
            return "parametrize", expected_storages, storage_var, storage_addr

    # Non-storage divergence: parametrize the full post dict
    if any(case_results):
        post_values = [
            generate_post_value_string(r) for r in case_results
        ]
        return "full_post", post_values, None, None

    return "fallback", None, None, None


# ---------------------------------------------------------------------------
# Patching
# ---------------------------------------------------------------------------


def patch_test_file(test_path: Path, dry_run: bool = False) -> str:
    """Patch a single test file. Returns status message."""
    content = test_path.read_text()

    # Skip if already has post assertions
    if "post = {}" not in content:
        return "SKIP (already has post)"

    # Extract filler path
    filler_rel = extract_filler_path(content)
    if not filler_rel:
        return "SKIP (no ported_from marker)"

    filler_path = Path(filler_rel)

    # Load expect results from filler (git history)
    expect_entries = load_filler_expect_results(filler_path)
    if not expect_entries:
        return "SKIP (no expect entries in filler)"

    # Extract address variable mapping
    addr_vars = extract_addr_vars(content)

    multi = is_multi_case(content)

    if not multi:
        # Single-case: use first (and only) expect entry
        result = resolve_expect_for_case(expect_entries, 0, 0, 0)
        if not result:
            return "SKIP (no matching expect for d0g0v0)"

        post_lines = generate_post_lines(result, addr_vars)
        new_post = "\n".join(post_lines)

        if new_post.strip() == "post = {}":
            return "SKIP (post would still be empty after filtering)"

        new_content = content.replace("    post = {}", new_post, 1)

        if not dry_run:
            test_path.write_text(new_content)
        return "PATCHED"

    else:
        # Multi-case test
        num_cases = extract_parametrize_case_count(content)
        dimensions = load_filler_tx_dimensions(filler_path)
        post_type, extra, storage_var, _ = compute_multi_case_post(
            expect_entries, num_cases, addr_vars,
            dimensions=dimensions,
        )

        if post_type == "shared":
            # All cases share same result
            all_results = [e.get("result", {}) for e in expect_entries]
            post_lines = generate_post_lines(all_results[0], addr_vars)
            new_post = "\n".join(post_lines)
            if new_post.strip() == "post = {}":
                return "SKIP (post would still be empty after filtering)"
            new_content = content.replace("    post = {}", new_post, 1)
            if not dry_run:
                test_path.write_text(new_content)
            return "PATCHED (shared post)"

        elif post_type == "parametrize" and extra and storage_var:
            # Need to add expected_storage to parametrize and function sig
            new_content = _inject_expected_storage(
                content, extra, storage_var,
            )
            if new_content is None:
                return "SKIP (could not inject parametrize)"
            if not dry_run:
                test_path.write_text(new_content)
            return "PATCHED (parametrized storage)"

        elif post_type == "full_post" and extra:
            # Parametrize the full post dict
            new_content = _inject_expected_post(content, extra)
            if new_content is None:
                return "SKIP (could not inject full post)"
            # Add Op import if any post value uses Op
            if any(post_value_uses_op(v) for v in extra):
                if "from execution_testing.vm import Op" not in new_content:
                    new_content = new_content.replace(
                        "from execution_testing import (",
                        "from execution_testing.vm import Op\n"
                        "from execution_testing import (",
                        1,
                    )
            if not dry_run:
                test_path.write_text(new_content)
            return "PATCHED (parametrized post)"

        else:
            return "SKIP (multi-case with complex divergence)"


def _inject_expected_storage(
    content: str,
    expected_storages: list[str],
    storage_var: str,
) -> str | None:
    """Inject expected_storage into parametrize decorator and function signature.

    Returns patched content, or None if unable to patch.
    """
    lines = content.split("\n")
    new_lines: list[str] = []
    i = 0

    param_names_injected = False
    in_values_list = False  # True when between [ and ] of parametrize values
    bracket_depth = 0
    value_index = 0
    values_done = False
    func_sig_injected = False
    post_injected = False

    while i < len(lines):
        line = lines[i]

        # Step 1: Find @pytest.mark.parametrize( and inject param name
        if not param_names_injected and "@pytest.mark.parametrize(" in line:
            new_lines.append(line)
            i += 1
            # Next line should be the "param_names" string
            if i < len(lines):
                name_line = lines[i]
                name_match = re.match(r'^(\s*)"(.+)",$', name_line)
                if name_match:
                    indent = name_match.group(1)
                    existing = name_match.group(2)
                    new_lines.append(
                        f'{indent}"{existing}, expected_storage",'
                    )
                    param_names_injected = True
                    i += 1
                    continue
                else:
                    new_lines.append(name_line)
                    i += 1
            continue

        # Step 2: Track the values list [ ... ] after param names injected
        if param_names_injected and not values_done:
            stripped = line.strip()

            # Detect start of values list
            if not in_values_list and stripped == "[":
                in_values_list = True
                bracket_depth = 1
                new_lines.append(line)
                i += 1
                continue

            if in_values_list:
                # Track bracket depth
                bracket_depth += line.count("[") - line.count("]")

                if bracket_depth <= 0:
                    # End of values list
                    in_values_list = False
                    values_done = True
                    new_lines.append(line)
                    i += 1
                    continue

                # Inside the values list — augment each entry
                storage = (
                    expected_storages[value_index]
                    if value_index < len(expected_storages)
                    else "{}"
                )

                # pytest.param(...),
                param_match = re.match(
                    r'^(\s*)pytest\.param\((.+)\),$', line
                )
                if param_match:
                    indent = param_match.group(1)
                    inner = param_match.group(2)
                    id_match = re.search(r',\s*(id=.*)$', inner)
                    if id_match:
                        vals_part = inner[: id_match.start()]
                        suffix = id_match.group(1)
                        new_lines.append(
                            f"{indent}pytest.param("
                            f"{vals_part}, {storage}, {suffix}),"
                        )
                    else:
                        new_lines.append(
                            f"{indent}pytest.param("
                            f"{inner}, {storage}),"
                        )
                    value_index += 1
                    i += 1
                    continue

                # Tuple: (val1, val2),
                tuple_match = re.match(r'^(\s*)\((.+)\),$', line)
                if tuple_match:
                    indent = tuple_match.group(1)
                    vals = tuple_match.group(2)
                    new_lines.append(f"{indent}({vals}, {storage}),")
                    value_index += 1
                    i += 1
                    continue

                # Bare value: indented, not a bracket/ids/comment
                if (
                    stripped.endswith(",")
                    and not stripped.startswith(("[", "]", "#"))
                    and "ids=" not in stripped
                ):
                    indent = line[: len(line) - len(line.lstrip())]
                    val = stripped.rstrip(",")
                    new_lines.append(f"{indent}({val}, {storage}),")
                    value_index += 1
                    i += 1
                    continue

        # Step 3: Inject expected_storage into function signature
        if not func_sig_injected and re.match(r"^\) -> None:", line):
            new_lines.append("    expected_storage: dict,")
            func_sig_injected = True

        # Step 4: Replace post = {} with post using expected_storage
        if not post_injected and line.strip() == "post = {}":
            new_lines.append(f"    post = {{")
            new_lines.append(
                f"        {storage_var}: Account("
                f"storage=expected_storage),"
            )
            new_lines.append(f"    }}")
            post_injected = True
            i += 1
            continue

        new_lines.append(line)
        i += 1

    if not post_injected:
        return None

    return "\n".join(new_lines)


def _parse_parametrize_block(lines: list[str], start: int) -> tuple[
    int, int, str, list[str], int, int
] | None:
    """Parse a @pytest.mark.parametrize(...) block.

    Return (param_line_start, param_line_end, names_str,
            value_lines, values_start, values_end)
    or None on failure.  value_lines are the raw lines between [ and ].
    """
    # `start` is the line with @pytest.mark.parametrize(
    # Track paren depth to find the end of the decorator
    paren_depth = 0
    block_end = start
    for j in range(start, len(lines)):
        paren_depth += lines[j].count("(") - lines[j].count(")")
        if paren_depth <= 0:
            block_end = j
            break

    # Find the param names string (first quoted string after parametrize)
    names_str = None
    names_line = None
    for j in range(start, block_end + 1):
        m = re.search(r'"([^"]+)"', lines[j])
        if m:
            names_str = m.group(1)
            names_line = j
            break

    if names_str is None or names_line is None:
        return None

    # Find the [ ... ] values block
    bracket_start = None
    bracket_end = None
    depth = 0
    for j in range(names_line, block_end + 1):
        for ci, ch in enumerate(lines[j]):
            if ch == "[":
                if depth == 0:
                    bracket_start = j
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    bracket_end = j
                    break
        if bracket_end is not None:
            break

    if bracket_start is None or bracket_end is None:
        return None

    return (
        start,
        block_end,
        names_str,
        lines[bracket_start:bracket_end + 1],
        bracket_start,
        bracket_end,
    )


def _parse_parametrize_values(
    value_lines: list[str],
) -> list[tuple[str, str | None, str | None]]:
    """Parse individual entries from parametrize values list.

    Return list of (original_values, id_str_or_None, marks_str_or_None).
    Each entry is the raw text of the value (without wrapping pytest.param).
    """
    # Join into single string for easier parsing
    block = "\n".join(value_lines)
    # Remove outer [ ] (and any trailing comma/whitespace outside them)
    inner = block.strip()
    # Strip leading [
    if inner.startswith("["):
        inner = inner[1:]
    # Strip trailing ] and any comma after it
    inner = inner.rstrip()
    if inner.endswith("],"):
        inner = inner[:-2]
    elif inner.endswith("]"):
        inner = inner[:-1]

    entries: list[tuple[str, str | None, str | None]] = []
    # Split by top-level commas (respecting nesting)
    current: list[str] = []
    depth = 0
    for ch in inner:
        if ch in ("(", "[", "{"):
            depth += 1
            current.append(ch)
        elif ch in (")", "]", "}"):
            depth -= 1
            current.append(ch)
        elif ch == "," and depth == 0:
            piece = "".join(current).strip()
            if piece:
                entries.append(_parse_single_entry(piece))
            current = []
        else:
            current.append(ch)
    piece = "".join(current).strip()
    if piece:
        entries.append(_parse_single_entry(piece))

    return entries


def _parse_single_entry(
    text: str,
) -> tuple[str, str | None, str | None]:
    """Parse a single parametrize entry.

    Return (values_str, id_str_or_None, marks_str_or_None).
    """
    text = text.strip()

    # pytest.param(vals..., id="...", marks=...)
    if text.startswith("pytest.param(") and text.endswith(")"):
        inner = text[len("pytest.param("):-1]
        # Extract id= and marks= kwargs from the end
        id_str = None
        marks_str = None

        # Find kwargs by scanning from right, respecting nesting
        # We need to split positional args from kwargs
        parts = _split_top_level(inner, ",")
        val_parts: list[str] = []
        for p in parts:
            p_stripped = p.strip()
            if p_stripped.startswith("id="):
                id_str = p_stripped[3:]
            elif p_stripped.startswith("marks="):
                marks_str = p_stripped[6:]
            else:
                val_parts.append(p.strip())

        vals = ", ".join(val_parts)
        return (vals, id_str, marks_str)

    # Tuple: (val1, val2)
    if text.startswith("(") and text.endswith(")"):
        return (text[1:-1].strip(), None, None)

    # Bare value
    return (text, None, None)


def _split_top_level(text: str, sep: str) -> list[str]:
    """Split text by sep at top nesting level only."""
    parts: list[str] = []
    current: list[str] = []
    depth = 0
    for ch in text:
        if ch in ("(", "[", "{"):
            depth += 1
            current.append(ch)
        elif ch in (")", "]", "}"):
            depth -= 1
            current.append(ch)
        elif ch == sep and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    rest = "".join(current)
    if rest.strip():
        parts.append(rest)
    return parts


def _inject_expected_post(
    content: str,
    post_values: list[str],
) -> str | None:
    """Inject expected_post into parametrize and function signature.

    Handles bare-value, tuple, and pytest.param formats.
    Rebuilds entries as pytest.param(original_vals..., {post}, id="caseN")
    preserving any marks= kwargs.

    Return patched content, or None if unable to patch.
    """
    lines = content.split("\n")

    # Find @pytest.mark.parametrize line
    param_start = None
    for i, line in enumerate(lines):
        if "@pytest.mark.parametrize(" in line:
            param_start = i
            break

    if param_start is None:
        return None

    parsed = _parse_parametrize_block(lines, param_start)
    if parsed is None:
        return None

    (
        _block_start,
        block_end,
        names_str,
        value_lines,
        values_start,
        values_end,
    ) = parsed

    # Parse entries
    entries = _parse_parametrize_values(value_lines)
    if not entries:
        return None

    # Build new parametrize block
    new_names = names_str + ", expected_post"

    # Find the ids= line if present (between ] and the closing paren)
    ids_str = None
    for j in range(values_end, block_end + 1):
        m = re.search(r"ids=(\[[^\]]*\])", lines[j])
        if m:
            ids_str = m.group(1)
            break

    # Determine indent from the original @pytest.mark.parametrize line
    orig_param_line = lines[param_start]
    base_indent = orig_param_line[
        : len(orig_param_line) - len(orig_param_line.lstrip())
    ]
    val_indent = base_indent + "    "

    # Build new entry lines
    new_entry_lines: list[str] = []
    for idx, entry in enumerate(entries):
        vals, entry_id, marks = entry
        post = (
            post_values[idx]
            if idx < len(post_values)
            else "{}"
        )

        # Determine the id
        if entry_id is not None:
            id_part = f"id={entry_id}"
        else:
            id_part = f'id="case{idx}"'

        # Build the pytest.param line
        if marks:
            suffix = f"{id_part}, marks={marks}"
        else:
            suffix = id_part

        param_inner = f"{vals}, {post}, {suffix}"
        single_line = (
            f"{val_indent}pytest.param({param_inner}),"
        )

        if len(single_line) <= 99:
            new_entry_lines.append(single_line)
        else:
            # Multi-line format
            new_entry_lines.append(
                f"{val_indent}pytest.param("
            )
            new_entry_lines.append(
                f"{val_indent}    {vals},"
            )
            new_entry_lines.append(
                f"{val_indent}    {post},"
            )
            if marks:
                new_entry_lines.append(
                    f"{val_indent}    {id_part},"
                )
                new_entry_lines.append(
                    f"{val_indent}    marks={marks},"
                )
            else:
                new_entry_lines.append(
                    f"{val_indent}    {id_part},"
                )
            new_entry_lines.append(f"{val_indent}),")

    # Rebuild the full parametrize decorator
    new_block: list[str] = [
        f"{base_indent}@pytest.mark.parametrize(",
        f'{val_indent}"{new_names}",',
        f"{val_indent}[",
    ]
    new_block.extend(new_entry_lines)
    new_block.append(f"{val_indent}],")
    new_block.append(f"{base_indent})")

    # Replace old block (from param_start to block_end)
    result_lines = lines[:param_start] + new_block + lines[block_end + 1:]

    # Now inject expected_post into function signature
    result = "\n".join(result_lines)

    # Add expected_post param before `) -> None:`
    result = re.sub(
        r"^(\) -> None:)",
        "    expected_post: dict,\n\\1",
        result,
        count=1,
        flags=re.MULTILINE,
    )

    # Replace `post = {}` with `post = expected_post`
    result = result.replace("    post = {}", "    post = expected_post", 1)

    if "post = expected_post" not in result:
        return None

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Patch generated tests with post-state assertions."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't write changes, just report what would be done",
    )
    parser.add_argument(
        "--single",
        type=Path,
        default=None,
        help="Patch a single test file",
    )
    parser.add_argument(
        "--dir",
        type=Path,
        default=Path("tests/static/state_tests"),
        help="Directory to scan for test files",
    )
    args = parser.parse_args()

    if args.single:
        files = [args.single]
    else:
        files = sorted(args.dir.rglob("test_*.py"))

    stats: dict[str, int] = {}
    for test_path in files:
        result = patch_test_file(test_path, dry_run=args.dry_run)
        tag = result.split(" (")[0]  # e.g. "PATCHED" or "SKIP"
        stats[tag] = stats.get(tag, 0) + 1
        if not result.startswith("SKIP"):
            prefix = "DRY " if args.dry_run else ""
            print(f"  {prefix}{result}: {test_path}")

    print(f"\n{'=' * 60}")
    print("Summary")
    print(f"{'=' * 60}")
    print(f"Total files:  {len(files)}")
    for tag, count in sorted(stats.items()):
        print(f"  {tag}: {count}")


if __name__ == "__main__":
    main()
