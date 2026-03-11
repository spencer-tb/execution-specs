"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stPreCompiledContracts/sec80Filler.json
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
    ["tests/static/state_tests/stPreCompiledContracts/sec80Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_sec80(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x39c2fbd2d4e46fa75775649472ddb79e836160b0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=(
            Op.JUMP(pc=0x1B)
            + Op.JUMPDEST
            + Op.PUSH1[0x0]
            + Op.SSTORE
            + Op.JUMPDEST
            + Op.STOP
            + Op.JUMPDEST
            + Op.PUSH4[0xBADF00D]
            + Op.JUMP(pc=0x3)
            + Op.JUMPDEST
            + Op.PUSH4[0xC001F00D]
            + Op.JUMP(pc=0x3)
            + Op.JUMPDEST
            + Op.PUSH20[0x19E7E376E7C213B7E7E7E46CC70A5DD086DAFF2A]
            + Op.MSTORE(
                offset=0x0,
                value=0x22AE6DA6B482F9B1B19B0B897C3FD43884180A1C5EE361E1107A1BC635649DDA,  # noqa: E501
            )
            + Op.MSTORE8(offset=0x3F, value=0x1B)
            + Op.MSTORE(
                offset=0x40,
                value=0x16433DCE375CE6DC8151D3F0A22728BC4A1D9FD6ED39DFD18B4609331937367F,  # noqa: E501
            )
            + Op.MSTORE(
                offset=0x60,
                value=0x306964C0CF5D74F04129FDC60B54D35B596DDE1BF89AD92CB4123318F4C0E400,  # noqa: E501
            )
            + Op.JUMPI(
                pc=0x7,
                condition=Op.ISZERO(
                    Op.CALLCODE(
                        gas=0xFFFF,
                        address=0x1,
                        value=0x0,
                        args_offset=0x0,
                        args_size=0x7F,
                        ret_offset=0x80,
                        ret_size=0x20,
                    ),
                ),
            )
            + Op.MLOAD(offset=0x80)
            + Op.JUMPI(pc=0x12, condition=Op.EQ)
            + Op.JUMP(pc=0x9)
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=10000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={0: 0xC001F00D},
            code=(
                Op.JUMP(pc=0x1B)
                + Op.JUMPDEST
                + Op.PUSH1[0x0]
                + Op.SSTORE
                + Op.JUMPDEST
                + Op.STOP
                + Op.JUMPDEST
                + Op.PUSH4[0xBADF00D]
                + Op.JUMP(pc=0x3)
                + Op.JUMPDEST
                + Op.PUSH4[0xC001F00D]
                + Op.JUMP(pc=0x3)
                + Op.JUMPDEST
                + Op.PUSH20[0x19E7E376E7C213B7E7E7E46CC70A5DD086DAFF2A]
                + Op.MSTORE(
                    offset=0x0,
                    value=0x22AE6DA6B482F9B1B19B0B897C3FD43884180A1C5EE361E1107A1BC635649DDA,  # noqa: E501
                )
                + Op.MSTORE8(offset=0x3F, value=0x1B)
                + Op.MSTORE(
                    offset=0x40,
                    value=0x16433DCE375CE6DC8151D3F0A22728BC4A1D9FD6ED39DFD18B4609331937367F,  # noqa: E501
                )
                + Op.MSTORE(
                    offset=0x60,
                    value=0x306964C0CF5D74F04129FDC60B54D35B596DDE1BF89AD92CB4123318F4C0E400,  # noqa: E501
                )
                + Op.JUMPI(
                    pc=0x7,
                    condition=Op.ISZERO(
                        Op.CALLCODE(
                            gas=0xFFFF,
                            address=0x1,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x7F,
                            ret_offset=0x80,
                            ret_size=0x20,
                        ),
                    ),
                )
                + Op.MLOAD(offset=0x80)
                + Op.JUMPI(pc=0x12, condition=Op.EQ)
                + Op.JUMP(pc=0x9)
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
