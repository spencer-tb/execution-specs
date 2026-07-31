"""
Test_ab_acalls_suicide1.

Ported from:
state_tests/stSystemOperationsTest/ABAcallsSuicide1Filler.json

@manually-enhanced: Do not overwrite. Per-era post: pre-EIP-150 the
third call level dies on its unaffordable full fixed ask, so level
two's store and free SELFDESTRUCT commit and the beneficiary is paid;
from TangerineWhistle the unwind OOGs every frame (repriced
SELFDESTRUCT included) and all effects revert.
"""

import pytest
from execution_testing import (
    EOA,
    Account,
    Address,
    Alloc,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.forks import Fork, TangerineWhistle
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["state_tests/stSystemOperationsTest/ABAcallsSuicide1Filler.json"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "d, g, v",
    [
        pytest.param(
            0,
            0,
            0,
            id="d0",
        ),
        pytest.param(
            1,
            0,
            0,
            id="d1",
        ),
    ],
)
@pytest.mark.pre_alloc_mutable
def test_ab_acalls_suicide1(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    d: int,
    g: int,
    v: int,
) -> None:
    """Test_ab_acalls_suicide1."""
    coinbase = Address(0x2ADC25665018AA1FE0E6BC666DAC8FC2697FF9BA)
    contract_0 = Address(0x095E7BAEA6A6C7C4C2DFEB977EFAC326AF552D87)
    contract_1 = Address(0x945304EB96065B2A98B57A48A06AE28D285A71B5)
    sender = EOA(
        key=0x45A915E4D060149EB4365960E6A7A45F334393093061116B197E3240065FF2D8
    )

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000)
    # Source: lll
    # {  (MSTORE 0 (CALLDATALOAD 0)) [[ (PC) ]] (CALL (CALLDATALOAD 0) 0x945304eb96065b2a98b57a48a06ae28d285a71b5 24 0 32 0 0)   }  # noqa: E501
    a_prefix = Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0))
    a_call = Op.CALL(
        gas=Op.CALLDATALOAD(offset=0x0),
        address=0x945304EB96065B2A98B57A48A06AE28D285A71B5,
        value=0x18,
        args_offset=0x0,
        args_size=0x20,
        ret_offset=0x0,
        ret_size=0x0,
    )
    contract_0 = pre.deploy_contract(  # noqa: F841
        code=a_prefix + Op.SSTORE(key=Op.PC, value=a_call) + Op.STOP,
        balance=0xDE0B6B3A7640000,
        nonce=0,
        address=Address(0x095E7BAEA6A6C7C4C2DFEB977EFAC326AF552D87),  # noqa: E501
    )
    # The store's key is the code offset of its PC opcode, which sits
    # right after the assembled prefix and call expression.
    a_pc_key = len(bytes(a_prefix)) + len(bytes(a_call))
    # Source: lll
    # {  (MSTORE 0 (CALLDATALOAD 0)) [[ (PC) ]] (ADD 1 (CALL (SUB (CALLDATALOAD 0) 50000) 0x095e7baea6a6c7c4c2dfeb977efac326af552d87 23 0 32 0 0)) (SELFDESTRUCT 0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6) }  # noqa: E501
    contract_1 = pre.deploy_contract(  # noqa: F841
        code=Op.MSTORE(offset=0x0, value=Op.CALLDATALOAD(offset=0x0))
        + Op.SSTORE(
            key=Op.PC,
            value=Op.ADD(
                0x1,
                Op.CALL(
                    gas=Op.SUB(Op.CALLDATALOAD(offset=0x0), 0xC350),
                    address=0x95E7BAEA6A6C7C4C2DFEB977EFAC326AF552D87,
                    value=0x17,
                    args_offset=0x0,
                    args_size=0x20,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            ),
        )
        + Op.SELFDESTRUCT(address=0xF572E5295C57F15886F9B263E2F6D2D6C7B5EC6)
        + Op.STOP,
        balance=23,
        nonce=0,
        address=Address(0x945304EB96065B2A98B57A48A06AE28D285A71B5),  # noqa: E501
    )

    tx_data = [
        Hash(0x186A0),
        Hash(0x486A0),
    ]
    tx_gas = [10000000]
    tx_value = [100000]

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=sender,
        to=contract_0,
        data=tx_data[d],
        gas_limit=tx_gas[g],
        value=tx_value[v],
    )

    beneficiary = Address(0x0F572E5295C57F15886F9B263E2F6D2D6C7B5EC6)
    if fork >= TangerineWhistle:
        # EIP-150: the 63/64 rule lets the recursion descend until the
        # unwind's stores and the repriced SELFDESTRUCT (5000 + 25000
        # for a fresh beneficiary) OOG every frame on its retained
        # gas, reverting all stores, transfers, and the destruct.
        a_storage: dict[int, int] = {}
        contract_1_post: Account | None = Account(storage={}, balance=23)
        beneficiary_post: Account | None = Account.NONEXISTENT
    else:
        # Pre-EIP-150 the full fixed ask is charged up front: the
        # third level cannot afford it and dies there. Level two then
        # affords its store and the free SELFDESTRUCT, paying its
        # balance (23 initial plus the 24 received) to the
        # beneficiary, and level one stores the success flag.
        a_storage = {a_pc_key: 1}
        contract_1_post = Account.NONEXISTENT
        beneficiary_post = Account(balance=23 + 0x18)

    post = {
        contract_0: Account(storage=a_storage),
        beneficiary: beneficiary_post,
        contract_1: contract_1_post,
        sender: Account(nonce=1),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
