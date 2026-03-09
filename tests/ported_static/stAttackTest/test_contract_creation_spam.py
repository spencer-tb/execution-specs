"""
Ported from:
tests/static/state_tests/stAttackTest/ContractCreationSpamFiller.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stAttackTest/ContractCreationSpamFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_contract_creation_spam(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x6a0a0fc761c612c340a0e98d33b37a75e5268472")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000000,
    )

    pre[contract] = Account(
        balance=0xde0b6b3a7640000,
        nonce=0,
        code=(
        Op.MSTORE(offset=0x0, value=0x6004600c60003960046000f3600035ff00000000000000000000000000000000)
        + Op.CREATE(value=0x0, offset=0x0, size=0x20) + Op.SLOAD(key=0x0) + Op.DUP1
        + Op.JUMPDEST + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1)
        + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0))
        + Op.JUMPI(pc=Op.PUSH3[0x2f], condition=Op.LT(0x6000, Op.GAS)) + Op.PUSH1[0x0]
        + Op.SSTORE
    ),
    )
    pre[sender] = Account(balance=0xc9f2c9cd04674edea40000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 0x10c20},
            code=Op.MSTORE(offset=0x0, value=0x6004600c60003960046000f3600035ff00000000000000000000000000000000) + Op.CREATE(value=0x0, offset=0x0, size=0x20) + Op.SLOAD(key=0x0) + Op.DUP1 + Op.JUMPDEST + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.PUSH1[0x1] + Op.ADD + Op.MSTORE(offset=0x0, value=Op.DUP1) + Op.POP(Op.CALL(gas=0x6, address=Op.DUP8, value=Op.DUP1, args_offset=Op.DUP2, args_size=0x20, ret_offset=Op.DUP1, ret_size=0x0)) + Op.JUMPI(pc=Op.PUSH3[0x2f], condition=Op.LT(0x6000, Op.GAS)) + Op.PUSH1[0x0] + Op.SSTORE,
        ),
        Address("0xcc8c7a84d4f2872441499fa72b48bd45b03923ab"): Account(
            code=Op.SELFDESTRUCT(address=Op.CALLDATALOAD(offset=0x0)),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
