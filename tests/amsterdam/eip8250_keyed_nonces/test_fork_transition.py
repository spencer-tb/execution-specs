"""
Tests for EIP-8250 fork transition behavior.

At the boundary the `NONCE_MANAGER` system contract is initialized and
frame transactions switch to the keyed payload; pre-fork frame
transactions do not survive it.
"""

import pytest
from execution_testing import (
    Alloc,
    BlockchainTestFiller,
)

from .spec import ref_spec_8250

REFERENCE_SPEC_GIT_PATH = ref_spec_8250.git_path
REFERENCE_SPEC_VERSION = ref_spec_8250.version


# TODO: Un-skip once a dedicated bogota fork module (and its framework
#  transition fork) exists; the pseudo-fork shares the Amsterdam spec
#  module on both sides of the boundary, so the pre-fork side cannot
#  execute the un-keyed frame transaction payload.
@pytest.mark.skip(reason="requires a dedicated bogota fork module")
@pytest.mark.valid_at_transition_to("EIP8250")
def test_payload_switch_across_transition(
    blockchain_test: BlockchainTestFiller, pre: Alloc
) -> None:
    """
    Run an un-keyed frame transaction before the fork and a keyed one
    after: the pre-fork payload is rejected from the boundary on, and
    the nonce manager exists with its code and nonce from the first
    post-fork block.
    """
