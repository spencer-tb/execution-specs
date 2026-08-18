"""
Tests for EIP-8200 fork transition behavior.

At the boundary the replacement bytecode is deployed at the retired
precompile addresses, which stop being treated as precompiles.
"""

import pytest
from execution_testing import (
    Alloc,
    BlockchainTestFiller,
)

from .spec import ref_spec_8200

REFERENCE_SPEC_GIT_PATH = ref_spec_8200.git_path
REFERENCE_SPEC_VERSION = ref_spec_8200.version


# TODO: Un-skip once a dedicated bogota fork module (and its framework
#  transition fork) exists; the pseudo-fork pre-allocates the
#  replacement code, so the pre-fork side cannot execute the native
#  precompiles.
@pytest.mark.skip(reason="requires a dedicated bogota fork module")
@pytest.mark.valid_at_transition_to("EIP8200")
def test_deployment_across_transition(
    blockchain_test: BlockchainTestFiller, pre: Alloc
) -> None:
    """
    Call each retired address on both sides of the fork: native
    precompile pricing and semantics before, deployed bytecode with
    ordinary EVM costs from the boundary on.
    """
