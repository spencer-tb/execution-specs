"""
A zero `data_hash` stands for the declaring transaction's signature hash
(EIP-8288 at ethereum/EIPs@72ca2dd791). The block commits to the
substituted claim, so a digest over the literal zero bytes is rejected.

The rejection cases stop before a proof would verify, so they need no
stored proof. The valid case needs a proof over the transaction's
signature hash, generated with `export_eip8288_test_proofs`.
"""

from typing import Tuple

import pytest
from execution_testing import (
    Alloc,
    Block,
    BlockchainTestFiller,
    BlockException,
    Fork,
    Header,
    Op,
    RecursiveStark,
    Transaction,
)

from tests.bogota.eip8141_frame_transactions.helpers import (
    sender_frame,
    verify_frame,
)

from .helpers import (
    Dependency,
    claim,
    dependencies_hash,
    dependency_frame,
    expected_recursive_stark,
)
from .spec import Spec, ref_spec_8288

REFERENCE_SPEC_GIT_PATH = ref_spec_8288.git_path
REFERENCE_SPEC_VERSION = ref_spec_8288.version

pytestmark = pytest.mark.valid_from("EIP8288")


def zero_data_hash_transaction(
    pre: Alloc, fork: Fork
) -> Tuple[Transaction, Dependency, Dependency]:
    """
    Return a frame transaction declaring one claim with a zero
    `data_hash`, with that literal claim and its substituted form.
    """
    _, _, key = claim(0)
    literal = (Spec.LEANSPHINCS_SCHEME, bytes(32), key)
    tx = Transaction(
        sender=pre.fund_eoa(),
        frames=[
            dependency_frame(fork, [literal]),
            verify_frame(),
            sender_frame(target=pre.deploy_contract(code=Op.STOP)),
        ],
    )
    signed = tx.model_copy(deep=True)
    signed.sign()
    sig_hash = bytes(signed.rlp_signing_bytes().keccak256())
    return tx, literal, (Spec.LEANSPHINCS_SCHEME, sig_hash, key)


def test_zero_data_hash_valid(
    blockchain_test: BlockchainTestFiller, pre: Alloc, fork: Fork
) -> None:
    """Accept a block committing to the substituted claim with its proof."""
    tx, _, substituted = zero_data_hash_transaction(pre, fork)
    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                txs=[tx],
                header_verify=Header(
                    recursive_stark=expected_recursive_stark([substituted])
                ),
            )
        ],
        post={},
    )


@pytest.mark.exception_test
@pytest.mark.parametrize(
    "substituted,exception",
    [
        pytest.param(
            False,
            BlockException.INVALID_BLOCK_DEPS_HASH,
            id="digest_over_literal_zero",
        ),
        pytest.param(
            True,
            BlockException.INVALID_RECURSIVE_STARK,
            id="digest_over_sig_hash_without_proof",
        ),
    ],
)
def test_zero_data_hash_commitment(
    blockchain_test: BlockchainTestFiller,
    pre: Alloc,
    fork: Fork,
    substituted: bool,
    exception: BlockException,
) -> None:
    """
    Commit the header to the signature hash in place of a zero
    `data_hash`: the literal digest fails the digest check, the
    substituted one passes it and fails only on the missing proof.
    """
    tx, literal, sig_hash_claim = zero_data_hash_transaction(pre, fork)
    committed = sig_hash_claim if substituted else literal
    blockchain_test(
        pre=pre,
        blocks=[
            Block(
                txs=[tx],
                rlp_modifier=Header(
                    recursive_stark=RecursiveStark(
                        block_deps_hash=dependencies_hash([committed])
                    )
                ),
                exception=exception,
            )
        ],
        post={},
    )
