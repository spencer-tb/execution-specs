"""
Optional stateless guest operations for filler backends.

The blockchain-test stateless pipeline needs a handful of operations
that only the spec can perform: run the stateless guest, rebuild its
serialized input, and decode or verify its payloads. `StatelessBackend`
declares them as an optional capability protocol -- backends gain guest
support by implementing the methods, without any change to backends
that lack it. The pipeline resolves the capability with
`require_stateless_backend` at the point of use, so fork resolution and
payload knowledge stay on the spec side of the interface.
"""

from typing import Protocol, Tuple, runtime_checkable

from execution_testing.base_types import Bytes
from execution_testing.forks import Fork
from execution_testing.test_types import ExecutionWitness
from execution_testing.test_types.execution_witness import (
    StatelessValidationError,
)


@runtime_checkable
class StatelessBackend(Protocol):
    """
    Optional filler-backend capability for stateless guest operations.

    Every operation takes the fork with the block number and timestamp
    that select the active fork, plus serialized guest payloads.
    """

    def stateless_validation_result(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        output_bytes: Bytes,
    ) -> bool:
        """Decode serialized guest output and return its validation flag."""
        ...

    def stateless_input_public_keys(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
    ) -> Tuple[Bytes, ...]:
        """Extract the transaction public keys from serialized input."""
        ...

    def stateless_verify_input_public_keys(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
        chain_id: int,
    ) -> None:
        """Verify input public keys against transaction recovery."""
        ...

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
        """Re-serialize guest input with overridden witness or keys."""
        ...

    def stateless_run_guest(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
    ) -> Tuple[Bytes, Bytes, bool]:
        """
        Run the stateless guest on serialized input.

        Return the input bytes, the serialized guest output, and the
        guest's validation flag.
        """
        ...

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
        """Verify serialized guest output invariants against its input."""
        ...


def require_stateless_backend(backend: object) -> StatelessBackend:
    """Return the backend as a `StatelessBackend`, or reject the fill."""
    if isinstance(backend, StatelessBackend):
        return backend
    raise StatelessValidationError(
        f"{type(backend).__name__} does not support stateless guest operations"
    )
