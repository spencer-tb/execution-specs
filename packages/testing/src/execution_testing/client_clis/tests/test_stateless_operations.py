"""Tests for the optional stateless guest backend capability."""

from typing import Tuple

import pytest

from execution_testing.base_types import Bytes
from execution_testing.client_clis.stateless_operations import (
    StatelessBackend,
    require_stateless_backend,
)
from execution_testing.forks import Fork
from execution_testing.test_types import ExecutionWitness
from execution_testing.test_types.execution_witness import (
    StatelessValidationError,
)


class _GuestBackend:
    """Backend stub implementing every stateless guest operation."""

    def stateless_validation_result(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        output_bytes: Bytes,
    ) -> bool:
        del fork, block_number, timestamp, output_bytes
        return True

    def stateless_input_public_keys(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
    ) -> Tuple[Bytes, ...]:
        del fork, block_number, timestamp, input_bytes
        return ()

    def stateless_verify_input_public_keys(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
        chain_id: int,
    ) -> None:
        del fork, block_number, timestamp, input_bytes, chain_id
        return None

    def stateless_rebuild_input(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
        execution_witness: ExecutionWitness | None = None,
        public_keys: Tuple[Bytes, ...] | None = None,
    ) -> Bytes:
        del fork, block_number, timestamp
        del execution_witness, public_keys
        return input_bytes

    def stateless_run_guest(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
    ) -> Tuple[Bytes, Bytes, bool]:
        del fork, block_number, timestamp
        return input_bytes, Bytes(b""), True

    def stateless_verify_output(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        chain_id: int,
        input_bytes: Bytes,
        output_bytes: Bytes,
        input_bytes_modified: bool,
    ) -> None:
        del fork, block_number, timestamp, chain_id
        del input_bytes, output_bytes, input_bytes_modified
        return None


def test_supporting_backend_satisfies_the_capability() -> None:
    """Return the backend unchanged when it implements every operation."""
    backend = _GuestBackend()
    assert isinstance(backend, StatelessBackend)
    assert require_stateless_backend(backend) is backend


def test_unsupporting_backend_is_rejected() -> None:
    """Reject a backend that lacks the stateless guest operations."""

    class _PlainBackend:
        pass

    backend = _PlainBackend()
    assert not isinstance(backend, StatelessBackend)
    with pytest.raises(StatelessValidationError, match="_PlainBackend"):
        require_stateless_backend(backend)


def test_partial_backend_is_rejected() -> None:
    """Reject a backend implementing only some operations."""

    class _PartialBackend:
        def stateless_run_guest(self, **kwargs: object) -> None:
            del kwargs
            return None

    with pytest.raises(StatelessValidationError, match="_PartialBackend"):
        require_stateless_backend(_PartialBackend())
