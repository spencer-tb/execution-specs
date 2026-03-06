"""
Ported from:
tests/static/state_tests/stEIP158Specific/vitalikTransactionTestParisFiller.json
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
    ["tests/static/state_tests/stEIP158Specific/vitalikTransactionTestParisFiller.json"],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.pre_alloc_mutable
def test_vitalik_transaction_test_paris(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Test ported from static filler."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xcd2a3d9f938e13cd947ec05abc7fe734df8dd826")
    contract = Address("0xee098e6c2a43d9e2c04f08f0c3a87b0ba59079d4")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[coinbase] = Account(balance=0, nonce=1)
    pre[sender] = Account(balance=0xffffffffffffffffffff, nonce=335)
    pre[contract] = Account(balance=10, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xc85ef7d79691fe79573b1a7064c19c1a9819ebdbd1faaab1a8ec92344438aaf4"
        ),
        to=None,
        data=bytes.fromhex(
            "6000607f5359610043806100135939610056566c010000000000000000000000007fee09"
            "8e6c2a43d9e2c04f08f0c3a87b0ba59079d4d53532071d6cd0cb86facd5605ff61000080"
            "61003f60003961003f565b6000f35b816000f0905050596100718061006c59396100dd56"
            "61005f8061000e60003961006d566000603f5359610043806100135939610056566c0100"
            "00000000000000000000007fee098e6c2a43d9e2c04f08f0c3a87b0ba59079d4d5353207"
            "1d6cd0cb86facd5605ff6100008061003f60003961003f565b6000f35b816000f0905050"
            "fe5b6000f35b816000f0905060405260006000600060006000604051620249f0f1506100"
            "0080610108600039610108565b6000f3"
        ),
        gas_limit=2097151,
        gas_price=10,
        nonce=335,
        value=0,
    )

    post = {
        Address("0x1bc78ae0e5ec5cb439f1d5355d6f90d38343e109"): Account(
            storage={},
            nonce=3,
            code=b"",
        ),
        Address("0x51f9d7f98e997bdd6bebde4c2dd27be8c99303aa"): Account(
            storage={},
            nonce=1,
            balance=0,
            code=Op.PUSH1[0x0] + Op.PUSH1[0x3f] + Op.MSTORE8 + Op.MSIZE + Op.PUSH2[0x43] + Op.DUP1 + Op.PUSH2[0x13] + Op.MSIZE + Op.CODECOPY + Op.PUSH2[0x56] + Op.JUMP + Op.PUSH13[0x1000000000000000000000000] + Op.PUSH32[0xee098e6c2a43d9e2c04f08f0c3a87b0ba59079d4d53532071d6cd0cb86facd56] + Op.SDIV + Op.SELFDESTRUCT + Op.PUSH2[0x0] + Op.DUP1 + Op.PUSH2[0x3f] + Op.PUSH1[0x0] + Op.CODECOPY + Op.PUSH2[0x3f] + Op.JUMP + Op.JUMPDEST + Op.PUSH1[0x0] + Op.RETURN + Op.JUMPDEST + Op.DUP2 + Op.PUSH1[0x0] + Op.CREATE + Op.SWAP1 + Op.POP + Op.POP + Op.INVALID,
        ),
        sender: Account(storage={}, nonce=336, code=b""),
        contract: Account(storage={}, nonce=0, balance=10, code=b""),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
