"""Tests for the fork dispatching stateless guest entry point."""

import pytest
from ethereum_types.bytes import Bytes

from ethereum_spec_tools.stateless_guest import (
    fork_for_stateless_input,
    run_stateless_guest,
)


def test_amsterdam_input_resolves_to_amsterdam() -> None:
    """Resolve the amsterdam fork index to the amsterdam fork."""
    hardfork = fork_for_stateless_input(Bytes(bytes([0x15, 0x01])))
    assert hardfork is not None
    assert hardfork.short_name == "amsterdam"


def test_unknown_fork_index_resolves_to_none() -> None:
    """Return None for a fork index no fork claims."""
    assert fork_for_stateless_input(Bytes(bytes([0xEE, 0x01]))) is None


def test_empty_input_resolves_to_none() -> None:
    """Return None when there is no schema id to peek."""
    assert fork_for_stateless_input(Bytes(b"")) is None


def test_unknown_fork_index_rejects_the_run() -> None:
    """Refuse to run when no fork matches the input fork index."""
    with pytest.raises(ValueError, match="no fork with stateless support"):
        run_stateless_guest(Bytes(bytes([0xEE, 0x01])))


def test_pinned_guest_rejects_other_forks() -> None:
    """A pinned guest refuses inputs naming a different fork."""
    from ethereum_spec_tools.forks import Hardfork

    forks = {h.short_name: h for h in Hardfork.discover()}
    with pytest.raises(ValueError, match="different fork"):
        run_stateless_guest(
            Bytes(bytes([0x15, 0x01])), fork=forks["osaka"]
        )
