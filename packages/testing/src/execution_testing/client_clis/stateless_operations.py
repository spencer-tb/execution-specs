"""
Stateless guest operations exposed by filler backends.

The blockchain-test stateless pipeline needs a handful of operations
that only the spec can perform: run the stateless guest, rebuild its
serialized input, and decode or verify its payloads. `StatelessOperations`
declares them for every filler backend, with defaults that reject the
call. Keeping these behind the backend interface keeps fork resolution
and payload knowledge on the spec side, so the pipeline itself stays
fork-agnostic. Backends override them when their transition tool gains
guest support.
"""

from typing import NoReturn, Tuple

from execution_testing.base_types import Bytes
from execution_testing.forks import Fork
from execution_testing.test_types import ExecutionWitness


class StatelessOperations:
    """
    Stateless guest operations with unsupported-by-default behavior.

    Every operation takes the fork with the block number and timestamp
    that select the active fork, plus serialized guest payloads. A
    backend that cannot perform an operation raises `NotImplementedError`
    through these defaults; the stateless pipeline only reaches them for
    fills that produced guest payloads in the first place.
    """

    def _stateless_unsupported(self, operation: str) -> NoReturn:
        """Reject a stateless guest operation this backend cannot do."""
        raise NotImplementedError(
            f"{type(self).__name__} does not support stateless guest "
            f"{operation}"
        )

    def stateless_validation_result(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        output_bytes: Bytes,
    ) -> bool:
        """Decode serialized guest output and return its validation flag."""
        del fork, block_number, timestamp, output_bytes
        self._stateless_unsupported("output decoding")

    def stateless_input_public_keys(
        self,
        *,
        fork: Fork,
        block_number: int,
        timestamp: int,
        input_bytes: Bytes,
    ) -> Tuple[Bytes, ...]:
        """Extract the transaction public keys from serialized input."""
        del fork, block_number, timestamp, input_bytes
        self._stateless_unsupported("input decoding")

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
        del fork, block_number, timestamp, input_bytes, chain_id
        self._stateless_unsupported("input verification")

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
        del fork, block_number, timestamp, input_bytes
        del execution_witness, public_keys
        self._stateless_unsupported("input rebuilding")

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
        del fork, block_number, timestamp, input_bytes
        self._stateless_unsupported("execution")

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
        del fork, block_number, timestamp, chain_id
        del input_bytes, output_bytes, input_bytes_modified
        self._stateless_unsupported("output verification")
