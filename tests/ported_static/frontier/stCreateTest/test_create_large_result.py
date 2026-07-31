"""
Measure CREATE/CREATE2 gas when the constructor returns or reverts results
of increasing size: a legal deposit is priced per byte, an oversized one
(EIP-170) forfeits the whole child grant, and a revert charges only the
work done.

Ported from:
state_tests/stCreateTest/createLargeResultFiller.yml

@manually-enhanced: Do not overwrite. The runtime EXTCODECOPY factory and
its absolute GAS-delta pins (functions of the removed 80M gas limit) were
replaced by a calldata-delivered init code and a gas-capped creator frame,
so every expectation derives from fork composites and the EIP-150 63/64
rule; this also lifts the old Prague ceiling. The size axis derives from
fork.max_code_size() (EIP-7954 raises it). Floors at Berlin: the SSTORE
composites price warm/cold access, mismatching pre-Berlin schedules.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    Bytes,
    Fork,
    Hash,
    StateTestFiller,
    Transaction,
    compute_create_address,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"

ADDR_SLOT = 0x0
GAS_SLOT = 0x1
HASH_SLOT = 0x2
CREATE2_SALT = 0x5A17
# A comfortably legal deployed-code size; the other sizes derive from the
# fork's deployed-code ceiling (EIP-170, raised by EIP-7954).
NORMAL_SIZE = 0x100
# The init code image: the constructor template padded to this offset,
# followed by one word holding the requested deployed-code size.
SIZE_WORD_OFFSET = 0x100
INIT_CODE_SIZE = SIZE_WORD_OFFSET + 0x20
# Creator memory: the init code image, then the gas snapshot word.
SNAPSHOT_OFFSET = INIT_CODE_SIZE
CREATOR_MEMORY = SNAPSHOT_OFFSET + 0x20
# Fixed budget for the creator frame; the forfeited grant of an oversized
# deposit derives from it via the 63/64 rule. It must cover the priciest
# legal deposit (the fork's whole code-size ceiling) with headroom.
CREATOR_GAS = 6_000_000
BUDGET_MARGIN = 10_000


@pytest.mark.ported_from(
    ["state_tests/stCreateTest/createLargeResultFiller.yml"],
)
@pytest.mark.valid_from("Berlin")
@pytest.mark.parametrize(
    "create_op, reverts, size_kind",
    [
        pytest.param(Op.CREATE, False, "normal", id="CREATE-RETURN"),
        pytest.param(Op.CREATE2, False, "normal", id="CREATE2-RETURN"),
        pytest.param(Op.CREATE, True, "normal", id="CREATE-REVERT"),
        pytest.param(Op.CREATE2, True, "normal", id="CREATE2-REVERT"),
        pytest.param(Op.CREATE, False, "max", id="CREATE-RETURN-MAX"),
        pytest.param(Op.CREATE2, False, "max", id="CREATE2-RETURN-MAX"),
        pytest.param(Op.CREATE, True, "max", id="CREATE-REVERT-MAX"),
        pytest.param(Op.CREATE2, True, "max", id="CREATE2-REVERT-MAX"),
        pytest.param(Op.CREATE, False, "toobig", id="CREATE-RETURN-TOOBIG"),
        pytest.param(Op.CREATE2, False, "toobig", id="CREATE2-RETURN-TOOBIG"),
        pytest.param(Op.CREATE, True, "toobig", id="CREATE-REVERT-TOOBIG"),
        pytest.param(Op.CREATE2, True, "toobig", id="CREATE2-REVERT-TOOBIG"),
        pytest.param(Op.CREATE, False, "huge", id="CREATE-RETURN-HUGE"),
        pytest.param(Op.CREATE2, False, "huge", id="CREATE2-RETURN-HUGE"),
        pytest.param(Op.CREATE, True, "huge", id="CREATE-REVERT-HUGE"),
        pytest.param(Op.CREATE2, True, "huge", id="CREATE2-REVERT-HUGE"),
    ],
)
def test_create_large_result(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
    create_op: Op,
    reverts: bool,
    size_kind: str,
) -> None:
    """Create a contract of the requested size and measure the gas."""
    max_code_size = fork.max_code_size()
    deploy_size = {
        "normal": NORMAL_SIZE,
        "max": max_code_size,
        "toobig": max_code_size + 1,
        "huge": 2 * max_code_size,
    }[size_kind]
    deployed = deploy_size <= max_code_size and not reverts

    # The constructor writes a marker word, copies its trailing size word
    # into scratch memory, and returns (or reverts) that many bytes.
    child_memory = max(INIT_CODE_SIZE, deploy_size)
    end_op = Op.REVERT if reverts else Op.RETURN
    end_kwargs: dict = {
        "offset": 0x0,
        "size": Op.MLOAD(
            offset=SIZE_WORD_OFFSET,
            old_memory_size=INIT_CODE_SIZE,
            new_memory_size=INIT_CODE_SIZE,
        ),
        "old_memory_size": INIT_CODE_SIZE,
        "new_memory_size": child_memory,
    }
    if not reverts:
        end_kwargs["code_deposit_size"] = deploy_size
    child_code = (
        Op.MSTORE(offset=0x0, value=Op.NOT(0x0), new_memory_size=0x20)
        + Op.CODECOPY(
            dest_offset=SIZE_WORD_OFFSET,
            offset=SIZE_WORD_OFFSET,
            size=0x20,
            data_size=0x20,
            old_memory_size=0x20,
            new_memory_size=INIT_CODE_SIZE,
        )
        + end_op(**end_kwargs)
    )
    assert len(bytes(child_code)) <= SIZE_WORD_OFFSET
    init_code = Bytes(
        bytes(child_code).ljust(SIZE_WORD_OFFSET, b"\x00") + Hash(deploy_size)
    )

    # The creator loads the init code from calldata, then measures the
    # create inside a GAS-snapshot window and records the code hash.
    prelude = Op.CALLDATACOPY(
        dest_offset=0x0,
        offset=0x0,
        size=Op.CALLDATASIZE,
        data_size=INIT_CODE_SIZE,
        new_memory_size=INIT_CODE_SIZE,
    )
    head = Op.MSTORE(
        offset=SNAPSHOT_OFFSET,
        value=Op.GAS,
        old_memory_size=INIT_CODE_SIZE,
        new_memory_size=CREATOR_MEMORY,
    )
    create_kwargs: dict = {
        "value": 0x0,
        "offset": 0x0,
        "size": INIT_CODE_SIZE,
        "init_code_size": INIT_CODE_SIZE,
        "old_memory_size": CREATOR_MEMORY,
        "new_memory_size": CREATOR_MEMORY,
    }
    if create_op == Op.CREATE2:
        create_kwargs["salt"] = CREATE2_SALT
    create_code = create_op(**create_kwargs)
    body = Op.SSTORE(
        key=ADDR_SLOT,
        value=create_code,
        key_warm=False,
        original_value=0,
        new_value=1 if deployed else 0,
    )
    tail = Op.SSTORE(
        key=GAS_SLOT,
        value=Op.SUB(
            Op.MLOAD(
                offset=SNAPSHOT_OFFSET,
                old_memory_size=CREATOR_MEMORY,
                new_memory_size=CREATOR_MEMORY,
            ),
            Op.GAS,
        ),
        key_warm=False,
        original_value=0,
        new_value=1,
    )
    hash_store = Op.SSTORE(
        key=HASH_SLOT,
        value=Op.EXTCODEHASH(
            address=Op.SLOAD(key=ADDR_SLOT, key_warm=True),
            address_warm=deployed,
        ),
        key_warm=False,
        original_value=0,
        new_value=1 if deployed else 0,
    )
    creator = pre.deploy_contract(
        code=prelude + head + body + tail + hash_store + Op.STOP,
    )

    # A fixed outer grant makes the creator's window independent of the
    # transaction gas limit (the entry's 63/64 withhold never binds).
    entry = pre.deploy_contract(
        code=Op.CALLDATACOPY(dest_offset=0x0, offset=0x0, size=Op.CALLDATASIZE)
        + Op.CALL(
            gas=CREATOR_GAS,
            address=creator,
            args_offset=0x0,
            args_size=Op.CALLDATASIZE,
        )
        + Op.STOP,
    )

    tx = Transaction(
        protected=fork.supports_protected_txs(),
        sender=pre.fund_eoa(),
        to=entry,
        data=init_code,
    )

    # With a maxed-out state-gas reservoir (no explicit gas limit), the
    # GAS-visible window is the execution cost alone; before EIP-8037 the
    # execution cost is the whole cost, so one expression fits every fork.
    if reverts or deployed:
        child_consumed = child_code.execution_cost(fork)
    else:
        # An oversized deposit aborts the child (EIP-170), forfeiting the
        # whole grant the EIP-150 63/64 rule forwarded to it.
        available = (
            CREATOR_GAS
            - prelude.execution_cost(fork)
            - head.execution_cost(fork)
            - create_code.execution_cost(fork)
        )
        child_consumed = available - available // 64
    gas_delta = (
        head.execution_cost(fork) + body.execution_cost(fork) + child_consumed
    )
    # The budget must cover the whole creator frame (or, when the child
    # forfeits its grant, the 1/64 retention must cover the unwind).
    unwind_cost = tail.execution_cost(fork) + hash_store.execution_cost(fork)
    if reverts or deployed:
        assert (
            CREATOR_GAS
            > prelude.execution_cost(fork)
            + gas_delta
            + unwind_cost
            + BUDGET_MARGIN
        ), "creator budget too small"
    else:
        assert available // 64 > unwind_cost + BUDGET_MARGIN, (
            "grant retention too small for the unwind"
        )

    if create_op == Op.CREATE:
        created = compute_create_address(address=creator, nonce=1)
    else:
        created = compute_create_address(
            address=creator,
            salt=CREATE2_SALT,
            initcode=init_code,
            opcode=Op.CREATE2,
        )
    # The deployed image: the constructor's marker word, then zeroed
    # memory, with the copied size word visible when the result is large
    # enough to reach it.
    image = bytearray(deploy_size)
    image[0:32] = b"\xff" * 32
    if deploy_size > SIZE_WORD_OFFSET:
        word = bytes(Hash(deploy_size))
        image[SIZE_WORD_OFFSET : SIZE_WORD_OFFSET + 0x20] = word[
            : deploy_size - SIZE_WORD_OFFSET
        ]
    deployed_code = Bytes(bytes(image))

    post = {
        creator: Account(
            storage={
                ADDR_SLOT: created if deployed else 0,
                GAS_SLOT: gas_delta,
                HASH_SLOT: deployed_code.keccak256() if deployed else 0,
            },
        ),
        created: (
            Account(nonce=1, balance=0) if deployed else Account.NONEXISTENT
        ),
    }

    state_test(pre=pre, post=post, tx=tx)
