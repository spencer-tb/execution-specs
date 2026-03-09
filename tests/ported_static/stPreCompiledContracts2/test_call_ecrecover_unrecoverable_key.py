"""
CALL to ECREC precompile with input that has a valid signature structure...

Ported from:
tests/static/state_tests/stPreCompiledContracts2
CallEcrecoverUnrecoverableKeyFiller.json
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
        "tests/static/state_tests/stPreCompiledContracts2/CallEcrecoverUnrecoverableKeyFiller.json",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.pre_alloc_mutable
def test_call_ecrecover_unrecoverable_key(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """CALL to ECREC precompile with input that has a valid signature..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xebaf50debf10e08302fe4280c32df010463ca297")
    contract = Address("0x85c44d846ed50ac9e384c1b575fd96f3edf5751f")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[contract] = Account(
        balance=0x1312D00,
        nonce=0,
        code=bytes.fromhex(
            "7fa8b53bdf3306a35a7103ab5504a0c9b492295564b6202b1942a84ef300107281600052"  # noqa: E501
            "601b6020527f307835653165303366353363653138623737326363623030393366663731"  # noqa: E501
            "66336040527f663533663563373562373464636233316138356161386238383932623465"  # noqa: E501
            "38626060527f112233445566778899101112131415161718192021222324252627282930"  # noqa: E501
            "3132608052602060806080600060006001620493e0f15060805160005500"
        ),
    )
    pre[sender] = Account(balance=0xDE0B6B3A7640000, nonce=0)

    tx = Transaction(
        secret_key=Hash(
            "0xe04d1ac7ddda0c98397d56a0b501e960d4cd325a39286919ac23c1a07009a869"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=3652240,
        gas_price=10,
        nonce=0,
        value=100000,
    )

    post = {
        contract: Account(
            storage={
                0: 0x1122334455667788991011121314151617181920212223242526272829303132,  # noqa: E501
            },
            code=bytes.fromhex(
                "7fa8b53bdf3306a35a7103ab5504a0c9b492295564b6202b1942a84ef300107281600052601b6020527f30783565316530336635336365313862373732636362303039336666373166336040527f66353366356337356237346463623331613835616138623838393262346538626060527f1122334455667788991011121314151617181920212223242526272829303132608052602060806080600060006001620493e0f15060805160005500"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
