"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest306Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest306Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest306(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0xce8d3e84f685b2eed55366547289ac4d314de277")

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
            "60d36e84517b3285b0867cd4144ff5f688d60b6a07592395d95e37246c06736c78c9fa9e"  # noqa: E501
            "4b5e5db5a4b6ac4ced6dd169cda4fc3c11e9a6f0b4cec2f56019617df7a363788c155473"  # noqa: E501
            "412582d556f06c6d5864cf4be6a2d1318b8e40ba1377454cc8d0510823591dee680d7ddd"  # noqa: E501
            "c8c149bfcc24c65c69e66c2b9d3e28f05faf2587c446509405759901ec0946bf3d786827"  # noqa: E501
            "225faf5da81e158cd9b2b4666f71a29fbe89f77c340dcbd7d67aedf852136b6c76affb38"  # noqa: E501
            "beb802e0af269e65c22f52807c677b5e2c7d8c473aff18fe912c7ed21ab60fe5d4916a76"  # noqa: E501
            "c93539332c6ab16b3f81b990f4b34b0228c7f5b1656bdd21d458717330e4be7d7bb91cc9"  # noqa: E501
            "5818140eef086cd82d2d6f0d66c92a7ffb27125a625c77a8967268f212339508d6f60d9c"  # noqa: E501
            "93a9e201f2ae883cb9752460ec0dcb4ba3b84a4db899c29f08ef1b0f506b4f3c05601f60"  # noqa: E501
            "01601060116328b0eb5f73ce8d3e84f685b2eed55366547289ac4d314de277630a4eb375"  # noqa: E501
            "f17df238e15d7d51240301521f173d628e7a68d01354faaf406ce541f753db89671f6aed"  # noqa: E501
            "cf261f632e6244e8c3799a2de002f15ba4681fd3c609c0f522dfd964f95def9926f81232"  # noqa: E501
            "7781b2de33196cc22776e9b26d8a0d65c57bdac987d0b3e0db66c0f1232c7add3365f209"  # noqa: E501
            "cc53592f73502d0c5889b1bbf131f8bb6a6b5e2e067b9ef676768d48b3f5790c3304e046"  # noqa: E501
            "f0a9c8a838a0596583d6258f196dcf982a9de5cec4f871470e7a6c9289615e1e7d140fdc"  # noqa: E501
            "038972916223fb8012e29350295f3919cb28a36411845930d5e91b68510faac5e0677953"  # noqa: E501
            "467cedb653f73818749e8cbaf15a5d64ba7ee5cabc98137167b924a2aac9147f159713d1"  # noqa: E501
            "15e0225a84a54d6471dc7a01a7e4e814145305c9d04d2880c5be42fc6c52ced3e983d91a"  # noqa: E501
            "580a4142021b73e99c3180117914b9ad03c580a8dac862be9b599a73ccfcfb230bcffc42"  # noqa: E501
            "5c13c265f3b06b8c9f104c10752740765567374c211601a5f51501d18c48081998ff7b7a"  # noqa: E501
            "8bfdf0bec9eb4385b554870a996e0cab662d991d0e5f9357f2f99f98"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "79f7441ed5bec692c84f9c7783152d38908fea76de8a06eca5ebcf7e81423a68b78d5f1a"  # noqa: E501
            "84706bdb516f17a29dd779ee16374163c1ab2a85a2097e7b6235aecf7cc509b9d184688f"  # noqa: E501
            "56ccfe8638c51ee70858f690e71b338261fd2b72db56f2a0923a6d1bc51dd15ff9aae183"  # noqa: E501
            "48213d68fc8e120c307a7490f46b2d528d86e503a251fd188764646dd3b8bc3c7066a32d"  # noqa: E501
            "caa91da430f61aed0466338f17d9703f1c8648d0b19db4fcdcd0893f0f6f21c789306b8f"  # noqa: E501
            "8d110fbd563111fd088de367b9f001758786ced578880bb55e224855b0293f9277dc7201"  # noqa: E501
            "e63845a8d8eae7dc8e3e642820b61315716544e2fd297f018fe1df86427052e3a85c0c77"  # noqa: E501
            "48f6fa89b890be2a3b916794ecfff1e87a87582c991b0c61687637866981d0819020714f"  # noqa: E501
            "baee296a9ac19ac255226d4d2cf967104b669a622e77fc4c7469aee1553e5cf5cb2a7972"  # noqa: E501
            "6f07829adfa8a988fb07479add89c1a8947d88a9b361493025a66fd49776d7304a036894"  # noqa: E501
            "ecda2e148f7f87270cdd52727667c09ee625c7a37ac99ab8a195cd0a97fa9e7247f9d0f1"  # noqa: E501
            "7888132eb3f44d24d3d49c0a2e6d4850ee413c36893d04dfa9826f7236a10c77f7da3d31"  # noqa: E501
            "db8eae3070972c9d722347d4a95604d40ba66a2f53710451be8f1994756471ba4d09257f"  # noqa: E501
            "6abe619cc850f123d4715bacc2b9cf167be82e629cf36521b290bab47b9597664c0890a5"  # noqa: E501
            "d6242211d344805a3d75460c21ca9ad05dec187ddecc44c9b1c0b4c0d34c66926db22974"  # noqa: E501
            "c0bc059a6aa6354a43bf26f06e7dfa7f0e07f4f3607a8bc1227b7f0d65d660aa3c1eb773"  # noqa: E501
            "1850729f5dc3285b398806dd4b54aecbe7cb367573a1aa8f062b33e27db1e2fdef478ac3"  # noqa: E501
            "06ec57be3b6b0fd0fbbe558507ead60ce60a61eade67afdd8ba512300ecc686d51131057"  # noqa: E501
            "8908f49660d163e372ddd2636dbf1c1b6d39292b97dbd48fee420c354d341365e64505ae"  # noqa: E501
            "ffc89b6e764afc7f97200924ff8d68846e387f6bca4c4ea3f4e04ac8061efd5260577aa6"  # noqa: E501
            "9c34a7287609d2448bb32d2687a46d54c893ba21520ec26e792c836ebb8c9c1005ab55d9"  # noqa: E501
            "9c62150413fb7a7f8e2ec4766471e2452ee833fa10995e94d2c1cf89c64260836aab9b3c"  # noqa: E501
            "6a1f699776b5900f48b7c1f97dba13656a85fea0cc2d4fe85aa7a9766d767cfd6a3314ac"  # noqa: E501
            "c32eea93e15c3077fa26a3917a48af0765b5690af372219af6c2e7e5b194e6db7f76ca0b"  # noqa: E501
            "28647c5066bfbf142ac3eb1361b77953e328106b1e817e8649a9bdf4f27834bd25279dc2"  # noqa: E501
            "b7a6fab4d4e4830602f84d298f5d2682183a226118fc6c452c99ead827293548afcfeaf9"  # noqa: E501
            "655e76240e57846151bb7b1c1cc5971f0ad83dc7b02c05c2bc0a3adeb65bf608eb5c0aaf"  # noqa: E501
            "186a887a4357e31bdd83940e443289727a6e36bfc974bc20e97fa8983f18137be520500b"  # noqa: E501
            "388fe2f63185c5c66bcc71a48c7fc9c210f73a4a73c4561f62adb5ed9d7ae9a0e4833f19"  # noqa: E501
            "8dd3faa1af3ad59c282f3277fac135659e7eb7c9926fd5e954f6f42a9cd2cb6498da0767"  # noqa: E501
            "958716"
        ),
        gas_limit=1970726856,
        gas_price=10,
        nonce=0,
        value=1525687154,
    )

    post = {
        coinbase: Account(
            code=bytes.fromhex("6000355415600957005b60203560003555"),
        ),
        contract: Account(
            code=bytes.fromhex(
                "60d36e84517b3285b0867cd4144ff5f688d60b6a07592395d95e37246c06736c78c9fa9e4b5e5db5a4b6ac4ced6dd169cda4fc3c11e9a6f0b4cec2f56019617df7a363788c155473412582d556f06c6d5864cf4be6a2d1318b8e40ba1377454cc8d0510823591dee680d7dddc8c149bfcc24c65c69e66c2b9d3e28f05faf2587c446509405759901ec0946bf3d786827225faf5da81e158cd9b2b4666f71a29fbe89f77c340dcbd7d67aedf852136b6c76affb38beb802e0af269e65c22f52807c677b5e2c7d8c473aff18fe912c7ed21ab60fe5d4916a76c93539332c6ab16b3f81b990f4b34b0228c7f5b1656bdd21d458717330e4be7d7bb91cc95818140eef086cd82d2d6f0d66c92a7ffb27125a625c77a8967268f212339508d6f60d9c93a9e201f2ae883cb9752460ec0dcb4ba3b84a4db899c29f08ef1b0f506b4f3c05601f6001601060116328b0eb5f73ce8d3e84f685b2eed55366547289ac4d314de277630a4eb375f17df238e15d7d51240301521f173d628e7a68d01354faaf406ce541f753db89671f6aedcf261f632e6244e8c3799a2de002f15ba4681fd3c609c0f522dfd964f95def9926f812327781b2de33196cc22776e9b26d8a0d65c57bdac987d0b3e0db66c0f1232c7add3365f209cc53592f73502d0c5889b1bbf131f8bb6a6b5e2e067b9ef676768d48b3f5790c3304e046f0a9c8a838a0596583d6258f196dcf982a9de5cec4f871470e7a6c9289615e1e7d140fdc038972916223fb8012e29350295f3919cb28a36411845930d5e91b68510faac5e0677953467cedb653f73818749e8cbaf15a5d64ba7ee5cabc98137167b924a2aac9147f159713d115e0225a84a54d6471dc7a01a7e4e814145305c9d04d2880c5be42fc6c52ced3e983d91a580a4142021b73e99c3180117914b9ad03c580a8dac862be9b599a73ccfcfb230bcffc425c13c265f3b06b8c9f104c10752740765567374c211601a5f51501d18c48081998ff7b7a8bfdf0bec9eb4385b554870a996e0cab662d991d0e5f9357f2f99f98"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
