"""Tests for witness index metadata and collection-time stateless skips."""

from pathlib import Path
from types import SimpleNamespace

from execution_testing.base_types import HexNumber
from execution_testing.cli.gen_index import _witness_index_metadata
from execution_testing.cli.pytest_commands.plugins.consume.consume import (
    _stateless_index_skip_reason,
)
from execution_testing.fixtures.consume import TestCaseIndexFile


def _entry(**kwargs: bool | None) -> TestCaseIndexFile:
    return TestCaseIndexFile(
        id="test",
        json_path=Path("test.json"),
        fixture_hash=HexNumber(1),
        fork=None,
        format=None,
        **kwargs,
    )


def _payload(witness: object | None, mutated: bool | None) -> SimpleNamespace:
    return SimpleNamespace(
        execution_witness=witness,
        execution_witness_mutated=mutated,
    )


def test_witness_metadata_for_witness_carrying_fixture() -> None:
    """Report a witness present and unmutated for ordinary payloads."""
    fixture = SimpleNamespace(
        payloads=[_payload(None, None), _payload(object(), None)]
    )
    assert _witness_index_metadata(fixture) == (True, False)


def test_witness_metadata_for_mutated_fixture() -> None:
    """Report the mutation when any payload witness was mutated."""
    fixture = SimpleNamespace(
        payloads=[_payload(object(), None), _payload(object(), True)]
    )
    assert _witness_index_metadata(fixture) == (True, True)


def test_witness_metadata_for_witnessless_fixture() -> None:
    """Report no witness when no payload carries one."""
    fixture = SimpleNamespace(payloads=[_payload(None, None)])
    assert _witness_index_metadata(fixture) == (False, False)


def test_witness_metadata_unknown_for_non_engine_formats() -> None:
    """Report unknown metadata for fixtures without payloads."""
    fixture = SimpleNamespace(blocks=[])
    assert _witness_index_metadata(fixture) == (None, None)


def test_skip_reason_for_mutated_entry() -> None:
    """Mutated entries skip with the mutation reason."""
    entry = _entry(has_execution_witness=True, execution_witness_mutated=True)
    reason = _stateless_index_skip_reason(entry)
    assert reason is not None and "deliberately mutated" in reason


def test_skip_reason_for_witnessless_entry() -> None:
    """Witnessless entries skip with the no-witness reason."""
    entry = _entry(
        has_execution_witness=False, execution_witness_mutated=False
    )
    reason = _stateless_index_skip_reason(entry)
    assert reason is not None and "no executionWitness" in reason


def test_no_skip_reason_for_witness_carrying_entry() -> None:
    """Witness-carrying entries are consumable."""
    entry = _entry(has_execution_witness=True, execution_witness_mutated=False)
    assert _stateless_index_skip_reason(entry) is None


def test_no_skip_reason_for_old_index_entries() -> None:
    """Entries without witness metadata defer to the runtime gate."""
    assert _stateless_index_skip_reason(_entry()) is None
    assert _entry().has_execution_witness is None
    assert _entry().execution_witness_mutated is None
