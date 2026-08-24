"""
Tests for EIP-7666 fork transition behavior.

At the boundary the identity EVM code is deployed at the retired
precompile address, which stops being treated as a precompile.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
)

from .spec import Spec, ref_spec_7666

REFERENCE_SPEC_GIT_PATH = ref_spec_7666.git_path
REFERENCE_SPEC_VERSION = ref_spec_7666.version


# TODO: Un-skip once a dedicated bogota fork module (and its framework
#  transition fork) exists; the pseudo-fork pre-allocates the
#  replacement code, so the pre-fork side cannot execute the native
#  precompile.
@pytest.mark.skip(reason="requires a dedicated bogota fork module")
@pytest.mark.valid_at_transition_to("EIP7666")
def test_deployment_across_transition(
    blockchain_test: BlockchainTestFiller, pre: Alloc
) -> None:
    """
    Call the identity address on both sides of the fork: precompile
    pricing before, the deployed seven-byte code with ordinary EVM
    costs from the boundary on.
    """
    identity = Spec.IDENTITY_PRECOMPILE_ADDRESS
    nonce = 7
    balance = 10**18
    storage = {1: 2}

    # The fork transition replaces only the code. In particular, it must not
    # reset state that can already exist at a precompile address.
    pre[identity] = Account(
        nonce=nonce,
        balance=balance,
        code=b"\x00",
        storage=storage,
    )

    blockchain_test(
        pre=pre,
        blocks=[Block(timestamp=14_999), Block(timestamp=15_000)],
        post={
            identity: Account(
                nonce=nonce,
                balance=balance,
                code=Spec.EVM_CODE,
                storage=storage,
            )
        },
    )
