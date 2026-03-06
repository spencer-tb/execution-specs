#!/usr/bin/env python3
"""
Regenerate all test files from filler data (no compiled fixtures needed).

Reads each filler from disk, synthesizes the minimal fixture data
structure that generate_test_file() expects, then calls it to produce the
Python test file.

Usage:
    uv run python scripts/regenerate_from_fillers.py \
        --output tests/static/state_tests/ [--single FILLER_PATH]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from fixture_to_python import (
    _load_filler_data,
    _normalize_address,
    filler_name_to_test_name,
    fork_before,
    generate_test_file,
    load_filler_comment,
    load_filler_network_upper_bound,
)

FORK_FOR_TESTS = "Cancun"  # All static tests target Cancun


def _ensure_hex(val: Any) -> str:
    """Ensure a value is a hex string."""
    if isinstance(val, int):
        return hex(val)
    s = str(val)
    if s.startswith("0x") or s.startswith("0X"):
        return s
    if s.startswith(":label"):
        return "0x"
    try:
        int(s)
        return hex(int(s))
    except ValueError:
        return s if s else "0x"


def _normalize_storage(storage: dict) -> dict:
    """Normalize filler storage to hex-string keys and values."""
    result = {}
    for k, v in storage.items():
        k_hex = _ensure_hex(k)
        v_hex = _ensure_hex(v)
        result[k_hex] = v_hex
    return result


def _normalize_pre(pre: dict) -> dict:
    """Normalize a filler's pre section to fixture format."""
    result = {}
    for addr, acct in pre.items():
        if str(addr).startswith("//"):
            continue
        norm_addr = _normalize_address(str(addr))
        entry: dict[str, Any] = {}
        entry["balance"] = _ensure_hex(acct.get("balance", "0x0"))
        entry["nonce"] = _ensure_hex(acct.get("nonce", "0x0"))
        entry["code"] = str(acct.get("code", "0x"))
        storage = acct.get("storage", {})
        entry["storage"] = _normalize_storage(storage)
        result[norm_addr] = entry
    return result


def filler_to_fixture_data(
    filler_data: dict,
    filler_path: str,
) -> dict[str, Any] | None:
    """Convert filler data into the fixture_data structure.

    Generate one fixture key per (case × fork) combination.
    """
    for test_name, test_data in filler_data.items():
        if not isinstance(test_data, dict):
            continue

        env_raw = test_data.get("env", {})
        pre_raw = test_data.get("pre", {})
        tx_raw = test_data.get("transaction", {})

        # Normalize env
        env: dict[str, str] = {}
        for k, v in env_raw.items():
            if str(k).startswith("//"):
                continue
            env[k] = _ensure_hex(v) if isinstance(v, int) else str(v)

        # Normalize pre
        pre = _normalize_pre(pre_raw)

        # Transaction arrays
        data_list = tx_raw.get("data", ["0x"])
        gas_list = tx_raw.get("gasLimit", ["0x5f5e100"])
        value_list = tx_raw.get("value", ["0x0"])
        access_lists = tx_raw.get("accessLists", [])

        # Common tx fields
        sender = tx_raw.get("sender", "")
        if not sender:
            secret_key = tx_raw.get("secretKey", "")
            if secret_key:
                # Derive sender (simplified: use a placeholder)
                sender = "0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b"
        to_addr = tx_raw.get("to", "")
        gas_price = tx_raw.get("gasPrice", "0x1")
        nonce = tx_raw.get("nonce", "0x0")
        max_fee = tx_raw.get("maxFeePerGas", "")
        max_priority = tx_raw.get("maxPriorityFeePerGas", "")

        nd = len(data_list)
        ng = len(gas_list)
        nv = len(value_list)

        # Build fixture data: one key per (d, g, v)
        fixture_data: dict[str, Any] = {}
        case_idx = 0
        for d_i in range(nd):
            for g_i in range(ng):
                for v_i in range(nv):
                    key = (
                        f"{filler_path}::{test_name}"
                        f"[d{d_i}g{g_i}v{v_i}-{FORK_FOR_TESTS}]"
                    )
                    # Build per-case transaction
                    data_val = str(data_list[d_i])
                    if data_val.startswith(":label"):
                        data_val = "0x"
                    gas_val = _ensure_hex(gas_list[g_i])
                    val_val = _ensure_hex(value_list[v_i])

                    al = None
                    if access_lists:
                        al_idx = d_i if d_i < len(access_lists) else 0
                        al = access_lists[al_idx]

                    tx: dict[str, Any] = {
                        "data": [data_val],
                        "gasLimit": [gas_val],
                        "value": [val_val],
                        "sender": sender,
                        "to": to_addr,
                        "gasPrice": _ensure_hex(gas_price),
                        "nonce": _ensure_hex(nonce),
                        "secretKey": tx_raw.get("secretKey", ""),
                    }
                    if max_fee:
                        tx["maxFeePerGas"] = _ensure_hex(max_fee)
                    if max_priority:
                        tx["maxPriorityFeePerGas"] = _ensure_hex(
                            max_priority
                        )
                    if al is not None:
                        tx["accessLists"] = [al]

                    fixture_data[key] = {
                        "env": env,
                        "pre": pre,
                        "transaction": tx,
                        "post": {
                            FORK_FOR_TESTS: [
                                {
                                    "state": {},
                                    "indexes": {
                                        "data": d_i,
                                        "gas": g_i,
                                        "value": v_i,
                                    },
                                }
                            ]
                        },
                    }
                    case_idx += 1

        if fixture_data:
            return fixture_data

    return None


def find_fillers_on_disk(base: Path) -> list[str]:
    """Find all filler files on disk under base directory."""
    results: list[str] = []
    for p in sorted(base.rglob("*Filler.json")):
        results.append(str(p))
    for p in sorted(base.rglob("*Filler.yml")):
        results.append(str(p))
    return sorted(results)


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Regenerate test files from filler data."
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for generated Python tests",
    )
    parser.add_argument(
        "--single",
        type=str,
        default=None,
        help="Process a single filler path (repo-relative)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't write files, just report",
    )
    args = parser.parse_args()

    if args.single:
        filler_paths = [args.single]
    else:
        filler_paths = find_fillers_on_disk(
            Path("tests/static/state_tests")
        )

    if not filler_paths:
        print("No filler files found.")
        sys.exit(1)

    success = 0
    fail = 0
    for filler_path_str in filler_paths:
        filler_path = Path(filler_path_str)

        # Load filler data
        filler_data = _load_filler_data(filler_path)
        if not filler_data:
            fail += 1
            continue

        # Convert to fixture data
        fixture_data = filler_to_fixture_data(filler_data, filler_path_str)
        if not fixture_data:
            fail += 1
            continue

        # Load metadata
        filler_comment = load_filler_comment(filler_path)
        upper_bound = load_filler_network_upper_bound(filler_path)
        valid_until = fork_before(upper_bound) if upper_bound else None

        try:
            python_code = generate_test_file(
                fixture_data,
                filler_path_str,
                filler_comment,
                valid_until=valid_until,
                filler_full_path=filler_path,
            )
        except Exception as e:
            fail += 1
            print(f"FAIL: {filler_path_str}: {e}", file=sys.stderr)
            continue

        # Determine output path
        filler_stem = filler_path.stem
        test_name = filler_name_to_test_name(filler_stem)

        filler_parts = filler_path.parts
        category = ""
        for i, part in enumerate(filler_parts):
            if part == "state_tests" and i + 1 < len(filler_parts):
                remaining = filler_parts[i + 1 : -1]
                category = str(Path(*remaining)) if remaining else ""
                break

        out_dir = args.output / category if category else args.output
        out_file = out_dir / f"{test_name}.py"

        if not args.dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            init_file = out_dir / "__init__.py"
            if not init_file.exists():
                init_file.write_text("")
            out_file.write_text(python_code)

        success += 1

    print(f"\nDone: {success} generated, {fail} failed")
    if fail > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
