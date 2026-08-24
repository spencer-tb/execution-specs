"""
Tests for [EIP-8115: Batch priority fees at end of block](https://eips.ethereum.org/EIPS/eip-8115).

Priority fees are no longer credited to the fee recipient after each
transaction; they are summed and credited once, after all transactions
but before withdrawals. Pin the single post-execution credit, the
mid-block invisibility of accrued fees, the fee recipient's inability
to spend them within the block, and the preserved touch semantics.
"""

import pytest
from execution_testing import (
    Account,
    Alloc,
    BalAccountExpectation,
    BalBalanceChange,
    Block,
    BlockAccessListExpectation,
    BlockchainTestFiller,
    Environment,
    Fork,
    Header,
    Op,
    RecipientType,
    StateTestFiller,
    Storage,
    Transaction,
    TransactionException,
    Withdrawal,
)

from .spec import ref_spec_8115

REFERENCE_SPEC_GIT_PATH = ref_spec_8115.git_path
REFERENCE_SPEC_VERSION = ref_spec_8115.version

pytestmark = pytest.mark.valid_from("EIP8115")

GWEI = 10**9

GENESIS_BASE_FEE = 0x7


def child_base_fee(fork: Fork, genesis_env: Environment) -> int:
    """Derive the base fee of the first block from the genesis environment."""
    return fork.base_fee_per_gas_calculator()(
        parent_base_fee_per_gas=int(genesis_env.base_fee_per_gas or 0),
        parent_gas_used=0,
        parent_gas_limit=genesis_env.gas_limit,
    )


def plain_transfer_gas(fork: Fork) -> int:
    """Gas used by a plain value transfer to an existing EOA."""
    return fork.transaction_intrinsic_cost_calculator()(
        calldata=b"",
        contract_creation=False,
        access_list=[],
        recipient_type=RecipientType.EOA,
        sends_value=True,
    )


def test_state_test_credits_batched_priority_fee(
    state_test: StateTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A state test represents a one-transaction block, so its post-state
    includes the batched priority-fee credit applied after that transaction.
    """
    base_fee_per_gas = GENESIS_BASE_FEE
    tip_rate = 3
    gas_used = plain_transfer_gas(fork)

    sender = pre.fund_eoa()
    recipient = pre.fund_eoa(amount=1)
    coinbase = pre.fund_eoa(amount=0)

    state_test(
        env=Environment(
            base_fee_per_gas=base_fee_per_gas,
            fee_recipient=coinbase,
        ),
        pre=pre,
        tx=Transaction(
            sender=sender,
            to=recipient,
            value=1,
            gas_limit=gas_used,
            gas_price=base_fee_per_gas + tip_rate,
        ),
        post={coinbase: Account(balance=gas_used * tip_rate)},
    )


def test_priority_fees_credited_once_at_end_of_block(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    The fee recipient receives the block's summed priority fees as a
    single balance change at the post-execution block access index,
    with no per-transaction credits.
    """
    genesis_env = Environment(base_fee_per_gas=GENESIS_BASE_FEE)
    base_fee_per_gas = child_base_fee(fork, genesis_env)
    gas_used = plain_transfer_gas(fork)

    tip_rates = [1, 2, 3]
    value = 100

    bob = pre.fund_eoa(amount=1)
    coinbase = pre.fund_eoa(amount=0)

    txs = [
        Transaction(
            sender=pre.fund_eoa(
                amount=gas_used * (base_fee_per_gas + tip_rate) + value
            ),
            to=bob,
            value=value,
            gas_limit=gas_used,
            gas_price=base_fee_per_gas + tip_rate,
        )
        for tip_rate in tip_rates
    ]

    total_priority_fees = gas_used * sum(tip_rates)
    post_execution_index = len(txs) + 1

    block = Block(
        txs=txs,
        fee_recipient=coinbase,
        header_verify=Header(base_fee_per_gas=base_fee_per_gas),
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                # A single credit at the post-execution index; the
                # exact list pins the absence of per-transaction
                # credits at indices 1..len(txs).
                coinbase: BalAccountExpectation(
                    balance_changes=[
                        BalBalanceChange(
                            block_access_index=post_execution_index,
                            post_balance=total_priority_fees,
                        )
                    ],
                ),
            }
        ),
    )

    blockchain_test(
        pre=pre,
        blocks=[block],
        post={
            coinbase: Account(balance=total_priority_fees),
            bob: Account(balance=1 + value * len(txs)),
        },
        genesis_environment=genesis_env,
    )


def test_intra_block_coinbase_balance_excludes_accrued_fees(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A later transaction reading the fee recipient's balance sees the
    pre-block balance: fees accrued by earlier transactions in the same
    block are not yet credited.
    """
    genesis_env = Environment(base_fee_per_gas=GENESIS_BASE_FEE)
    base_fee_per_gas = child_base_fee(fork, genesis_env)
    gas_used = plain_transfer_gas(fork)

    coinbase_initial_balance = 0x1000
    coinbase = pre.fund_eoa(amount=coinbase_initial_balance)

    tip_rate = 5
    tip = gas_used * tip_rate
    value = 100

    bob = pre.fund_eoa(amount=1)
    alice = pre.fund_eoa(
        amount=gas_used * (base_fee_per_gas + tip_rate) + value
    )

    # The observer sees the coinbase balance untouched by alice's fee.
    storage = Storage()
    observer = pre.deploy_contract(
        code=Op.SSTORE(
            storage.store_next(coinbase_initial_balance),
            Op.BALANCE(Op.COINBASE),
        )
    )
    carol = pre.fund_eoa()

    txs = [
        Transaction(
            sender=alice,
            to=bob,
            value=value,
            gas_limit=gas_used,
            gas_price=base_fee_per_gas + tip_rate,
        ),
        # Zero tip keeps the fee recipient's final balance independent
        # of this transaction's gas usage.
        Transaction(
            sender=carol,
            to=observer,
            gas_price=base_fee_per_gas,
        ),
    ]

    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                txs=txs,
                fee_recipient=coinbase,
                header_verify=Header(base_fee_per_gas=base_fee_per_gas),
            )
        ],
        post={
            observer: Account(storage=storage),
            coinbase: Account(balance=coinbase_initial_balance + tip),
            bob: Account(balance=1 + value),
        },
        genesis_environment=genesis_env,
    )


@pytest.mark.parametrize(
    "covers_own_fee",
    [
        pytest.param(True, id="solvent_without_accrued_fees"),
        pytest.param(
            False,
            id="requires_accrued_fees",
            marks=pytest.mark.exception_test,
        ),
    ],
)
def test_coinbase_cannot_spend_accrued_fees(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
    covers_own_fee: bool,
) -> None:
    """
    The fee recipient cannot fund a later transaction of its own with
    priority fees accrued earlier in the block: if its pre-block
    balance falls short of the transaction's maximum gas fee by even
    one wei, the block is invalid.
    """
    genesis_env = Environment(base_fee_per_gas=GENESIS_BASE_FEE)
    base_fee_per_gas = child_base_fee(fork, genesis_env)
    transfer_gas = plain_transfer_gas(fork)

    # Alice's tip alone would cover the shortfall many times over.
    tip_rate = 1000
    tip = transfer_gas * tip_rate
    value = 100

    bob = pre.fund_eoa(amount=1)
    alice = pre.fund_eoa(
        amount=transfer_gas * (base_fee_per_gas + tip_rate) + value
    )

    coinbase_tx_gas = fork.transaction_intrinsic_cost_calculator()(
        calldata=b"",
        contract_creation=False,
        access_list=[],
        recipient_type=RecipientType.EOA,
        sends_value=False,
    )
    max_gas_fee = coinbase_tx_gas * base_fee_per_gas
    coinbase_initial_balance = (
        max_gas_fee if covers_own_fee else max_gas_fee - 1
    )
    coinbase = pre.fund_eoa(amount=coinbase_initial_balance)

    txs = [
        Transaction(
            sender=alice,
            to=bob,
            value=value,
            gas_limit=transfer_gas,
            gas_price=base_fee_per_gas + tip_rate,
        ),
        Transaction(
            sender=coinbase,
            to=bob,
            gas_limit=coinbase_tx_gas,
            gas_price=base_fee_per_gas,
            error=(
                None
                if covers_own_fee
                else TransactionException.INSUFFICIENT_ACCOUNT_FUNDS
            ),
        ),
    ]

    if covers_own_fee:
        blockchain_test(
            pre=pre,
            blocks=[
                Block(
                    txs=txs,
                    fee_recipient=coinbase,
                    header_verify=Header(base_fee_per_gas=base_fee_per_gas),
                )
            ],
            # The coinbase spends its whole pre-block balance on gas and
            # ends the block holding exactly alice's tip.
            post={
                coinbase: Account(balance=tip),
                bob: Account(balance=1 + value),
            },
            genesis_environment=genesis_env,
        )
    else:
        blockchain_test(
            pre=pre,
            blocks=[
                Block(
                    txs=txs,
                    fee_recipient=coinbase,
                    exception=TransactionException.INSUFFICIENT_ACCOUNT_FUNDS,
                )
            ],
            post={},
            genesis_environment=genesis_env,
        )


def test_zero_tip_block_still_touches_fee_recipient(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A block whose transactions pay no priority fees still touches the
    fee recipient once at the end of the block: it appears in the block
    access list without changes and, being empty, is not created.
    """
    genesis_env = Environment(base_fee_per_gas=GENESIS_BASE_FEE)
    base_fee_per_gas = child_base_fee(fork, genesis_env)
    gas_used = plain_transfer_gas(fork)

    value = 100
    bob = pre.fund_eoa(amount=1)
    alice = pre.fund_eoa(amount=gas_used * base_fee_per_gas + value)
    coinbase = pre.fund_eoa(amount=0)

    block = Block(
        txs=[
            Transaction(
                sender=alice,
                to=bob,
                value=value,
                gas_limit=gas_used,
                gas_price=base_fee_per_gas,
            )
        ],
        fee_recipient=coinbase,
        header_verify=Header(base_fee_per_gas=base_fee_per_gas),
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                coinbase: BalAccountExpectation.empty(),
            }
        ),
    )

    blockchain_test(
        pre=pre,
        blocks=[block],
        post={
            coinbase: Account.NONEXISTENT,
            bob: Account(balance=1 + value),
        },
        genesis_environment=genesis_env,
    )


def test_fee_credit_merges_with_withdrawal_at_post_execution_index(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
) -> None:
    """
    A fee recipient that also receives a withdrawal shows one balance
    change at the post-execution index carrying both credits, the fees
    landing before the withdrawal.
    """
    genesis_env = Environment(base_fee_per_gas=GENESIS_BASE_FEE)
    base_fee_per_gas = child_base_fee(fork, genesis_env)
    gas_used = plain_transfer_gas(fork)

    tip_rate = 3
    tip = gas_used * tip_rate
    value = 100
    withdrawal_amount_gwei = 10

    bob = pre.fund_eoa(amount=1)
    alice = pre.fund_eoa(
        amount=gas_used * (base_fee_per_gas + tip_rate) + value
    )
    coinbase = pre.fund_eoa(amount=0)

    final_balance = tip + withdrawal_amount_gwei * GWEI
    post_execution_index = 2

    block = Block(
        txs=[
            Transaction(
                sender=alice,
                to=bob,
                value=value,
                gas_limit=gas_used,
                gas_price=base_fee_per_gas + tip_rate,
            )
        ],
        fee_recipient=coinbase,
        withdrawals=[
            Withdrawal(
                index=0,
                validator_index=0,
                address=coinbase,
                amount=withdrawal_amount_gwei,
            )
        ],
        header_verify=Header(base_fee_per_gas=base_fee_per_gas),
        expected_block_access_list=BlockAccessListExpectation(
            account_expectations={
                coinbase: BalAccountExpectation(
                    balance_changes=[
                        BalBalanceChange(
                            block_access_index=post_execution_index,
                            post_balance=final_balance,
                        )
                    ],
                ),
            }
        ),
    )

    blockchain_test(
        pre=pre,
        blocks=[block],
        post={
            coinbase: Account(balance=final_balance),
            bob: Account(balance=1 + value),
        },
        genesis_environment=genesis_env,
    )
