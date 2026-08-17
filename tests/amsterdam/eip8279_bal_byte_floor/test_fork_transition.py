"""
Tests for EIP-8279 fork transition behavior.

The byte floor activates at the fork boundary: the same floor-bound
transaction settles higher from the first post-fork block on.
"""

import pytest
from execution_testing import (
    Alloc,
    Block,
    BlockchainTestFiller,
    Fork,
    Header,
    Op,
    Transaction,
)

from .helpers import COLD_SLOT, STORAGE_KEY_FLOOR, scaffold_data
from .spec import ref_spec_8279

REFERENCE_SPEC_GIT_PATH = ref_spec_8279.git_path
REFERENCE_SPEC_VERSION = ref_spec_8279.version


# TODO: Un-skip once a dedicated bogota fork module (and its framework
#  transition fork) exists; the pseudo-fork shares the Amsterdam spec
#  module on both sides of the boundary, so the pre-fork block cannot
#  execute without the meter.
@pytest.mark.skip(reason="requires a dedicated bogota fork module")
@pytest.mark.valid_at_transition_to("EIP8279")
def test_floor_across_transition(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """
    Run the same floor-bound cold-read transaction on both sides of the
    fork: before it settles at the calldata floor alone, from the fork
    on the slot key's bytes raise it.
    """
    pre_fork = fork.fork_at(timestamp=14_999)
    data = scaffold_data(
        pre_fork, execution_headroom=STORAGE_KEY_FLOOR + 5_000
    )
    reader = pre.deploy_contract(code=Op.SLOAD(COLD_SLOT))
    calldata_floor = pre_fork.transaction_data_floor_cost_calculator()(
        data=data
    )
    sender = pre.fund_eoa()
    blocks = [
        Block(
            timestamp=timestamp,
            txs=[Transaction(sender=sender, to=reader, data=data)],
            header_verify=Header(gas_used=gas_used),
        )
        for timestamp, gas_used in (
            (14_999, calldata_floor),
            (15_000, calldata_floor + STORAGE_KEY_FLOOR),
            (15_001, calldata_floor + STORAGE_KEY_FLOOR),
        )
    ]
    blockchain_test(pre=pre, post={}, blocks=blocks)
