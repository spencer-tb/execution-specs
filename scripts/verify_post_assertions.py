#!/usr/bin/env python3
"""
Verify that generated test files contain proper post-state assertions.

Reads each source filler and its corresponding generated test file, then
verifies that assertion fields from the filler's expect[].result were
translated into the generated test.

Usage:
    python scripts/verify_post_assertions.py \
        --fillers /path/to/fillers/ \
        --generated tests/static/state_tests/
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from fixture_to_python import (
    COINBASE_ADDRESS,
    filler_name_to_test_name,
    load_filler_expect_results,
)


def find_generated_test(generated_dir: Path, filler_path: Path) -> Path | None:
    """Find the generated test file corresponding to a filler."""
    stem = filler_path.stem  # e.g. "add11Filler"
    test_name = filler_name_to_test_name(stem)
    # Walk generated_dir to find the test file
    for p in generated_dir.rglob(f"{test_name}.py"):
        return p
    return None


def check_post_assertions(
    test_content: str,
    expect_results: list[dict],
) -> tuple[int, int, list[str]]:
    """Check if post assertions exist in the test file.

    Return (expected_count, found_count, missing_descriptions).
    """
    expected = 0
    found = 0
    missing: list[str] = []

    # Collect all addresses and their fields across all expect entries
    all_fields: dict[str, set[str]] = {}
    for entry in expect_results:
        result = entry.get("result", {})
        for addr, fields in result.items():
            if addr.lower() == COINBASE_ADDRESS:
                continue
            if addr.lower() not in all_fields:
                all_fields[addr.lower()] = set()
            for field_name in fields:
                if field_name.startswith("//"):
                    continue
                all_fields[addr.lower()].add(field_name)

    has_post_empty = "post = {}" in test_content
    has_post_dict = re.search(r"post\s*=\s*\{[^}]", test_content) is not None
    has_expected_storage = "expected_storage" in test_content

    for addr, fields in all_fields.items():
        for field in fields:
            expected += 1

            if field == "shouldnotexist":
                if "Account.NONEXISTENT" in test_content:
                    found += 1
                elif has_post_empty:
                    missing.append(f"{addr}: shouldnotexist (post=empty)")
                else:
                    missing.append(f"{addr}: shouldnotexist")
            elif field == "storage":
                if has_post_dict or has_expected_storage:
                    # Check if storage= appears in the post dict
                    if (
                        "storage=" in test_content
                        or "expected_storage" in test_content
                    ):
                        found += 1
                    else:
                        missing.append(f"{addr}: storage")
                else:
                    missing.append(f"{addr}: storage (post=empty)")
            elif field == "nonce":
                if has_post_dict and "nonce=" in test_content:
                    found += 1
                elif has_post_empty:
                    missing.append(f"{addr}: nonce (post=empty)")
                else:
                    missing.append(f"{addr}: nonce")
            elif field == "balance":
                if has_post_dict and "balance=" in test_content:
                    found += 1
                elif has_post_empty:
                    missing.append(f"{addr}: balance (post=empty)")
                else:
                    missing.append(f"{addr}: balance")
            elif field == "code":
                if has_post_dict and "code=" in test_content:
                    found += 1
                elif has_post_empty:
                    missing.append(f"{addr}: code (post=empty)")
                else:
                    missing.append(f"{addr}: code")

    return expected, found, missing


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Verify post-state assertions in generated tests."
    )
    parser.add_argument(
        "--fillers",
        type=Path,
        required=True,
        help="Path to source filler directory",
    )
    parser.add_argument(
        "--generated",
        type=Path,
        required=True,
        help="Path to generated test directory",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show details for each filler",
    )
    args = parser.parse_args()

    # Find all filler files
    filler_files: list[Path] = []
    for ext in ("*.json", "*.yml", "*.yaml"):
        filler_files.extend(args.fillers.rglob(ext))
    # Filter to actual filler files (contain "Filler" in stem)
    filler_files = [f for f in filler_files if "Filler" in f.stem]
    filler_files.sort()

    total_fillers = 0
    total_expected = 0
    total_found = 0
    empty_post_count = 0
    all_missing: list[tuple[str, list[str]]] = []

    for filler_path in filler_files:
        total_fillers += 1
        expect_results = load_filler_expect_results(filler_path)
        if not expect_results:
            continue

        test_path = find_generated_test(args.generated, filler_path)
        if not test_path:
            if args.verbose:
                print(f"  SKIP: No generated test for {filler_path.name}")
            continue

        test_content = test_path.read_text()

        if (
            "post = {}" in test_content
            and "expected_storage" not in test_content
        ):
            empty_post_count += 1

        exp, fnd, missing = check_post_assertions(test_content, expect_results)
        total_expected += exp
        total_found += fnd

        if missing:
            all_missing.append((str(filler_path.name), missing))
            if args.verbose:
                print(f"  MISS: {filler_path.name}")
                for m in missing:
                    print(f"        - {m}")
        elif args.verbose:
            print(f"    OK: {filler_path.name} ({fnd}/{exp} assertions)")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"Verification Summary")
    print(f"{'=' * 60}")
    print(f"Total fillers checked:       {total_fillers}")
    print(f"Total assertion fields:      {total_expected}")
    print(f"Assertions found:            {total_found}")
    coverage = (total_found / total_expected * 100) if total_expected else 0
    print(f"Coverage:                    {coverage:.1f}%")
    print(f"Tests with empty post={{}}:    {empty_post_count}")
    print(f"Fillers with missing fields: {len(all_missing)}")

    if all_missing and not args.verbose:
        print(f"\nFirst 10 fillers with missing assertions:")
        for name, missing in all_missing[:10]:
            print(f"  {name}:")
            for m in missing[:3]:
                print(f"    - {m}")
            if len(missing) > 3:
                print(f"    ... and {len(missing) - 3} more")

    sys.exit(1 if all_missing else 0)


if __name__ == "__main__":
    main()
