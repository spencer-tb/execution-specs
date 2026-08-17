"""
Tests for EIP-8372 fork transition behavior.

At the boundary the state-byte price and the raw state-gas limit
contract together while the header's normalized charge per state byte
stays put.
"""

import pytest
from execution_testing import (
    Alloc,
    BlockchainTestFiller,
)

from .spec import ref_spec_8372

REFERENCE_SPEC_GIT_PATH = ref_spec_8372.git_path
REFERENCE_SPEC_VERSION = ref_spec_8372.version


# TODO: Un-skip once a dedicated bogota fork module (and its framework
#  transition fork) exists; the pseudo-fork shares the Amsterdam spec
#  module on both sides of the boundary, so the pre-fork side cannot
#  price state at the un-calibrated rate.
@pytest.mark.skip(reason="requires a dedicated bogota fork module")
@pytest.mark.valid_at_transition_to("EIP8372")
def test_calibration_across_transition(
    blockchain_test: BlockchainTestFiller, pre: Alloc
) -> None:
    """
    Run the same fresh-slot write on both sides of the fork: the raw
    receipt charge halves at the boundary while the header's
    normalized charge stays identical.
    """
