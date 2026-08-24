"""Memory pricing and limits flip at the EIP-7686 activation fork."""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Block,
    BlockchainTestFiller,
    CodeGasMeasure,
    Op,
    Transaction,
    TransitionFork,
)

from .spec import ref_spec_7686

REFERENCE_SPEC_GIT_PATH = ref_spec_7686.git_path
REFERENCE_SPEC_VERSION = ref_spec_7686.version

# TODO(EIP-7686): The pseudo-fork model executes both sides of the
# boundary on the same spec module, so a behavior-changing EIP cannot
# fill transition tests until a dedicated bogota fork module exists.
PSEUDO_FORK_SKIP = pytest.mark.skip(
    reason="requires a dedicated bogota fork module"
)


@PSEUDO_FORK_SKIP
@pytest.mark.valid_at_transition_to("EIP7686")
def test_memory_pricing_at_transition(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: TransitionFork,
) -> None:
    """
    The same memory expansion costs the quadratic price before the
    fork boundary and the linear price after it.
    """
    memory_size = 32 * 1024
    before = fork.fork_at(timestamp=14_999)
    after = fork.fork_at(timestamp=15_000)

    measured_code = Op.MLOAD(
        offset=memory_size - 32,
        new_memory_size=memory_size,
    )
    bare_code = Op.MLOAD(new_memory_size=memory_size)
    overhead_cost = measured_code.gas_cost(before) - bare_code.gas_cost(before)
    assert overhead_cost == measured_code.gas_cost(after) - bare_code.gas_cost(
        after
    )

    cost_before = bare_code.gas_cost(before)
    cost_after = bare_code.gas_cost(after)
    assert cost_before > cost_after

    measure_code = CodeGasMeasure(
        code=measured_code,
        overhead_cost=overhead_cost,
        extra_stack_items=1,
    )
    contract_before = pre.deploy_contract(code=measure_code)
    contract_after = pre.deploy_contract(code=measure_code)
    sender = pre.fund_eoa()

    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                timestamp=14_999,
                txs=[Transaction(sender=sender, to=contract_before)],
            ),
            Block(
                timestamp=15_000,
                txs=[Transaction(sender=sender, to=contract_after)],
            ),
        ],
        post={
            contract_before: Account(storage={0: cost_before}),
            contract_after: Account(storage={0: cost_after}),
        },
    )


@PSEUDO_FORK_SKIP
@pytest.mark.valid_at_transition_to("EIP7686")
def test_memory_limit_at_transition(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: TransitionFork,
) -> None:
    """
    An expansion beyond one byte per gas of the frame's grant succeeds
    before the fork boundary and halts after it.
    """
    gas_limit = 100_000
    # Beyond the post-fork cap, affordable under pre-fork quadratic
    # pricing: chosen so only the new hard limit rejects it.
    offset = gas_limit

    contract_before = pre.deploy_contract(
        code=Op.MSTORE8(offset, 1) + Op.SSTORE(0, 1),
    )
    contract_after = pre.deploy_contract(
        code=Op.MSTORE8(offset, 1) + Op.SSTORE(0, 1),
    )
    sender = pre.fund_eoa()

    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                timestamp=14_999,
                txs=[
                    Transaction(
                        sender=sender,
                        to=contract_before,
                        gas_limit=gas_limit,
                    )
                ],
            ),
            Block(
                timestamp=15_000,
                txs=[
                    Transaction(
                        sender=sender,
                        to=contract_after,
                        gas_limit=gas_limit,
                    )
                ],
            ),
        ],
        post={
            contract_before: Account(storage={0: 1}),
            contract_after: Account(storage={0: 0}),
        },
    )
