"""
Geth Failed this test on Frontier and Homestead.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest644Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest644Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest644(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Geth Failed this test on Frontier and Homestead."""
    coinbase = Address("0x02ebba385bd7f6dde6c57e2d3929a11a1ea0da7e")
    sender = Address("0xc1c850561ed7cf000973d0bd66c9a11a519af7cc")
    contract = Address("0x0000000000000000000000000000000000000001")
    callee = Address("0x0346ad0b28ea31b7c3d398881dc11ebc97869461")
    callee_1 = Address("0xe4882ba8527df19159e6536f4aee12c298d28f33")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=27244094167015944,
    )

    pre[coinbase] = Account(
        balance=0x532F42C819FA5BED,
        nonce=28,
        code=bytes.fromhex(
            "77351c4c5a02c8f13fa7c7f5800fa5c9ba2f3b971c13764f9b61c2db66c3f909c17e434a"  # noqa: E501
            "68d685402956cc341dbf6779516900ed0a1e2666dfa40e70f3bcee773c2bffd5b5422a2c"  # noqa: E501
            "f32b19e541f15ae2b6fbe16fd19bbd567728190f83569f036dccd3886aa69c1e685736da"  # noqa: E501
            "06152e3b24728b13546ea1abd48ee47b1b2e1ec70b37fa14cc709d35fce7380230f42645"  # noqa: E501
            "5385da80771ffc6e261f3bfe7bfe7f1827d17b0cf49a7d7ff8ceb60b6a86ebbb762eb3e4"  # noqa: E501
            "dd1a8a09eaa9a500bc65cbefd4251865b70ca7e26682f1a2bad52a4a697aa0baf4ebe051"  # noqa: E501
            "30ec6a62e66e719d6bb753654f0ff08533f6d088e16d682dca6786082a55eda4d65f21e9"  # noqa: E501
            "1074345d12b775ce0f47447731e5eeeff44ca0a946e1df77f77e3d07cc9daa30a1b2941c"  # noqa: E501
            "17f9039ffa3baddf70dce808a071acb22d3fe0b1ecea101f659fd3fcfe7d9f16546273b0"  # noqa: E501
            "236232b792621189427302ebba385bd7f6dde6c57e2d3929a11a1ea0da7e3c6247f03762"  # noqa: E501
            "6ab8de621acb67625b60d5636bd269627302ebba385bd7f6dde6c57e2d3929a11a1ea0da"  # noqa: E501
            "7e630b2df5d6f1623402af629589806317ef5652f032"
        ),
    )
    pre[callee] = Account(
        balance=0x23C22AEB4961B17E,
        nonce=148,
        code=bytes.fromhex(
            "73a66737fdcc16cd591384a0b12fb650ce85011e553b7d85cc6995d8948ac88f5726f166"  # noqa: E501
            "27d809c92dba32d01471809ad1c5046b53687d1ff18bca5a755a0c6cd7ce36e1dc18c7c2"  # noqa: E501
            "a909f6bc0073d53f4c10a2121e6b4f0aeadc71b441c331b19ec57822835269748ae55869"  # noqa: E501
            "7a082470abaa3595d4b8256f8954c7ed655896eb04017a7f522be50fd88e38ee27de7ebd"  # noqa: E501
            "20794466f490bcb43162328a337a6e42fd88cacf6a8ecb264fe21836cf31d0ae7be53da5"  # noqa: E501
            "fe2cac802905640c0a18b2ccfd806fed6d7cbaf1fc19c6931d6c37b9320599ca50611210"  # noqa: E501
            "76a6546fc888f04e94c09adcc8a3cc9d002448838977c1010c1cdef7438b3d1e99cf6d78"  # noqa: E501
            "b9d4f55962b04476323f3441"
        ),
    )
    pre[sender] = Account(balance=0x236D08FE524712CB, nonce=0)
    pre[callee_1] = Account(
        balance=0x9183FD5B40D86E03,
        nonce=28,
        code=bytes.fromhex(
            "74357a5ade2da3b4a5f5459faff84e5ea9b714b60ed26257ef597d9aa2e6d9316426366f"  # noqa: E501
            "e24fb9ed56c4a9e5dcf06af08c42368fdaa12b71476283c5bd6147ed93625663ae6252d3"  # noqa: E501
            "73624971d86228ec1a730000000000000000000000000000000000000005630c30a604f4"  # noqa: E501
            "78fe44add6669b247cad0f00251697572fa913a16c98038931df54"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x0a10c9449493a34fd272f4bf6fc827c5b46ece7d0253518e71286f47ec3ae23a"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7300000000000000000000000000000000000000013b7ea30da9ff11bd5f11e4529c93ce"  # noqa: E501
            "4b37d5a256d61e1f1a0ecccb5fbb21fec97f6b3d456b8caaaa84ef30a44fd8779fae5a48"  # noqa: E501
            "354b937835d82d57999d194d4edfbaf0a8dd026d727e3315a53e907b0e1873b4dcb7f806"  # noqa: E501
            "014bc23164e8cc0560256f0c6a8c09c0df2f0f8208ff622bb459d46ffab16ce9d64bcf9c"  # noqa: E501
            "ec668338ebbc7f9e64656ae99c617d0dd709c1f78f96bea46e2df76db8418e2b657fc77f"  # noqa: E501
            "f2f979952911a73b767a6ce270c7392d2ff340648610fe0219aaf24df2b26e97e2761497"  # noqa: E501
            "bc6b97dea1269de3aca3b69ec7098a7257114a4a2e22c401ec6319bc2deb70980ebef372"  # noqa: E501
            "a327809b3c2473ab86578d2fccd458e6b99a277c4a1d3e96351fbebe62fe63d300444afd"  # noqa: E501
            "3a9077c20905d2a92b5b2945de6bf9b28d1d42795ca74b029dce6934312994a31fed72e4"  # noqa: E501
            "5da26c73c636b40b1f6d529f35488625624a9dfd0b62309f286277b5ab6259b2fd621447"  # noqa: E501
            "22631c4722737300000000000000000000000000000000000000056317345497f13368b2"  # noqa: E501
            "a96595a00933d8dd6dc111a13b90768f330898544a443407620316d3625614816282f1e9"  # noqa: E501
            "622e741d730346ad0b28ea31b7c3d398881dc11ebc97869461631d791a38fa"
        ),
        gas_limit=48887,
        gas_price=10,
        nonce=0,
        value=4077944035,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex(
                "77351c4c5a02c8f13fa7c7f5800fa5c9ba2f3b971c13764f9b61c2db66c3f909c17e434a68d685402956cc341dbf6779516900ed0a1e2666dfa40e70f3bcee773c2bffd5b5422a2cf32b19e541f15ae2b6fbe16fd19bbd567728190f83569f036dccd3886aa69c1e685736da06152e3b24728b13546ea1abd48ee47b1b2e1ec70b37fa14cc709d35fce7380230f426455385da80771ffc6e261f3bfe7bfe7f1827d17b0cf49a7d7ff8ceb60b6a86ebbb762eb3e4dd1a8a09eaa9a500bc65cbefd4251865b70ca7e26682f1a2bad52a4a697aa0baf4ebe05130ec6a62e66e719d6bb753654f0ff08533f6d088e16d682dca6786082a55eda4d65f21e91074345d12b775ce0f47447731e5eeeff44ca0a946e1df77f77e3d07cc9daa30a1b2941c17f9039ffa3baddf70dce808a071acb22d3fe0b1ecea101f659fd3fcfe7d9f16546273b0236232b792621189427302ebba385bd7f6dde6c57e2d3929a11a1ea0da7e3c6247f037626ab8de621acb67625b60d5636bd269627302ebba385bd7f6dde6c57e2d3929a11a1ea0da7e630b2df5d6f1623402af629589806317ef5652f032"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "73a66737fdcc16cd591384a0b12fb650ce85011e553b7d85cc6995d8948ac88f5726f16627d809c92dba32d01471809ad1c5046b53687d1ff18bca5a755a0c6cd7ce36e1dc18c7c2a909f6bc0073d53f4c10a2121e6b4f0aeadc71b441c331b19ec57822835269748ae558697a082470abaa3595d4b8256f8954c7ed655896eb04017a7f522be50fd88e38ee27de7ebd20794466f490bcb43162328a337a6e42fd88cacf6a8ecb264fe21836cf31d0ae7be53da5fe2cac802905640c0a18b2ccfd806fed6d7cbaf1fc19c6931d6c37b9320599ca5061121076a6546fc888f04e94c09adcc8a3cc9d002448838977c1010c1cdef7438b3d1e99cf6d78b9d4f55962b04476323f3441"  # noqa: E501
            ),
        ),
        callee_1: Account(
            code=bytes.fromhex(
                "74357a5ade2da3b4a5f5459faff84e5ea9b714b60ed26257ef597d9aa2e6d9316426366fe24fb9ed56c4a9e5dcf06af08c42368fdaa12b71476283c5bd6147ed93625663ae6252d373624971d86228ec1a730000000000000000000000000000000000000005630c30a604f478fe44add6669b247cad0f00251697572fa913a16c98038931df54"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
