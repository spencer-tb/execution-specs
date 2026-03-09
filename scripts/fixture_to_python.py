#!/usr/bin/env python3
"""
Convert compiled state_test fixtures to Python test files.

Reads compiled fixture JSON (from --fill-static-tests) and source filler
(for _info.comment), then generates a Python test file with:
- Module docstring from _info.comment
- Op-language bytecode (readable, self-documenting)
- Proper pytest markers and structure
- Maximum embedded context for future Amsterdam porting

Usage:
    python scripts/fixture_to_python.py \
        --fixtures /tmp/compiled_static/ \
        --fillers tests/static/state_tests/ \
        --output tests/ported_static/
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Fork ordering (earliest to latest)
# ---------------------------------------------------------------------------

FORK_ORDER = [
    "Frontier",
    "Homestead",
    "EIP150",
    "EIP158",
    "Byzantium",
    "Constantinople",
    "ConstantinopleFix",
    "Istanbul",
    "Berlin",
    "London",
    "Paris",
    "Shanghai",
    "Cancun",
    "Prague",
    "Osaka",
]
FORK_RANK = {name: i for i, name in enumerate(FORK_ORDER)}


def earliest_fork(forks: set[str]) -> str:
    """Return the earliest fork from a set, by FORK_ORDER."""
    known = [f for f in forks if f in FORK_RANK]
    if not known:
        return sorted(forks)[0]  # fallback alphabetical
    return min(known, key=lambda f: FORK_RANK[f])


def fork_before(fork_name: str) -> str | None:
    """Return the fork immediately before the given fork in FORK_ORDER."""
    if fork_name not in FORK_RANK:
        return None
    idx = FORK_RANK[fork_name]
    if idx <= 0:
        return None
    return FORK_ORDER[idx - 1]


def parse_network_upper_bound(network_str: str) -> str | None:
    """
    Parse the upper fork bound from a network string.

    Examples:
        ">=Cancun"       -> None (no upper bound)
        ">=Cancun<Osaka" -> "Osaka" (exclusive upper bound)
        "Cancun"         -> None (exact fork)
    """
    match = re.search(r"<(\w+)$", network_str.strip())
    if match:
        return match.group(1)
    return None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case, preserving leading numbers."""
    # Insert _ before uppercase letters preceded by lowercase or digits
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    # Insert _ before uppercase letters followed by lowercase (e.g. ABCDef -> ABC_Def)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return s.lower()


def filler_name_to_test_name(filler_stem: str) -> str:
    """Convert filler stem to Python test function/file name.

    e.g. 'callcode_checkPCFiller' -> 'test_callcode_check_pc'
    e.g. 'ContractCreationSpamFiller' -> 'test_contract_creation_spam'
    """
    # Strip 'Filler' suffix
    name = re.sub(r"Filler$", "", filler_stem)
    result = "test_" + camel_to_snake(name)
    # Replace hyphens and other invalid chars with underscores
    result = re.sub(r"[^a-z0-9_]", "_", result)
    # Collapse multiple underscores
    result = re.sub(r"_+", "_", result)
    return result.strip("_")


def hex_to_int(v: str) -> int:
    """Convert hex string to int."""
    return int(v, 16)


def format_int(v: int, *, force_hex: bool = False) -> str:
    """Format an int as Python literal. Use hex for large values."""
    if force_hex or v > 0xFFFF:
        return hex(v)
    return str(v)


def format_balance(v: int) -> str:
    """Format balance as Python literal."""
    return format_int(v, force_hex=(v > 9999))


def format_storage(storage: dict[str, str]) -> str:
    """Format storage dict as Python literal."""
    if not storage:
        return "{}"
    items = []
    for k, v in sorted(storage.items(), key=lambda x: int(x[0], 16)):
        items.append(f"{hex(int(k, 16))}: {hex(int(v, 16))}")
    return "{" + ", ".join(items) + "}"


def _format_exception(exc_str: str) -> str:
    """Format an expectException string as Python code.

    Single: 'TransactionException.FOO' -> 'TransactionException.FOO'
    Compound: 'TransactionException.FOO|TransactionException.BAR'
        -> '[TransactionException.FOO, TransactionException.BAR]'
    """
    parts = [p.strip() for p in exc_str.split("|")]
    if len(parts) == 1:
        return parts[0]
    return "[" + ", ".join(parts) + "]"


def _format_access_list(al: list[dict[str, Any]]) -> str:
    """Format an access list as Python code."""
    if not al:
        return "[]"
    items = []
    for entry in al:
        addr = entry["address"]
        keys = entry.get("storageKeys", [])
        if keys:
            key_strs = ", ".join(f'Hash("{k}")' for k in keys)
            items.append(
                f'AccessList(address=Address("{addr}"), storage_keys=[{key_strs}])'
            )
        else:
            items.append(
                f'AccessList(address=Address("{addr}"), storage_keys=[])'
            )
    if len(items) == 1:
        return f"[{items[0]}]"
    inner = ",\n            ".join(items)
    return f"[\n            {inner},\n        ]"


def bytecode_to_op_string(hex_code: str) -> str | None:
    """Convert hex bytecode to Op expression string.

    Returns None if bytecode is empty, conversion fails, or roundtrip
    produces different bytecode (evm_bytes has edge cases with PUSH parsing).
    """
    if hex_code in ("0x", "0x00", ""):
        return None

    raw = hex_code[2:] if hex_code.startswith("0x") else hex_code

    try:
        from execution_testing.cli.evm_bytes import process_evm_bytes_string
        from execution_testing.vm import Op  # noqa: F811

        op_str = process_evm_bytes_string(raw, assembly=False)
        # Verify roundtrip: compile Op back to hex and compare
        compiled = eval(op_str)  # noqa: S307
        if compiled.hex() != raw.lower():
            return None  # Roundtrip mismatch — fall back to bytes.fromhex
        return op_str
    except Exception:
        return None


def bytecode_to_assembly_summary(
    hex_code: str, max_lines: int = 20
) -> str | None:
    """Get a short assembly summary of bytecode for docstrings."""
    if hex_code in ("0x", "0x00", ""):
        return None

    raw = hex_code[2:] if hex_code.startswith("0x") else hex_code

    try:
        from execution_testing.cli.evm_bytes import process_evm_bytes_string

        asm = process_evm_bytes_string(raw, assembly=True)
        lines = [l for l in asm.split("\n") if l.strip()]
        if len(lines) <= max_lines:
            return "\n".join(lines)
        return (
            "\n".join(lines[:max_lines])
            + f"\n... ({len(lines) - max_lines} more instructions)"
        )
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Filler context extraction
# ---------------------------------------------------------------------------

# Git ref that contains the original filler files (before they were replaced
# with auto-ported Python tests).
_FILLER_GIT_REF = "b0e75de2a~1"


def _load_filler_data(filler_path: Path) -> dict | None:
    """Load and parse a filler file (JSON or YAML).

    Try the on-disk path first.  If the file doesn't exist (fillers were
    deleted), fall back to ``git show <ref>:<relative_path>``.
    Returns the parsed dict, or None on failure.
    """
    raw: str | None = None
    suffix = filler_path.suffix

    # Check on-disk: try both the path as-is and relative to repo root
    repo_root: Path | None = None
    try:
        repo_root = Path(
            subprocess.check_output(
                ["git", "rev-parse", "--show-toplevel"],
                stderr=subprocess.DEVNULL,
            )
            .decode()
            .strip()
        )
    except (subprocess.CalledProcessError, OSError):
        pass

    if filler_path.exists():
        raw = filler_path.read_text()
    elif repo_root and (repo_root / filler_path).exists():
        raw = (repo_root / filler_path).read_text()
    else:
        # Extract from git history — filler_path is repo-root-relative
        # (e.g. "tests/static/state_tests/stExample/add11Filler.json")
        try:
            # Use as-is first (works when path is already repo-relative)
            raw = subprocess.check_output(
                ["git", "show", f"{_FILLER_GIT_REF}:{filler_path}"],
                stderr=subprocess.DEVNULL,
                cwd=repo_root,
            ).decode()
        except (subprocess.CalledProcessError, OSError):
            return None

    if raw is None:
        return None

    try:
        if suffix == ".json":
            return json.loads(raw)
        elif suffix in (".yml", ".yaml"):
            try:
                import yaml

                return yaml.safe_load(raw)
            except ImportError:
                return None
        return None
    except Exception:
        return None


def load_filler_comment(filler_path: Path) -> str:
    """Extract _info.comment from a filler file."""
    data = _load_filler_data(filler_path)
    if not data:
        return ""
    try:
        for test_name, test_data in data.items():
            if isinstance(test_data, dict) and "_info" in test_data:
                comment = test_data["_info"].get("comment", "")
                if comment:
                    return comment
    except Exception:
        pass
    return ""


def load_filler_network_upper_bound(filler_path: Path) -> str | None:
    """Extract the strictest upper fork bound from a filler's network fields.

    Parses expect[].network entries like ">=Cancun<Osaka" and returns the
    excluded fork name (e.g. "Osaka").  Returns None if no upper bound.
    """
    data = _load_filler_data(filler_path)
    if not data:
        return None
    try:
        upper_bounds: list[str] = []
        all_exact_forks: list[str] = []
        has_range = False
        for _test_name, test_data in data.items():
            if not isinstance(test_data, dict):
                continue
            expect = test_data.get("expect", [])
            if not isinstance(expect, list):
                continue
            for expect_entry in expect:
                if not isinstance(expect_entry, dict):
                    continue
                network = expect_entry.get("network", [])
                if isinstance(network, list):
                    for net_str in network:
                        s = str(net_str).strip()
                        bound = parse_network_upper_bound(s)
                        if bound:
                            upper_bounds.append(bound)
                            has_range = True
                        elif ">=" in s:
                            has_range = True
                        elif s in FORK_RANK:
                            all_exact_forks.append(s)

        # Range syntax like ">=Cancun<Osaka" — return the excluded fork
        if upper_bounds:
            known = [b for b in upper_bounds if b in FORK_RANK]
            if known:
                return min(known, key=lambda f: FORK_RANK[f])
            return upper_bounds[0]

        # Exact fork names only (e.g. ["Cancun", "Prague"]) — the fork
        # after the latest listed fork is the excluded upper bound
        if all_exact_forks and not has_range:
            latest = max(all_exact_forks, key=lambda f: FORK_RANK[f])
            latest_idx = FORK_RANK[latest]
            if latest_idx + 1 < len(FORK_ORDER):
                return FORK_ORDER[latest_idx + 1]

        return None
    except Exception:
        return None


COINBASE_ADDRESS = "0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba"

# Regex to strip YAML label syntax:
#   <contract:target:0xADDR> -> 0xADDR  (3-part)
#   <eoa:0xADDR> -> 0xADDR              (2-part)
_LABEL_RE = re.compile(r"<[^>]*?(0x[0-9a-fA-F]+)>")


def _strip_label(s: str) -> str:
    """Strip YAML label syntax, returning just the address."""
    m = _LABEL_RE.match(s.strip())
    if m:
        return m.group(1).lower()
    return s.strip().lower()


def _normalize_address(addr: str) -> str:
    """Normalize an address to lowercase with 0x prefix."""
    addr = _strip_label(addr)
    if not addr.startswith("0x"):
        addr = "0x" + addr
    return addr.lower()


def load_filler_expect_results(filler_path: Path) -> list[dict]:
    """Load expect entries from a filler file.

    Return list of dicts with keys:
        indexes: {"data": ..., "gas": ..., "value": ...}
        result: {address: {field: value, ...}, ...}
    """
    data = _load_filler_data(filler_path)
    if not data:
        return []
    try:
        for _test_name, test_data in data.items():
            if not isinstance(test_data, dict):
                continue
            expect = test_data.get("expect", [])
            if not isinstance(expect, list):
                continue

            entries = []
            for expect_entry in expect:
                if not isinstance(expect_entry, dict):
                    continue
                raw_indexes = expect_entry.get("indexes", {})
                raw_result = expect_entry.get("result", {})

                # Strip // prefixed keys (JSON comment hack)
                indexes = {
                    k: v
                    for k, v in raw_indexes.items()
                    if not str(k).startswith("//")
                }
                result: dict[str, dict] = {}
                for addr_key, fields in raw_result.items():
                    if str(addr_key).startswith("//"):
                        continue
                    if not isinstance(fields, dict):
                        continue
                    norm_addr = _normalize_address(str(addr_key))
                    # Strip // prefixed field keys
                    clean_fields = {
                        k: v
                        for k, v in fields.items()
                        if not str(k).startswith("//")
                    }
                    if clean_fields:
                        result[norm_addr] = clean_fields

                entries.append(
                    {
                        "indexes": indexes,
                        "result": result,
                    }
                )
            return entries
        return []
    except Exception:
        return []


def load_filler_tx_dimensions(
    filler_path: Path,
) -> tuple[int, int, int] | None:
    """Load transaction dimensions (data, gas, value) from a filler.

    Return (num_data, num_gas, num_value) or None on failure.
    """
    data = _load_filler_data(filler_path)
    if not data:
        return None
    try:
        for _test_name, test_data in data.items():
            if not isinstance(test_data, dict):
                continue
            tx = test_data.get("transaction", {})
            if not isinstance(tx, dict):
                continue
            num_data = len(tx.get("data", [""]))
            num_gas = len(tx.get("gasLimit", [""]))
            num_value = len(tx.get("value", [""]))
            return (num_data, num_gas, num_value)
        return None
    except Exception:
        return None


def _index_matches(selector: Any, case_idx: int) -> bool:
    """Check if an index selector matches a specific case index.

    Selector can be:
    - -1: matches any index
    - int: matches that exact index
    - list: matches if case_idx is in the list (items can be ints or ranges)
    - str range "0-2": matches 0, 1, 2
    - str label ":label ...": treated as matching the index position
    """
    if isinstance(selector, int):
        return selector == -1 or selector == case_idx
    if isinstance(selector, str):
        s = selector.strip()
        # Range like "0-2"
        range_match = re.match(r"^(\d+)-(\d+)$", s)
        if range_match:
            lo, hi = int(range_match.group(1)), int(range_match.group(2))
            return lo <= case_idx <= hi
        # Label syntax — can't resolve without the data array, treat as match
        if s.startswith(":label"):
            return True
        # Try as integer
        try:
            return int(s) == case_idx
        except ValueError:
            return True  # Unknown format, be permissive
    if isinstance(selector, list):
        return any(_index_matches(item, case_idx) for item in selector)
    return True  # Unknown type, be permissive


def resolve_expect_for_case(
    expect_entries: list[dict],
    data_idx: int,
    gas_idx: int,
    value_idx: int,
) -> dict | None:
    """Find the expect entry whose indexes match the given case."""
    for entry in expect_entries:
        indexes = entry.get("indexes", {})
        d_sel = indexes.get("data", -1)
        g_sel = indexes.get("gas", -1)
        v_sel = indexes.get("value", -1)
        if (
            _index_matches(d_sel, data_idx)
            and _index_matches(g_sel, gas_idx)
            and _index_matches(v_sel, value_idx)
        ):
            return entry.get("result")
    return None


def extract_case_indices(fixture_key: str) -> tuple[int, int, int]:
    """Extract (data_idx, gas_idx, value_idx) from fixture key.

    Key format: "tests/.../XFiller.json::TestName[d0g0v0-Cancun]"
    """
    m = re.search(r"\[d(\d+)g(\d+)v(\d+)-", fixture_key)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3))
    return 0, 0, 0


# ---------------------------------------------------------------------------
# Code generation
# ---------------------------------------------------------------------------


def generate_code_expr(
    hex_code: str, indent: str = "        "
) -> tuple[str, str]:
    """Generate Python code expression for bytecode.

    Returns (code_expr, pre_comment) where:
    - code_expr is the Python expression (Op chain or bytes.fromhex fallback)
    - pre_comment is always empty (kept for API compatibility)
    """
    if hex_code in ("0x", ""):
        return 'b""', ""

    raw = hex_code[2:] if hex_code.startswith("0x") else hex_code

    # Always use Op format — readable and round-trips to identical bytecode
    op_str = bytecode_to_op_string(hex_code)
    if op_str is not None:
        # Wrap long Op chains
        if len(op_str) > 80:
            parts = op_str.split(" + ")
            lines = []
            current_line = parts[0]
            for part in parts[1:]:
                if len(current_line) + len(part) + 3 > 76:
                    lines.append(current_line)
                    current_line = part
                else:
                    current_line += " + " + part
            lines.append(current_line)

            joined = ("\n" + indent + "+ ").join(lines)
            return f"(\n{indent}{joined}\n{indent[4:]})", ""
        return op_str, ""

    # bytes.fromhex fallback only if Op conversion fails entirely
    if len(raw) > 72:
        chunks = [raw[i : i + 72] for i in range(0, len(raw), 72)]
        if len(chunks) == 1:
            return f'bytes.fromhex(\n{indent}"{chunks[0]}"\n{indent[4:]})', ""
        hex_lines = f'"\n{indent}"'.join(chunks)
        return f'bytes.fromhex(\n{indent}"{hex_lines}"\n{indent[4:]})', ""

    return f'bytes.fromhex("{raw}")', ""


def generate_account_setup(
    address: str,
    account: dict[str, Any],
    var_name: str,
    indent: str = "    ",
) -> str:
    """Generate pre[addr] = Account(...) code."""
    lines = []
    code_hex = account.get("code", "0x")
    balance = hex_to_int(account.get("balance", "0x00"))
    nonce = hex_to_int(account.get("nonce", "0x00"))
    storage = account.get("storage", {})

    # Determine if this is an EOA (no code) or contract
    is_eoa = code_hex in ("0x", "")

    parts = []
    parts.append(f"balance={format_balance(balance)}")
    parts.append(f"nonce={nonce}")

    if not is_eoa:
        code_expr, code_comment = generate_code_expr(
            code_hex, indent=indent + "    "
        )
        if code_comment:
            lines.append(code_comment.rstrip())
        parts.append(f"code={code_expr}")

    if storage:
        parts.append(f"storage={format_storage(storage)}")

    # Format as single line or multi-line
    single = f"{indent}pre[{var_name}] = Account({', '.join(parts)})"
    if len(single) <= 100 and "\n" not in "".join(parts):
        lines.append(single)
    else:
        lines.append(f"{indent}pre[{var_name}] = Account(")
        for i, part in enumerate(parts):
            comma = ","
            lines.append(f"{indent}    {part}{comma}")
        lines.append(f"{indent})")

    return "\n".join(lines)


def _parse_result_int(v: Any) -> int:
    """Parse an int from a filler result value (may be str, int, hex)."""
    if isinstance(v, int):
        return v
    s = str(v).strip()
    if not s or s in ("0x", "0X"):
        return 0
    # YAML label syntax: <contract:name:0xADDR> or <contract:name>
    if s.startswith("<") and ":" in s:
        m = re.search(r"(0x[0-9a-fA-F]+)", s)
        if m:
            return int(m.group(1), 16)
        return 0
    if s.startswith("0x") or s.startswith("0X"):
        return int(s, 16)
    try:
        return int(s)
    except ValueError:
        return 0


def _format_storage_from_result(storage: dict) -> str:
    """Format storage dict from filler result (keys/values may be various formats)."""
    if not storage:
        return "{}"
    items = []
    for k, v in sorted(storage.items(), key=lambda x: _parse_result_int(x[0])):
        key_int = _parse_result_int(k)
        val_int = _parse_result_int(v)
        items.append(f"{format_int(key_int)}: {format_int(val_int)}")
    return "{" + ", ".join(items) + "}"


def generate_post_dict(
    result: dict[str, dict],
    addr_vars: dict[str, str],
) -> str:
    """Generate the post = {...} dict from filler expect result.

    Handle all 5 field types: storage, nonce, balance, code, shouldnotexist.
    Skip coinbase address.
    """
    lines = ["    post = {"]
    has_entries = False
    for addr, fields in sorted(result.items()):
        # Skip coinbase
        if addr.lower() == COINBASE_ADDRESS:
            continue
        padded = _pad_address(addr)
        var = addr_vars.get(addr.lower(), f'Address("{padded}")')

        # shouldnotexist
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
                    raw = (
                        code_hex[2:] if code_hex.startswith("0x") else code_hex
                    )
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
        return "    post = {}"
    return "\n".join(lines)


def _pad_address(addr: str) -> str:
    """Pad a short hex address to 40 hex chars (20 bytes)."""
    raw = addr[2:] if addr.startswith("0x") else addr
    if len(raw) < 40:
        raw = raw.zfill(40)
    return "0x" + raw


def generate_post_value_string(result: dict | None) -> str:
    """Generate a post dict expression for use in parametrize values.

    Use Address("0x...") literals (not variable names) since parametrize
    evaluates at module import time.  Return "{}" for None/empty results.
    """
    if not result:
        return "{}"
    parts: list[str] = []
    for addr, fields in sorted(result.items()):
        if addr.lower() == COINBASE_ADDRESS:
            continue

        # Skip unresolved Yul/label addresses
        if "<" in addr:
            continue

        padded = _pad_address(addr)

        if "shouldnotexist" in fields:
            parts.append(
                f'Address("{padded}"): Account.NONEXISTENT'
            )
            continue

        acct_parts: list[str] = []
        if "storage" in fields:
            acct_parts.append(
                f"storage="
                f"{_format_storage_from_result(fields['storage'])}"
            )
        if "nonce" in fields:
            acct_parts.append(
                f"nonce={_parse_result_int(fields['nonce'])}"
            )
        if "balance" in fields:
            val = _parse_result_int(fields["balance"])
            acct_parts.append(f"balance={format_balance(val)}")
        if "code" in fields:
            code_hex = str(fields["code"])
            if "<" in code_hex:
                pass  # Skip unresolved label references
            elif code_hex in ("0x", ""):
                acct_parts.append('code=b""')
            else:
                op_str = bytecode_to_op_string(code_hex)
                if op_str is not None:
                    acct_parts.append(f"code={op_str}")
                else:
                    raw = (
                        code_hex[2:]
                        if code_hex.startswith("0x")
                        else code_hex
                    )
                    acct_parts.append(
                        f'code=bytes.fromhex("{raw}")'
                    )

        if acct_parts:
            acct_str = ", ".join(acct_parts)
            parts.append(
                f'Address("{padded}"): Account({acct_str})'
            )

    if not parts:
        return "{}"
    if len(parts) == 1:
        return "{" + parts[0] + "}"
    inner = ", ".join(parts)
    return "{" + inner + "}"


def _generate_post_from_fixture_state(
    post_state: dict[str, dict],
    addr_vars: dict[str, str],
) -> str:
    """Generate the post = {...} dict from compiled fixture post state.

    The fixture post state format is:
        {address: {balance: "0x...", nonce: "0x...", code: "0x...",
                   storage: {key: value}}}

    Only assert on storage and code (not balance/nonce) since those
    depend on gas costs which vary across forks.
    Skip coinbase and accounts with no interesting assertions.
    """
    lines = ["    post = {"]
    has_entries = False
    for addr, fields in sorted(post_state.items()):
        addr_l = addr.lower()
        # Skip coinbase
        if addr_l == COINBASE_ADDRESS:
            continue
        padded = _pad_address(addr_l)
        var = addr_vars.get(padded, f'Address("{padded}")')

        parts = []
        if "storage" in fields and fields["storage"]:
            parts.append(
                f"storage="
                f"{_format_storage_from_result(fields['storage'])}"
            )
        if "code" in fields:
            code_hex = str(fields["code"])
            if code_hex not in ("0x", ""):
                op_str = bytecode_to_op_string(code_hex)
                if op_str is not None:
                    parts.append(f"code={op_str}")
                else:
                    raw = (
                        code_hex[2:]
                        if code_hex.startswith("0x")
                        else code_hex
                    )
                    parts.append(f'code=bytes.fromhex("{raw}")')

        if parts:
            parts_str = ", ".join(parts)
            single = f"        {var}: Account({parts_str}),"
            if len(single) <= 100 and "\n" not in parts_str:
                lines.append(single)
            else:
                lines.append(f"        {var}: Account(")
                for j, p in enumerate(parts):
                    comma = "," if j < len(parts) - 1 else ","
                    lines.append(f"            {p}{comma}")
                lines.append("        ),")
            has_entries = True

    lines.append("    }")
    if not has_entries:
        return "    post = {}"
    return "\n".join(lines)


def _generate_post_value_from_fixture_state(
    post_state: dict[str, dict],
) -> str:
    """Generate a post dict expression from fixture state for parametrize.

    Use Address("0x...") literals (not variable names).
    Only assert on storage and code (not balance/nonce).
    Return "{}" for empty state.
    """
    if not post_state:
        return "{}"
    parts: list[str] = []
    for addr, fields in sorted(post_state.items()):
        addr_l = addr.lower()
        if addr_l == COINBASE_ADDRESS:
            continue
        padded = _pad_address(addr_l)

        acct_parts: list[str] = []
        if "storage" in fields and fields["storage"]:
            acct_parts.append(
                f"storage="
                f"{_format_storage_from_result(fields['storage'])}"
            )
        if "code" in fields:
            code_hex = str(fields["code"])
            if code_hex not in ("0x", ""):
                op_str = bytecode_to_op_string(code_hex)
                if op_str is not None:
                    acct_parts.append(f"code={op_str}")
                else:
                    raw = (
                        code_hex[2:]
                        if code_hex.startswith("0x")
                        else code_hex
                    )
                    acct_parts.append(
                        f'code=bytes.fromhex("{raw}")'
                    )

        if acct_parts:
            acct_str = ", ".join(acct_parts)
            parts.append(
                f'Address("{padded}"): Account({acct_str})'
            )

    if not parts:
        return "{}"
    if len(parts) == 1:
        return "{" + parts[0] + "}"
    inner = ", ".join(parts)
    return "{" + inner + "}"


def post_value_uses_op(post_str: str) -> bool:
    """Check whether a post value string references Op."""
    return "Op." in post_str


def generate_test_file(
    fixture_data: dict[str, Any],
    filler_path: str,
    filler_comment: str,
    valid_until: str | None = None,
    filler_full_path: Path | None = None,
) -> str:
    """Generate a complete Python test file from fixture data."""
    # Compiled fixtures have one top-level key per (case × fork).
    # Collect all forks, find the earliest, then collect cases for that fork.
    all_keys = list(fixture_data.keys())
    first_test = fixture_data[all_keys[0]]

    env = first_test["env"]
    pre = first_test["pre"]

    # Detect all forks present across all entries
    all_forks: set[str] = set()
    for key in all_keys:
        test = fixture_data[key]
        all_forks.update(test["post"].keys())
    fork_name = earliest_fork(all_forks)

    # Collect all cases for this fork
    cases_for_fork: list[dict[str, Any]] = []
    for key in all_keys:
        test = fixture_data[key]
        if fork_name in test["post"]:
            tx = test["transaction"]
            post_entry = test["post"][fork_name][0]
            post_state = post_entry.get("state", {})
            expect_exception = post_entry.get("expectException")
            # accessLists is a list of access lists (one per case index)
            access_lists = tx.get("accessLists", [])
            al = (
                access_lists[0] if access_lists else None
            )  # None = no access list
            cases_for_fork.append(
                {
                    "data": tx["data"][0] if tx["data"] else "0x",
                    "gas_limit": hex_to_int(tx["gasLimit"][0])
                    if tx["gasLimit"]
                    else 100000,
                    "value": hex_to_int(tx["value"][0]) if tx["value"] else 0,
                    "access_list": al,
                    "expect_exception": expect_exception,
                    "post_state": post_state,
                }
            )

    is_multi = len(cases_for_fork) > 1

    # Use first case's tx for shared fields (secret_key, to, gas_price, nonce)
    tx = first_test["transaction"]

    # Determine test name
    filler_stem = Path(filler_path).stem  # e.g. "callcode_checkPCFiller"
    test_func_name = filler_name_to_test_name(filler_stem)

    # Identify accounts
    sender_addr = tx.get("sender", "").lower()
    to_addr = (tx.get("to") or "").lower()
    coinbase_addr = env.get("currentCoinbase", "").lower()

    # Build address variable mapping
    addr_vars: dict[str, str] = {}
    var_names: list[tuple[str, str, str]] = []  # (addr, var_name, display)

    # Always add coinbase
    if coinbase_addr:
        addr_vars[coinbase_addr] = "coinbase"
        var_names.append((coinbase_addr, "coinbase", coinbase_addr))

    # Add sender
    if sender_addr:
        addr_vars[sender_addr] = "sender"
        var_names.append((sender_addr, "sender", sender_addr))

    # Reserve "contract" for the to_addr first
    if to_addr and to_addr not in addr_vars:
        addr_vars[to_addr] = "contract"
        var_names.append((to_addr, "contract", to_addr))

    # Add other accounts with unique names
    contract_idx = 0
    for addr in sorted(pre.keys()):
        addr_l = addr.lower()
        if addr_l in addr_vars:
            continue
        if contract_idx == 0 and "contract" not in addr_vars.values():
            name = "contract"
        else:
            name = f"callee_{contract_idx}" if contract_idx > 0 else "callee"
        addr_vars[addr_l] = name
        var_names.append((addr_l, name, addr_l))
        contract_idx += 1

    # Module docstring
    doc_lines = []
    if filler_comment:
        doc_lines.append(filler_comment)
        doc_lines.append("")
    doc_lines.append("Ported from:")
    doc_lines.append(filler_path)

    # Add assembly summaries for contracts
    for addr in sorted(pre.keys()):
        addr_l = addr.lower()
        code_hex = pre[addr].get("code", "0x")
        if code_hex in ("0x", ""):
            continue
        var = addr_vars.get(addr_l, addr)
        asm = bytecode_to_assembly_summary(code_hex)
        if asm:
            doc_lines.append("")
            doc_lines.append(f"{var} code:")
            for line in asm.split("\n"):
                doc_lines.append(f"    {line}")

    module_doc = '"""\n' + "\n".join(doc_lines) + '\n"""'

    # Check if we need Op import
    needs_op = False
    for addr in pre:
        code_hex = pre[addr].get("code", "0x")
        if (
            code_hex not in ("0x", "")
            and bytecode_to_op_string(code_hex) is not None
        ):
            needs_op = True
            break

    # Check if we need AccessList import
    needs_access_list = any(
        c["access_list"] is not None for c in cases_for_fork
    )
    # Check if we need TransactionException import
    needs_tx_exception = any(c.get("expect_exception") for c in cases_for_fork)

    # Build imports
    imports = [
        "import pytest",
        "from execution_testing import (",
    ]
    if needs_access_list:
        imports.append("    AccessList,")
    imports.extend(
        [
            "    Account,",
            "    Address,",
            "    Alloc,",
            "    Environment,",
            "    Hash,",
            "    StateTestFiller,",
            "    Transaction,",
        ]
    )
    if needs_tx_exception:
        imports.append("    TransactionException,")
    imports.append(")")
    if needs_op:
        imports.append("from execution_testing.vm import Op")

    # Build env
    env_parts = []
    env_parts.append("fee_recipient=coinbase")

    num = hex_to_int(env.get("currentNumber", "0x01"))
    env_parts.append(f"number={num}")

    ts = hex_to_int(env.get("currentTimestamp", "0x03e8"))
    env_parts.append(f"timestamp={ts}")

    diff = hex_to_int(env.get("currentDifficulty", "0x00"))
    if diff > 0:
        env_parts.append(f"difficulty={hex(diff)}")

    randao = hex_to_int(env.get("currentRandom", "0x00"))
    if randao > 0:
        env_parts.append(f"prev_randao={hex(randao)}")

    base_fee = hex_to_int(env.get("currentBaseFee", "0x0a"))
    if base_fee > 0:
        env_parts.append(f"base_fee_per_gas={base_fee}")

    excess_blob = hex_to_int(env.get("currentExcessBlobGas", "0x00"))
    if excess_blob > 0:
        env_parts.append(f"excess_blob_gas={excess_blob}")

    # Include gas_limit from original fixture for hasher match.
    # Amsterdam update (commit 2) will remove this to get framework default 100M.
    block_gas_limit = hex_to_int(env.get("currentGasLimit", "0x05f5e100"))
    env_parts.append(f"gas_limit={block_gas_limit}")

    # Detect which tx params vary across cases
    if is_multi:
        all_data = [c["data"] for c in cases_for_fork]
        all_gas = [c["gas_limit"] for c in cases_for_fork]
        all_val = [c["value"] for c in cases_for_fork]
        all_al = [
            json.dumps(c["access_list"], sort_keys=True)
            for c in cases_for_fork
        ]
        all_exc = [c.get("expect_exception") or "" for c in cases_for_fork]
        data_varies = len(set(all_data)) > 1
        gas_varies = len(set(all_gas)) > 1
        value_varies = len(set(all_val)) > 1
        al_varies = len(set(all_al)) > 1
        exc_varies = len(set(all_exc)) > 1

    # Build tx
    tx_parts = []
    tx_parts.append(
        f'secret_key=Hash(\n            "0x{tx["secretKey"][2:]}"\n        )'
    )

    if to_addr:
        tx_parts.append(
            f"to={addr_vars.get(to_addr, f'Address({chr(34)}{to_addr}{chr(34)})')}"
        )
    else:
        tx_parts.append("to=None")

    # For single-case, use values directly
    if not is_multi:
        case = cases_for_fork[0]
        data_hex = case["data"]
        data_raw = data_hex[2:] if data_hex.startswith("0x") else data_hex
        if data_raw:
            if len(data_raw) > 72:
                chunks = [
                    data_raw[i : i + 72] for i in range(0, len(data_raw), 72)
                ]
                hex_joined = '"\n            "'.join(chunks)
                tx_parts.append(
                    f'data=bytes.fromhex(\n            "{hex_joined}"\n        )'
                )
            else:
                tx_parts.append(f'data=bytes.fromhex("{data_raw}")')
        else:
            tx_parts.append('data=b""')
        tx_parts.append(f"gas_limit={case['gas_limit']}")
    else:
        if data_varies:
            tx_parts.append("data=tx_data")
        else:
            data_hex = cases_for_fork[0]["data"]
            data_raw = data_hex[2:] if data_hex.startswith("0x") else data_hex
            if data_raw:
                tx_parts.append(f'data=bytes.fromhex("{data_raw}")')
            else:
                tx_parts.append('data=b""')
        if gas_varies:
            tx_parts.append("gas_limit=tx_gas_limit")
        else:
            tx_parts.append(f"gas_limit={cases_for_fork[0]['gas_limit']}")

    gas_price = tx.get("gasPrice")
    max_fee = tx.get("maxFeePerGas")
    max_priority = tx.get("maxPriorityFeePerGas")
    max_fee_blob = tx.get("maxFeePerBlobGas")
    blob_hashes = tx.get("blobVersionedHashes")

    if max_fee:
        tx_parts.append(f"max_fee_per_gas={hex_to_int(max_fee)}")
        if max_priority:
            tx_parts.append(
                f"max_priority_fee_per_gas={hex_to_int(max_priority)}"
            )
    elif gas_price:
        tx_parts.append(f"gas_price={hex_to_int(gas_price)}")

    if max_fee_blob:
        tx_parts.append(f"max_fee_per_blob_gas={hex_to_int(max_fee_blob)}")
    if blob_hashes is not None:
        if blob_hashes:
            hash_strs = ", ".join(f'Hash("{h}")' for h in blob_hashes)
            tx_parts.append(f"blob_versioned_hashes=[{hash_strs}]")
        else:
            tx_parts.append("blob_versioned_hashes=[]")

    tx_nonce = hex_to_int(tx.get("nonce", "0x00"))
    tx_parts.append(f"nonce={tx_nonce}")

    if not is_multi:
        tx_parts.append(f"value={cases_for_fork[0]['value']}")
        # Access list for single case
        al = cases_for_fork[0]["access_list"]
        if al is not None:
            tx_parts.append(f"access_list={_format_access_list(al)}")
    elif value_varies:
        tx_parts.append("value=tx_value")
    else:
        tx_parts.append(f"value={cases_for_fork[0]['value']}")

    # Access list for multi-case
    if is_multi:
        if al_varies:
            tx_parts.append("access_list=tx_access_list")
        else:
            al = cases_for_fork[0]["access_list"]
            if al is not None:
                tx_parts.append(f"access_list={_format_access_list(al)}")

    # Expected transaction error (e.g. blob tx with to=None)
    if is_multi and exc_varies:
        tx_parts.append("error=tx_error")
    else:
        expect_exception = cases_for_fork[0].get("expect_exception")
        if expect_exception:
            tx_parts.append(f"error={_format_exception(expect_exception)}")

    # -----------------------------------------------------------------------
    # Compute post-state assertions from compiled fixture post state
    # -----------------------------------------------------------------------
    post_code = "    post = {}"
    extra_param_name: str | None = None  # e.g. "expected_storage"
    extra_param_vals: list[str] = []  # per-case values
    extra_func_param: str | None = None  # e.g. "    expected_storage: dict,"

    if not is_multi:
        # Single-case: use compiled fixture's post state directly
        ps = cases_for_fork[0].get("post_state", {})
        if ps:
            post_code = _generate_post_from_fixture_state(
                ps, addr_vars
            )
    else:
        # Multi-case: check if all post states are identical
        all_post_states = [
            c.get("post_state", {}) for c in cases_for_fork
        ]
        all_same = len(all_post_states) > 0 and all(
            ps == all_post_states[0] for ps in all_post_states
        )

        if all_same and all_post_states[0]:
            post_code = _generate_post_from_fixture_state(
                all_post_states[0], addr_vars
            )
        elif any(all_post_states):
            extra_param_name = "expected_post"
            extra_func_param = "    expected_post: dict,"
            for ps in all_post_states:
                extra_param_vals.append(
                    _generate_post_value_from_fixture_state(ps)
                )
            post_code = "    post = expected_post"

    # Check if post assertions use Op (needs import)
    if "Op." in post_code:
        needs_op = True
    if any(post_value_uses_op(v) for v in extra_param_vals):
        needs_op = True
    # Add Op import if detected after initial import build
    op_import = "from execution_testing.vm import Op"
    if needs_op and op_import not in imports:
        imports.append(op_import)

    # -----------------------------------------------------------------------
    # Assemble the file
    # -----------------------------------------------------------------------
    out = []
    out.append(module_doc)
    out.append("")
    out.extend(imports)
    out.append("")
    out.append('REFERENCE_SPEC_GIT_PATH = "N/A"')
    out.append('REFERENCE_SPEC_VERSION = "N/A"')
    out.append("")

    # Parametrize for multi-case
    if is_multi:
        # Build parameter names and values based on what varies
        param_names = []
        if data_varies:
            param_names.append("tx_data_hex")
        if gas_varies:
            param_names.append("tx_gas_limit")
        if value_varies:
            param_names.append("tx_value")
        if al_varies:
            param_names.append("tx_access_list")
        if exc_varies:
            param_names.append("tx_error")
        if extra_param_name:
            param_names.append(extra_param_name)

        out.append("")
        out.append("@pytest.mark.ported_from(")
        out.append(f'    ["{filler_path}"],')
        out.append(")")
        out.append(f'@pytest.mark.valid_from("{fork_name}")')
        if valid_until:
            out.append(f'@pytest.mark.valid_until("{valid_until}")')

        # Build parametrize values
        param_vals = []
        param_ids = []
        case_has_exc = []
        for i, case in enumerate(cases_for_fork):
            vals = []
            if data_varies:
                data_raw = (
                    case["data"][2:]
                    if case["data"].startswith("0x")
                    else case["data"]
                )
                vals.append(f'"{data_raw}"')
            if gas_varies:
                vals.append(str(case["gas_limit"]))
            if value_varies:
                vals.append(str(case["value"]))
            if al_varies:
                al = case["access_list"]
                if al is None:
                    vals.append("None")
                else:
                    vals.append(_format_access_list(al))
            if exc_varies:
                exc = case.get("expect_exception") or ""
                if exc:
                    vals.append(_format_exception(exc))
                    case_has_exc.append(True)
                else:
                    vals.append("None")
                    case_has_exc.append(False)
            else:
                case_has_exc.append(False)
            if extra_param_vals:
                vals.append(
                    extra_param_vals[i] if i < len(extra_param_vals) else "{}"
                )
            param_vals.append(vals)
            param_ids.append(f"case{i}")

        if exc_varies:
            # Use pytest.param for individual entries (each needs its own id + maybe marks)
            out.append(f"@pytest.mark.parametrize(")
            out.append(f'    "{", ".join(param_names)}",')
            out.append(f"    [")
            for i, (vals, has_exc) in enumerate(zip(param_vals, case_has_exc)):
                if has_exc:
                    entry = f'pytest.param({", ".join(vals)}, id="{param_ids[i]}", marks=pytest.mark.exception_test)'
                elif len(vals) == 1:
                    entry = f'pytest.param({vals[0]}, id="{param_ids[i]}")'
                else:
                    entry = (
                        f'pytest.param({", ".join(vals)}, id="{param_ids[i]}")'
                    )
                out.append(f"        {entry},")
            out.append(f"    ],")
            out.append(f")")
        elif len(param_names) == 1:
            out.append(f"@pytest.mark.parametrize(")
            out.append(f'    "{param_names[0]}",')
            out.append(f"    [")
            for i, vals in enumerate(param_vals):
                out.append(f"        {vals[0]},")
            out.append(f"    ],")
            out.append(f"    ids={param_ids},")
            out.append(f")")
        else:
            out.append(f"@pytest.mark.parametrize(")
            out.append(f'    "{", ".join(param_names)}",')
            out.append(f"    [")
            for i, vals in enumerate(param_vals):
                out.append(f"        ({', '.join(vals)}),")
            out.append(f"    ],")
            out.append(f"    ids={param_ids},")
            out.append(f")")
    else:
        out.append("")
        out.append("@pytest.mark.ported_from(")
        out.append(f'    ["{filler_path}"],')
        out.append(")")
        out.append(f'@pytest.mark.valid_from("{fork_name}")')
        if valid_until:
            out.append(f'@pytest.mark.valid_until("{valid_until}")')

    # pre_alloc_mutable since generated tests assign pre[addr] = Account(...)
    out.append("@pytest.mark.pre_alloc_mutable")

    # Add exception_test marker if ALL cases expect transaction failure
    # (when exc_varies, some cases succeed so the global marker can't be used)
    if needs_tx_exception and not (is_multi and exc_varies):
        out.append("@pytest.mark.exception_test")

    # Function signature
    func_params = ["    state_test: StateTestFiller,", "    pre: Alloc,"]
    if is_multi:
        if data_varies:
            func_params.append("    tx_data_hex: str,")
        if gas_varies:
            func_params.append("    tx_gas_limit: int,")
        if value_varies:
            func_params.append("    tx_value: int,")
        if al_varies:
            func_params.append("    tx_access_list,")
        if exc_varies:
            func_params.append("    tx_error,")
        if extra_func_param:
            func_params.append(extra_func_param)
    out.append(f"def {test_func_name}(")
    out.extend(func_params)
    out.append(") -> None:")

    # Function docstring
    if filler_comment:
        out.append(f'    """{filler_comment}."""')
    else:
        out.append(f'    """Test ported from static filler."""')

    # Address variables
    for addr, var, _ in var_names:
        out.append(f'    {var} = Address("{addr}")')
    out.append("")

    # Environment
    out.append("    env = Environment(")
    for p in env_parts:
        out.append(f"        {p},")
    out.append("    )")
    out.append("")

    # Pre-state accounts
    for addr in sorted(pre.keys()):
        addr_l = addr.lower()
        var = addr_vars.get(addr_l, f'Address("{addr}")')
        account_code = generate_account_setup(
            addr, pre[addr], var, indent="    "
        )
        out.append(account_code)

    out.append("")

    # Multi-case tx data conversion
    if is_multi and data_varies:
        out.append(
            '    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""'
        )
        out.append("")

    # Transaction
    out.append("    tx = Transaction(")
    for p in tx_parts:
        out.append(f"        {p},")
    out.append("    )")
    out.append("")

    # Post state assertions
    out.append(post_code)

    out.append("")
    out.append("    state_test(env=env, pre=pre, post=post, tx=tx)")
    out.append("")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def find_fixture_files(fixtures_dir: Path) -> list[Path]:
    """Find all state_test fixture JSON files."""
    results = []
    for p in fixtures_dir.rglob("*.json"):
        if ".meta" not in p.parts:
            results.append(p)
    return sorted(results)


def fixture_to_filler_path(fixture_data: dict) -> str | None:
    """Extract the filler path from a fixture's test key."""
    for key in fixture_data:
        # Key format: "tests/static/state_tests/.../XFiller.json::TestName[...]"
        if "::" in key:
            return key.split("::")[0]
    return None


def process_single_fixture(
    fixture_path: Path,
    fillers_dir: Path,
    output_dir: Path,
) -> tuple[bool, str]:
    """Process a single fixture file. Returns (success, message)."""
    with open(fixture_path) as f:
        fixture_data = json.load(f)

    filler_path = fixture_to_filler_path(fixture_data)
    if not filler_path:
        return False, f"Could not extract filler path from {fixture_path}"

    # Load filler comment
    filler_full_path = fillers_dir.parent.parent / filler_path
    if not filler_full_path.exists():
        # Try relative to repo root
        filler_full_path = Path(filler_path)
    filler_comment = load_filler_comment(filler_full_path)

    # Detect fork upper bound from filler's network field (e.g. ">=Cancun<Osaka")
    upper_bound = load_filler_network_upper_bound(filler_full_path)
    valid_until = fork_before(upper_bound) if upper_bound else None

    # Generate Python test
    try:
        python_code = generate_test_file(
            fixture_data,
            filler_path,
            filler_comment,
            valid_until=valid_until,
            filler_full_path=filler_full_path,
        )
    except Exception as e:
        return False, f"Error generating {fixture_path}: {e}"

    # Determine output path
    filler_stem = Path(filler_path).stem  # e.g. "callcode_checkPCFiller"
    test_name = filler_name_to_test_name(filler_stem)

    # Extract category from filler path
    # e.g. tests/static/state_tests/stCallCodes/... -> stCallCodes
    filler_parts = Path(filler_path).parts
    # Find the part after "state_tests"
    category = ""
    for i, part in enumerate(filler_parts):
        if part == "state_tests" and i + 1 < len(filler_parts):
            # If there's a subfolder (e.g. Cancun/stEIP...), include it
            remaining = filler_parts[i + 1 : -1]
            category = str(Path(*remaining)) if remaining else ""
            break

    out_dir = output_dir / category if category else output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    # Write __init__.py if needed
    init_file = out_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("")

    out_file = out_dir / f"{test_name}.py"
    out_file.write_text(python_code)

    return True, f"Generated {out_file}"


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Convert compiled state_test fixtures to Python test files."
    )
    parser.add_argument(
        "--fixtures",
        type=Path,
        required=True,
        help="Path to compiled fixture directory (from --fill-static-tests)",
    )
    parser.add_argument(
        "--fillers",
        type=Path,
        required=True,
        help="Path to source filler directory (tests/static/state_tests/)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for generated Python tests",
    )
    parser.add_argument(
        "--single",
        type=Path,
        default=None,
        help="Process a single fixture file (for testing)",
    )
    parser.add_argument(
        "--filter",
        type=Path,
        default=None,
        help="Only convert fixtures whose filler path is in this file (one per line)",
    )
    args = parser.parse_args()

    # Load filter list if provided
    filter_set: set[str] | None = None
    if args.filter:
        with open(args.filter) as f:
            filter_set = {line.strip() for line in f if line.strip()}

    if args.single:
        files = [args.single]
    else:
        files = find_fixture_files(args.fixtures)

    # Filter fixtures to only those matching the filter list
    if filter_set is not None:
        filtered = []
        for fp in files:
            with open(fp) as f:
                data = json.load(f)
            filler_path = fixture_to_filler_path(data)
            if filler_path and filler_path in filter_set:
                filtered.append(fp)
        print(
            f"Filtered: {len(filtered)}/{len(files)} fixtures match filter list"
        )
        files = filtered

    if not files:
        print("No fixture files found.")
        sys.exit(1)

    args.output.mkdir(parents=True, exist_ok=True)

    success_count = 0
    fail_count = 0
    for fixture_path in files:
        ok, msg = process_single_fixture(
            fixture_path, args.fillers, args.output
        )
        if ok:
            success_count += 1
            print(f"  OK: {msg}")
        else:
            fail_count += 1
            print(f"FAIL: {msg}", file=sys.stderr)

    print(f"\nDone: {success_count} generated, {fail_count} failed")
    if fail_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
