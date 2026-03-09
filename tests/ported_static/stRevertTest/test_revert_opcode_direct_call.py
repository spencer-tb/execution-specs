"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertOpcodeDirectCallFiller.json
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
    [
        "tests/static/state_tests/stRevertTest/RevertOpcodeDirectCallFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            460000,
            {
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    storage={2: 14},
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    ),
                ),
                Address("0xf94d87faf19d8c731e70e1b0a25f9668718f6e17"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600060003561ea60f1600a5500"
                    )
                ),
            },
        ),
        (
            62912,
            {
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xf94d87faf19d8c731e70e1b0a25f9668718f6e17"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600060003561ea60f1600a5500"
                    )
                ),
            },
        ),
    ],
    ids=["case0", "case1"],
)
@pytest.mark.pre_alloc_mutable
def test_revert_opcode_direct_call(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6")
    callee = Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b")
    callee_1 = Address("0xf94d87faf19d8c731e70e1b0a25f9668718f6e17")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex("600c60015560016000fd600d60035500"),
    )
    pre[contract] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f160"  # noqa: E501
            "0055600e60025500"
        ),
    )
    pre[callee_1] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex("6000600060006000600060003561ea60f1600a5500"),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "000000000000000000000000ceb48d108c874b5b014acdd1a2466d65a3d01de6"
        ),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
