"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/stMemExpandingEIP150Calls/OOGinReturnFiller.yml
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
        "tests/static/state_tests/stMemExpandingEIP150Calls/OOGinReturnFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "1a8451e60000000000000000000000009f5c4c430e37b429d18f8aba147e2302af08f2100000000000000000000000000000000000000000000000000000000000000036",  # noqa: E501
            {
                Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000f300")
                ),
                Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000fd00")
                ),
                Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(
                    storage={0: 0xDEAD60A7, 1: 0xDEAD60A7},
                    code=bytes.fromhex(
                        "60043561012052602435610140526360a760a760005261010060006000600060006101205161014051f16101005260005160005560003d11604157600050604a565b602060006101603e5b6101605160015500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000cee9f0c6117cc881ad7b4c378c2bebee8fcd04a90000000000000000000000000000000000000000000000000000000000000036",  # noqa: E501
            {
                Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000f300")
                ),
                Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000fd00")
                ),
                Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(
                    storage={0: 0xDEAD60A7, 1: 0xDEAD60A7},
                    code=bytes.fromhex(
                        "60043561012052602435610140526360a760a760005261010060006000600060006101205161014051f16101005260005160005560003d11604157600050604a565b602060006101603e5b6101605160015500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000009f5c4c430e37b429d18f8aba147e2302af08f2100000000000000000000000000000000000000000000000000000000000000025",  # noqa: E501
            {
                Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000f300")
                ),
                Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000fd00")
                ),
                Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(
                    storage={0: 0x60A760A7},
                    code=bytes.fromhex(
                        "60043561012052602435610140526360a760a760005261010060006000600060006101205161014051f16101005260005160005560003d11604157600050604a565b602060006101603e5b6101605160015500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000cee9f0c6117cc881ad7b4c378c2bebee8fcd04a90000000000000000000000000000000000000000000000000000000000000025",  # noqa: E501
            {
                Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000f300")
                ),
                Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000fd00")
                ),
                Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(
                    storage={0: 0x60A760A7},
                    code=bytes.fromhex(
                        "60043561012052602435610140526360a760a760005261010060006000600060006101205161014051f16101005260005160005560003d11604157600050604a565b602060006101603e5b6101605160015500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "1a8451e60000000000000000000000009f5c4c430e37b429d18f8aba147e2302af08f2100000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            {
                Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000f300")
                ),
                Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000fd00")
                ),
                Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(
                    storage={0: 0x60A760A7},
                    code=bytes.fromhex(
                        "60043561012052602435610140526360a760a760005261010060006000600060006101205161014051f16101005260005160005560003d11604157600050604a565b602060006101603e5b6101605160015500"  # noqa: E501
                    ),
                ),
            },
        ),
        (
            "1a8451e6000000000000000000000000cee9f0c6117cc881ad7b4c378c2bebee8fcd04a90000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            {
                Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000f300")
                ),
                Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9"): Account(
                    code=bytes.fromhex("63dead60a76000526101006000fd00")
                ),
                Address("0xebd3191dd8150f47e30f87927db4592163ee9224"): Account(
                    storage={0: 0x60A760A7},
                    code=bytes.fromhex(
                        "60043561012052602435610140526360a760a760005261010060006000600060006101205161014051f16101005260005160005560003d11604157600050604a565b602060006101603e5b6101605160015500"  # noqa: E501
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3", "case4", "case5"],
)
@pytest.mark.pre_alloc_mutable
def test_oo_gin_return(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0x56724d001b4f2a2888a81971a64aad37cd43f881")
    contract = Address("0xebd3191dd8150f47e30f87927db4592163ee9224")
    callee = Address("0x9f5c4c430e37b429d18f8aba147e2302af08f210")
    callee_1 = Address("0xcee9f0c6117cc881ad7b4c378c2bebee8fcd04a9")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=4294967296,
    )

    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("63dead60a76000526101006000f300"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("63dead60a76000526101006000fd00"),
    )
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "60043561012052602435610140526360a760a76000526101006000600060006000610120"  # noqa: E501
            "5161014051f16101005260005160005560003d11604157600050604a565b602060006101"  # noqa: E501
            "603e5b6101605160015500"
        ),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x40ac0fc28c27e961ee46ec43355a094de205856edbd4654cf2577c2608d4ec1e"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=9437184,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
