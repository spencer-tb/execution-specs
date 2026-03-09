"""
Puts the given data into the ECPAIRING precompile.

Ported from:
tests/static/state_tests/stZeroKnowledge
ecpairing_three_point_fail_1Filler.json
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
        "tests/static/state_tests/stZeroKnowledge/ecpairing_three_point_fail_1Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit, expected_post",
    [
        (
            422568,
            {
                Address("0xc305c901078781c232a2a521c2af7980f8385ee9"): Account(
                    storage={
                        0: 0x290DECD9548B62A8D60345A988386FC84BA6BC95484008F6362F93160EF3E563  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "600035601c52740100000000000000000000000000000000000000006020526fffffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff000000000000000000000000000000016060527402540be3fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffdabf41c00000000000000000000000002540be40060a0526330c8d1da600051141561012c576107806004356004013511151558576004356004013560200160043560040161014037602061092061014051610160600060086305f5e0fff11558576020610900526109006040806109608284600060046018f150505061096080516020820120905060005561096060206020820352604081510160206001820306601f820103905060208203f350005b"  # noqa: E501
                    ),
                )
            },
        ),
        (
            90000,
            {
                Address("0xc305c901078781c232a2a521c2af7980f8385ee9"): Account(
                    storage={
                        0: 0xB10E2D527612073B26EECDFD717E6A320CF44B4AFAC2B0732D9FCBE2B7FA0CF6  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "600035601c52740100000000000000000000000000000000000000006020526fffffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff000000000000000000000000000000016060527402540be3fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffdabf41c00000000000000000000000002540be40060a0526330c8d1da600051141561012c576107806004356004013511151558576004356004013560200160043560040161014037602061092061014051610160600060086305f5e0fff11558576020610900526109006040806109608284600060046018f150505061096080516020820120905060005561096060206020820352604081510160206001820306601f820103905060208203f350005b"  # noqa: E501
                    ),
                )
            },
        ),
        (
            110000,
            {
                Address("0xc305c901078781c232a2a521c2af7980f8385ee9"): Account(
                    storage={
                        0: 0xB10E2D527612073B26EECDFD717E6A320CF44B4AFAC2B0732D9FCBE2B7FA0CF6  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "600035601c52740100000000000000000000000000000000000000006020526fffffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff000000000000000000000000000000016060527402540be3fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffdabf41c00000000000000000000000002540be40060a0526330c8d1da600051141561012c576107806004356004013511151558576004356004013560200160043560040161014037602061092061014051610160600060086305f5e0fff11558576020610900526109006040806109608284600060046018f150505061096080516020820120905060005561096060206020820352604081510160206001820306601f820103905060208203f350005b"  # noqa: E501
                    ),
                )
            },
        ),
        (
            150000,
            {
                Address("0xc305c901078781c232a2a521c2af7980f8385ee9"): Account(
                    storage={
                        0: 0xB10E2D527612073B26EECDFD717E6A320CF44B4AFAC2B0732D9FCBE2B7FA0CF6  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "600035601c52740100000000000000000000000000000000000000006020526fffffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff000000000000000000000000000000016060527402540be3fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffdabf41c00000000000000000000000002540be40060a0526330c8d1da600051141561012c576107806004356004013511151558576004356004013560200160043560040161014037602061092061014051610160600060086305f5e0fff11558576020610900526109006040806109608284600060046018f150505061096080516020820120905060005561096060206020820352604081510160206001820306601f820103905060208203f350005b"  # noqa: E501
                    ),
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_ecpairing_three_point_fail_1(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """Puts the given data into the ECPAIRING precompile."""
    coinbase = Address("0x3535353535353535353535353535353535353535")
    sender = Address("0x82a978b3f5962a5b0957d9ee9eef472ee55b42f1")
    contract = Address("0xc305c901078781c232a2a521c2af7980f8385ee9")
    callee = Address("0x0000000000000000000000000000000000000001")
    callee_1 = Address("0x0000000000000000000000000000000000000002")
    callee_2 = Address("0x0000000000000000000000000000000000000003")
    callee_3 = Address("0x0000000000000000000000000000000000000004")
    callee_4 = Address("0x0000000000000000000000000000000000000005")
    callee_5 = Address("0x0000000000000000000000000000000000000006")
    callee_6 = Address("0x0000000000000000000000000000000000000007")
    callee_7 = Address("0x0000000000000000000000000000000000000008")
    callee_8 = Address("0x10a1c1cb95c92ec31d3f22c66eef1d9f3f258c6b")
    callee_9 = Address("0x13cbb8d99c6c4e0f2728c7d72606e78a29c4e224")
    callee_10 = Address("0x24143873e0e0815fdcbcffdbe09c979cbf9ad013")
    callee_11 = Address("0x598443f1880ef585b21f1d7585bd0577402861e5")
    callee_12 = Address("0x77db2bebba79db42a978f896968f4afce746ea1f")
    callee_13 = Address("0x7d577a597b2742b498cb5cf0c26cdcd726d39e6e")
    callee_14 = Address("0x90f0b1ebbba1c1936aff7aaf20a7878ff9e04b6c")
    callee_15 = Address("0xdceceaf3fc5c0a63d195d69b1a90011b7b19650d")
    callee_16 = Address("0xe0fc04fa2d34a66b779fd5cee748268032a146c0")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(balance=1, nonce=0)
    pre[callee_1] = Account(balance=1, nonce=0)
    pre[callee_2] = Account(balance=1, nonce=0)
    pre[callee_3] = Account(balance=1, nonce=0)
    pre[callee_4] = Account(balance=1, nonce=0)
    pre[callee_5] = Account(balance=1, nonce=0)
    pre[callee_6] = Account(balance=1, nonce=0)
    pre[callee_7] = Account(balance=1, nonce=0)
    pre[callee_8] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_9] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_10] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[coinbase] = Account(balance=0x48EB8E, nonce=0)
    pre[callee_11] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_12] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_13] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[sender] = Account(balance=0xDE0B6B3A71B1472, nonce=19)
    pre[callee_14] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex(
            "600035601c52740100000000000000000000000000000000000000006020526fffffffff"  # noqa: E501
            "ffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff00000000"  # noqa: E501
            "0000000000000000000000016060527402540be3fffffffffffffffffffffffffdabf41c"  # noqa: E501
            "006080527ffffffffffffffffffffffffdabf41c00000000000000000000000002540be4"  # noqa: E501
            "0060a0526330c8d1da600051141561012c57610780600435600401351115155857600435"  # noqa: E501
            "6004013560200160043560040161014037602061092061014051610160600060086305f5"  # noqa: E501
            "e0fff11558576020610900526109006040806109608284600060046018f1505050610960"  # noqa: E501
            "80516020820120905060005561096060206020820352604081510160206001820306601f"  # noqa: E501
            "820103905060208203f350005b"
        ),
        storage={
            0x0: 0xB10E2D527612073B26EECDFD717E6A320CF44B4AFAC2B0732D9FCBE2B7FA0CF6,  # noqa: E501
        },
    )
    pre[callee_15] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    pre[callee_16] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x044852b2a670ade5407e78fb2863c51de9fcb96542a07186fe3aeda6bb8a116d"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "30c8d1da0000000000000000000000000000000000000000000000000000000000000020"  # noqa: E501
            "0000000000000000000000000000000000000000000000000000000000000240105456a3"  # noqa: E501
            "33e6d636854f987ea7bb713dfd0ae8371a72aea313ae0c32c0bf10160cf031d41b41557f"  # noqa: E501
            "3e7e3ba0c51bebe5da8e6ecd855ec50fc87efcdeac168bcc0476be093a6d2b4bbf907172"  # noqa: E501
            "049874af11e1b6267606e00804d3ff0037ec57fd3010c68cb50161b7d1d96bb71edfec98"  # noqa: E501
            "80171954e56871abf3d93cc94d745fa114c059d74e5b6c4ec14ae5864ebe23a71781d86c"  # noqa: E501
            "29fb8fb6cce94f70d3de7a2101b33461f39d9e887dbb100f170a2345dde3c07e256d1dfa"  # noqa: E501
            "2b657ba5cd03042700000000000000000000000000000000000000000000000000000000"  # noqa: E501
            "000000010000000000000000000000000000000000000000000000000000000000000002"  # noqa: E501
            "1a2c3013d2ea92e13c800cde68ef56a294b883f6ac35d25f587c09b1b3c635f7290158a8"  # noqa: E501
            "0cd3d66530f74dc94c94adb88f5cdb481acca997b6e60071f08a115f00cacf3523caf879"  # noqa: E501
            "d7d05e30549f1e6fdce364cbb8724b0329c6c2a39d4f018e0692e55db067300e6e3fe562"  # noqa: E501
            "18fa2f940054e57e7ef92bf7d475a9d8a8502fd200000000000000000000000000000000"  # noqa: E501
            "000000000000000000000000000000010000000000000000000000000000000000000000"  # noqa: E501
            "000000000000000000000002198e9393920d483a7260bfb731fb5d25f1aa493335a9e712"  # noqa: E501
            "97e485b7aef312c21800deef121f1e76426a00665e5c4479674322d4f75edadd46debd5c"  # noqa: E501
            "d992f6ed090689d0585ff075ec9e99ad690c3395bc4b313370b38ef355acdadcd122975b"  # noqa: E501
            "12c85ea5db8c6deb4aab71808dcb408fe3d1e7690c43d37b4ce6cc0166fa7daa"
        ),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=19,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
