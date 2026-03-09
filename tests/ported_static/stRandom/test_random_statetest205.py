"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest205Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest205Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest205(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xd6c9d572b7645ecae86a7bdb66c7ae1fb04b0321")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=bytes.fromhex("6000355415600957005b60203560003555"),
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "3360b261edefa0326fdc74d570982966277b49cdb30a453fa06c34a7423da44ba2d04341"  # noqa: E501
            "af08c478b17a57318ab10ab43b3744333b0aa8864ac27b3fd022e380056735a5fcda3e9f"  # noqa: E501
            "dc25695972a076884de6d6b6b06dd45416c8110bae3c70576b433a4672777847e8182302"  # noqa: E501
            "4ddd1292b929ad28e64a732b74c0ae1941d5936ecd35738e2f279273788f4aaf19907a53"  # noqa: E501
            "2a6b0f117c32b6cb967aae8bdfcf86e2d4d64599986abcf65a20754f5a816c58ed669138"  # noqa: E501
            "f6a0448670b906bbf1eb145ced896c578de5aa27769006b1a784e84b6316d4e60c7053b0"  # noqa: E501
            "b6550c70a177cb7a3e88d4e83fb1897a09c2161ff6cc2679c178292687137854da672e31"  # noqa: E501
            "6c66ef03dc9ac37e8e430b7c64d1939bf67383c4bafeb2f0471fe896b7c0e114bf6f152b"  # noqa: E501
            "266cc769ae4d38f3df618f5eeb9085601f601060086016632c019e2e73d6c9d572b7645e"  # noqa: E501
            "cae86a7bdb66c7ae1fb04b0321626b8a0ef179e6b62e86237845e9605d61219d97c1d014"  # noqa: E501
            "5516f5355fe73384e87a6a87cc6d2378c81797ac3746bc562e2fd1145e14781307bc4ada"  # noqa: E501
            "39732e9d0e8725fde75c5abc313c11e3238c7cd9b7186a6a14f8d5c3cad9da5339446ad1"  # noqa: E501
            "311ccc67a0691559157a674825358b301ac42d7bcae31beb8b0849903402175ca3740f3f"  # noqa: E501
            "d690ad66287d6bf67a98c09e6de5717596052d30f4b9bb8046a6b67ef51b1b13c496e97b"  # noqa: E501
            "f9a2e67aeca97fa10a266f8cf22c10cc0375b514b25de466a146576b2cb565754efc80d4"  # noqa: E501
            "b8aa5497aa0fb4cbab90ee57298d322474d276366e04eab856c9f6070c80701fa30596dd"  # noqa: E501
            "0b6ea5bc38ba64e1d16aff1b8c61caa379064465a9308dbb1465294ddcb5fa32833e4ffb"  # noqa: E501
            "049c71761ed93472c7e58f171c6c8b51e2ec704d34897b80466e826b0c1ce2488511cbb1"  # noqa: E501
            "aaad26b075ed5ebf070be6e14eaa6b973423bcb2e0541307d88ff66d1b7e29fffb10218c"  # noqa: E501
            "a75bf3f9957d6ee27a0945278d5f9303b3e3f28a325a7f17905f7467c4afcbb3a43dbbd3"  # noqa: E501
            "7e9591e3f5a82841ee9cb8b23f68b4572e8cd96d0f7daacbd3ab3bd5a8f427baf6ea7ae7"  # noqa: E501
            "0d98d3948eafb74e2e4a158ac116c5219403c9073a457409c6e464bae32b2c856b15bda1"  # noqa: E501
            "b2176295fd1cecfe7d794ab2692061aa79387004112272204198437fc78d1dbe0e8932ce"  # noqa: E501
            "6f47828a2bf4df47446291b99d92a90de3623954589d36"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "74ac5e422199cb842b1fdcdef502d4142d033387c6d17fe1f03f0fc4a3c05daadf323f3b"  # noqa: E501
            "b04b7e33dbad9b32f058aa6df6d54c8d7ac95568ba4a6b33a2b0ce8d8c7480ab9e818cf8"  # noqa: E501
            "998564e6d38b92aa1ecd76aa8aff266dd266c96af419778c16a109cba6976922093e50bd"  # noqa: E501
            "a96ac1333a946574ad748ad839546ff861257bb6a41cab34045ea7335e1c9667c67424f9"  # noqa: E501
            "baf8781e79e002a233a622f41f2744c21b6baed43543e0dfb9aa81fd1050326b0ebad84f"  # noqa: E501
            "da176f3438d3a7f083"
        ),
        gas_limit=7300000,
        gas_price=10,
        nonce=0,
        value=1305713546,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            code=bytes.fromhex(
                "3360b261edefa0326fdc74d570982966277b49cdb30a453fa06c34a7423da44ba2d04341af08c478b17a57318ab10ab43b3744333b0aa8864ac27b3fd022e380056735a5fcda3e9fdc25695972a076884de6d6b6b06dd45416c8110bae3c70576b433a4672777847e81823024ddd1292b929ad28e64a732b74c0ae1941d5936ecd35738e2f279273788f4aaf19907a532a6b0f117c32b6cb967aae8bdfcf86e2d4d64599986abcf65a20754f5a816c58ed669138f6a0448670b906bbf1eb145ced896c578de5aa27769006b1a784e84b6316d4e60c7053b0b6550c70a177cb7a3e88d4e83fb1897a09c2161ff6cc2679c178292687137854da672e316c66ef03dc9ac37e8e430b7c64d1939bf67383c4bafeb2f0471fe896b7c0e114bf6f152b266cc769ae4d38f3df618f5eeb9085601f601060086016632c019e2e73d6c9d572b7645ecae86a7bdb66c7ae1fb04b0321626b8a0ef179e6b62e86237845e9605d61219d97c1d0145516f5355fe73384e87a6a87cc6d2378c81797ac3746bc562e2fd1145e14781307bc4ada39732e9d0e8725fde75c5abc313c11e3238c7cd9b7186a6a14f8d5c3cad9da5339446ad1311ccc67a0691559157a674825358b301ac42d7bcae31beb8b0849903402175ca3740f3fd690ad66287d6bf67a98c09e6de5717596052d30f4b9bb8046a6b67ef51b1b13c496e97bf9a2e67aeca97fa10a266f8cf22c10cc0375b514b25de466a146576b2cb565754efc80d4b8aa5497aa0fb4cbab90ee57298d322474d276366e04eab856c9f6070c80701fa30596dd0b6ea5bc38ba64e1d16aff1b8c61caa379064465a9308dbb1465294ddcb5fa32833e4ffb049c71761ed93472c7e58f171c6c8b51e2ec704d34897b80466e826b0c1ce2488511cbb1aaad26b075ed5ebf070be6e14eaa6b973423bcb2e0541307d88ff66d1b7e29fffb10218ca75bf3f9957d6ee27a0945278d5f9303b3e3f28a325a7f17905f7467c4afcbb3a43dbbd37e9591e3f5a82841ee9cb8b23f68b4572e8cd96d0f7daacbd3ab3bd5a8f427baf6ea7ae70d98d3948eafb74e2e4a158ac116c5219403c9073a457409c6e464bae32b2c856b15bda1b2176295fd1cecfe7d794ab2692061aa79387004112272204198437fc78d1dbe0e8932ce6f47828a2bf4df47446291b99d92a90de3623954589d36"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
