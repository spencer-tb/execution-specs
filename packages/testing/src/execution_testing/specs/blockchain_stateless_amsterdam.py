"""
Amsterdam bridge for stateless blockchain-test generation.

Every function here reaches into the EELS Amsterdam stateless modules,
imported lazily because they land with the witness-generation tier.
Witnesses are fork-versioned by design -- the guest program is the
spec -- so this module is deliberately fork-specific rather than
resolving through the fork; the temporary mypy overrides in
`pyproject.toml` are scoped to it.
"""

from typing import Any, List, Tuple

from execution_testing.base_types import Bytes, Hash, ZeroPaddedHexNumber
from execution_testing.client_clis import Result
from execution_testing.fixtures.blockchain import FixtureHeader
from execution_testing.forks import Fork
from execution_testing.test_types import (
    Environment,
    ExecutionWitness,
    Transaction,
    Withdrawal,
)
from execution_testing.test_types.block_access_list import BlockAccessList
from execution_testing.test_types.execution_witness.exceptions import (
    StatelessValidationError,
)


def rebuild_amsterdam_stateless_input_with_overrides(
    *,
    fork: Fork,
    block_number: int,
    timestamp: int,
    original_stateless_input_bytes: Bytes,
    execution_witness: ExecutionWitness | None = None,
    public_keys: Tuple[Bytes, ...] | None = None,
) -> Bytes:
    """
    Rebuild the stateless input bytes with test overrides.

    Amsterdam is currently the only fork with stateless guest support in this
    repository, so the rebuild path is kept Amsterdam-specific.
    """
    active_fork = fork.fork_at(block_number=block_number, timestamp=timestamp)
    if active_fork.name() != "Amsterdam":
        raise StatelessValidationError(
            "Execution witness input rebuild is only supported for Amsterdam"
        )

    from ethereum.forks.amsterdam.stateless import (
        ExecutionWitness as AmsterdamExecutionWitness,
    )
    from ethereum.forks.amsterdam.stateless import (
        StatelessInput as AmsterdamStatelessInput,
    )
    from ethereum.forks.amsterdam.stateless_guest import (
        deserialize_stateless_input,
    )
    from ethereum.forks.amsterdam.stateless_host import (
        serialize_stateless_input,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes

    original_input = deserialize_stateless_input(
        AmsterdamBytes(bytes(original_stateless_input_bytes))
    )
    rebuilt_witness = original_input.witness
    if execution_witness is not None:
        rebuilt_witness = AmsterdamExecutionWitness(
            state=tuple(
                AmsterdamBytes(bytes(node)) for node in execution_witness.state
            ),
            codes=tuple(
                AmsterdamBytes(bytes(code)) for code in execution_witness.codes
            ),
            headers=tuple(
                AmsterdamBytes(bytes(header))
                for header in execution_witness.headers
            ),
        )
    rebuilt_input = AmsterdamStatelessInput(
        new_payload_request=original_input.new_payload_request,
        witness=rebuilt_witness,
        chain_id=original_input.chain_id,
        public_keys=(
            tuple(AmsterdamBytes(bytes(key)) for key in public_keys)
            if public_keys is not None
            else original_input.public_keys
        ),
    )
    rebuilt_input_bytes = serialize_stateless_input(rebuilt_input)
    return Bytes(bytes(rebuilt_input_bytes))


def rerun_amsterdam_stateless_guest_with_input_bytes(
    *,
    fork: Fork,
    block_number: int,
    timestamp: int,
    stateless_input_bytes: Bytes,
) -> tuple[Bytes, Bytes, bool]:
    """
    Rerun the Amsterdam stateless guest with raw stateless input bytes.
    """
    active_fork = fork.fork_at(block_number=block_number, timestamp=timestamp)
    if active_fork.name() != "Amsterdam":
        raise StatelessValidationError(
            "Stateless guest raw input rerun is only supported for Amsterdam"
        )

    from ethereum.forks.amsterdam.stateless_guest import run_stateless_guest
    from ethereum.forks.amsterdam.stateless_host import (
        deserialize_stateless_output,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes

    guest_input_bytes = AmsterdamBytes(bytes(stateless_input_bytes))
    stateless_output_bytes = run_stateless_guest(guest_input_bytes)
    stateless_output = deserialize_stateless_output(stateless_output_bytes)

    return (
        Bytes(bytes(guest_input_bytes)),
        Bytes(bytes(stateless_output_bytes)),
        stateless_output.successful_validation,
    )


def get_amsterdam_stateless_input_public_key_data(
    *,
    fork: Fork,
    block_number: int,
    timestamp: int,
    stateless_input_bytes: Bytes,
) -> tuple[Tuple[Bytes, ...], Tuple[Bytes, ...]]:
    """
    Decode Amsterdam stateless input public keys and payload transactions.
    """
    active_fork = fork.fork_at(block_number=block_number, timestamp=timestamp)
    if active_fork.name() != "Amsterdam":
        raise StatelessValidationError(
            "Stateless input public-key decoding is only supported for "
            "Amsterdam"
        )

    from ethereum.forks.amsterdam.stateless_guest import (
        deserialize_stateless_input,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes

    stateless_input = deserialize_stateless_input(
        AmsterdamBytes(bytes(stateless_input_bytes))
    )
    public_keys = tuple(
        Bytes(bytes(public_key)) for public_key in stateless_input.public_keys
    )
    payload_transactions = tuple(
        Bytes(bytes(transaction))
        for transaction in (
            stateless_input.new_payload_request.execution_payload.transactions
        )
    )
    return public_keys, payload_transactions


def verify_stateless_input_public_keys(
    public_keys: Tuple[Bytes, ...],
    payload_transactions: Tuple[Bytes, ...],
    chain_id: int,
) -> None:
    """
    Verify that every payload transaction has its recovered public key.
    """
    payload_transaction_count = len(payload_transactions)
    if len(public_keys) != payload_transaction_count:
        raise AssertionError(
            "Stateless input public key count does not match payload "
            f"transactions: got {len(public_keys)} public keys for "
            f"{payload_transaction_count} transactions"
        )

    from ethereum.forks.amsterdam.transactions import (
        decode_transaction,
        recover_transaction_public_key,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes
    from ethereum_types.numeric import U64

    for index, (public_key, payload_transaction) in enumerate(
        zip(public_keys, payload_transactions, strict=True)
    ):
        transaction = decode_transaction(
            AmsterdamBytes(bytes(payload_transaction))
        )
        expected_public_key = recover_transaction_public_key(
            U64(chain_id),
            transaction,
        )
        if bytes(public_key) != bytes(expected_public_key):
            raise AssertionError(
                "Stateless input public key "
                f"{index} does not match recovered transaction public key"
            )


def _decode_amsterdam_header_bytes(header_rlp: Bytes) -> Any | None:
    """
    Decode an Amsterdam or immediate pre-Amsterdam RLP header.
    """
    from ethereum.forks.amsterdam.stateless import _decode_header
    from ethereum_types.bytes import Bytes as AmsterdamBytes

    try:
        return _decode_header(AmsterdamBytes(bytes(header_rlp)))
    except Exception:
        return None


def _convert_amsterdam_execution_witness(
    execution_witness: ExecutionWitness,
) -> Any:
    """
    Convert fixture execution witness data to Amsterdam fork types.
    """
    from ethereum.forks.amsterdam.stateless import (
        ExecutionWitness as AmsterdamExecutionWitness,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes

    return AmsterdamExecutionWitness(
        state=tuple(
            AmsterdamBytes(bytes(node)) for node in execution_witness.state
        ),
        codes=tuple(
            AmsterdamBytes(bytes(code)) for code in execution_witness.codes
        ),
        headers=tuple(
            AmsterdamBytes(bytes(header))
            for header in execution_witness.headers
        ),
    )


def _convert_amsterdam_withdrawals(
    withdrawals: List[Withdrawal] | None,
) -> Any:
    """
    Convert fixture withdrawals to Amsterdam fork withdrawals.
    """
    from ethereum.forks.amsterdam.blocks import (
        Withdrawal as AmsterdamWithdrawal,
    )
    from ethereum.state import Address as AmsterdamAddress
    from ethereum_types.numeric import U64

    if withdrawals is None:
        return ()
    return tuple(
        AmsterdamWithdrawal(
            index=U64(int(withdrawal.index)),
            validator_index=U64(int(withdrawal.validator_index)),
            address=AmsterdamAddress(bytes(withdrawal.address)),
            amount=U64(int(withdrawal.amount)),
        )
        for withdrawal in withdrawals
    )


def _convert_amsterdam_block_access_list(
    block_access_list: BlockAccessList,
) -> Any:
    """
    Convert fixture BAL data to Amsterdam fork BAL data.
    """
    import importlib

    block_access_lists = importlib.import_module(
        "ethereum.forks.amsterdam.block_access_lists"
    )

    def bal_type(name: str) -> Any:
        return getattr(block_access_lists, name)

    account_changes = bal_type("AccountChanges")
    balance_change = bal_type("BalanceChange")
    code_change = bal_type("CodeChange")
    nonce_change = bal_type("NonceChange")
    slot_changes = bal_type("SlotChanges")
    storage_change = bal_type("StorageChange")

    from ethereum.state import Address as AmsterdamAddress
    from ethereum_types.bytes import Bytes as AmsterdamBytes
    from ethereum_types.numeric import U32, U64, U256

    return [
        account_changes(
            address=AmsterdamAddress(bytes(account.address)),
            storage_changes=tuple(
                slot_changes(
                    slot=U256(int(slot.slot)),
                    changes=tuple(
                        storage_change(
                            block_access_index=U32(
                                int(change.block_access_index)
                            ),
                            new_value=U256(int(change.post_value)),
                        )
                        for change in slot.slot_changes
                    ),
                )
                for slot in account.storage_changes
            ),
            storage_reads=tuple(
                U256(int(slot)) for slot in account.storage_reads
            ),
            balance_changes=tuple(
                balance_change(
                    block_access_index=U32(int(change.block_access_index)),
                    post_balance=U256(int(change.post_balance)),
                )
                for change in account.balance_changes
            ),
            nonce_changes=tuple(
                nonce_change(
                    block_access_index=U32(int(change.block_access_index)),
                    new_nonce=U64(int(change.post_nonce)),
                )
                for change in account.nonce_changes
            ),
            code_changes=tuple(
                code_change(
                    block_access_index=U32(int(change.block_access_index)),
                    new_code=AmsterdamBytes(bytes(change.new_code)),
                )
                for change in account.code_changes
            ),
        )
        for account in block_access_list.root
    ]


def build_amsterdam_stateless_artifacts_from_t8n(
    *,
    fork: Fork,
    block_number: int,
    timestamp: int,
    header: FixtureHeader,
    previous_env: Environment,
    txs: List[Transaction],
    result: Result,
    withdrawals: List[Withdrawal] | None,
    requests_list: List[Bytes] | None,
    execution_witness: ExecutionWitness,
    block_access_list: BlockAccessList,
    chain_id: int,
) -> tuple[Bytes, Bytes] | None:
    """
    Build Amsterdam stateless input/output bytes from t8n witness artifacts.

    Returns ``None`` when the finalized request list cannot be decoded into
    the Amsterdam request container, matching the existing EELS t8n behavior.
    """
    active_fork = fork.fork_at(block_number=block_number, timestamp=timestamp)
    if active_fork.name() != "Amsterdam" or block_number == 0:
        return None

    from ethereum.forks.amsterdam.blocks import (
        Block as AmsterdamBlock,
    )
    from ethereum.forks.amsterdam.blocks import (
        Header as AmsterdamHeader,
    )
    from ethereum.forks.amsterdam.execution_engine.requests import (
        decode_execution_requests,
    )
    from ethereum.forks.amsterdam.stateless import (
        StatelessValidationResult,
        compute_new_payload_request_root,
    )
    from ethereum.forks.amsterdam.stateless_guest import (
        serialize_stateless_output,
    )
    from ethereum.forks.amsterdam.stateless_host import (
        build_stateless_input,
        serialize_stateless_input,
    )
    from ethereum.forks.amsterdam.stateless_ssz import (
        STATELESS_INPUT_SCHEMA_ID,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes
    from ethereum_types.numeric import U16, U64

    parent_number = ZeroPaddedHexNumber(block_number - 1)
    parent_header_rlp = previous_env.block_headers.get(parent_number)
    if parent_header_rlp is None:
        return None
    parent_header = _decode_amsterdam_header_bytes(parent_header_rlp)
    if parent_header is None:
        return None
    if Hash(parent_header_rlp.keccak256()) != header.parent_hash:
        return None

    current_header = _decode_amsterdam_header_bytes(header.rlp)
    if not isinstance(current_header, AmsterdamHeader):
        return None

    try:
        execution_requests = decode_execution_requests(
            tuple(
                AmsterdamBytes(bytes(request))
                for request in requests_list or []
            )
        )
    except Exception:
        return None

    rejected_indices = {
        int(rejected.index) for rejected in result.rejected_transactions
    }
    accepted_txs = tuple(
        AmsterdamBytes(bytes(tx.rlp()))
        for index, tx in enumerate(txs)
        if index not in rejected_indices
    )
    block = AmsterdamBlock(
        header=current_header,
        transactions=accepted_txs,
        ommers=(),
        withdrawals=_convert_amsterdam_withdrawals(withdrawals),
    )
    stateless_input = build_stateless_input(
        block,
        execution_witness=_convert_amsterdam_execution_witness(
            execution_witness
        ),
        execution_requests=execution_requests,
        block_access_list=_convert_amsterdam_block_access_list(
            block_access_list
        ),
        chain_id=U64(chain_id),
    )
    stateless_input_bytes = serialize_stateless_input(stateless_input)
    # Temporary trust path for external benchmark filling until Geth emits
    # both stateless byte fields.
    stateless_output = StatelessValidationResult(
        new_payload_request_root=compute_new_payload_request_root(
            stateless_input
        ),
        successful_validation=True,
        chain_id=U64(chain_id),
        schema_id=U16(STATELESS_INPUT_SCHEMA_ID),
    )
    stateless_output_bytes = serialize_stateless_output(stateless_output)
    return (
        Bytes(bytes(stateless_input_bytes)),
        Bytes(bytes(stateless_output_bytes)),
    )


def decode_amsterdam_stateless_output(
    *,
    fork: Fork,
    block_number: int,
    timestamp: int,
    stateless_output_bytes: Bytes | None,
) -> Any | None:
    """
    Decode Amsterdam stateless output, if available for the active fork.

    Amsterdam is currently the only fork with stateless guest support in this
    repository, so the decode path is kept Amsterdam-specific.
    """
    active_fork = fork.fork_at(block_number=block_number, timestamp=timestamp)
    if active_fork.name() != "Amsterdam" or stateless_output_bytes is None:
        return None

    from ethereum.forks.amsterdam.stateless_host import (
        deserialize_stateless_output,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes

    return deserialize_stateless_output(
        AmsterdamBytes(bytes(stateless_output_bytes))
    )


def assert_amsterdam_stateless_output_chain_id(
    *,
    block_number: int,
    chain_id: int,
    stateless_output: Any | None,
    expected_chain_id: Any | None = None,
) -> None:
    """
    Assert the stateless output reports the expected chain identifier.
    """
    if stateless_output is None:
        return

    if expected_chain_id is None:
        from ethereum_types.numeric import U64

        expected_chain_id = U64(chain_id)

    if stateless_output.chain_id != expected_chain_id:
        raise AssertionError(
            "Stateless output chain_id mismatch for block "
            f"{block_number}: got {stateless_output.chain_id}, "
            f"want {expected_chain_id}"
        )


def is_invalid_input_stateless_output(stateless_output: Any) -> bool:
    """
    Return whether output is the invalid stateless input sentinel.
    """
    from ethereum_types.numeric import U16, U64

    return (
        not stateless_output.successful_validation
        and bytes(stateless_output.new_payload_request_root) == b"\0" * 32
        and stateless_output.chain_id == U64(0)
        and stateless_output.schema_id == U16(0)
    )


def assert_amsterdam_stateless_output_request_root(
    *,
    block_number: int,
    stateless_input: Any,
    stateless_output: Any,
) -> None:
    """
    Assert the output commits to the decoded Amsterdam payload request.
    """
    from ethereum.forks.amsterdam.stateless import (
        compute_new_payload_request_root,
    )

    expected_root = compute_new_payload_request_root(stateless_input)
    actual_root = stateless_output.new_payload_request_root
    if actual_root != expected_root:
        raise AssertionError(
            "Stateless output new_payload_request_root mismatch for block "
            f"{block_number}: got 0x{bytes(actual_root).hex()}, "
            f"want 0x{bytes(expected_root).hex()}"
        )


def assert_amsterdam_stateless_output_schema_id(
    *,
    block_number: int,
    stateless_output: Any,
) -> None:
    """
    Assert the output identifies the input schema executed by the guest.
    """
    from ethereum.forks.amsterdam.stateless_ssz import (
        STATELESS_INPUT_SCHEMA_ID,
    )
    from ethereum_types.numeric import U16

    expected_schema_id = U16(STATELESS_INPUT_SCHEMA_ID)

    if stateless_output.schema_id != expected_schema_id:
        raise AssertionError(
            "Stateless output schema_id mismatch for block "
            f"{block_number}: got {stateless_output.schema_id}, "
            f"want {expected_schema_id}"
        )


def verify_amsterdam_stateless_output(
    *,
    block_number: int,
    chain_id: int,
    stateless_input_bytes: Bytes,
    stateless_output: Any,
    input_bytes_modified: bool,
) -> None:
    """
    Verify the public values returned by the Amsterdam stateless guest.
    """
    from ethereum.forks.amsterdam.stateless_guest import (
        deserialize_stateless_input,
    )
    from ethereum_types.bytes import Bytes as AmsterdamBytes

    try:
        stateless_input = deserialize_stateless_input(
            AmsterdamBytes(bytes(stateless_input_bytes))
        )
    except Exception as exc:
        if input_bytes_modified and is_invalid_input_stateless_output(
            stateless_output
        ):
            return
        raise AssertionError(
            "Stateless input decoding failed for block "
            f"{block_number}, but its output is not the invalid-input sentinel"
        ) from exc

    assert_amsterdam_stateless_output_request_root(
        block_number=block_number,
        stateless_input=stateless_input,
        stateless_output=stateless_output,
    )
    assert_amsterdam_stateless_output_schema_id(
        block_number=block_number,
        stateless_output=stateless_output,
    )
    assert_amsterdam_stateless_output_chain_id(
        block_number=block_number,
        chain_id=chain_id,
        stateless_output=stateless_output,
        expected_chain_id=(
            stateless_input.chain_id if input_bytes_modified else None
        ),
    )
