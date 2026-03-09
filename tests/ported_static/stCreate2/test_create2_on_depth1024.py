"""
Create2OnDepth1024, 0x0400 indicates 1022 level.

Ported from:
tests/static/state_tests/stCreate2/Create2OnDepth1024Filler.json
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
    ["tests/static/state_tests/stCreate2/Create2OnDepth1024Filler.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.valid_until("Prague")
@pytest.mark.pre_alloc_mutable
def test_create2_on_depth1024(
    state_test: StateTestFiller,
    pre: Alloc,
) -> None:
    """Create2OnDepth1024, 0x0400 indicates 1022 level."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xb94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    callee = Address("0xc94f5374fce5edbc8e2a8697c15331677e6ebf0b")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=9223372036854775807,
    )

    pre[sender] = Account(
        balance=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # noqa: E501
        nonce=0,
    )
    pre[contract] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "600035600052600051600201600052610400600051146043576000600060206000610400"  # noqa: E501
            "6000511473c94f5374fce5edbc8e2a8697c15331677e6ebf0b5af150606d565b78686000"  # noqa: E501
            "600060006000f56000526000600960176000f56001556020526000601960276000f56001"  # noqa: E501
            "555b00"
        ),
    )
    pre[callee] = Account(
        balance=0,
        nonce=0,
        code=bytes.fromhex(
            "6000356000526000600060206000600073b94f5374fce5edbc8e2a8697c15331677e6ebf"  # noqa: E501
            "0b5af100"
        ),
    )

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=b"",
        gas_limit=9151314442816847871,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = {
        Address("0xb250d8cdad4a7a81323be508f4ac44584dd27597"): Account(
            storage={1: 0x436B8F99E8D953CDAF8F9472116ADD83CCD82A65},
        ),
        contract: Account(
            storage={1: 0xB250D8CDAD4A7A81323BE508F4AC44584DD27597},
            code=bytes.fromhex(
                "6000356000526000516002016000526104006000511460435760006000602060006104006000511473c94f5374fce5edbc8e2a8697c15331677e6ebf0b5af150606d565b78686000600060006000f56000526000600960176000f56001556020526000601960276000f56001555b00"  # noqa: E501
            ),
        ),
        callee: Account(
            code=bytes.fromhex(
                "6000356000526000600060206000600073b94f5374fce5edbc8e2a8697c15331677e6ebf0b5af100"  # noqa: E501
            ),
        ),
    }

    state_test(env=env, pre=pre, post=post, tx=tx)
