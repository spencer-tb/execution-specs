"""
Tests for EIP-7819 fork transition behavior.

Before the fork, `0xF6` is an undefined opcode and halts the frame;
from the fork on, it writes a delegation designation.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    Op,
    Transaction,
    compute_setdelegate_address,
)
from execution_testing.checklists import EIPChecklist

from .spec import Spec, ref_spec_7819

REFERENCE_SPEC_GIT_PATH = ref_spec_7819.git_path
REFERENCE_SPEC_VERSION = ref_spec_7819.version

SALT = 0xC0FFEE


# TODO: Re-enable when a dedicated bogota fork module (and its
#  transition fork) exists; the pseudo-fork shares the amsterdam
#  spec module, so the pre-fork side cannot treat `0xF6` as an
#  undefined opcode as this test needs.
@pytest.mark.skip(reason="requires a real post-Amsterdam fork module")
@EIPChecklist.Opcode.Test.ForkTransition.Invalid()
@pytest.mark.valid_at_transition_to("EIP7819")
def test_setdelegate_across_transition(
    blockchain_test: BlockchainTestFiller, pre: Alloc
) -> None:
    """
    Run the same SETDELEGATE transaction on both sides of the fork.

    The pre-fork transaction halts on the undefined opcode and writes
    nothing; the post-fork transaction writes the designation.
    """
    target = pre.fund_eoa(amount=0)
    factory = pre.deploy_contract(
        code=Op.SSTORE(0, 1) + Op.POP(Op.SETDELEGATE(SALT, target)),
    )
    location = compute_setdelegate_address(factory, SALT)
    sender = pre.fund_eoa()

    blocks = [
        Block(
            timestamp=timestamp,
            txs=[Transaction(sender=sender, to=factory, gas_limit=1_000_000)],
        )
        for timestamp in (14_999, 15_000)
    ]

    post = {
        # The pre-fork halt rolls back the canary store; the post-fork
        # transaction sets it and writes the designation.
        factory: Account(storage={0: 1}),
        location: Account(
            code=Spec.delegation_designation(target),
            nonce=1,
        ),
    }
    blockchain_test(pre=pre, blocks=blocks, post=post)
