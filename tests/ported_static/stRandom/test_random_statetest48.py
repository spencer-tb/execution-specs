"""
Test ported from static filler.

Ported from:
tests/static/state_tests/stRandom/randomStatetest48Filler.json
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
    ["tests/static/state_tests/stRandom/randomStatetest48Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_random_statetest48(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x4f3f701464972e74606d6ea82d4d3080599a0e79")
    sender = Address("0x2e3d0156d2b99a6eacba540c55f423c8f5a33143")
    contract = Address("0x292e762689b448debe7899ade7acb27a84a85c44")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    # Source: raw bytecode
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=(
            Op.CODESIZE
            + Op.LOG3(
                offset=0xA73B,
                size=0x2F05,
                topic_1=0x698FC0E9CED2F6A0087344559C43,
                topic_2=0x6060B6D9,
                topic_3=0x5231D8E75DB11D6DA7040CEE1A12EBF739E5022CAA60F92D51,
            )
            + Op.CALL(
                gas=0x70F82D9F,
                address=0x292E762689B448DEBE7899ADE7ACB27A84A85C44,
                value=0x186262C1,
                args_offset=0x9,
                args_size=0x14,
                ret_offset=0xD,
                ret_size=0xA,
            )
            + Op.PUSH1[0x41]
            + Op.PUSH7[0xF49EF1FEA120AF]
            + Op.PUSH24[0xBA4CCE3F35BC52CA5C40BF14C77E95EA92E69520143FF9C7]
            + Op.DUP3
            + Op.PUSH28[
                0xCFE760AEE06D241E31A0773476DA22F7CE8131475838C23B59F7A3C4
            ]
            + Op.PUSH12[0x2B99C0955E169EE3527CA9F7]
            + Op.PUSH8[0x4467BDF2C0EEBF6F]
            + Op.PUSH1[0x12]
            + Op.SWAP3
            + Op.ORIGIN
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)
    # Source: raw bytecode
    pre[coinbase] = Account(
        balance=46,
        nonce=0,
        code=(
            Op.JUMPI(
                pc=0x9,
                condition=Op.ISZERO(Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))),
            )
            + Op.STOP
            + Op.JUMPDEST
            + Op.SSTORE(
                key=Op.CALLDATALOAD(offset=0x0),
                value=Op.CALLDATALOAD(offset=0x20),
            )
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0xb1f4cbc3a50042184425a6f9e996d0910f7ba879457ce5dac5c71e498ad3c005"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "76dd12f3185b84dfc71eb93f4df4ca30dcf34446f25793016424a5e33b6a65fb5d64a939"  # noqa: E501
            "4d7ebefb1c15de971a2d2f53377765d50c698d4e26adea05dd2f6a1688f60eb8b172d796"  # noqa: E501
            "a45c6f79596bfb719df5a571ce8c339e9d7e9b3905324643a2b9fd541956552fc258e688"  # noqa: E501
            "303ecb25082776fde7334cdf046f70c8669a6a05c36909038278e925f0156be9ddb9b837"  # noqa: E501
            "86de8a325ab28e61d18397714bcda0fd5ca879c870d383721c638733b1f78074cc1079e7"  # noqa: E501
            "2e0bbbad262348a8976eaaf313a261dccb69dbaf283beebcac7ac3b8166a4deb1fe5099a"  # noqa: E501
            "1c7f3ef595357e76ca260a703bec4848a3cc9804d6de6e5b853b54dd65979292f596ee13"  # noqa: E501
            "2edf67eb948e4e4d22f9cb7629bf8b642cb921b2ed9b13e47cb06d6c6f4384c7b372ee7c"  # noqa: E501
            "b61f76a363f8fa68309e3d308179ad3e15fd752d6586e9030c8c1f274878bf7fbe1b5699"  # noqa: E501
            "44fdda166c47411878f3702bbe1bbabbce8b10701076e0338bfa289d424c13f4f438474a"  # noqa: E501
            "fd71abc18290e0a3c853537a13ce9869d3942c7b6802bfb0f345a9af828b96"
        ),
        gas_limit=2120993272,
        gas_price=10,
        nonce=0,
        value=1548512824,
    )

    post = {
        contract: Account(
            code=(
                Op.CODESIZE
                + Op.LOG3(
                    offset=0xA73B,
                    size=0x2F05,
                    topic_1=0x698FC0E9CED2F6A0087344559C43,
                    topic_2=0x6060B6D9,
                    topic_3=0x5231D8E75DB11D6DA7040CEE1A12EBF739E5022CAA60F92D51,  # noqa: E501
                )
                + Op.CALL(
                    gas=0x70F82D9F,
                    address=0x292E762689B448DEBE7899ADE7ACB27A84A85C44,
                    value=0x186262C1,
                    args_offset=0x9,
                    args_size=0x14,
                    ret_offset=0xD,
                    ret_size=0xA,
                )
                + Op.PUSH1[0x41]
                + Op.PUSH7[0xF49EF1FEA120AF]
                + Op.PUSH24[0xBA4CCE3F35BC52CA5C40BF14C77E95EA92E69520143FF9C7]
                + Op.DUP3
                + Op.PUSH28[
                    0xCFE760AEE06D241E31A0773476DA22F7CE8131475838C23B59F7A3C4
                ]
                + Op.PUSH12[0x2B99C0955E169EE3527CA9F7]
                + Op.PUSH8[0x4467BDF2C0EEBF6F]
                + Op.PUSH1[0x12]
                + Op.SWAP3
                + Op.ORIGIN
            ),
        ),
        coinbase: Account(
            code=(
                Op.JUMPI(
                    pc=0x9,
                    condition=Op.ISZERO(
                        Op.SLOAD(key=Op.CALLDATALOAD(offset=0x0))
                    ),
                )
                + Op.STOP
                + Op.JUMPDEST
                + Op.SSTORE(
                    key=Op.CALLDATALOAD(offset=0x0),
                    value=Op.CALLDATALOAD(offset=0x20),
                )
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
