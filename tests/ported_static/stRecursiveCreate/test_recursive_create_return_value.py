"""
Ported from:
tests/static/state_tests/stRecursiveCreate/recursiveCreateReturnValueFiller.json
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
    ["tests/static/state_tests/stRecursiveCreate/recursiveCreateReturnValueFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_recursive_create_return_value(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0x095e7baea6a6c7c4c2dfeb977efac326af552d87")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000000,
    )

    pre[contract] = Account(
        balance=0x1312d00,
        nonce=0,
        code=(
        Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x20)
        + Op.SSTORE(key=0x0, value=Op.ADD(Op.CREATE(value=0x0, offset=0x0, size=0x20), 0x1))
        + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xde0b6b3a7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=1000000000,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        Address("0x0124ac36deebf89244c22bedfcb6e05fb2f62f3b"): Account(
            storage={0: 0xbbc2aea32a7763bf59ea9157274f20e73c47210e},
        ),
        Address("0x0153629ea98627274192fa275a6a9ad20191ab03"): Account(
            storage={0: 0x953fe148abf5e5d1b957446919f7d460fb8e0e05},
        ),
        Address("0x015fc611579b182f9eddaf3662514c999974bed2"): Account(
            storage={0: 0xe178ab0c8c219833cb17090483147b44af97ea74},
        ),
        Address("0x02660b1fc1d262f440733e8787f6ca21fb55bcd4"): Account(
            storage={0: 0x73714e7e266d879bafd2cb37528e2169cb508514},
        ),
        Address("0x03b30e6dcce89e39590901b797c16935f14cfe7d"): Account(
            storage={0: 0x4aea3bd98ccc05d8b80d0225a47258fd9ead31b4},
        ),
        Address("0x03cd9f61e105543325910d9d7f8427235a29e850"): Account(
            storage={0: 0x502e8922fff35256c92f22f970802241c85a875b},
        ),
        Address("0x0563ece055f8043c2fa7eae79f85a5974e2459ad"): Account(
            storage={0: 0x2a5afab4b1b210196e2f8d6ddb24d7d1a3e8a365},
        ),
        Address("0x05f76726986912c1fbda22db3aafdd295dc833aa"): Account(
            storage={0: 0x5553af7faaa8eb68de8787e8022dda0c58bed06e},
        ),
        Address("0x061b1ef6ec7572d0837a557a5d673d95d645cb8a"): Account(
            storage={0: 0x21e2e15b2af6454ad91e1b36e3830238cf755b49},
        ),
        Address("0x078fcf5f2a71a260b50b04efe2feede4a4155f42"): Account(
            storage={0: 0x38cdbb61fc5323dd5f6f4aa599d4f36406b766ff},
        ),
        Address("0x07d4c830ba3d7b13dd3435b6a9de7f2bdcf90bc7"): Account(
            storage={0: 0xf610a2a3a281686a9d78073eeb0a5f6a4619213c},
        ),
        Address("0x089a70486f0cc448c7e5ac2ba11a9f71b970808e"): Account(
            storage={0: 0x69ad22b81f58d128a7736328fdac92d7dfd63cef},
        ),
        Address("0x08e3ffdc8d29af262542744f4d400983fe31c590"): Account(
            storage={0: 0x52aea75e06e98440b2daa28313d03c31129acef7},
        ),
        Address("0x094439b76fdd228f193958d098d2c8bf6238de1c"): Account(
            storage={0: 0xb83f1b5b2f0fb059368e680b040b1dc118db2587},
        ),
        contract: Account(
            storage={0: 0xd2571607e241ecf590ed94b12d87c94babe36db7},
            code=Op.CODECOPY(dest_offset=0x0, offset=0x0, size=0x20) + Op.SSTORE(key=0x0, value=Op.ADD(Op.CREATE(value=0x0, offset=0x0, size=0x20), 0x1)) + Op.STOP,
        ),
        Address("0x09a35a6f6607eebc286c6b5194a213370bcadb30"): Account(
            storage={0: 0x18205df1c43e9e29920725e96a362260aa5d3242},
        ),
        Address("0x0a3fdfc866b2404c1ed78d478482c0f5107ce776"): Account(
            storage={0: 0xe8849b2d422c4231af55a706bcf7572f38f7a01a},
        ),
        Address("0x0b057f3d7be9b4be7edf09b66f0a154da6a46ae4"): Account(
            storage={0: 0x350a4186374a87dc45cada137c2eed0022e23f0e},
        ),
        Address("0x0b7cdb850b37437912005a1b54b1306452425679"): Account(
            storage={0: 0x33c0b6cb54994491d359af637dfb34e3065c98c7},
        ),
        Address("0x0b9ee042a78ff660da0c6bd6fee0b2e22b414c03"): Account(
            storage={0: 0x26a1838800d9131a3e7d3ee0a43d2f0122746fb5},
        ),
        Address("0x0d3bc01519ee0a1216a632b99c19a06df8017c6b"): Account(
            storage={0: 0x9a35a6f6607eebc286c6b5194a213370bcadb31},
        ),
        Address("0x0e0f3dc21b49a768b9933909a09531de8198f0a9"): Account(
            storage={0: 0x81cd35ac42bc6c520c5c41640dec4c9a3a9de9d2},
        ),
        Address("0x0f4f5cf7567448a171b08d58c9fcfc8c1acc0aa9"): Account(
            storage={0: 0xd4f5a4a0a9770c53e8a43e80dfddfe30ddc67a2b},
        ),
        Address("0x10b3a8c098467317d86d530931b7424dd8a74f3c"): Account(
            storage={0: 0x8fa40127106dbf70f7931ddd510e2f0211dfd15e},
        ),
        Address("0x11802a2c1f85a5da238086378dc4820ccd19134f"): Account(
            storage={0: 0x9aae8b11a923f49fcab42904f8c6759fcbad37fa},
        ),
        Address("0x135dde330f78ca8bdf3c694ea49d08065d49bdfd"): Account(
            storage={0: 0xd454705bbb4750ff5d62cbf2a5134d02b272db17},
        ),
        Address("0x138de55ad30a7e72b8d19a27048203c0297a7750"): Account(
            storage={0: 0xdf1050bdf2c8617339324e68a1e6e0e102e3ca32},
        ),
        Address("0x13e0f4c536fc64dc3b82fa9055f717783566a99e"): Account(
            storage={0: 0x230dd0589ed6366c0c89dc257ed902fc4e6648e4},
        ),
        Address("0x14a6985982a43b5fcc2046c3d5ba3622e5ca00d2"): Account(
            storage={0: 0x4132baf092924fcb4b3185213462643a64e00670},
        ),
        Address("0x14aef68e79d441e5d9fa6a397c8ea11fdaa111c8"): Account(
            storage={0: 0x7e641e26dfac957ede0a2b9ca358ea9082150052},
        ),
        Address("0x15533643df9a543582de7d814e1cd06c8d93ce73"): Account(
            storage={0: 0xa95abf1f117ec9cba5da9412ab5776299f19c9cd},
        ),
        Address("0x18205df1c43e9e29920725e96a362260aa5d3241"): Account(
            storage={0: 0x29133526942f54e611d0dee32bbb3386cf1c891c},
        ),
        Address("0x1902813a7606ced9e69222e4d756bd81bde3eff5"): Account(
            storage={0: 0x812f8f7534d22508b43fc38e7679a3c5756d8e43},
        ),
        Address("0x19a0689c7c59dbbe8a569b594572abdc7bd5c77c"): Account(
            storage={0: 0xe0f3dc21b49a768b9933909a09531de8198f0aa},
        ),
        Address("0x1a21d699163a7f697a68977ce1fb21887d59cd7c"): Account(
            storage={0: 0xb651a1e8312709eae2dc95103bbe7fca9e6e3574},
        ),
        Address("0x1c38fae029602412d3789f348541577249bee123"): Account(
            storage={0: 0xba80321b067a71fc689104a602a589634a5f76cd},
        ),
        Address("0x1cf9918897600e9c9e17f7c6e2797ed8fdd8af10"): Account(
            storage={0: 0x90f83fce5fb9bbecb55981c96f223f044786c40e},
        ),
        Address("0x1d9cb40fa087e41cb84a4d56ad104226e3d6f018"): Account(
            storage={0: 0xdc963c747dded8c966cca2e13c10a65cf04cefc5},
        ),
        Address("0x1e22452e40c125d338ca6b53c49773da2e3760eb"): Account(
            storage={0: 0x4e2634d8427a529403ecdd1d44aa6dd137da4625},
        ),
        Address("0x1ec3bf52d870e0226044c2c0e84f0cd2883bbd92"): Account(
            storage={0: 0x58675e090154b7e827e68883b3b9ecaf1c8bb8d5},
        ),
        Address("0x1f1af23e708f4720910cb4ca9f83ef0188a23f0a"): Account(
            storage={0: 0x3206fb12e53a9eea5a1d4501394042fc9333aeeb},
        ),
        Address("0x1fd0c0883bd94f7a6a87a7a216359f1dbfab7f51"): Account(
            storage={0: 0x68610b9db9ea182ff1921fab9863150d1849c5f6},
        ),
        Address("0x21e2e15b2af6454ad91e1b36e3830238cf755b48"): Account(
            storage={0: 0xf9a151d133c315854462c5653437e34656cfdc38},
        ),
        Address("0x22f1aff96e05248331ec9f15270c5552d665f41e"): Account(
            storage={0: 0x2460590bf5fcc3d6e76cf72004944265b8ecdc14},
        ),
        Address("0x230dd0589ed6366c0c89dc257ed902fc4e6648e3"): Account(
            storage={0: 0x4f7b7c8e24bf233866a0fad0ac657226de940b64},
        ),
        Address("0x23192662f87a4ab3db2759748c755d819e59cd2a"): Account(
            storage={0: 0x4a53eaa64b683d0c95b5ba0b681b64cfd95e5e40},
        ),
        Address("0x2460590bf5fcc3d6e76cf72004944265b8ecdc13"): Account(
            storage={0: 0x683013d2114cae8b41473ca318267c7db219b8a0},
        ),
        Address("0x24a18b9ffe06edc928eb9037ef40c9b24349d9ea"): Account(
            storage={0: 0xe53a708ed6f6ef523576e12ddf568c79d25b79f8},
        ),
        Address("0x24aafb1cf6510457d2a4aa39512393b490b24c61"): Account(
            storage={0: 0x854c4f512b9ecc17467e602f6512496a89d5705d},
        ),
        Address("0x2566a11ad8ac081e7c26ba1afff8d1c208642f5d"): Account(
            storage={0: 0x2852018b3ce85cb2d700b9fb8699a2ecdad0dc0b},
        ),
        Address("0x25d8caa13d191aefbbc4a6b2f60ac679a2a56e00"): Account(
            storage={0: 0x4bd7b245f707b5fdb259c3fe61dac9255cb8bb25},
        ),
        Address("0x26963175b50e69c2400aa12887cad973aa275ff0"): Account(
            storage={0: 0x923945f4390ee06a73a80c1f56f979f7959755e0},
        ),
        Address("0x26a1838800d9131a3e7d3ee0a43d2f0122746fb4"): Account(
            storage={0: 0x5ee8a44ac78e6c8e2db3297dba0e4e0e61b08de5},
        ),
        Address("0x270fb896f474137cc0a51ac5cfa01e01994da981"): Account(
            storage={0: 0xaa0a91be8c06c9ba16ce1ce5836941e920ca9afa},
        ),
        Address("0x283b585ba5bc85d64a99cb5ecb9a8495ac944948"): Account(
            storage={0: 0x4326e4b5aa29095a293f86c51e4776beeeb13c9c},
        ),
        Address("0x2852018b3ce85cb2d700b9fb8699a2ecdad0dc0a"): Account(
            storage={0: 0x3ca9b7faddd261997977e206a2f288b4b8374666},
        ),
        Address("0x28cc863e08832ad7b9c1b28bfa2fbff5a1611745"): Account(
            storage={0: 0x3cd9f61e105543325910d9d7f8427235a29e851},
        ),
        Address("0x29133526942f54e611d0dee32bbb3386cf1c891b"): Account(
            storage={0: 0xb0f2564f0a4cb0d593a648d256b69b4ecdaa036b},
        ),
        Address("0x295cac445bfac8cb2244bc70cdb32d99594d47e3"): Account(
            storage={0: 0xae3fe33dc09c697bfb635c9ab4bf8f0bf4264680},
        ),
        Address("0x29ba5a51398ab1b9a6e68f9afe8a08c301e098f0"): Account(
            storage={0: 0x6473f78ce5e4e31a7057ef32b70dcb9e3afd1d87},
        ),
        Address("0x2a5afab4b1b210196e2f8d6ddb24d7d1a3e8a364"): Account(
            storage={0: 0xbd5649faf8bcc002dc4a58e3a58dc0ff4413e20e},
        ),
        Address("0x2a8c62782a9ac9ad37ceed561522cf5279e80fed"): Account(
            storage={0: 0x23192662f87a4ab3db2759748c755d819e59cd2b},
        ),
        Address("0x2b26fac300d8a9bab12c79d8374726af0e2eec13"): Account(
            storage={0: 0x632465eed4e41f3aaaaac5bb576838cb3f0ea943},
        ),
        Address("0x2c0b3f7eba30e844978dd6a58127cca7fa9dd329"): Account(
            storage={0: 0x94f69c9e63cf82c2f3a04943b4c57909d99397e6},
        ),
        Address("0x2ccf72ae225fbeddf894606c87629c42f685ea77"): Account(
            storage={0: 0x687dccb33dc4dfa5e5dea197c151095a4e19fdd3},
        ),
        Address("0x2cec8e078d4f0b40547db5134af753177afb7157"): Account(
            storage={0: 0xbabbd30645c383315b3f157d518ab54f22465ab3},
        ),
        Address("0x2ea5d28deea6fd475333f03590fadb6a29514936"): Account(
            storage={0: 0x2660b1fc1d262f440733e8787f6ca21fb55bcd5},
        ),
        Address("0x2eccfda404dee5308012197c894b86789921ca30"): Account(
            storage={0: 0x4e11236c11ebdec00068c3c1997937935290a1ee},
        ),
        Address("0x2fa655ac7839b95773bb43a5ca5bdd636c1c3f42"): Account(
            storage={0: 0x94439b76fdd228f193958d098d2c8bf6238de1d},
        ),
        Address("0x3043fe71ffbc8cc57fc0e4373b9a2106dfa64402"): Account(
            storage={0: 0xadcc47cd626cc70a6326f9858e889932aec7487d},
        ),
        Address("0x3206fb12e53a9eea5a1d4501394042fc9333aeea"): Account(
            storage={0: 0xd85fdff87cf6d94195cf56b5e9ad410e936ac125},
        ),
        Address("0x33c0b6cb54994491d359af637dfb34e3065c98c6"): Account(
            storage={0: 0x1a21d699163a7f697a68977ce1fb21887d59cd7d},
        ),
        Address("0x3435a3a9c7a82796be5c2bf306e39132482b146a"): Account(
            storage={0: 0x41871652222884569a03b4f357441dec29dd4c04},
        ),
        Address("0x350a4186374a87dc45cada137c2eed0022e23f0d"): Account(
            storage={0: 0x3c3efeb193be9bdcc59a190ba343b7aa51ab3418},
        ),
        Address("0x3515873bc24d6721857b331afbb9d2e18099e79f"): Account(
            storage={0: 0xaeec6641cb72fb4f1839cf9df13fa59b80d91e34},
        ),
        Address("0x359d51cf93b31de8b40707b6c1b22f8f1b70a336"): Account(
            storage={0: 0x49d4ef28805e87178cafc25b34e0f4fa720a7a57},
        ),
        Address("0x35e9444cc45b5659787356b9a03a82789e5f6c37"): Account(
            storage={0: 0x5718e750d8554e12e6aa9f5eaad8f9858b4049df},
        ),
        Address("0x35ed71279933c3412f3277b383d1f8ed491d0196"): Account(
            storage={0: 0xcbaf2598fc92602ba5debac6782965149d2d371f},
        ),
        Address("0x3846f21bbb8c38b4cccce0236b1f0c9e3c0d7ed2"): Account(
            storage={0: 0x9b5b0f5d4e3ebc57965b4bb63d9ffca825eb8cc7},
        ),
        Address("0x38a10d085030b351f1e4522bd42c789e2718ff9a"): Account(
            storage={0: 0x25d8caa13d191aefbbc4a6b2f60ac679a2a56e01},
        ),
        Address("0x38cdbb61fc5323dd5f6f4aa599d4f36406b766fe"): Account(
            storage={0: 0x6e6ab35a1c5454676d10e4e1f462030bb4dc00d8},
        ),
        Address("0x39670caa919437d736560edef3f698ed952a836c"): Account(
            storage={0: 0xd41572cab02800c2dc729a8d03332f572de96277},
        ),
        Address("0x39bcb9056a944f0955dba921096bbc2ef4025942"): Account(
            storage={0: 0xa2998816bc7b076ae2573878d1d8e599223652a6},
        ),
        Address("0x3b1d2e5cb2f280a25afddefb35cbce1754421341"): Account(
            storage={0: 0xac2d104f5688a6d5c4498132f916602e4af9254c},
        ),
        Address("0x3bd18e0f7e4d743565dacc89d36faa37c70bbb41"): Account(
            storage={0: 0x4889ebf7ecb03869ec2f481276f46f8c02dc0ec5},
        ),
        Address("0x3c3efeb193be9bdcc59a190ba343b7aa51ab3417"): Account(
            storage={0: 0x124ac36deebf89244c22bedfcb6e05fb2f62f3c},
        ),
        Address("0x3ca9b7faddd261997977e206a2f288b4b8374665"): Account(
            storage={0: 0x7360e396473716a4fb94022e3b5fe49ac5efd989},
        ),
        Address("0x3dc54aa1f5987de1e630798ab223bd724f2eafeb"): Account(
            storage={0: 0x24aafb1cf6510457d2a4aa39512393b490b24c62},
        ),
        Address("0x3e705425914e5043a7fe28a422494fbddd1fa0b7"): Account(
            storage={0: 0x5e370cb559f97e00c4ccff71324fcfc1d0f4f52b},
        ),
        Address("0x4132baf092924fcb4b3185213462643a64e0066f"): Account(
            storage={0: 0x80bf7cc16403098d8db95ef9f802b168337aff8c},
        ),
        Address("0x4163459a50d3f33505101c03a67798d9aaff86a7"): Account(
            storage={0: 0x9e9c39c1f8f48a4c7d92d2bead877287715d3ef2},
        ),
        Address("0x41871652222884569a03b4f357441dec29dd4c03"): Account(
            storage={0: 0x3515873bc24d6721857b331afbb9d2e18099e7a0},
        ),
        Address("0x41c744f06610636c5f3a78acf7019671046bbb17"): Account(
            storage={0: 0x1902813a7606ced9e69222e4d756bd81bde3eff6},
        ),
        Address("0x420d3ebd21ac77b879ff7d60d91a4178d88da386"): Account(
            storage={0: 0x2ccf72ae225fbeddf894606c87629c42f685ea78},
        ),
        Address("0x4326e4b5aa29095a293f86c51e4776beeeb13c9b"): Account(
            storage={0: 0x26963175b50e69c2400aa12887cad973aa275ff1},
        ),
        Address("0x44392aa670f14348e65eaace495fe52fb1f0276c"): Account(
            storage={0: 0xee2618f6774250978c45b19de72dc9568eb06a14},
        ),
        Address("0x4889ebf7ecb03869ec2f481276f46f8c02dc0ec4"): Account(
            storage={0: 0xda27862cfde315dd4db961ae77d0e70eaf09c36b},
        ),
        Address("0x49d4ef28805e87178cafc25b34e0f4fa720a7a56"): Account(
            storage={0: 0xf0f5be7cfbe4ed7e2ee8c2949fdbdee6bc283621},
        ),
        Address("0x4a53eaa64b683d0c95b5ba0b681b64cfd95e5e3f"): Account(
            storage={0: 0x7f16b98de9de619a80a6cbd8721896f9870b01cb},
        ),
        Address("0x4aea3bd98ccc05d8b80d0225a47258fd9ead31b3"): Account(
            storage={0: 0x4c6cf3cd7e2089b5624a20feb57bd012e9337188},
        ),
        Address("0x4b503c8ea51caa8f3617973b8068c89f787e3f36"): Account(
            storage={0: 0xf89eec0743bac4cee8ee6ad04a821e09232a2fb6},
        ),
        Address("0x4bd7b245f707b5fdb259c3fe61dac9255cb8bb24"): Account(
            storage={0: 0xc928a97a6e85c0a06e6d7bc17aea51059acc533c},
        ),
        Address("0x4bdd7ba923660706078f4f1b5f11b3ef68267f8c"): Account(
            storage={0: 0x5d72a22e4d2f63e5adcf14699cc9306fba181ab8},
        ),
        Address("0x4be74ed02236365b2796309e9725fb380ca539eb"): Account(
            storage={0: 0x8a26224559ea93f4eb25c5d7a9df4ca7bcadebbd},
        ),
        Address("0x4c356bcbb80f0903fb14144a2040ffb35fc15fbc"): Account(
            storage={0: 0xc50549cd84f0f605f2787c3861c80db90af82e96},
        ),
        Address("0x4c6cf3cd7e2089b5624a20feb57bd012e9337187"): Account(
            storage={0: 0xa563d05cdf426b6dcc4353ebae2acd475b854c8c},
        ),
        Address("0x4d439e47505b6556114b968a9eb09a09c8074198"): Account(
            storage={0: 0xacfd156153124afdbc8a9404d3aa431e6621e59f},
        ),
        Address("0x4e11236c11ebdec00068c3c1997937935290a1ed"): Account(
            storage={0: 0x51c2f19b94b6ec398d71fd6b748b1d4f04d0696c},
        ),
        Address("0x4e2634d8427a529403ecdd1d44aa6dd137da4624"): Account(
            storage={0: 0x11802a2c1f85a5da238086378dc4820ccd191350},
        ),
        Address("0x4f7b7c8e24bf233866a0fad0ac657226de940b63"): Account(
            storage={0: 0xe6b02f114be963fc082526163d31bd78b9e906f8},
        ),
        Address("0x502e8922fff35256c92f22f970802241c85a875a"): Account(
            storage={0: 0x90f7031246d07c171c746ca8d0b5ac0c4a3b8bd2},
        ),
        Address("0x504ee43710737cf77785cfa9774c812584c40979"): Account(
            storage={0: 0xb4bd0b1eb4ea1c0730a80a3c635c2ca2995d83d0},
        ),
        Address("0x51c2f19b94b6ec398d71fd6b748b1d4f04d0696b"): Account(
            storage={0: 0x91a66cb6ea7854ca76ca6bcb6441e801dd046580},
        ),
        Address("0x528648dcb94ec4db2a1adc469cc6e4aeecab70f1"): Account(
            storage={0: 0x86f8ac4309c8386f45df0fb9658ee6c0abe59155},
        ),
        Address("0x52aea75e06e98440b2daa28313d03c31129acef6"): Account(
            storage={0: 0x782cc3ff4fd6be97eca0737e6772f96731cb75b3},
        ),
        Address("0x53652ad6f344eec5e2b9e33b816ad9163998d0aa"): Account(
            storage={0: 0xf0c49beea4b33147fd5d8940e30349c739b97626},
        ),
        Address("0x551b0315698442787a7791ccfaee559fa18480a5"): Account(
            storage={0: 0xd28566158cfa53f25ef6228228a227a8700b6883},
        ),
        Address("0x551cc3090c98d0e0a07c34e7f7219d1139fede7e"): Account(
            storage={0: 0xb057f3d7be9b4be7edf09b66f0a154da6a46ae5},
        ),
        Address("0x552cb7ef312124663550f57d159fe2d03a05ef69"): Account(
            storage={0: 0x28cc863e08832ad7b9c1b28bfa2fbff5a1611746},
        ),
        Address("0x5553af7faaa8eb68de8787e8022dda0c58bed06d"): Account(
            storage={0: 0x35e9444cc45b5659787356b9a03a82789e5f6c38},
        ),
        Address("0x56aaf858af96546df92985645d7f456c530bc0d1"): Account(
            storage={0: 0xf8ff2045b963a3dcfbcc41f79f930a96af8becc1},
        ),
        Address("0x5718e750d8554e12e6aa9f5eaad8f9858b4049de"): Account(
            storage={0: 0xb16dd4f11693f1157aec4a982de406463bb2b715},
        ),
        Address("0x576cfefd063104a0e03717593a425e69863b1736"): Account(
            storage={0: 0x22f1aff96e05248331ec9f15270c5552d665f41f},
        ),
        Address("0x57906c3c5ec33e754f23ddefe0cf9e80e9170dbc"): Account(
            storage={0: 0x39670caa919437d736560edef3f698ed952a836d},
        ),
        Address("0x58660d7c9e7b1d306dbf86fa4c975eb9e9a25452"): Account(
            storage={0: 0x53652ad6f344eec5e2b9e33b816ad9163998d0ab},
        ),
        Address("0x58675e090154b7e827e68883b3b9ecaf1c8bb8d4"): Account(
            storage={0: 0xecf592d553a78ea9eb580651a22d34f635a36011},
        ),
        Address("0x5d72a22e4d2f63e5adcf14699cc9306fba181ab7"): Account(
            storage={0: 0x38a10d085030b351f1e4522bd42c789e2718ff9b},
        ),
        Address("0x5e370cb559f97e00c4ccff71324fcfc1d0f4f52a"): Account(
            storage={0: 0xb5cd7c146eadd4dd6788a453c8ea2db89df35b07},
        ),
        Address("0x5ee8a44ac78e6c8e2db3297dba0e4e0e61b08de4"): Account(
            storage={0: 0x3dc54aa1f5987de1e630798ab223bd724f2eafec},
        ),
        Address("0x5f630aa382bd9cd2e33754130a500db2dc0109f2"): Account(
            storage={0: 0xf22fd55ac64a4b6f96bee3771818c73341cd4d05},
        ),
        Address("0x606ab504d721676914e421c96c9c9907fa329386"): Account(
            storage={0: 0x75a2a617b94f78ecfff896fc7d7a55c8a000b149},
        ),
        Address("0x60a9bf51b795423799851fdd8671858554886415"): Account(
            storage={0: 0x135dde330f78ca8bdf3c694ea49d08065d49bdfe},
        ),
        Address("0x6224dfbaf1cccbe1f486789567ec41b633fe7562"): Account(
            storage={0: 0x872d846f9cfd4e4a80106a89f75a79105b8a18e1},
        ),
        Address("0x6252860664c6175b92453fbc567a66251f764853"): Account(
            storage={0: 0xdc2b1f4f871b90b2232e02bb7a114f88831338a3},
        ),
        Address("0x632465eed4e41f3aaaaac5bb576838cb3f0ea942"): Account(
            storage={0: 0xd0204eceaa9950caea0162fe07fd1dc84d1244e9},
        ),
        Address("0x63c0e98de8f3816f46eaefe7f8797dbcdaa01ff8"): Account(
            storage={0: 0xe2d49548ef5acace79d3aa334fbda460a0662efc},
        ),
        Address("0x63c7a6d6988214080daca01dd8fa02ba7143e86c"): Account(
            storage={0: 0xe60264d9ec4d7c93f8cfb6b1f47ecae4c099a3c2},
        ),
        Address("0x63db02c046296069b0c31419b1549f4e27e59cac"): Account(
            storage={0: 0x678e131646361f7722be1d0cdfd0a4e79767f2f8},
        ),
        Address("0x647123dbfb8f16b4dd98fac0e86d8e780f4aefe8"): Account(
            storage={0: 0x9b6263a8f6b9c8eb400ea447ad7f66102047d500},
        ),
        Address("0x6473f78ce5e4e31a7057ef32b70dcb9e3afd1d86"): Account(
            storage={0: 0x24a18b9ffe06edc928eb9037ef40c9b24349d9eb},
        ),
        Address("0x64a3e2a2ea958c6647add08ad95b9ab6972fb558"): Account(
            storage={0: 0xa6ca5f3180992a52ca65843e9922baa1e715a14b},
        ),
        Address("0x6559462bb07df725d804c6c3eb11f86488cb8f34"): Account(
            storage={0: 0x2b26fac300d8a9bab12c79d8374726af0e2eec14},
        ),
        Address("0x66e84b7af7d89cf1e05b902eb34fa4a75fb4371b"): Account(
            storage={0: 0x1f1af23e708f4720910cb4ca9f83ef0188a23f0b},
        ),
        Address("0x66fddf0c330ee5edcb4854883d27e9e01213de2c"): Account(
            storage={0: 0xbc15fcea3abf3edd959316d68ef6c6c01611869f},
        ),
        Address("0x678e131646361f7722be1d0cdfd0a4e79767f2f7"): Account(
            storage={0: 0xf41adf0227f6556206527e96f729cf6260fbebe0},
        ),
        Address("0x683013d2114cae8b41473ca318267c7db219b89f"): Account(
            storage={0: 0xccc2223346b6ff188191b5ab747e75ac90388a37},
        ),
        Address("0x68610b9db9ea182ff1921fab9863150d1849c5f5"): Account(
            storage={0: 0x93321908d7923818d3caedba4fe206138dc9c322},
        ),
        Address("0x687dccb33dc4dfa5e5dea197c151095a4e19fdd2"): Account(
            storage={0: 0xe53e22d617f23da57fb232dee4f8afa03b5960a2},
        ),
        Address("0x6965235e025001fb620d441803fedb005f7ac710"): Account(
            storage={0: 0x283b585ba5bc85d64a99cb5ecb9a8495ac944949},
        ),
        Address("0x69ad22b81f58d128a7736328fdac92d7dfd63cee"): Account(
            storage={0: 0x13e0f4c536fc64dc3b82fa9055f717783566a99f},
        ),
        Address("0x6a49ef58af93afcda6eb267bb7f082b36868771a"): Account(
            storage={0: 0xdf71363d94e67de4bc54ebae9a5ddcadfb4be71b},
        ),
        Address("0x6b61d79d8680a739ac957dc2309a722b8d587d86"): Account(
            storage={0: 0x138de55ad30a7e72b8d19a27048203c0297a7751},
        ),
        Address("0x6b6856673ca8777e1e08b9448f3dcc902c7656e4"): Account(
            storage={0: 0x2cec8e078d4f0b40547db5134af753177afb7158},
        ),
        Address("0x6c36ae21a70aecc27860c44f7424dfc409d56a44"): Account(
            storage={0: 0x15533643df9a543582de7d814e1cd06c8d93ce74},
        ),
        Address("0x6e6ab35a1c5454676d10e4e1f462030bb4dc00d7"): Account(
            storage={0: 0xfb2413a3ebe46beeb6ce7350f7a0110aed31fafa},
        ),
        Address("0x6e6ed53d9520671e00646b51160cc7ba65dc7ae3"): Account(
            storage={0: 0x15fc611579b182f9eddaf3662514c999974bed3},
        ),
        Address("0x705055cea2b5eead57e7f2b2451bd151f692259a"): Account(
            storage={0: 0xe878ad7340c78ca7a62ad9fc0ca05a00368d5705},
        ),
        Address("0x7262c537e8b7c65f5fb1183478d802c05e847c89"): Account(
            storage={0: 0x8142d2fe5b473e4819d9477f93d137c4fc03acb9},
        ),
        Address("0x72a2277942502b64d1b9d7273f3e0bf70c9959af"): Account(
            storage={0: 0x8aa608ff16f8b19413561959d8c221bd2c13408b},
        ),
        Address("0x72d03f30e5e592eba13e4f38a578e7bb37001ac3"): Account(
            storage={0: 0x78fcf5f2a71a260b50b04efe2feede4a4155f43},
        ),
        Address("0x7360e396473716a4fb94022e3b5fe49ac5efd988"): Account(
            storage={0: 0xe24b78e82b9f3052fae947427821b8bfc9e58181},
        ),
        Address("0x73714e7e266d879bafd2cb37528e2169cb508513"): Account(
            storage={0: 0x66fddf0c330ee5edcb4854883d27e9e01213de2d},
        ),
        Address("0x74298cb3d811abc2a7cabee9aaf9e32d1f0dda46"): Account(
            storage={0: 0x8600fb81735e28330dd83b581f8fd160c4c7f7e6},
        ),
        Address("0x74ace49be181f5733c773d34e1f0a4a651cb4c87"): Account(
            storage={0: 0x8be0154a131c2e2296748939688b11c3a9330a5e},
        ),
        Address("0x74db82093ec212c48163e5cc87c62842d4f0298f"): Account(
            storage={0: 0xa0a40e0ce528a8924656630e2c85faad3b20e763},
        ),
        Address("0x74e34b17132ede1d8c0f02b06954a19d0bda0a00"): Account(
            storage={0: 0x9b0fb1e205c2c42f0bfe448ffe62cf16959eede1},
        ),
        Address("0x759101d9f01353039f5785449cf3eaf8c5f2b50b"): Account(
            storage={0: 0x910c972a81e9a2d07ea2d582103703fa5c1e6e64},
        ),
        Address("0x75a2a617b94f78ecfff896fc7d7a55c8a000b148"): Account(
            storage={0: 0xab9bbc26a4438d3c46652f51cc78516cc875790a},
        ),
        Address("0x782cc3ff4fd6be97eca0737e6772f96731cb75b2"): Account(
            storage={0: 0x9e4e90382b3d41cd05242850ab52f2066e944fcc},
        ),
        Address("0x7840b2c702362fd49bed617e921503950a1dce07"): Account(
            storage={0: 0x74298cb3d811abc2a7cabee9aaf9e32d1f0dda47},
        ),
        Address("0x788be3440d2c6fd3d071c54c503cfa485813924f"): Account(
            storage={0: 0xcc78e0755e700914cc0082d847836fe20fbabacd},
        ),
        Address("0x78e4c25b1965b3027e42c8be47c912bcf7343dca"): Account(
            storage={0: 0x7840b2c702362fd49bed617e921503950a1dce08},
        ),
        Address("0x7960e69b2bfda2f03bacdacdd87e3042223eb9db"): Account(
            storage={0: 0xdb7a5d82b82f7fe75af931f626740bd651b1713d},
        ),
        Address("0x799be994d950d06c04996073ea4494dd2a0a438e"): Account(
            storage={0: 0xad8fc1a395db2c84e5b943c19d9977cf29f2ba05},
        ),
        Address("0x79f1fdc03b73036a99412bf37dc7bb535ca65002"): Account(
            storage={0: 0xf4f5cf7567448a171b08d58c9fcfc8c1acc0aaa},
        ),
        Address("0x7a5601bc727e42164cab285c9f7cab96d434e14a"): Account(
            storage={0: 0x88f2abf6a3fb18f836f2b69d368162244331a036},
        ),
        Address("0x7aca2ed7a1e6f7b82f47a6b20607819f15007ebf"): Account(
            storage={0: 0x4d439e47505b6556114b968a9eb09a09c8074199},
        ),
        Address("0x7b43a066271d7ef10f66f8c652064db040c8fa8c"): Account(
            storage={0: 0x3bd18e0f7e4d743565dacc89d36faa37c70bbb42},
        ),
        Address("0x7bbde03011a48d70bcc79c120c28177d1c7667d5"): Account(
            storage={0: 0x3b1d2e5cb2f280a25afddefb35cbce1754421342},
        ),
        Address("0x7e495061f514448f3dd51bb0cf909eef3c3f4712"): Account(
            storage={0: 0xb1fe911acf07cc8107d984408a443c5af42389e1},
        ),
        Address("0x7e641e26dfac957ede0a2b9ca358ea9082150051"): Account(
            storage={0: 0xb3a36932e89006258cd41594a66fd217465aa0fb},
        ),
        Address("0x7f16b98de9de619a80a6cbd8721896f9870b01ca"): Account(
            storage={0: 0x551b0315698442787a7791ccfaee559fa18480a6},
        ),
        Address("0x80bf7cc16403098d8db95ef9f802b168337aff8b"): Account(
            storage={0: 0xa60ebc9287019330b003770ec548fb7f38d3a021},
        ),
        Address("0x812f8f7534d22508b43fc38e7679a3c5756d8e42"): Account(
            storage={0: 0x8ec4b51809eb738f7bbbac138f5f33fbf9ca46d9},
        ),
        Address("0x8142d2fe5b473e4819d9477f93d137c4fc03acb8"): Account(
            storage={0: 0xb90320de803c40f7a1ee25482c4758c908872250},
        ),
        Address("0x81b7c9ad8bf567196485da9d114dfc8eb77cd426"): Account(
            storage={0: 0x552cb7ef312124663550f57d159fe2d03a05ef6a},
        ),
        Address("0x81cd35ac42bc6c520c5c41640dec4c9a3a9de9d1"): Account(
            storage={0: 0x705055cea2b5eead57e7f2b2451bd151f692259b},
        ),
        Address("0x8200a1966873be093601ab0ed1b06d7297307834"): Account(
            storage={0: 0xdd03b49d9974ca4eee27114f78463675ba13ce3d},
        ),
        Address("0x825ffa59b7cd20192e871732df014067950a339c"): Account(
            storage={0: 0xc8cbd95130a1e15bd93c9bf678fdfe4e4b04c147},
        ),
        Address("0x84dd24d594f6d2d7991b7fcc96cb3dbe15396aaf"): Account(
            storage={0: 0xa63723e01e6bd3d3cfb739ebb745e5be82571d3c},
        ),
        Address("0x854a2da430c3b5657ff41b9c3cbd5fc72525d31f"): Account(
            storage={0: 0x60a9bf51b795423799851fdd8671858554886416},
        ),
        Address("0x854c4f512b9ecc17467e602f6512496a89d5705c"): Account(
            storage={0: 0x8a1137c56e3e63637336431b883d5ae8008a4fbf},
        ),
        Address("0x8600fb81735e28330dd83b581f8fd160c4c7f7e5"): Account(
            storage={0: 0x5f630aa382bd9cd2e33754130a500db2dc0109f3},
        ),
        Address("0x86f8ac4309c8386f45df0fb9658ee6c0abe59154"): Account(
            storage={0: 0x295cac445bfac8cb2244bc70cdb32d99594d47e4},
        ),
        Address("0x870080f904af2582e08624580c2e0b69f261ff21"): Account(
            storage={0: 0xf1f45715a43fef3ad11aaf60910e0fd0ed2b3feb},
        ),
        Address("0x872d846f9cfd4e4a80106a89f75a79105b8a18e0"): Account(
            storage={0: 0x4c356bcbb80f0903fb14144a2040ffb35fc15fbd},
        ),
        Address("0x88f2abf6a3fb18f836f2b69d368162244331a035"): Account(
            storage={0: 0x29ba5a51398ab1b9a6e68f9afe8a08c301e098f1},
        ),
        Address("0x8a1137c56e3e63637336431b883d5ae8008a4fbe"): Account(
            storage={0: 0xeee14f748174f224761d6be0a65dd4cb4cfb8fee},
        ),
        Address("0x8a26224559ea93f4eb25c5d7a9df4ca7bcadebbc"): Account(
            storage={0: 0x1ec3bf52d870e0226044c2c0e84f0cd2883bbd93},
        ),
        Address("0x8a59b09be87866145ecf0506298de203b1d10cb9"): Account(
            storage={0: 0xe3df7661083a3bcc1f459826aa8936831a90b985},
        ),
        Address("0x8aa608ff16f8b19413561959d8c221bd2c13408a"): Account(
            storage={0: 0xba6933ceffd2fb8d9dea6b18817108e44f32ae95},
        ),
        Address("0x8ae3c9da496eea395020df847f542f9d6af31310"): Account(
            storage={0: 0xb22c14d45949e3b53947b6c7fcc5132c8b041381},
        ),
        Address("0x8be0154a131c2e2296748939688b11c3a9330a5d"): Account(
            storage={0: 0x79f1fdc03b73036a99412bf37dc7bb535ca65003},
        ),
        Address("0x8cf4d1a905bb50ffbaaf359e63fb7cdf0dc33428"): Account(
            storage={0: 0xd27caf5f748dc645c35bfb970494e3da492bf97d},
        ),
        Address("0x8ec4b51809eb738f7bbbac138f5f33fbf9ca46d8"): Account(
            storage={0: 0xfb79e8d788245fdf3328e3b74fad52eff821481e},
        ),
        Address("0x8ed58354ec6fd381d608771c3eeff99b1422b840"): Account(
            storage={0: 0xc3f7ab15f0973e66575bc8b987435b78e541442d},
        ),
        Address("0x8fa40127106dbf70f7931ddd510e2f0211dfd15d"): Account(
            storage={0: 0x61b1ef6ec7572d0837a557a5d673d95d645cb8b},
        ),
        Address("0x8fd38e52d47dcb6cf8252e3ceb99ab2fa983cb1d"): Account(
            storage={0: 0x5f76726986912c1fbda22db3aafdd295dc833ab},
        ),
        Address("0x8fe5d9c1ce55fb9d72ad33d25d46758ecbd9f806"): Account(
            storage={0: 0x3435a3a9c7a82796be5c2bf306e39132482b146b},
        ),
        Address("0x90f7031246d07c171c746ca8d0b5ac0c4a3b8bd1"): Account(
            storage={0: 0xdaf24907563344e025b30baa8aa25e4b4c37eaf5},
        ),
        Address("0x90f83fce5fb9bbecb55981c96f223f044786c40d"): Account(
            storage={0: 0xb08fe65db809f8efa5bb5cf2fd2d2a1f45f7c453},
        ),
        Address("0x910c972a81e9a2d07ea2d582103703fa5c1e6e63"): Account(
            storage={0: 0x1c38fae029602412d3789f348541577249bee124},
        ),
        Address("0x91a66cb6ea7854ca76ca6bcb6441e801dd04657f"): Account(
            storage={0: 0x153629ea98627274192fa275a6a9ad20191ab04},
        ),
        Address("0x91ed00a0a906270d466af043c4e111dadca970a3"): Account(
            storage={0: 0xb679828fa6040990410b3282e916bfbd6c74f891},
        ),
        Address("0x9212a0150ffaecc685aff0e94d15e75d8079c527"): Account(
            storage={0: 0x14a6985982a43b5fcc2046c3d5ba3622e5ca00d3},
        ),
        Address("0x923945f4390ee06a73a80c1f56f979f7959755df"): Account(
            storage={0: 0xec51d36be1c8fd3ff3c74210e408a8710163ceb9},
        ),
        Address("0x93321908d7923818d3caedba4fe206138dc9c321"): Account(
            storage={0: 0x7a5601bc727e42164cab285c9f7cab96d434e14b},
        ),
        Address("0x94f69c9e63cf82c2f3a04943b4c57909d99397e5"): Account(
            storage={0: 0xd5a313463930d740250c19f53d6ea3fe596d18aa},
        ),
        Address("0x953fe148abf5e5d1b957446919f7d460fb8e0e04"): Account(
            storage={0: 0xafb048240716cb7c59aa3322a6845ab7250080a8},
        ),
        Address("0x9586ce20c98a913a4ce397ff5d9443de21df9f04"): Account(
            storage={0: 0x8e3ffdc8d29af262542744f4d400983fe31c591},
        ),
        Address("0x964b8be9139d7c7100e34018979d17d83005748b"): Account(
            storage={0: 0xd25f4f651d67b188b5ad87d9976b02585c2f3116},
        ),
        Address("0x98f02c7f4f6f0c1ad8bff7411e07af88404ccfa2"): Account(
            storage={0: 0x4163459a50d3f33505101c03a67798d9aaff86a8},
        ),
        Address("0x996d22e0533ff751ab345656c14a5159df187211"): Account(
            storage={0: 0x6b61d79d8680a739ac957dc2309a722b8d587d87},
        ),
        Address("0x9aae8b11a923f49fcab42904f8c6759fcbad37f9"): Account(
            storage={0: 0xb650ecfe63d1f0cd6fa262334621f60b09ef1598},
        ),
        Address("0x9b0fb1e205c2c42f0bfe448ffe62cf16959eede0"): Account(
            storage={0: 0x8200a1966873be093601ab0ed1b06d7297307835},
        ),
        Address("0x9b5b0f5d4e3ebc57965b4bb63d9ffca825eb8cc6"): Account(
            storage={0: 0xc11ac6e735399ccc13f277b7e0d14accfcbdfd5d},
        ),
        Address("0x9b6263a8f6b9c8eb400ea447ad7f66102047d4ff"): Account(
            storage={0: 0xb9ee042a78ff660da0c6bd6fee0b2e22b414c04},
        ),
        Address("0x9bcc019a0001b920dbf169c44d1fb6896e223254"): Account(
            storage={0: 0xe9a9082e1eee305d59b35c5d0a4fbeccdedfd9bd},
        ),
        Address("0x9e4e90382b3d41cd05242850ab52f2066e944fcb"): Account(
            storage={0: 0xf0350f749f60c4700f1bb72e4757d424137dbce7},
        ),
        Address("0x9e9c39c1f8f48a4c7d92d2bead877287715d3ef1"): Account(
            storage={0: 0xd8c4c59e7cc8fde66a855d1fc636f8df05e38103},
        ),
        Address("0x9f21fb734cd0e961d27de46f5fd806e7fb8e96cd"): Account(
            storage={0: 0x72d03f30e5e592eba13e4f38a578e7bb37001ac4},
        ),
        Address("0xa0a40e0ce528a8924656630e2c85faad3b20e762"): Account(
            storage={0: 0x6252860664c6175b92453fbc567a66251f764854},
        ),
        Address("0xa2998816bc7b076ae2573878d1d8e599223652a5"): Account(
            storage={0: 0x6e6ed53d9520671e00646b51160cc7ba65dc7ae4},
        ),
        Address("0xa563d05cdf426b6dcc4353ebae2acd475b854c8b"): Account(
            storage={0: 0xc0427bdc9ec7678c5bfd7a55c2e71f084e02016e},
        ),
        Address("0xa60ebc9287019330b003770ec548fb7f38d3a020"): Account(
            storage={0: 0x6224dfbaf1cccbe1f486789567ec41b633fe7563},
        ),
        Address("0xa63723e01e6bd3d3cfb739ebb745e5be82571d3b"): Account(
            storage={0: 0x57906c3c5ec33e754f23ddefe0cf9e80e9170dbd},
        ),
        Address("0xa6ca5f3180992a52ca65843e9922baa1e715a14a"): Account(
            storage={0: 0x606ab504d721676914e421c96c9c9907fa329387},
        ),
        Address("0xa9150d0b2a6611206daab64ef804dcec594ef5f9"): Account(
            storage={0: 0x359d51cf93b31de8b40707b6c1b22f8f1b70a337},
        ),
        Address("0xa95abf1f117ec9cba5da9412ab5776299f19c9cc"): Account(
            storage={0: 0x9f21fb734cd0e961d27de46f5fd806e7fb8e96ce},
        ),
        Address("0xaa0a91be8c06c9ba16ce1ce5836941e920ca9af9"): Account(
            storage={0: 0x759101d9f01353039f5785449cf3eaf8c5f2b50c},
        ),
        Address("0xab9bbc26a4438d3c46652f51cc78516cc8757909"): Account(
            storage={0: 0x6b6856673ca8777e1e08b9448f3dcc902c7656e5},
        ),
        Address("0xac2d104f5688a6d5c4498132f916602e4af9254b"): Account(
            storage={0: 0x44392aa670f14348e65eaace495fe52fb1f0276d},
        ),
        Address("0xaca4bb8422d054c48dc6b614cd712eb7cb25fb8d"): Account(
            storage={0: 0x9bcc019a0001b920dbf169c44d1fb6896e223255},
        ),
        Address("0xacfd156153124afdbc8a9404d3aa431e6621e59e"): Account(
            storage={0: 0x647123dbfb8f16b4dd98fac0e86d8e780f4aefe9},
        ),
        Address("0xad8fc1a395db2c84e5b943c19d9977cf29f2ba04"): Account(
            storage={0: 0xd2261c1645cbbd7422cc42c8f317bfe74053a495},
        ),
        Address("0xadcc47cd626cc70a6326f9858e889932aec7487c"): Account(
            storage={0: 0x14aef68e79d441e5d9fa6a397c8ea11fdaa111c9},
        ),
        Address("0xae3fe33dc09c697bfb635c9ab4bf8f0bf426467f"): Account(
            storage={0: 0x8a59b09be87866145ecf0506298de203b1d10cba},
        ),
        Address("0xaeec6641cb72fb4f1839cf9df13fa59b80d91e33"): Account(
            storage={0: 0x7aca2ed7a1e6f7b82f47a6b20607819f15007ec0},
        ),
        Address("0xafb048240716cb7c59aa3322a6845ab7250080a7"): Account(
            storage={0: 0x10b3a8c098467317d86d530931b7424dd8a74f3d},
        ),
        Address("0xb0117629d3e337ac0f2937b29d4c913bda81d962"): Account(
            storage={0: 0x72a2277942502b64d1b9d7273f3e0bf70c9959b0},
        ),
        Address("0xb08fe65db809f8efa5bb5cf2fd2d2a1f45f7c452"): Account(
            storage={0: 0x576cfefd063104a0e03717593a425e69863b1737},
        ),
        Address("0xb0e9e2634bfacae0505f803d5507d5afaeb78d84"): Account(
            storage={0: 0x3e705425914e5043a7fe28a422494fbddd1fa0b8},
        ),
        Address("0xb0f2564f0a4cb0d593a648d256b69b4ecdaa036a"): Account(
            storage={0: 0xe18c58dd8e5f9a3e0711112d5393563586e63320},
        ),
        Address("0xb16dd4f11693f1157aec4a982de406463bb2b714"): Account(
            storage={0: 0x63db02c046296069b0c31419b1549f4e27e59cad},
        ),
        Address("0xb1aa49d81f87a70ead4809b17ebbc7c8ac43089c"): Account(
            storage={0: 0x8cf4d1a905bb50ffbaaf359e63fb7cdf0dc33429},
        ),
        Address("0xb1fe911acf07cc8107d984408a443c5af42389e0"): Account(
            storage={0: 0xfa39c0440bdb586ab891b5b0a2db29d81c2068fa},
        ),
        Address("0xb22c14d45949e3b53947b6c7fcc5132c8b041380"): Account(
            storage={0: 0x41c744f06610636c5f3a78acf7019671046bbb18},
        ),
        Address("0xb3a36932e89006258cd41594a66fd217465aa0fa"): Account(
            storage={0: 0x58660d7c9e7b1d306dbf86fa4c975eb9e9a25453},
        ),
        Address("0xb4bd0b1eb4ea1c0730a80a3c635c2ca2995d83cf"): Account(
            storage={0: 0x81b7c9ad8bf567196485da9d114dfc8eb77cd427},
        ),
        Address("0xb52eaef155fa7e16b29c6d65342567f71d6501f3"): Account(
            storage={0: 0x2eccfda404dee5308012197c894b86789921ca31},
        ),
        Address("0xb5cb668cdf8a1bf46fd5baadfb7ae5e0271879c0"): Account(
            storage={0: 0xb0e9e2634bfacae0505f803d5507d5afaeb78d85},
        ),
        Address("0xb5cd7c146eadd4dd6788a453c8ea2db89df35b06"): Account(
            storage={0: 0xcd1b84945f85266bc3eaf65c3c2d6fe47521353a},
        ),
        Address("0xb650ecfe63d1f0cd6fa262334621f60b09ef1597"): Account(
            storage={0: 0x2ea5d28deea6fd475333f03590fadb6a29514937},
        ),
        Address("0xb651a1e8312709eae2dc95103bbe7fca9e6e3573"): Account(
            storage={0: 0x420d3ebd21ac77b879ff7d60d91a4178d88da387},
        ),
        Address("0xb679828fa6040990410b3282e916bfbd6c74f890"): Account(
            storage={0: 0x6965235e025001fb620d441803fedb005f7ac711},
        ),
        Address("0xb83f1b5b2f0fb059368e680b040b1dc118db2586"): Account(
            storage={0: 0xb52eaef155fa7e16b29c6d65342567f71d6501f4},
        ),
        Address("0xb90320de803c40f7a1ee25482c4758c90887224f"): Account(
            storage={0: 0x35ed71279933c3412f3277b383d1f8ed491d0197},
        ),
        Address("0xb94539ff043ed6f9e56e2a06ca170f05013d23a8"): Account(
            storage={0: 0xf64c3ef1b6468d63c6119d7ba03e10196b8585a9},
        ),
        Address("0xba6933ceffd2fb8d9dea6b18817108e44f32ae94"): Account(
            storage={0: 0x7960e69b2bfda2f03bacdacdd87e3042223eb9dc},
        ),
        Address("0xba80321b067a71fc689104a602a589634a5f76cc"): Account(
            storage={0: 0xccf9f53823c1162df56358db1b8389c5df3d2119},
        ),
        Address("0xbabbd30645c383315b3f157d518ab54f22465ab2"): Account(
            storage={0: 0x7bbde03011a48d70bcc79c120c28177d1c7667d6},
        ),
        Address("0xbad86da28de3a7d068479aa21c26bd0cef848adf"): Account(
            storage={0: 0xfad1cc360b83e277c5df214536a634cbec266a1c},
        ),
        Address("0xbbc2aea32a7763bf59ea9157274f20e73c47210d"): Account(
            storage={0: 0x2c0b3f7eba30e844978dd6a58127cca7fa9dd32a},
        ),
        Address("0xbc15fcea3abf3edd959316d68ef6c6c01611869e"): Account(
            storage={0: 0x996d22e0533ff751ab345656c14a5159df187212},
        ),
        Address("0xbc1ad174b38e4a427dcf903c04c1db5862bd1130"): Account(
            storage={0: 0x4bdd7ba923660706078f4f1b5f11b3ef68267f8d},
        ),
        Address("0xbd5649faf8bcc002dc4a58e3a58dc0ff4413e20d"): Account(
            storage={0: 0x6559462bb07df725d804c6c3eb11f86488cb8f35},
        ),
        Address("0xc0427bdc9ec7678c5bfd7a55c2e71f084e02016d"): Account(
            storage={0: 0x89a70486f0cc448c7e5ac2ba11a9f71b970808f},
        ),
        Address("0xc11ac6e735399ccc13f277b7e0d14accfcbdfd5c"): Account(
            storage={0: 0x3043fe71ffbc8cc57fc0e4373b9a2106dfa64403},
        ),
        Address("0xc1c10fad7c38dca307a3623fb8a78b8c191d7bd8"): Account(
            storage={0: 0xfeccdb40b5dbcd1993aa688e95a183b40ed76a06},
        ),
        Address("0xc3e5e4000ed488092bd820cf94d0a52e7a072e37"): Account(
            storage={0: 0xaca4bb8422d054c48dc6b614cd712eb7cb25fb8e},
        ),
        Address("0xc3f7ab15f0973e66575bc8b987435b78e541442c"): Account(
            storage={0: 0x504ee43710737cf77785cfa9774c812584c4097a},
        ),
        Address("0xc50549cd84f0f605f2787c3861c80db90af82e95"): Account(
            storage={0: 0x84dd24d594f6d2d7991b7fcc96cb3dbe15396ab0},
        ),
        Address("0xc514bbdbe823fe790b5fadbafd713452c4664051"): Account(
            storage={0: 0xf46269856da75ae565825a9795ce581de90047db},
        ),
        Address("0xc54066516aee09a32006c21475dfe31b6c06b41c"): Account(
            storage={0: 0xb94539ff043ed6f9e56e2a06ca170f05013d23a9},
        ),
        Address("0xc750f2459a31030bc412e28d6b8ac9920bd5af5e"): Account(
            storage={0: 0x8ed58354ec6fd381d608771c3eeff99b1422b841},
        ),
        Address("0xc77a90da618a4b5066b130e6ba2934e70f78183c"): Account(
            storage={0: 0xc750f2459a31030bc412e28d6b8ac9920bd5af5f},
        ),
        Address("0xc8cbd95130a1e15bd93c9bf678fdfe4e4b04c146"): Account(
            storage={0: 0xfd6287deb8f1d10bdb5ca199af8f8129a6443894},
        ),
        Address("0xc928a97a6e85c0a06e6d7bc17aea51059acc533b"): Account(
            storage={0: 0xc77a90da618a4b5066b130e6ba2934e70f78183d},
        ),
        Address("0xcbaf2598fc92602ba5debac6782965149d2d371e"): Account(
            storage={0: 0x270fb896f474137cc0a51ac5cfa01e01994da982},
        ),
        Address("0xcc78e0755e700914cc0082d847836fe20fbabacc"): Account(
            storage={0: 0x6a49ef58af93afcda6eb267bb7f082b36868771b},
        ),
        Address("0xcc7da81f5f8612dc269b8acc1db3327100597646"): Account(
            storage={0: 0x74ace49be181f5733c773d34e1f0a4a651cb4c88},
        ),
        Address("0xccc2223346b6ff188191b5ab747e75ac90388a36"): Account(
            storage={0: 0x1d9cb40fa087e41cb84a4d56ad104226e3d6f019},
        ),
        Address("0xccee3bdd325f22421d250412d7d6edff7c1b9ceb"): Account(
            storage={0: 0x63c7a6d6988214080daca01dd8fa02ba7143e86d},
        ),
        Address("0xccf9f53823c1162df56358db1b8389c5df3d2118"): Account(
            storage={0: 0x7d4c830ba3d7b13dd3435b6a9de7f2bdcf90bc8},
        ),
        Address("0xcd1b84945f85266bc3eaf65c3c2d6fe475213539"): Account(
            storage={0: 0x7262c537e8b7c65f5fb1183478d802c05e847c8a},
        ),
        Address("0xd0204eceaa9950caea0162fe07fd1dc84d1244e8"): Account(
            storage={0: 0x63c0e98de8f3816f46eaefe7f8797dbcdaa01ff9},
        ),
        Address("0xd2261c1645cbbd7422cc42c8f317bfe74053a494"): Account(
            storage={0: 0xd3a7d8ebc95c90cc78de4ba3d795aaa2fe444d5c},
        ),
        Address("0xd2571607e241ecf590ed94b12d87c94babe36db6"): Account(
            storage={0: 0x91ed00a0a906270d466af043c4e111dadca970a4},
        ),
        Address("0xd25f4f651d67b188b5ad87d9976b02585c2f3115"): Account(
            storage={0: 0xccee3bdd325f22421d250412d7d6edff7c1b9cec},
        ),
        Address("0xd27caf5f748dc645c35bfb970494e3da492bf97c"): Account(
            storage={0: 0xe33483cade7ba1732161f33edf083cb797b576b2},
        ),
        Address("0xd28566158cfa53f25ef6228228a227a8700b6882"): Account(
            storage={0: 0xf66ef7ec17f226c5af3af4f6ded9c6a9539f1fbd},
        ),
        Address("0xd3a7d8ebc95c90cc78de4ba3d795aaa2fe444d5b"): Account(storage={0: 1}),
        Address("0xd41572cab02800c2dc729a8d03332f572de96276"): Account(
            storage={0: 0xc3e5e4000ed488092bd820cf94d0a52e7a072e38},
        ),
        Address("0xd454705bbb4750ff5d62cbf2a5134d02b272db16"): Account(
            storage={0: 0x6c36ae21a70aecc27860c44f7424dfc409d56a45},
        ),
        Address("0xd4c40012e56397cf9ee6f19e278ab28fabd9ad9b"): Account(
            storage={0: 0x9212a0150ffaecc685aff0e94d15e75d8079c528},
        ),
        Address("0xd4f5a4a0a9770c53e8a43e80dfddfe30ddc67a2a"): Account(
            storage={0: 0x3b30e6dcce89e39590901b797c16935f14cfe7e},
        ),
        Address("0xd5a313463930d740250c19f53d6ea3fe596d18a9"): Account(
            storage={0: 0x1e22452e40c125d338ca6b53c49773da2e3760ec},
        ),
        Address("0xd85fdff87cf6d94195cf56b5e9ad410e936ac124"): Account(
            storage={0: 0x563ece055f8043c2fa7eae79f85a5974e2459ae},
        ),
        Address("0xd8c4c59e7cc8fde66a855d1fc636f8df05e38102"): Account(
            storage={0: 0xff10977181344b4af1385688b8e9a4fb6848d0d0},
        ),
        Address("0xda27862cfde315dd4db961ae77d0e70eaf09c36a"): Account(
            storage={0: 0x3846f21bbb8c38b4cccce0236b1f0c9e3c0d7ed3},
        ),
        Address("0xda3864f09aba17cd282a26dface1e193f1611801"): Account(
            storage={0: 0x98f02c7f4f6f0c1ad8bff7411e07af88404ccfa3},
        ),
        Address("0xdaf24907563344e025b30baa8aa25e4b4c37eaf4"): Account(
            storage={0: 0xef3fb25bd47c023518e9427e300b142698b4d650},
        ),
        Address("0xdb7a5d82b82f7fe75af931f626740bd651b1713c"): Account(
            storage={0: 0x8ae3c9da496eea395020df847f542f9d6af31311},
        ),
        Address("0xdc2b1f4f871b90b2232e02bb7a114f88831338a2"): Account(
            storage={0: 0x4b503c8ea51caa8f3617973b8068c89f787e3f37},
        ),
        Address("0xdc963c747dded8c966cca2e13c10a65cf04cefc4"): Account(
            storage={0: 0x8fe5d9c1ce55fb9d72ad33d25d46758ecbd9f807},
        ),
        Address("0xdd03b49d9974ca4eee27114f78463675ba13ce3c"): Account(
            storage={0: 0x56aaf858af96546df92985645d7f456c530bc0d2},
        ),
        Address("0xdf1050bdf2c8617339324e68a1e6e0e102e3ca31"): Account(
            storage={0: 0x39bcb9056a944f0955dba921096bbc2ef4025943},
        ),
        Address("0xdf71363d94e67de4bc54ebae9a5ddcadfb4be71a"): Account(
            storage={0: 0x9586ce20c98a913a4ce397ff5d9443de21df9f05},
        ),
        Address("0xe178ab0c8c219833cb17090483147b44af97ea73"): Account(
            storage={0: 0x64a3e2a2ea958c6647add08ad95b9ab6972fb559},
        ),
        Address("0xe18c58dd8e5f9a3e0711112d5393563586e6331f"): Account(
            storage={0: 0x964b8be9139d7c7100e34018979d17d83005748c},
        ),
        Address("0xe24b78e82b9f3052fae947427821b8bfc9e58180"): Account(
            storage={0: 0x78e4c25b1965b3027e42c8be47c912bcf7343dcb},
        ),
        Address("0xe2d49548ef5acace79d3aa334fbda460a0662efb"): Account(
            storage={0: 0x2a8c62782a9ac9ad37ceed561522cf5279e80fee},
        ),
        Address("0xe33483cade7ba1732161f33edf083cb797b576b1"): Account(
            storage={0: 0xf2680e26d01ed858391494603d73dcda518b999e},
        ),
        Address("0xe3df7661083a3bcc1f459826aa8936831a90b984"): Account(
            storage={0: 0xb7cdb850b37437912005a1b54b130645242567a},
        ),
        Address("0xe3e9fd3c13583a0afe10d63a0d4a83e3469dfe3d"): Account(
            storage={0: 0x4be74ed02236365b2796309e9725fb380ca539ec},
        ),
        Address("0xe53a708ed6f6ef523576e12ddf568c79d25b79f7"): Account(
            storage={0: 0xb0117629d3e337ac0f2937b29d4c913bda81d963},
        ),
        Address("0xe53e22d617f23da57fb232dee4f8afa03b5960a1"): Account(
            storage={0: 0x870080f904af2582e08624580c2e0b69f261ff22},
        ),
        Address("0xe60264d9ec4d7c93f8cfb6b1f47ecae4c099a3c1"): Account(
            storage={0: 0xe3e9fd3c13583a0afe10d63a0d4a83e3469dfe3e},
        ),
        Address("0xe66f534f19722097ca4296330805aa61c330a0b2"): Account(
            storage={0: 0x19a0689c7c59dbbe8a569b594572abdc7bd5c77d},
        ),
        Address("0xe6b02f114be963fc082526163d31bd78b9e906f7"): Account(
            storage={0: 0x799be994d950d06c04996073ea4494dd2a0a438f},
        ),
        Address("0xe878ad7340c78ca7a62ad9fc0ca05a00368d5704"): Account(
            storage={0: 0x74e34b17132ede1d8c0f02b06954a19d0bda0a01},
        ),
        Address("0xe8849b2d422c4231af55a706bcf7572f38f7a019"): Account(
            storage={0: 0x1fd0c0883bd94f7a6a87a7a216359f1dbfab7f52},
        ),
        Address("0xe9a9082e1eee305d59b35c5d0a4fbeccdedfd9bc"): Account(
            storage={0: 0xcc7da81f5f8612dc269b8acc1db3327100597647},
        ),
        Address("0xec51d36be1c8fd3ff3c74210e408a8710163ceb8"): Account(
            storage={0: 0x7e495061f514448f3dd51bb0cf909eef3c3f4713},
        ),
        Address("0xecf592d553a78ea9eb580651a22d34f635a36010"): Account(
            storage={0: 0x2566a11ad8ac081e7c26ba1afff8d1c208642f5e},
        ),
        Address("0xee2618f6774250978c45b19de72dc9568eb06a13"): Account(
            storage={0: 0xda3864f09aba17cd282a26dface1e193f1611802},
        ),
        Address("0xeee14f748174f224761d6be0a65dd4cb4cfb8fed"): Account(
            storage={0: 0x66e84b7af7d89cf1e05b902eb34fa4a75fb4371c},
        ),
        Address("0xef3fb25bd47c023518e9427e300b142698b4d64f"): Account(
            storage={0: 0x74db82093ec212c48163e5cc87c62842d4f02990},
        ),
        Address("0xf0350f749f60c4700f1bb72e4757d424137dbce6"): Account(
            storage={0: 0xb1aa49d81f87a70ead4809b17ebbc7c8ac43089d},
        ),
        Address("0xf05ba15908d728019c3e10a8e6f3da341ae34963"): Account(
            storage={0: 0x1cf9918897600e9c9e17f7c6e2797ed8fdd8af11},
        ),
        Address("0xf0c49beea4b33147fd5d8940e30349c739b97625"): Account(
            storage={0: 0x788be3440d2c6fd3d071c54c503cfa4858139250},
        ),
        Address("0xf0f5be7cfbe4ed7e2ee8c2949fdbdee6bc283620"): Account(
            storage={0: 0x8fd38e52d47dcb6cf8252e3ceb99ab2fa983cb1e},
        ),
        Address("0xf1f45715a43fef3ad11aaf60910e0fd0ed2b3fea"): Account(
            storage={0: 0xf05ba15908d728019c3e10a8e6f3da341ae34964},
        ),
        Address("0xf22fd55ac64a4b6f96bee3771818c73341cd4d04"): Account(
            storage={0: 0x854a2da430c3b5657ff41b9c3cbd5fc72525d320},
        ),
        Address("0xf2680e26d01ed858391494603d73dcda518b999d"): Account(
            storage={0: 0xc514bbdbe823fe790b5fadbafd713452c4664052},
        ),
        Address("0xf41adf0227f6556206527e96f729cf6260fbebdf"): Account(
            storage={0: 0xd3bc01519ee0a1216a632b99c19a06df8017c6c},
        ),
        Address("0xf46269856da75ae565825a9795ce581de90047da"): Account(
            storage={0: 0xbc1ad174b38e4a427dcf903c04c1db5862bd1131},
        ),
        Address("0xf610a2a3a281686a9d78073eeb0a5f6a4619213b"): Account(
            storage={0: 0xd4c40012e56397cf9ee6f19e278ab28fabd9ad9c},
        ),
        Address("0xf64c3ef1b6468d63c6119d7ba03e10196b8585a8"): Account(
            storage={0: 0x2fa655ac7839b95773bb43a5ca5bdd636c1c3f43},
        ),
        Address("0xf66ef7ec17f226c5af3af4f6ded9c6a9539f1fbc"): Account(
            storage={0: 0xb5cb668cdf8a1bf46fd5baadfb7ae5e0271879c1},
        ),
        Address("0xf89eec0743bac4cee8ee6ad04a821e09232a2fb5"): Account(
            storage={0: 0x825ffa59b7cd20192e871732df014067950a339d},
        ),
        Address("0xf8ff2045b963a3dcfbcc41f79f930a96af8becc0"): Account(
            storage={0: 0xc1c10fad7c38dca307a3623fb8a78b8c191d7bd9},
        ),
        Address("0xf9a151d133c315854462c5653437e34656cfdc37"): Account(
            storage={0: 0xbad86da28de3a7d068479aa21c26bd0cef848ae0},
        ),
        Address("0xfa39c0440bdb586ab891b5b0a2db29d81c2068f9"): Account(
            storage={0: 0x551cc3090c98d0e0a07c34e7f7219d1139fede7f},
        ),
        Address("0xfad1cc360b83e277c5df214536a634cbec266a1b"): Account(
            storage={0: 0xa3fdfc866b2404c1ed78d478482c0f5107ce777},
        ),
        Address("0xfb2413a3ebe46beeb6ce7350f7a0110aed31faf9"): Account(
            storage={0: 0xc54066516aee09a32006c21475dfe31b6c06b41d},
        ),
        Address("0xfb79e8d788245fdf3328e3b74fad52eff821481d"): Account(
            storage={0: 0xe66f534f19722097ca4296330805aa61c330a0b3},
        ),
        Address("0xfd6287deb8f1d10bdb5ca199af8f8129a6443893"): Account(
            storage={0: 0x528648dcb94ec4db2a1adc469cc6e4aeecab70f2},
        ),
        Address("0xfeccdb40b5dbcd1993aa688e95a183b40ed76a05"): Account(
            storage={0: 0x7b43a066271d7ef10f66f8c652064db040c8fa8d},
        ),
        Address("0xff10977181344b4af1385688b8e9a4fb6848d0cf"): Account(
            storage={0: 0xa9150d0b2a6611206daab64ef804dcec594ef5fa},
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
