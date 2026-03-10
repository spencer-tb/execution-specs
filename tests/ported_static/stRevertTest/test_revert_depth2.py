"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertDepth2Filler.json
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
    ["tests/static/state_tests/stRevertTest/RevertDepth2Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            170685,
            {
                Address("0x0707f29673f05e46feeb7c4766419a222010ae45"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0xC350,
                            address=0xC47BCBF49DD735566CFDE927821E938D5B33014C,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x68ea09e164a8b66de117a2c306b3966e6d71ca93"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=0x707F29673F05E46FEEB7C4766419A222010AE45,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=0x78ED2EB0809CD080C7837DC83AFC388A2B98D200,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x78ed2eb0809cd080c7837dc83afc388a2b98d200"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0xC350,
                            address=0xC47BCBF49DD735566CFDE927821E938D5B33014C,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.GAS)
                    + Op.STOP
                ),
                Address("0xc47bcbf49dd735566cfde927821e938d5b33014c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
            },
        ),
        (
            136685,
            {
                Address("0x0707f29673f05e46feeb7c4766419a222010ae45"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0xC350,
                            address=0xC47BCBF49DD735566CFDE927821E938D5B33014C,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x68ea09e164a8b66de117a2c306b3966e6d71ca93"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=0x707F29673F05E46FEEB7C4766419A222010AE45,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(
                        key=0x2,
                        value=Op.CALL(
                            gas=0x249F0,
                            address=0x78ED2EB0809CD080C7837DC83AFC388A2B98D200,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.STOP
                ),
                Address("0x78ed2eb0809cd080c7837dc83afc388a2b98d200"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.SSTORE(
                        key=0x1,
                        value=Op.CALL(
                            gas=0xC350,
                            address=0xC47BCBF49DD735566CFDE927821E938D5B33014C,
                            value=0x0,
                            args_offset=0x0,
                            args_size=0x0,
                            ret_offset=0x0,
                            ret_size=0x0,
                        ),
                    )
                    + Op.SSTORE(key=0x2, value=Op.GAS)
                    + Op.STOP
                ),
                Address("0xc47bcbf49dd735566cfde927821e938d5b33014c"): Account(
                    code=Op.SSTORE(
                        key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))
                    )
                    + Op.STOP
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_revert_depth2(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x68ea09e164a8b66de117a2c306b3966e6d71ca93")
    callee = Address("0x0707f29673f05e46feeb7c4766419a222010ae45")
    callee_1 = Address("0x78ed2eb0809cd080c7837dc83afc388a2b98d200")
    callee_2 = Address("0xc47bcbf49dd735566cfde927821e938d5b33014c")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0)))
            + Op.SSTORE(
                key=0x1,
                value=Op.CALL(
                    gas=0xC350,
                    address=0xC47BCBF49DD735566CFDE927821E938D5B33014C,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0)))
            + Op.SSTORE(
                key=0x1,
                value=Op.CALL(
                    gas=0x249F0,
                    address=0x707F29673F05E46FEEB7C4766419A222010AE45,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(
                key=0x2,
                value=Op.CALL(
                    gas=0x249F0,
                    address=0x78ED2EB0809CD080C7837DC83AFC388A2B98D200,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.STOP
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0)))
            + Op.SSTORE(
                key=0x1,
                value=Op.CALL(
                    gas=0xC350,
                    address=0xC47BCBF49DD735566CFDE927821E938D5B33014C,
                    value=0x0,
                    args_offset=0x0,
                    args_size=0x0,
                    ret_offset=0x0,
                    ret_size=0x0,
                ),
            )
            + Op.SSTORE(key=0x2, value=Op.GAS)
            + Op.STOP
        ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.SSTORE(key=0x0, value=Op.ADD(0x1, Op.SLOAD(key=0x0))) + Op.STOP
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
