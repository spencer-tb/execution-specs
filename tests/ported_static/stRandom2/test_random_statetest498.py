"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest498Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest498Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest498(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x1a819dd2e8cec87d7e886df4843e21775f6672a4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6bd243dbcfdc6982733e4cd6261574fc6cdec93282ff50ef24d8be05d58be29301ddb00d"  # noqa: E501
            "7547f6b65997e73d232b76d6484c11eb15c87b01f89e2779c427711ba193e4e163967efd"  # noqa: E501
            "1b9315187c3227f67b9282fc7524692fbf851cb370d396d53f7a86353aacecc5c1eadedd"  # noqa: E501
            "bb3925522f935fc5ed03568fbf40261c056a124f1334cc9fa8eea2bdbf68f04c10cc08b6"  # noqa: E501
            "babcbb6ee8d3fb88dd42d06d445b5eab34cb5d64408cf652fd7568acaa81b573f66fa878"  # noqa: E501
            "1e83185438e42796631ae9a9987f714d986f94fc6354921a9367bb6b9e555f24107cb814"  # noqa: E501
            "557f8bd87547ad612c3e726f9f495b0ac9e37fbe5f23014c68d8d032bfae779a5213c337"  # noqa: E501
            "78af679417d77733645f87b6042be92c553dbb6d85a2c56b21a53c0e612ae0a8d78d60f1"  # noqa: E501
            "62b52efea464ebb0472b3e7794198cdb286cd2f21f06659320130750e7aa2c83ceb28015"  # noqa: E501
            "55785c9f02455252560846587006e90cbffc955445d9ef1f55eeb07011c02cee02df12dc"  # noqa: E501
            "35b36702539873e4b766e4ae9e829a442460dd7f845cd37dc08f93bef98a4d5b53ecd4cf"  # noqa: E501
            "4dd1a5c416f92116160f0fb673c30b7873b85a2ff6331a5d371f3d109f5794d712e03493"  # noqa: E501
            "b17fc562ac7589411127e654ce32d273f8300cc8544e7bd782aa7828b543958dadf872d7"  # noqa: E501
            "f13401a51b13835cc8a36be87cc7347cdf0f7aa2df420bb03e925c117d4befbc7e69472f"  # noqa: E501
            "d75f01f3f6c966de818174aba3b7a43014c3dd39414fb3d239d72e06852ae48e6203c60a"  # noqa: E501
            "7e844d6fd61c5b519d43780d383d103989f9bfce5ed122804cba183c188f5ce47c348a96"  # noqa: E501
            "973eca904f096aed4fb77d40ca9139447527f267a028eae5e3706e1975fc3e38327505e8"  # noqa: E501
            "1d0e8c9fab1f60ec7ece71cc87510f308984ebdcb8ab84e1905dfdc0a19ee3c5f37e88dc"  # noqa: E501
            "3a9f26497c51427da28f6d777d9585b4ec790722bacaa179b1dc5b086d945623f9d29f60"  # noqa: E501
            "13600c60096019634f4421eb731a819dd2e8cec87d7e886df4843e21775f6672a4631ac7"  # noqa: E501
            "54faf17506f9cc63229e7fe309b7a2f1acf074a43aa4dd2b75bf6dadf21aadb9a3e239a9"  # noqa: E501
            "592f576c9265eebd2420e2626d2b2f1f7ee7a56725d7d4fe23da45725e8b709d29767031"  # noqa: E501
            "47ef66a8fc9a6c1225df7b79eec95ddda5e91c6e19bbc55baf9d6c440cc805f0d229738d"  # noqa: E501
            "17a76f95e329f94d5bc48cc5964933f9597fb57a6f7290649722d68a72fa2d081c454794"  # noqa: E501
            "3b3bbca2edc5f4032c5c916e585fa6abd1b209e2b6fb64498a37b9796c95da3fdb8013c1"  # noqa: E501
            "3ef99ed49b29282ae55458c651fdb8598b527024d2da1e8a7015f65ee4ab0178b68ab8c8"  # noqa: E501
            "77d55f3c89a7f1f7bc6c0d86bc69688cbcc252972693993bf766aac4efb2b65b216cca2e"  # noqa: E501
            "721dea3f3b3df3abbbfb7b8d"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=bytes.fromhex("6000355415600957005b60203560003555"),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "7349d4fb4fa5c26263087f9f9885a7033ed1f85282806175626c7aff6e85d032f987501c"  # noqa: E501
            "7f07e672602eea9a752c14f2fea044cbadb4acbbbece186bfae0ddfa5c3a4f602e867451"  # noqa: E501
            "6e7ead3a1b9f0c321f53474588f38a996f7512fbdf364372a2f5b5329a5866cb8867c095"  # noqa: E501
            "26eabd04524486650cba94b9d20e8079263be537932206f67f64915b81ac1ea4b1f3723b"  # noqa: E501
            "aa86b2d9ad667f11ff36b05f0ec27d14051ce250c5c524eaa31472f153582c9aafa7a0b3"  # noqa: E501
            "17230863944f1b5e7444ad06685190a6f9ff72b7af0f52a4619591d022037c3bd19aa01d"  # noqa: E501
            "358a540c4ec6e43870dc653bab5c707f953b919477ed89448472e11b10e241ad82a32be0"  # noqa: E501
            "2adf21cd183ae47f2776bce3701b75afea9a175cd04e616f3a1913f3be49294c5e633b4d"  # noqa: E501
            "01cf719e06325d1f498e74d5a153c41ba83f49339f6d7f4711edfa5370e2ee9c7986401c"  # noqa: E501
            "6b27b5cb4f46435c84c8f0239876415740df4646423c790ce1917c3e178e3f0117f07b8a"  # noqa: E501
            "e37a6353868f7ca9313379cd727ae9732fb0a56da2b8a4cb682eb38ca47df0353f6b9322"  # noqa: E501
            "ac474740ac5b14488677765f48677e720ed20e2c76b94ca77acdd3e9e54f2230a0c2d120"  # noqa: E501
            "3130ebbf95aeb6212d52393d33efa63f79c2feba7168b770a3cd3fa97b8b515fd38a1995"  # noqa: E501
            "8fccde6ec198be7d2f780422a69c9047ab7474d8f1c3272b9836bca4050a856a916e9bb3"  # noqa: E501
            "0724727d1ba26058199098d65ad54d5580e51dcb2bd077db415b0ff41457c68f61d0f86d"  # noqa: E501
            "8c4c549388abf78a75cc9163016c7e988e60e97b95f1d253b52168cbb01407c8ebca87f9"  # noqa: E501
            "50ca4049e12ac76cbe3e374065a3c7703bcd5f7af279a1c12425c93ef8e74a12b699f4a9"  # noqa: E501
            "c651db15561be1d91ca95575636dad39636bea70b5309b3354a73bb1b83ba72ff63f6918"  # noqa: E501
            "2888e8f17d3e1ec0367173eb3831614e653fc63989af65bc9b676645638915ede2603666"  # noqa: E501
            "ccff0c03af0fda7ad7b7e846076158daad3df7ad07e1cfe8ce41757c4d77f02d65bee264"  # noqa: E501
            "fe0a98374a61532e797167af5719a427a267234fa27697f1a3f47a1453ea150821da1c66"  # noqa: E501
            "5de7878ac0e5e26fc78911427cc1d8d0b029ee09bf9322446635d50de718ecb79f"  # noqa: E501
        ),
        gas_limit=824267821,
        gas_price=10,
        nonce=0,
        value=1958828689,
    )

    post = {
        contract: Account(
            storage={
                0x94198CDB286CD2F21F06659320130750E7AA2C83CEB28015: 0xEBB0472B3E,  # noqa: E501
            },
            code=bytes.fromhex(
                "6bd243dbcfdc6982733e4cd6261574fc6cdec93282ff50ef24d8be05d58be29301ddb00d7547f6b65997e73d232b76d6484c11eb15c87b01f89e2779c427711ba193e4e163967efd1b9315187c3227f67b9282fc7524692fbf851cb370d396d53f7a86353aacecc5c1eadeddbb3925522f935fc5ed03568fbf40261c056a124f1334cc9fa8eea2bdbf68f04c10cc08b6babcbb6ee8d3fb88dd42d06d445b5eab34cb5d64408cf652fd7568acaa81b573f66fa8781e83185438e42796631ae9a9987f714d986f94fc6354921a9367bb6b9e555f24107cb814557f8bd87547ad612c3e726f9f495b0ac9e37fbe5f23014c68d8d032bfae779a5213c33778af679417d77733645f87b6042be92c553dbb6d85a2c56b21a53c0e612ae0a8d78d60f162b52efea464ebb0472b3e7794198cdb286cd2f21f06659320130750e7aa2c83ceb2801555785c9f02455252560846587006e90cbffc955445d9ef1f55eeb07011c02cee02df12dc35b36702539873e4b766e4ae9e829a442460dd7f845cd37dc08f93bef98a4d5b53ecd4cf4dd1a5c416f92116160f0fb673c30b7873b85a2ff6331a5d371f3d109f5794d712e03493b17fc562ac7589411127e654ce32d273f8300cc8544e7bd782aa7828b543958dadf872d7f13401a51b13835cc8a36be87cc7347cdf0f7aa2df420bb03e925c117d4befbc7e69472fd75f01f3f6c966de818174aba3b7a43014c3dd39414fb3d239d72e06852ae48e6203c60a7e844d6fd61c5b519d43780d383d103989f9bfce5ed122804cba183c188f5ce47c348a96973eca904f096aed4fb77d40ca9139447527f267a028eae5e3706e1975fc3e38327505e81d0e8c9fab1f60ec7ece71cc87510f308984ebdcb8ab84e1905dfdc0a19ee3c5f37e88dc3a9f26497c51427da28f6d777d9585b4ec790722bacaa179b1dc5b086d945623f9d29f6013600c60096019634f4421eb731a819dd2e8cec87d7e886df4843e21775f6672a4631ac754faf17506f9cc63229e7fe309b7a2f1acf074a43aa4dd2b75bf6dadf21aadb9a3e239a9592f576c9265eebd2420e2626d2b2f1f7ee7a56725d7d4fe23da45725e8b709d2976703147ef66a8fc9a6c1225df7b79eec95ddda5e91c6e19bbc55baf9d6c440cc805f0d229738d17a76f95e329f94d5bc48cc5964933f9597fb57a6f7290649722d68a72fa2d081c4547943b3bbca2edc5f4032c5c916e585fa6abd1b209e2b6fb64498a37b9796c95da3fdb8013c13ef99ed49b29282ae55458c651fdb8598b527024d2da1e8a7015f65ee4ab0178b68ab8c877d55f3c89a7f1f7bc6c0d86bc69688cbcc252972693993bf766aac4efb2b65b216cca2e721dea3f3b3df3abbbfb7b8d"  # noqa: E501
            ),
        ),
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
