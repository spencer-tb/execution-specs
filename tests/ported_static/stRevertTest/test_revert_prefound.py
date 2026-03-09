"""
Ported from:
tests/static/state_tests/stRevertTest/RevertPrefoundFiller.json
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
    ["tests/static/state_tests/stRevertTest/RevertPrefoundFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_revert_prefound(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xa000000000000000000000000000000000000000")
    callee = Address("0x7db299e0885c85039f56fa504a13dd8ce8a56aa7")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(balance=1, nonce=0)
    pre[contract] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.SSTORE(key=0x0, value=Op.CREATE(value=0x0, offset=0x0, size=0x20))
        + Op.SSTORE(key=0x1, value=0xc) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"
        ),
        to=contract,
        data=b"",
        gas_limit=1040000,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        contract: Account(
            storage={0: 0x7db299e0885c85039f56fa504a13dd8ce8a56aa7, 1: 12},
            code=Op.SSTORE(key=0x0, value=Op.CREATE(value=0x0, offset=0x0, size=0x20)) + Op.SSTORE(key=0x1, value=0xc) + Op.STOP,
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
