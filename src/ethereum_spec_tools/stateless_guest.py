"""
Fork dispatching entry point for the stateless guest.

The stateless input begins with a two byte schema id whose high byte is
the fork index, so one compiled guest program can serve any fork: peek
the index, resolve the fork through [`Hardfork`] discovery, and run that
fork's own guest. Each fork keeps its validation semantics and payload
schema, this module only dispatches.

[`Hardfork`]: ref:ethereum_spec_tools.forks.Hardfork
"""

from typing import List, Optional

from ethereum_types.bytes import Bytes

from .evm_tools.loaders.fork_loader import ForkLoad
from .forks import Hardfork


def _stateless_forks() -> List[Hardfork]:
    """Return the forks that ship a stateless guest."""
    return [
        hardfork
        for hardfork in Hardfork.discover()
        if ForkLoad(hardfork).has_execution_witness
    ]


def fork_for_stateless_input(input_bytes: Bytes) -> Optional[Hardfork]:
    """Resolve the fork named by the input's schema id fork index."""
    if len(input_bytes) < 1:
        return None
    fork_index = input_bytes[0]
    for hardfork in _stateless_forks():
        load = ForkLoad(hardfork)
        if load.stateless_input_fork_index == fork_index:
            return hardfork
    return None


def run_stateless_guest(input_bytes: Bytes) -> Bytes:
    """
    Run the stateless guest of the fork the input names.

    Raise `ValueError` when no known fork matches the input's fork
    index, since without a fork there is no output schema to encode a
    failure in.
    """
    hardfork = fork_for_stateless_input(input_bytes)
    if hardfork is None:
        raise ValueError(
            "no fork with stateless support matches the input fork index"
        )
    return ForkLoad(hardfork).run_stateless_guest(input_bytes)
