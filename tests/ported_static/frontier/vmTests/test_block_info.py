"""
Verify block-field opcodes store the block environment's values.

Ported from:
state_tests/VMTests/vmTests/blockInfoFiller.yml

@manually-enhanced: Do not overwrite. The CALL dispatcher, hardcoded
addresses, and the near-cap transaction gas limit were dropped; each
opcode's expectation now derives from the environment fields.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Environment,
    Fork,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

BLOCK_NUMBER = 1
TIMESTAMP = 1000
PREV_RANDAO = 0x20000
BLOCK_GAS_LIMIT = 100_000_000
VALUE_SLOT = 0x0


@pytest.mark.ported_from(
    ["state_tests/VMTests/vmTests/blockInfoFiller.yml"],
)
@pytest.mark.valid_from("Frontier")
@pytest.mark.parametrize(
    "opcode",
    [
        pytest.param(Op.COINBASE, id="coinbase"),
        pytest.param(Op.PREVRANDAO, id="difficulty"),
        pytest.param(Op.GASLIMIT, id="gaslimit"),
        pytest.param(Op.NUMBER, id="number"),
        pytest.param(Op.TIMESTAMP, id="timestamp"),
    ],
)
def test_block_info(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    opcode: Op,
) -> None:
    """Store one block-field opcode's result and match it to the env."""
    coinbase = pre.fund_eoa(amount=0)

    env = Environment(
        fee_recipient=coinbase,
        number=BLOCK_NUMBER,
        timestamp=TIMESTAMP,
        prev_randao=PREV_RANDAO,
        gas_limit=BLOCK_GAS_LIMIT,
    )

    contract = pre.deploy_contract(
        code=Op.SSTORE(key=VALUE_SLOT, value=opcode) + Op.STOP,
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=contract,
    )

    expected = {
        Op.COINBASE: coinbase,
        Op.PREVRANDAO: PREV_RANDAO,
        Op.GASLIMIT: BLOCK_GAS_LIMIT,
        Op.NUMBER: BLOCK_NUMBER,
        Op.TIMESTAMP: TIMESTAMP,
    }[opcode]

    post = {contract: Account(storage={VALUE_SLOT: expected})}

    state_test(env=env, pre=pre, post=post, tx=tx)
