"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stMemoryStressTest/static_CALL_Bounds3Filler.json
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    EOA,
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
        "tests/static/state_tests/stMemoryStressTest/static_CALL_Bounds3Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            150000,
            {
                Address("0x83143406093d1f3560dd269416596d3406f1c991"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0xFFFFFFFF,
                            args_size=0xFFFFFFFF,
                            ret_offset=0xFFFFFFFF,
                            ret_size=0xFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.STATICCALL(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                        args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0xcc704d60c46b9c08aab4d15281184441ac7ed35c"): Account(
                    code=Op.MSTORE(
                        offset=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            16777216,
            {
                Address("0x83143406093d1f3560dd269416596d3406f1c991"): Account(
                    code=Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0x0,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                            ret_offset=0x0,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0xFFFFFFFF,
                            args_size=0xFFFFFFFF,
                            ret_offset=0xFFFFFFFF,
                            ret_size=0xFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0xFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.POP(
                        Op.STATICCALL(
                            gas=0x7FFFFFFFFFFFFFF,
                            address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                            args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                            ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                        )
                    )
                    + Op.STATICCALL(
                        gas=0x7FFFFFFFFFFFFFF,
                        address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                        args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                        ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    )
                    + Op.STOP
                ),
                Address("0xcc704d60c46b9c08aab4d15281184441ac7ed35c"): Account(
                    code=Op.MSTORE(
                        offset=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_static_call_bounds3(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xEF111BBDAB3A1622936AFDFC9BBEC4B5BC05B4FA4B1EF0CE2A55CEF552F7650E
    )
    contract = Address("0x83143406093d1f3560dd269416596d3406f1c991")
    callee = Address("0xcc704d60c46b9c08aab4d15281184441ac7ed35c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
        nonce=0,
    )
    # Source: LLL
    # { (STATICCALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0 0xffffffffffffffff 0 0xffffffffffffffff)  (STATICCALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0 0xffffffffffffffffffffffffffffffff 0 0xffffffffffffffffffffffffffffffff)  (STATICCALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff 0 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) (STATICCALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0xffffffff 0xffffffff 0xffffffff 0xffffffff) (STATICCALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0xffffffffffffffff 0xffffffffffffffff 0xffffffffffffffff 0xffffffffffffffff) (STATICCALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0xffffffffffffffffffffffffffffffff 0xffffffffffffffffffffffffffffffff 0xffffffffffffffffffffffffffffffff 0xffffffffffffffffffffffffffffffff) (STATICCALL 0x7ffffffffffffff <contract:0x1000000000000000000000000000000000000001> 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff) }  # noqa: E501
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.POP(
                Op.STATICCALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                    args_offset=0x0,
                    args_size=0xFFFFFFFFFFFFFFFF,
                    ret_offset=0x0,
                    ret_size=0xFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.STATICCALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                    args_offset=0x0,
                    args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    ret_offset=0x0,
                    ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.STATICCALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                    args_offset=0x0,
                    args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                    ret_offset=0x0,
                    ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                ),
            )
            + Op.POP(
                Op.STATICCALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                    args_offset=0xFFFFFFFF,
                    args_size=0xFFFFFFFF,
                    ret_offset=0xFFFFFFFF,
                    ret_size=0xFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.STATICCALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                    args_offset=0xFFFFFFFFFFFFFFFF,
                    args_size=0xFFFFFFFFFFFFFFFF,
                    ret_offset=0xFFFFFFFFFFFFFFFF,
                    ret_size=0xFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.POP(
                Op.STATICCALL(
                    gas=0x7FFFFFFFFFFFFFF,
                    address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                    args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                    ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
                ),
            )
            + Op.STATICCALL(
                gas=0x7FFFFFFFFFFFFFF,
                address=0xCC704D60C46B9C08AAB4D15281184441AC7ED35C,
                args_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                args_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                ret_offset=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
                ret_size=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
            )
            + Op.STOP
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.MSTORE(offset=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0)))
            + Op.STOP
        ),
    )

    tx = Transaction(
        sender=sender,
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
