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
                    code=bytes.fromhex(
                        "6000546001016000556000600060006000600073c47bcbf49dd735566cfde927821e938d5b33014c61c350f160015500"  # noqa: E501
                    )
                ),
                Address("0x68ea09e164a8b66de117a2c306b3966e6d71ca93"): Account(
                    code=bytes.fromhex(
                        "60005460010160005560006000600060006000730707f29673f05e46feeb7c4766419a222010ae45620249f0f1600155600060006000600060007378ed2eb0809cd080c7837dc83afc388a2b98d200620249f0f160025500"  # noqa: E501
                    )
                ),
                Address("0x78ed2eb0809cd080c7837dc83afc388a2b98d200"): Account(
                    code=bytes.fromhex(
                        "6000546001016000556000600060006000600073c47bcbf49dd735566cfde927821e938d5b33014c61c350f16001555a60025500"  # noqa: E501
                    )
                ),
                Address("0xc47bcbf49dd735566cfde927821e938d5b33014c"): Account(
                    code=bytes.fromhex("60005460010160005500")
                ),
            },
        ),
        (
            136685,
            {
                Address("0x0707f29673f05e46feeb7c4766419a222010ae45"): Account(
                    code=bytes.fromhex(
                        "6000546001016000556000600060006000600073c47bcbf49dd735566cfde927821e938d5b33014c61c350f160015500"  # noqa: E501
                    )
                ),
                Address("0x68ea09e164a8b66de117a2c306b3966e6d71ca93"): Account(
                    code=bytes.fromhex(
                        "60005460010160005560006000600060006000730707f29673f05e46feeb7c4766419a222010ae45620249f0f1600155600060006000600060007378ed2eb0809cd080c7837dc83afc388a2b98d200620249f0f160025500"  # noqa: E501
                    )
                ),
                Address("0x78ed2eb0809cd080c7837dc83afc388a2b98d200"): Account(
                    code=bytes.fromhex(
                        "6000546001016000556000600060006000600073c47bcbf49dd735566cfde927821e938d5b33014c61c350f16001555a60025500"  # noqa: E501
                    )
                ),
                Address("0xc47bcbf49dd735566cfde927821e938d5b33014c"): Account(
                    code=bytes.fromhex("60005460010160005500")
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
        code=bytes.fromhex(
            "6000546001016000556000600060006000600073c47bcbf49dd735566cfde927821e938d"  # noqa: E501
            "5b33014c61c350f160015500"
        ),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "60005460010160005560006000600060006000730707f29673f05e46feeb7c4766419a22"  # noqa: E501
            "2010ae45620249f0f1600155600060006000600060007378ed2eb0809cd080c7837dc83a"  # noqa: E501
            "fc388a2b98d200620249f0f160025500"
        ),
    )
    pre[callee_1] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000546001016000556000600060006000600073c47bcbf49dd735566cfde927821e938d"  # noqa: E501
            "5b33014c61c350f16001555a60025500"
        ),
    )
    pre[callee_2] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex("60005460010160005500"),
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
