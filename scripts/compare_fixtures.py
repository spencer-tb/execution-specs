#!/usr/bin/env python3
"""
Compare two fixture directories by post-state hashes.

Matches fixtures across directories with different path layouts:
  compiled:  for_{fork}/static/state_tests/{category}/{name}.json
  generated: for_{fork}/ported_static/{category}/{name}/{name}.json

Fixtures are paired by (fork, category, name), then compared by
the set of post-state hashes inside each JSON.

Usage:
    python scripts/compare_fixtures.py LEFT RIGHT
    python scripts/compare_fixtures.py LEFT RIGHT --show-missing
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Key = (fork, category, name)
FixtureKey = tuple[str, str, str]


def _parse_key(path: Path, root: Path) -> FixtureKey | None:
    """Extract (fork, category, name) from a fixture JSON path.

    Handles both layouts by finding the for_* directory, then
    taking the last two meaningful path components before the file.

    compiled:  for_osaka / static/state_tests / stFoo / bar.json
    generated: for_osaka / ported_static      / stFoo / bar/bar.json
    """
    parts = path.relative_to(root).parts

    # Find fork directory
    fork = next(
        (p for p in parts if p.startswith("for_")), None
    )
    if fork is None:
        return None

    # Everything between fork and the filename
    fork_pos = parts.index(fork)
    between = parts[fork_pos + 1 : -1]

    # Walk backwards to find the category (first st*/vm*/VM* dir)
    category = None
    for part in reversed(between):
        low = part.lower()
        if low.startswith("st") or low.startswith("vm"):
            category = part
            break

    if category is None:
        return None

    return (fork, category, path.stem)


def _post_hashes(path: Path) -> set[tuple[str, str]]:
    """Extract the set of (fork, hash) from all post entries."""
    hashes: set[tuple[str, str]] = set()
    for _key, test in json.loads(path.read_text()).items():
        for fork, entries in test.get("post", {}).items():
            for entry in entries:
                h = entry.get("hash", "")
                if h:
                    hashes.add((fork, h))
    return hashes


def _index(root: Path) -> dict[FixtureKey, Path]:
    """Index fixture JSONs by (fork, category, name)."""
    idx: dict[FixtureKey, Path] = {}
    for p in root.rglob("*.json"):
        if p.parts[-2] == ".meta":
            continue
        key = _parse_key(p, root)
        if key is not None and key not in idx:
            idx[key] = p
    return idx


def compare(
    left: Path,
    right: Path,
    *,
    show_missing: bool = False,
) -> int:
    """Compare two fixture directories. Return number of mismatches."""
    left_idx = _index(left)
    right_idx = _index(right)

    common = sorted(set(left_idx) & set(right_idx))
    only_left = sorted(set(left_idx) - set(right_idx))
    only_right = sorted(set(right_idx) - set(left_idx))

    mismatches = 0
    for key in common:
        lh = _post_hashes(left_idx[key])
        rh = _post_hashes(right_idx[key])
        if lh != rh:
            mismatches += 1
            print(f"MISMATCH {'/'.join(key)}")
            print(f"  left:  {left_idx[key]}")
            print(f"  right: {right_idx[key]}")
            print(
                f"  {len(lh - rh)} only in left, "
                f"{len(rh - lh)} only in right"
            )

    total = len(common)
    print()
    print(f"Matched:    {total - mismatches}/{total}")
    if mismatches:
        print(f"Mismatched: {mismatches}/{total}")
    print(f"Left only:  {len(only_left)}")
    print(f"Right only: {len(only_right)}")

    if show_missing and only_left:
        print(f"\n-- Only in {left} ({len(only_left)}) --")
        for key in only_left:
            print(f"  {'/'.join(key)}")

    if show_missing and only_right:
        print(f"\n-- Only in {right} ({len(only_right)}) --")
        for key in only_right:
            print(f"  {'/'.join(key)}")

    return mismatches


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two fixture directories by post-state hashes."
        ),
    )
    parser.add_argument("left", type=Path)
    parser.add_argument("right", type=Path)
    parser.add_argument(
        "--show-missing",
        action="store_true",
        help="List fixtures that exist in only one directory",
    )
    args = parser.parse_args()
    sys.exit(1 if compare(args.left, args.right, show_missing=args.show_missing) else 0)


if __name__ == "__main__":
    main()
