"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/LoopCallsDepthThenRevert2Filler.json
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
    [
        "tests/static/state_tests/stRevertTest/LoopCallsDepthThenRevert2Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_loop_calls_depth_then_revert2(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xa000000000000000000000000000000000000000")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=10,
        nonce=0,
        code=(
            Op.JUMPI(pc=0x3F, condition=Op.EQ(Op.SLOAD(key=0x0), 0x3FF))
            + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
            + Op.POP(
                Op.CALL(
                    gas=Op.GAS,
                    address=0xA000000000000000000000000000000000000000,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.JUMPI(pc=0x53, condition=Op.LT(Op.SLOAD(key=0x0), 0x41A))
            + Op.JUMPDEST
            + Op.MSTORE(offset=0x0, value=0x600060006002F0)
            + Op.POP(Op.CREATE(value=0x3, offset=0x19, size=0x7))
            + Op.JUMPDEST
        ),
    )
    pre[sender] = Account(balance=0x13426172C74D822B878FE800000000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=9214364837600034817,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 1023},
            code=(
                Op.JUMPI(pc=0x3F, condition=Op.EQ(Op.SLOAD(key=0x0), 0x3FF))
                + Op.SSTORE(key=0x0, value=Op.ADD(Op.SLOAD(key=0x0), 0x1))
                + Op.POP(
                    Op.CALL(
                        gas=Op.GAS,
                        address=0xA000000000000000000000000000000000000000,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x0,
                        ret_offset=0x0,
                        ret_size=0x0,
                    ),
                )
                + Op.JUMPI(pc=0x53, condition=Op.LT(Op.SLOAD(key=0x0), 0x41A))
                + Op.JUMPDEST
                + Op.MSTORE(offset=0x0, value=0x600060006002F0)
                + Op.POP(Op.CREATE(value=0x3, offset=0x19, size=0x7))
                + Op.JUMPDEST
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
