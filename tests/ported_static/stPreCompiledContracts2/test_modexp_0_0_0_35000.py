"""
Puts the base 0, exponent 0 and modulus 0 into the MODEXP precompile, saves...

Ported from:
tests/static/state_tests/stPreCompiledContracts2/modexp_0_0_0_35000Filler.json
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
        "tests/static/state_tests/stPreCompiledContracts2/modexp_0_0_0_35000Filler.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_gas_limit",
    [
        57040,
        90000,
        110000,
        200000,
    ],
    ids=["case0", "case1", "case2", "case3"],
)
@pytest.mark.pre_alloc_mutable
def test_modexp_0_0_0_35000(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_gas_limit: int,
) -> None:
    """Puts the base 0, exponent 0 and modulus 0 into the MODEXP..."""
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
    pre[coinbase] = Account(balance=0x201EE, nonce=0)
    pre[sender] = Account(balance=0xDE0B6B3A761FE12, nonce=1)
    pre[contract] = Account(
        balance=0,
        nonce=1,
        code=bytes.fromhex(
            "600035601c52740100000000000000000000000000000000000000006020526fffffffff"  # noqa: E501
            "ffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff00000000"  # noqa: E501
            "0000000000000000000000016060527402540be3fffffffffffffffffffffffffdabf41c"  # noqa: E501
            "006080527ffffffffffffffffffffffffdabf41c00000000000000000000000002540be4"  # noqa: E501
            "0060a0526330c8d1da600051141561012b57608460043560040135111515585760043560"  # noqa: E501
            "04013560200160043560040161014037600161024061014051610160600060056305f5e0"  # noqa: E501
            "fff11558576001610220526102206021806102808284600060046015f150505061028080"  # noqa: E501
            "516020820120905060005561028060206020820352604081510160206001820306601f82"  # noqa: E501
            "0103905060208203f350005b"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x044852b2a670ade5407e78fb2863c51de9fcb96542a07186fe3aeda6bb8a116d"  # noqa: E501
        ),
        to=contract,
        data=bytes.fromhex(
            "30c8d1da0000000000000000000000000000000000000000000000000000000000000020"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000000000006000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
            "000000000000000000000000000000000000000000000000000000000000000000000000"  # noqa: E501
            "0000000000000000000000000000000000000000"
        ),
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=1,
        value=0,
    )

    post = {
        contract: Account(
            storage={
                0: 0xBC36789E7A1E281436464229828F817D6612F7B477D66591FF96A9E064BCC98A,  # noqa: E501
            },
            code=bytes.fromhex(
                "600035601c52740100000000000000000000000000000000000000006020526fffffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff000000000000000000000000000000016060527402540be3fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffdabf41c00000000000000000000000002540be40060a0526330c8d1da600051141561012b5760846004356004013511151558576004356004013560200160043560040161014037600161024061014051610160600060056305f5e0fff11558576001610220526102206021806102808284600060046015f150505061028080516020820120905060005561028060206020820352604081510160206001820306601f820103905060208203f350005b"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
