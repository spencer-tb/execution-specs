"""
Backend protocol used by ``BlockchainTest`` to fill block data.

``FillerBackend`` abstracts the "thing that fills a block" so fill's spec
loop (``BlockchainTest.generate_block_data``) can dispatch to either:

- a classical ``TransitionTool`` (t8n CLI/server — deterministic compute
  path, the historical default), or
- a live EL client (``ClientBackend`` — drives ``testing_buildBlockV1`` to
  produce stateful fixtures against a warm datadir snapshot).

The two concrete backends cover distinct territory — t8n is a state-
transition function, a client is a stateful chain — but both return the
same ``TransitionToolOutput`` shape so they are interchangeable from
fill's perspective.

``TransitionTool`` itself structurally satisfies this protocol, so existing
callers continue to work unchanged.
"""

from typing import List, Protocol, Tuple, runtime_checkable

from execution_testing.base_types import Bytes
from execution_testing.exceptions import ExceptionMapper
from execution_testing.forks import Fork
from execution_testing.test_types import ExecutionWitness

from .cli_types import Traces
from .transition_tool import TransitionTool, TransitionToolOutput


@runtime_checkable
class FillerBackend(Protocol):
    """
    Minimal interface required by ``BlockchainTest.generate_block_data``.

    Implementations:
    - ``TransitionTool`` (classical t8n path) — fill's default.
    - ``ClientBackend`` — drives ``testing_buildBlockV1`` against a live EL
      client to produce stateful fixtures without t8n.
    """

    exception_mapper: ExceptionMapper
    """
    Maps backend-specific errors to EEST transaction/block exceptions.
    ``exception_mapper.reliable`` indicates whether the mapping is trusted
    for test assertions (t8n: True; live-client: typically False).
    """

    def evaluate(
        self,
        *,
        transition_tool_data: "TransitionTool.TransitionToolData",
        slow_request: bool = False,
    ) -> TransitionToolOutput:
        """Build a block and return the result."""
        ...

    def get_traces(self) -> List[Traces] | None:
        """Return per-transaction traces if available, ``None`` otherwise."""
        ...

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
        """Run the stateless guest on serialized input."""
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
