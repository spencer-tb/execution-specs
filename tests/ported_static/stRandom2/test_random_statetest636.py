"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom2/randomStatetest636Filler.json
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
    ["tests/static/state_tests/stRandom2/randomStatetest636Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest636(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xbdc4b8af0f40b0ec2256166f7145b81cd824a868")

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
            "74619921c0750ac3268e7a6703ca2bf6c43308e6fc36607561af1ca16db843f7a2e05bfc"  # noqa: E501
            "2e46afc179930b7a8724a04f9f561bdc65bba0ad5797dde0a28d5e8aca56e1510b724f67"  # noqa: E501
            "6a6d33dee473d74664561e49e3d86338c8dcf260f06cbfa6283966d2d0f2591f54088e6f"  # noqa: E501
            "36545c0d90fcdea10d5629629ffb1b16626c339f6490829f1b1675f0f2f62b0b7c9d3f07"  # noqa: E501
            "0fafd53f99f90f31e19e81d3db688929213e34affc41116e6ae6f54ad5c2062b27a9fbec"  # noqa: E501
            "78a52f7a26c6347408631a6c0efcf33fe576953a4043e846b686471403f38a615a0a8e60"  # noqa: E501
            "1d600a600e60146301019a5173bdc4b8af0f40b0ec2256166f7145b81cd824a86863314b"  # noqa: E501
            "c0fef1600c7eb69785d3593d3a8552018a4faba5b591975e8b8056ebc01f5ce5f5f7c04e"  # noqa: E501
            "ca9062b458a835649be8fbaa906f3c4d8f92f8c27517f0addd45e050bfcf55792d8bf87c"  # noqa: E501
            "39d39ed9b1ef6c8c070d8da4a624ce548b37d03ae8107ca6da49be4adffc9f5ae896c52b"  # noqa: E501
            "936a18bed4bd9fcbae531274706e9e9b9030619a40714bb4b22e7bef8cf7b01551327188"  # noqa: E501
            "ee4bb6247118d0e95549a92f7dd9305484cc054e5f206d70d008699a85896061427b05ae"  # noqa: E501
            "2a7f16230f66ab4dd548e03b0972010f5afff39a4f9a90e55e91584e86629f3e8775f53d"  # noqa: E501
            "a16fceedd834103a50dbe72a6634e4dbf374c70e6bd041628dc8b30de3c3d7aa0e7bb48d"  # noqa: E501
            "f927c78ed30b286e249c2cbe79fb55956f492e413e771d0cd63f7357ab1e9a38026a4ba9"  # noqa: E501
            "278427812728699a2c747189"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "648ae7baf084600e60746edc292e4f932e5d92d41f0bef49fc6b696d03a44c705cb4daaf"  # noqa: E501
            "5160107d58356b0c4e1a7d81fb0b606143c7db58d8147776c02745b7de14b2c388e49568"  # noqa: E501
            "e963334e695b39de93766519c9912b2dccb22bb3bd486cdf043cbc5c0cd3b4a35f6addc0"  # noqa: E501
            "1cb4ad9b448c0c60ff6c78c1acc568b086c8181a90b01f613e5e6116e776e8d170f52005"  # noqa: E501
            "efeb96d06594b7477815ea249e6143aaee6798a00d9dbba0552a73cd878ec8872e0e494d"  # noqa: E501
            "f0325b92e8c7753a084c6b9763c56059eb608978797530a734a7ced61643b84aece9a393"  # noqa: E501
            "44fab3c6363d62631369ff8d931e17c50dcadb1f72256d2bcfd07e62b68627374ae05b8f"  # noqa: E501
            "f70a238f6b8717aebdaa6cd0696889d903742f20f313a8e4bcb5efae0edcbb74f41e2027"  # noqa: E501
            "dc90b56ee50a7c151872c3f01c0746579073c26c78e58ca65d93cd6c945401024b70fae5"  # noqa: E501
            "f6e17c1bc9636bd85c6c721b77f39c71e417a9bc43cf7288a2888f33b863c22e5e606ef7"  # noqa: E501
            "03db601f52cf73b09b88fe1772d6693064e95ea20aa3da12c76fc929d6982f7ae98c7195"  # noqa: E501
            "8c5fdd80f52a8d673027f0fa96116b85636464219d046962e9e728f947cc66e8a5806111"  # noqa: E501
            "1b752dbc3bbd70bf3fa2e463969371f089c8226cb217fcf86fed7c5c87ada364a13ca107"  # noqa: E501
            "785a1e76d56edd7b1f02caac7915e522478f790322601868ed8a345ba615388b5d77d405"  # noqa: E501
            "d62f0abd72ed81f218f27c6ee6a6cde612b9c528d4107c25f6d842f8d91a37f4f098e3f5"  # noqa: E501
            "52a5ce3c14d301fd1a0c7711f831c8c07197a419447c10662351b792bb34eef76c6f5d66"  # noqa: E501
            "414b182911d942896b1bb156c0ba37a9bfe4420bc17ddfe7be8daeabb37222d4ae081dd8"  # noqa: E501
            "89cb787c9bf801b07e186f274a70549a04"
        ),
        gas_limit=1635935265,
        gas_price=10,
        nonce=0,
        value=1962905609,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            storage={0x3C4D8F92F8C27517F0ADDD45E050BFCF: 0x9BE8FBAA90},
            code=bytes.fromhex(
                "74619921c0750ac3268e7a6703ca2bf6c43308e6fc36607561af1ca16db843f7a2e05bfc2e46afc179930b7a8724a04f9f561bdc65bba0ad5797dde0a28d5e8aca56e1510b724f676a6d33dee473d74664561e49e3d86338c8dcf260f06cbfa6283966d2d0f2591f54088e6f36545c0d90fcdea10d5629629ffb1b16626c339f6490829f1b1675f0f2f62b0b7c9d3f070fafd53f99f90f31e19e81d3db688929213e34affc41116e6ae6f54ad5c2062b27a9fbec78a52f7a26c6347408631a6c0efcf33fe576953a4043e846b686471403f38a615a0a8e601d600a600e60146301019a5173bdc4b8af0f40b0ec2256166f7145b81cd824a86863314bc0fef1600c7eb69785d3593d3a8552018a4faba5b591975e8b8056ebc01f5ce5f5f7c04eca9062b458a835649be8fbaa906f3c4d8f92f8c27517f0addd45e050bfcf55792d8bf87c39d39ed9b1ef6c8c070d8da4a624ce548b37d03ae8107ca6da49be4adffc9f5ae896c52b936a18bed4bd9fcbae531274706e9e9b9030619a40714bb4b22e7bef8cf7b01551327188ee4bb6247118d0e95549a92f7dd9305484cc054e5f206d70d008699a85896061427b05ae2a7f16230f66ab4dd548e03b0972010f5afff39a4f9a90e55e91584e86629f3e8775f53da16fceedd834103a50dbe72a6634e4dbf374c70e6bd041628dc8b30de3c3d7aa0e7bb48df927c78ed30b286e249c2cbe79fb55956f492e413e771d0cd63f7357ab1e9a38026a4ba9278427812728699a2c747189"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
