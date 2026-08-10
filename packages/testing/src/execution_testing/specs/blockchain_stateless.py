"""
Stateless helpers for blockchain test generation.

Fork-agnostic orchestration of stateless validation during filling:
option derivation, witness expectation application, and the artifact
pipeline between block-generation phases. Everything that reaches
into the EELS stateless modules lives in the fork-specific
`blockchain_stateless_amsterdam` bridge module.
"""

from dataclasses import dataclass, replace
from typing import Callable, List, Protocol, Tuple

from execution_testing.base_types import (
    Bytes,
    Hash,
)
from execution_testing.client_clis import LazyAlloc, Result
from execution_testing.fixtures.blockchain import FixtureHeader
from execution_testing.forks import Fork
from execution_testing.test_types import (
    Alloc,
    Environment,
    ExecutionWitness,
    Transaction,
    Withdrawal,
)
from execution_testing.test_types.block_access_list import BlockAccessList
from execution_testing.test_types.execution_witness import (
    ExecutionWitnessCodesExpectation,
    ExecutionWitnessHeadersExpectation,
    ExecutionWitnessStateExpectation,
)
from execution_testing.test_types.execution_witness.modifiers import (
    PublicKeyModifier,
)

from .blockchain_stateless_amsterdam import (
    build_amsterdam_stateless_artifacts_from_t8n,
    decode_amsterdam_stateless_output,
    get_amsterdam_stateless_input_public_key_data,
    rebuild_amsterdam_stateless_input_with_overrides,
    rerun_amsterdam_stateless_guest_with_input_bytes,
    verify_amsterdam_stateless_output,
    verify_stateless_input_public_keys,
)


class StatelessBlockProtocol(Protocol):
    """Block fields needed by stateless validation orchestration."""

    @property
    def rlp_modifier(self) -> object | None:
        """RLP modifier configured for the block."""
        ...

    @property
    def expected_execution_witness_codes(
        self,
    ) -> ExecutionWitnessCodesExpectation | None:
        """Expected execution witness codes."""
        ...

    @property
    def expected_execution_witness_state(
        self,
    ) -> ExecutionWitnessStateExpectation | None:
        """Expected execution witness state."""
        ...

    @property
    def expected_execution_witness_headers(
        self,
    ) -> ExecutionWitnessHeadersExpectation | None:
        """Expected execution witness headers."""
        ...

    @property
    def stateless_input_public_keys_modifier(
        self,
    ) -> PublicKeyModifier | None:
        """Public-key modifier for stateless input reruns."""
        ...

    @property
    def stateless_input_bytes_modifier(
        self,
    ) -> Callable[[Bytes], Bytes] | None:
        """Serialized stateless input modifier for raw-input reruns."""
        ...

    @property
    def expected_stateless_validation_success(self) -> bool | None:
        """Expected stateless guest validation result."""
        ...

    @property
    def exception(self) -> object | None:
        """Block exception expectation."""
        ...


@dataclass(frozen=True)
class StatelessBlockOptions:
    """Stateless options derived before transition-tool execution."""

    skip_validation: bool
    public_keys_modifier: PublicKeyModifier | None
    stateless_input_bytes_modifier: Callable[[Bytes], Bytes] | None
    expected_validation_success: bool | None

    @property
    def has_public_keys_modifier(self) -> bool:
        """Whether stateless input public keys should be mutated."""
        return self.public_keys_modifier is not None

    @property
    def has_stateless_input_bytes_modifier(self) -> bool:
        """Whether raw stateless input bytes should be mutated."""
        return self.stateless_input_bytes_modifier is not None


@dataclass(frozen=True)
class StatelessValidationArtifacts:
    """Stateless artifacts passed between blockchain generation phases."""

    execution_witness: ExecutionWitness | None
    execution_witness_mutated: bool
    stateless_input_bytes: Bytes | None = None
    stateless_output_bytes: Bytes | None = None


def stateless_options_for_block(
    *,
    block: StatelessBlockProtocol,
    skip_stateless_validation: bool,
) -> StatelessBlockOptions:
    """Derive stateless options and reject incompatible block settings."""
    has_witness_expectation = (
        block.expected_execution_witness_state is not None
        or block.expected_execution_witness_codes is not None
        or block.expected_execution_witness_headers is not None
    )
    public_keys_modifier = block.stateless_input_public_keys_modifier
    has_public_keys_modifier = public_keys_modifier is not None
    stateless_input_bytes_modifier = block.stateless_input_bytes_modifier
    has_stateless_input_bytes_modifier = (
        stateless_input_bytes_modifier is not None
    )
    expected_success = block.expected_stateless_validation_success
    omit_stateless_artifacts = block.rlp_modifier is not None

    if omit_stateless_artifacts and (
        has_witness_expectation
        or has_public_keys_modifier
        or has_stateless_input_bytes_modifier
        or expected_success is not None
    ):
        raise AssertionError(
            "Blocks with rlp_modifier omit stateless artifacts because "
            "they are generated before the RLP mutation. SSZ/stateless "
            "mutation tests require a separate explicit mechanism."
        )
    if skip_stateless_validation and (
        has_witness_expectation
        or has_public_keys_modifier
        or has_stateless_input_bytes_modifier
        or expected_success is not None
    ):
        raise AssertionError(
            "skip_stateless_validation cannot be combined with "
            "execution witness expectations, stateless input public-key "
            "modifiers, stateless input byte modifiers, or "
            "expected_stateless_validation_success"
        )

    return StatelessBlockOptions(
        skip_validation=skip_stateless_validation or omit_stateless_artifacts,
        public_keys_modifier=public_keys_modifier,
        stateless_input_bytes_modifier=stateless_input_bytes_modifier,
        expected_validation_success=expected_success,
    )


def apply_execution_witness_expectations(
    *,
    block: StatelessBlockProtocol,
    fork: Fork,
    previous_alloc: Alloc | LazyAlloc,
    block_number: int,
    timestamp: int,
    parent_hash: Hash,
    execution_witness: ExecutionWitness | None,
) -> StatelessValidationArtifacts:
    """Verify and apply execution witness expectations for a block."""
    adjusted_witness = execution_witness
    state_expectation = block.expected_execution_witness_state
    if state_expectation is not None and adjusted_witness is not None:
        state_expectation.verify_against(adjusted_witness)
        adjusted_witness = state_expectation.modify_if_invalid_test(
            adjusted_witness
        )

    codes_expectation = block.expected_execution_witness_codes
    if codes_expectation is not None and adjusted_witness is not None:
        effective_codes_expectation = with_execution_witness_implicit_codes(
            expectation=codes_expectation,
            fork=fork,
            alloc=previous_alloc,
            block_number=block_number,
            timestamp=timestamp,
        )
        effective_codes_expectation.verify_against(adjusted_witness)
        adjusted_witness = codes_expectation.modify_if_invalid_test(
            adjusted_witness
        )

    headers_expectation = block.expected_execution_witness_headers
    if headers_expectation is not None and adjusted_witness is not None:
        headers_expectation.verify_against(
            adjusted_witness,
            parent_hash=parent_hash,
            fork=fork,
        )
        adjusted_witness = headers_expectation.modify_if_invalid_test(
            adjusted_witness
        )

    return StatelessValidationArtifacts(
        execution_witness=adjusted_witness,
        execution_witness_mutated=_has_execution_witness_modifier(block),
    )


def stateless_artifacts_from_t8n(
    *,
    options: StatelessBlockOptions,
    artifacts: StatelessValidationArtifacts,
    fork: Fork,
    block_number: int,
    timestamp: int,
    header: FixtureHeader,
    previous_env: Environment,
    txs: List[Transaction],
    result: Result,
    withdrawals: List[Withdrawal] | None,
    requests_list: List[Bytes] | None,
    execution_witness: ExecutionWitness | None,
    block_access_list: BlockAccessList | None,
    chain_id: int,
) -> StatelessValidationArtifacts:
    """Collect or derive serialized stateless artifacts from t8n output."""
    stateless_input_bytes = result.stateless_input_bytes
    stateless_output_bytes = result.stateless_output_bytes
    if (
        not options.skip_validation
        and execution_witness is not None
        and block_access_list is not None
        and (stateless_input_bytes is None or stateless_output_bytes is None)
    ):
        built_artifacts = build_amsterdam_stateless_artifacts_from_t8n(
            fork=fork,
            block_number=block_number,
            timestamp=timestamp,
            header=header,
            previous_env=previous_env,
            txs=txs,
            result=result,
            withdrawals=withdrawals,
            requests_list=requests_list,
            execution_witness=execution_witness,
            block_access_list=block_access_list,
            chain_id=chain_id,
        )
        if built_artifacts is not None:
            stateless_input_bytes, stateless_output_bytes = built_artifacts

    return replace(
        artifacts,
        stateless_input_bytes=stateless_input_bytes,
        stateless_output_bytes=stateless_output_bytes,
    )


def finalize_stateless_artifacts(
    *,
    options: StatelessBlockOptions,
    artifacts: StatelessValidationArtifacts,
    block: StatelessBlockProtocol,
    fork: Fork,
    block_number: int,
    timestamp: int,
    chain_id: int,
) -> StatelessValidationArtifacts:
    """Verify, mutate, and rerun stateless guest artifacts as needed."""
    stateless_input_bytes = artifacts.stateless_input_bytes
    stateless_output_bytes = artifacts.stateless_output_bytes
    stateless_output = decode_amsterdam_stateless_output(
        fork=fork,
        block_number=block_number,
        timestamp=timestamp,
        stateless_output_bytes=stateless_output_bytes,
    )

    has_witness_modifier = artifacts.execution_witness_mutated
    if has_witness_modifier and options.expected_validation_success is None:
        raise AssertionError(
            "Mutated execution witness tests must set "
            "expected_stateless_validation_success explicitly"
        )
    if (
        options.has_public_keys_modifier
        and options.expected_validation_success is None
    ):
        raise AssertionError(
            "Mutated stateless input public-key tests must set "
            "expected_stateless_validation_success explicitly"
        )
    if (
        options.has_stateless_input_bytes_modifier
        and options.expected_validation_success is None
    ):
        raise AssertionError(
            "Mutated stateless input byte tests must set "
            "expected_stateless_validation_success explicitly"
        )

    public_keys: Tuple[Bytes, ...] | None = None
    should_verify_stateless_input_public_keys = (
        stateless_input_bytes is not None
        # The block could be invalid because of invalid txs, thus
        # the public keys might not be properly constructed given they
        # can't be decoded and thus provided in the execution witness.
        and block.exception is None
    )
    if stateless_input_bytes is not None and (
        should_verify_stateless_input_public_keys
        or options.has_public_keys_modifier
    ):
        payload_transactions: Tuple[Bytes, ...]
        public_keys, payload_transactions = (
            get_amsterdam_stateless_input_public_key_data(
                fork=fork,
                block_number=block_number,
                timestamp=timestamp,
                stateless_input_bytes=stateless_input_bytes,
            )
        )
        if should_verify_stateless_input_public_keys:
            verify_stateless_input_public_keys(
                public_keys,
                payload_transactions,
                chain_id,
            )
    elif options.has_public_keys_modifier:
        raise Exception(
            "Stateless input public-key mutation requires stateless "
            "input bytes"
        )

    canonical_successful_validation: bool | None = None
    if (
        has_witness_modifier
        or options.has_public_keys_modifier
        or options.expected_validation_success is not None
    ):
        if stateless_output_bytes is None:
            raise Exception(
                "Stateless guest verification requires stateless output bytes"
            )
        if stateless_output is None:
            raise Exception(
                "Stateless output decoding is only supported for Amsterdam"
            )
        canonical_successful_validation = (
            stateless_output.successful_validation
        )

    has_structured_stateless_overrides = (
        has_witness_modifier or options.has_public_keys_modifier
    )
    final_successful_validation = canonical_successful_validation
    if has_structured_stateless_overrides:
        if stateless_input_bytes is None:
            raise Exception(
                "Stateless guest rerun requires stateless input bytes"
            )
        if has_witness_modifier and artifacts.execution_witness is None:
            raise Exception(
                "Stateless guest witness mutation rerun requires "
                "execution witness"
            )
        modified_public_keys: Tuple[Bytes, ...] | None = None
        if options.public_keys_modifier is not None:
            if public_keys is None:
                raise Exception("Stateless guest rerun requires public keys")
            modified_public_keys = options.public_keys_modifier(public_keys)
        stateless_input_bytes = (
            rebuild_amsterdam_stateless_input_with_overrides(
                fork=fork,
                block_number=block_number,
                timestamp=timestamp,
                original_stateless_input_bytes=stateless_input_bytes,
                execution_witness=(
                    artifacts.execution_witness
                    if has_witness_modifier
                    else None
                ),
                public_keys=modified_public_keys,
            )
        )

    should_rerun_stateless_guest = (
        has_structured_stateless_overrides
        or options.has_stateless_input_bytes_modifier
    )
    if options.has_stateless_input_bytes_modifier:
        if stateless_input_bytes is None:
            raise Exception(
                "Stateless guest raw input rerun requires stateless "
                "input bytes"
            )
        stateless_input_bytes_modifier = options.stateless_input_bytes_modifier
        if stateless_input_bytes_modifier is None:
            raise Exception("Stateless input bytes modifier is required")
        stateless_input_bytes = stateless_input_bytes_modifier(
            stateless_input_bytes
        )

    if should_rerun_stateless_guest:
        if stateless_input_bytes is None:
            raise Exception(
                "Stateless guest rerun requires stateless input bytes"
            )
        (
            stateless_input_bytes,
            stateless_output_bytes,
            successful_validation,
        ) = rerun_amsterdam_stateless_guest_with_input_bytes(
            fork=fork,
            block_number=block_number,
            timestamp=timestamp,
            stateless_input_bytes=stateless_input_bytes,
        )
        stateless_output = decode_amsterdam_stateless_output(
            fork=fork,
            block_number=block_number,
            timestamp=timestamp,
            stateless_output_bytes=stateless_output_bytes,
        )
        final_successful_validation = successful_validation

    if (
        options.expected_validation_success is not None
        and final_successful_validation != options.expected_validation_success
    ):
        raise AssertionError(
            "Stateless guest validation result mismatch: "
            f"got {final_successful_validation}, "
            f"want {options.expected_validation_success}"
        )

    if stateless_output is not None:
        if stateless_input_bytes is None:
            raise Exception(
                "Stateless output verification requires stateless input bytes"
            )
        verify_amsterdam_stateless_output(
            block_number=block_number,
            chain_id=chain_id,
            stateless_input_bytes=stateless_input_bytes,
            stateless_output=stateless_output,
            input_bytes_modified=options.has_stateless_input_bytes_modifier,
        )

    return replace(
        artifacts,
        stateless_input_bytes=stateless_input_bytes,
        stateless_output_bytes=stateless_output_bytes,
    )


def execution_witness_implicit_codes_for_block(
    *,
    fork: Fork,
    alloc: Alloc | LazyAlloc,
    block_number: int,
    timestamp: int,
) -> List[Bytes]:
    """
    Return ambient witness bytecodes implied by block-level execution.

    These codes are resolved from the effective pre-state for the block, not
    from raw fork defaults, so test `pre` overrides are respected.
    """
    active_fork = fork.fork_at(block_number=block_number, timestamp=timestamp)
    addresses = active_fork.execution_witness_implicit_code_addresses(
        block_number=block_number,
        timestamp=timestamp,
    )
    if not addresses:
        return []

    effective_alloc = (
        alloc.materialize() if isinstance(alloc, LazyAlloc) else alloc
    )

    codes: List[Bytes] = []
    seen: set[Bytes] = set()
    for address in addresses:
        if address not in effective_alloc:
            continue
        account = effective_alloc[address]
        if account is None or len(account.code) == 0:
            continue
        code = Bytes(account.code)
        if code in seen:
            continue
        codes.append(code)
        seen.add(code)
    return codes


def with_execution_witness_implicit_codes(
    *,
    expectation: ExecutionWitnessCodesExpectation,
    fork: Fork,
    alloc: Alloc | LazyAlloc,
    block_number: int,
    timestamp: int,
) -> ExecutionWitnessCodesExpectation:
    """Return expectation copy with ambient block-level codes added."""
    codes_present = list(expectation.codes_present)
    seen = set(codes_present)

    for code in execution_witness_implicit_codes_for_block(
        fork=fork,
        alloc=alloc,
        block_number=block_number,
        timestamp=timestamp,
    ):
        if code in seen:
            continue
        codes_present.append(code)
        seen.add(code)

    return expectation.model_copy(update={"codes_present": codes_present})


def _has_execution_witness_modifier(
    block: StatelessBlockProtocol,
) -> bool:
    """Return whether any execution witness expectation mutates the witness."""
    return (
        (
            block.expected_execution_witness_state is not None
            and block.expected_execution_witness_state._modifier is not None
        )
        or (
            block.expected_execution_witness_codes is not None
            and block.expected_execution_witness_codes._modifier is not None
        )
        or (
            block.expected_execution_witness_headers is not None
            and block.expected_execution_witness_headers._modifier is not None
        )
    )
