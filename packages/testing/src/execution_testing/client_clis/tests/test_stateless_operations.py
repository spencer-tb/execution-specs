"""Tests for the stateless guest operations backend interface."""

import pytest

from execution_testing.base_types import Bytes
from execution_testing.client_clis import TransitionTool
from execution_testing.client_clis.client_backend import ClientBackend
from execution_testing.client_clis.stateless_operations import (
    StatelessOperations,
)
from execution_testing.forks import Amsterdam


def test_filler_backends_inherit_stateless_operations() -> None:
    """Expose the stateless guest operations on both filler backends."""
    assert issubclass(TransitionTool, StatelessOperations)
    assert issubclass(ClientBackend, StatelessOperations)


@pytest.mark.parametrize(
    "operation,kwargs",
    [
        ("stateless_validation_result", {"output_bytes": Bytes(b"")}),
        ("stateless_input_public_keys", {"input_bytes": Bytes(b"")}),
        (
            "stateless_verify_input_public_keys",
            {"input_bytes": Bytes(b""), "chain_id": 1},
        ),
        ("stateless_rebuild_input", {"input_bytes": Bytes(b"")}),
        ("stateless_run_guest", {"input_bytes": Bytes(b"")}),
        (
            "stateless_verify_output",
            {
                "input_bytes": Bytes(b""),
                "output_bytes": Bytes(b""),
                "chain_id": 1,
                "input_bytes_modified": False,
            },
        ),
    ],
)
def test_stateless_operations_unsupported_by_default(
    operation: str, kwargs: dict
) -> None:
    """Reject every stateless guest operation on the default backend."""
    backend = StatelessOperations()
    with pytest.raises(NotImplementedError, match="StatelessOperations"):
        getattr(backend, operation)(
            fork=Amsterdam, block_number=0, timestamp=0, **kwargs
        )
