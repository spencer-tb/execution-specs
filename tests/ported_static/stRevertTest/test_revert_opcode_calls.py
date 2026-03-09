"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRevertTest/RevertOpcodeCallsFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertOpcodeCallsFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, expected_post",
    [
        (
            "000000000000000000000000ceb48d108c874b5b014acdd1a2466d65a3d01de6",
            460000,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    ),
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    )
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    storage={2: 14},
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "000000000000000000000000ceb48d108c874b5b014acdd1a2466d65a3d01de6",
            83622,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    )
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    )
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000737f82ed94146e759790d925492df5a8ced35885",
            460000,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    ),
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    )
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    storage={2: 14},
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    ),
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000737f82ed94146e759790d925492df5a8ced35885",
            83622,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    )
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    )
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000006b8268ac8921e6a6e59a4b1d51a76f4e807e17af",
            460000,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    ),
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    )
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    storage={2: 14},
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    ),
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "0000000000000000000000006b8268ac8921e6a6e59a4b1d51a76f4e807e17af",
            83622,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    )
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    )
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000bf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c",
            460000,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    storage={10: 1},
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    ),
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    storage={5: 14},
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    ),
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    storage={0: 1, 2: 14},
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    ),
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
            },
        ),
        (
            "000000000000000000000000bf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c",
            83622,
            {
                Address("0x1ada72179309fd8a562e308928e38763a543ed6c"): Account(
                    code=bytes.fromhex(
                        "600060006000600060006000356203f7a0f1600a5500"
                    )
                ),
                Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600455600e60055500"  # noqa: E501
                    )
                ),
                Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af"): Account(
                    code=bytes.fromhex(
                        "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x737f82ed94146e759790d925492df5a8ced35885"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f2600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(
                    code=bytes.fromhex("600c60015560016000fd600d60035500")
                ),
                Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c"): Account(
                    code=bytes.fromhex(
                        "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1600055600e60025500"  # noqa: E501
                    )
                ),
                Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6"): Account(
                    code=bytes.fromhex(
                        "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f1600055600e60025500"  # noqa: E501
                    )
                ),
            },
        ),
    ],
    ids=[
        "case0",
        "case1",
        "case2",
        "case3",
        "case4",
        "case5",
        "case6",
        "case7",
    ],
)
@pytest.mark.pre_alloc_mutable
def test_revert_opcode_calls(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x1ada72179309fd8a562e308928e38763a543ed6c")
    callee = Address("0x652761b88018ea027f6f27e456fe55c2dc5d6a91")
    callee_1 = Address("0x6b8268ac8921e6a6e59a4b1d51a76f4e807e17af")
    callee_2 = Address("0x737f82ed94146e759790d925492df5a8ced35885")
    callee_3 = Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b")
    callee_4 = Address("0xbf3fc188d9c8d699ffa12f0369e3b2bcf8428f7c")
    callee_5 = Address("0xceb48d108c874b5b014acdd1a2466d65a3d01de6")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex("600060006000600060006000356203f7a0f1600a5500"),
    )
    pre[callee] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f160"  # noqa: E501
            "0455600e60055500"
        ),
    )
    pre[callee_1] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "60006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f4600055"  # noqa: E501
            "600e60025500"
        ),
    )
    pre[callee_2] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f260"  # noqa: E501
            "0055600e60025500"
        ),
    )
    pre[callee_3] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex("600c60015560016000fd600d60035500"),
    )
    pre[callee_4] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "6000600060006000600073652761b88018ea027f6f27e456fe55c2dc5d6a91620186a0f1"  # noqa: E501
            "600055600e60025500"
        ),
    )
    pre[callee_5] = Account(
        balance=1,
        nonce=0,
        code=bytes.fromhex(
            "600060006000600060007393a599bde9a3b6390afdb06952aa5ec0b8c44f3b61c350f160"  # noqa: E501
            "0055600e60025500"
        ),
    )
    pre[sender] = Account(balance=0xE8D4A51000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
