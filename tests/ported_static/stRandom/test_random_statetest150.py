"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest150Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest150Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest150(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xa00c267da6e57a9318a096c6333c4bced51306da")

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
            "668254d76c6f24d4806677d83f3a46a1a66f20ae2688cf4b75842ac7265966f5f5ca603e"  # noqa: E501
            "6062a268aba89067dc278e1f86710462dae624ac683889038d26894af02617c06b39c498"  # noqa: E501
            "8a5a60a12c0d9ad0ca65839c92f7c75c6ad3d6a7b617ac7fbd41f5a29377ca6ad48748a9"  # noqa: E501
            "4e31302254147fb3b5857568e516cb6e8aa23577af85d0e508dc17dc50e246130be577cb"  # noqa: E501
            "59826adc86af6c107fd8a98f47cccd9d22a867a43cd8ad77bbe8bb737af5acc0be67fd7b"  # noqa: E501
            "054f7281e771891dc4aad180996b9cb71c6016d0f6a9148c775e57ac8456a883eedc3182"  # noqa: E501
            "623898f32b5c83760465a2061c7652e785e7eef7a97b0aa6d6c15b5c296bcf05ee2e9b87"  # noqa: E501
            "aa60b5741b3f7d69a1df03df117b848b3a75f81c12dee2244f76e56bb261e9c75fb5ccc7"  # noqa: E501
            "69db72bfaeadee3f68cf22bbca665b0647ac74c1409778c71b73ed4adaa2c6ba1c181b07"  # noqa: E501
            "47c27506478c403b3943129e79223e788bf8b81f60abecb73be035d03a8bbdfa112cd8cb"  # noqa: E501
            "2f7a1065250292740d2d72259b4d7e3ef844783da8118b72912b9f96a61f6168f160ef69"  # noqa: E501
            "d7dd3dfc7e4ef204766f789cbaf2abeceadcf5bdd8dddfef773f0a628afdf3988861662b"  # noqa: E501
            "77882a5cebffc61e75f11835b109e81f7c915a91c13b09097b792d3d59de0ef5b0f00f95"  # noqa: E501
            "ea49860917656263925da2fd6685359c6d7e4c3c4d2001a30111de14c56503788453df98"  # noqa: E501
            "a29b8715561b2c2021cf78e0ccc4701b192ebf67bb6f522656788b3d21428b50a2fa1622"  # noqa: E501
            "4d926ce2ea5944760d501bfa0774238c6351dd224b743d3fc4d5a309166016a71b1c230f"  # noqa: E501
            "e9afd6479324716e71e3b27bdd3fb18cccc42f6ec973129f7958435f45da181aeb1608ed"  # noqa: E501
            "31713c33330ab4d2d4af54dd92d1df1560086014601d601f636b1d9a3573a00c267da6e5"  # noqa: E501
            "7a9318a096c6333c4bced51306da632aec0540f16cfb040c16bd7c3761bdb86dd6be658d"  # noqa: E501
            "2aefe157396217393663769965a66479176d702e7e2d5697681aac1beccc55825241cd77"  # noqa: E501
            "551f39526cfa77838faa9c4759aafa5c64df5e9199976f35f8298acd398d1913c1fd2dda"  # noqa: E501
            "cbbeac7cc29daee12c057385808f19d07110f30cfd900a130b0a713468bceaf4236153ab"  # noqa: E501
            "6c7bdc39cf86d0a5b03684624d187473b42a2968f1128872724b3d42218dbac11f5a9492"  # noqa: E501
            "651f09a866f61a72535c373274618d5914163abc7481bb7789394e62f247e78e7f83af55"  # noqa: E501
            "a5686926972af7c6519658aee40a564e3c2950f874def7a2110af0526f75629b20a108e1"  # noqa: E501
            "cfba0db03fcdee497ee2f8bcf78ef14317"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "70afe04f9b9074d39383f0718bb0b14ecdb6680c54b4c20ae65044c572a5c832c15f55e8"  # noqa: E501
            "c1b63ffbb7da41d4c8faa43f087b1960b54938bbdb14f35e3552723ad2053a3c74b98d03"  # noqa: E501
            "20f74bbe4ff06630f30e1caa6e13797a14d07bb94ae4972ce38da7aefa2ab07aedb81397"  # noqa: E501
            "137b698a63675aa8895c5b1207be9262507b0866acfa180cfbbdff5572fb9a74b245d118"  # noqa: E501
            "0e80a93b2dc5bcf891e1b84d6c66ab13b03e937d4268f4e9be0381417c1db9b7341c9912"  # noqa: E501
            "e685e38ee499f1fb82b027b84e01ef235f18b95b0bf567fcfcc5181f51c6dd0465d063d0"  # noqa: E501
            "f11f267ccd81aa8d4fda65e7e213e5ae4a6da0c6493209753a089323c5bfdde091556681"  # noqa: E501
            "b0648f59b8b2684d82a240f7d5b8eefd645e6320270660e960467877a8561129b7114a61"  # noqa: E501
            "7d36423905813b7dc594d88b0eb751ba946f54595f624b07da116f0971fc6e540a966364"  # noqa: E501
            "c8a1df698688b1ba91f9ac7a74f878a61c87ad3240d656c9ee80fd90d4f8c01ca89c8bc5"  # noqa: E501
            "37380df079ba8a2e6f2a3cbeb6bfb9687a7cc323f2a9eafd81789ae783355764b23354ba"  # noqa: E501
            "3f693c4d774ed6ab89da8846604172ad96ab938a4beff64adf9594812f491a0ba98e6f77"  # noqa: E501
            "d4c40454047c20cfb2625c43608dc26d032e6f8b53bfc1243fbd23a14c077e2071997635"  # noqa: E501
            "fdb2ffb317cd0e116f1ea7649dcf80ead9dea010cc4e456893f16d7c534f980d27c3312f"  # noqa: E501
            "34fbf5c8ba9b"
        ),
        gas_limit=2042667010,
        gas_price=10,
        nonce=0,
        value=1816460087,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            code=bytes.fromhex(
                "668254d76c6f24d4806677d83f3a46a1a66f20ae2688cf4b75842ac7265966f5f5ca603e6062a268aba89067dc278e1f86710462dae624ac683889038d26894af02617c06b39c4988a5a60a12c0d9ad0ca65839c92f7c75c6ad3d6a7b617ac7fbd41f5a29377ca6ad48748a94e31302254147fb3b5857568e516cb6e8aa23577af85d0e508dc17dc50e246130be577cb59826adc86af6c107fd8a98f47cccd9d22a867a43cd8ad77bbe8bb737af5acc0be67fd7b054f7281e771891dc4aad180996b9cb71c6016d0f6a9148c775e57ac8456a883eedc3182623898f32b5c83760465a2061c7652e785e7eef7a97b0aa6d6c15b5c296bcf05ee2e9b87aa60b5741b3f7d69a1df03df117b848b3a75f81c12dee2244f76e56bb261e9c75fb5ccc769db72bfaeadee3f68cf22bbca665b0647ac74c1409778c71b73ed4adaa2c6ba1c181b0747c27506478c403b3943129e79223e788bf8b81f60abecb73be035d03a8bbdfa112cd8cb2f7a1065250292740d2d72259b4d7e3ef844783da8118b72912b9f96a61f6168f160ef69d7dd3dfc7e4ef204766f789cbaf2abeceadcf5bdd8dddfef773f0a628afdf3988861662b77882a5cebffc61e75f11835b109e81f7c915a91c13b09097b792d3d59de0ef5b0f00f95ea49860917656263925da2fd6685359c6d7e4c3c4d2001a30111de14c56503788453df98a29b8715561b2c2021cf78e0ccc4701b192ebf67bb6f522656788b3d21428b50a2fa16224d926ce2ea5944760d501bfa0774238c6351dd224b743d3fc4d5a309166016a71b1c230fe9afd6479324716e71e3b27bdd3fb18cccc42f6ec973129f7958435f45da181aeb1608ed31713c33330ab4d2d4af54dd92d1df1560086014601d601f636b1d9a3573a00c267da6e57a9318a096c6333c4bced51306da632aec0540f16cfb040c16bd7c3761bdb86dd6be658d2aefe157396217393663769965a66479176d702e7e2d5697681aac1beccc55825241cd77551f39526cfa77838faa9c4759aafa5c64df5e9199976f35f8298acd398d1913c1fd2ddacbbeac7cc29daee12c057385808f19d07110f30cfd900a130b0a713468bceaf4236153ab6c7bdc39cf86d0a5b03684624d187473b42a2968f1128872724b3d42218dbac11f5a9492651f09a866f61a72535c373274618d5914163abc7481bb7789394e62f247e78e7f83af55a5686926972af7c6519658aee40a564e3c2950f874def7a2110af0526f75629b20a108e1cfba0db03fcdee497ee2f8bcf78ef14317"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
