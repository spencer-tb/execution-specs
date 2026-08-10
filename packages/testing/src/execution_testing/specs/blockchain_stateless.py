"""
Stateless helpers for blockchain test generation.

Fork-agnostic orchestration of stateless validation during filling:
option derivation, witness expectation application, and the artifact
pipeline between block-generation phases. Operations only the spec can
perform -- running the guest, rebuilding its input, decoding or
verifying its payloads -- dispatch through the filler backend's
stateless operations, which resolve the active fork on the spec side.
"""

from dataclasses import dataclass, replace
from typing import Callable, List, Protocol, Tuple

from execution_testing.base_types import (
    Bytes,
    Hash,
)
from execution_testing.client_clis import (
    ExecutionSpecsTransitionTool,
    FillerBackend,
    LazyAlloc,
    Result,
)
from execution_testing.fixtures.blockchain import FixtureHeader
from execution_testing.forks import Fork
from execution_testing.test_types import (
    Alloc,
    Environment,
    ExecutionWitness,
)
from execution_testing.test_types.block_access_list import BlockAccessList
from execution_testing.test_types.execution_witness import (
    ExecutionWitnessCodesExpectation,
    ExecutionWitnessHeadersExpectation,
    ExecutionWitnessStateExpectation,
    StatelessValidationError,
)
from execution_testing.test_types.execution_witness.modifiers import (
    PublicKeyModifier,
)

from .base import OpMode


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


def require_stateless_artifacts_or_trusted_fill(
    *,
    options: StatelessBlockOptions,
    result: Result,
    execution_witness: ExecutionWitness | None,
    block_access_list: BlockAccessList | None,
    t8n: FillerBackend,
    operation_mode: OpMode | None,
    block_exception: object | None,
) -> None:
    """
    Require t8n stateless bytes, or a fill trusted without them.

    The EELS t8n always emits both stateless byte fields beside a
    witness. External benchmark fills are the temporary trust path:
    they may produce a witness without serialized guest payloads, and
    are only trusted for valid blocks.
    """
    missing_stateless_artifacts = (
        not options.skip_validation
        and execution_witness is not None
        and block_access_list is not None
        and (
            result.stateless_input_bytes is None
            or result.stateless_output_bytes is None
        )
    )
    if not missing_stateless_artifacts:
        return
    if isinstance(t8n, ExecutionSpecsTransitionTool):
        raise StatelessValidationError(
            "EELS must provide stateless input and output bytes"
        )
    if operation_mode != OpMode.BENCHMARKING:
        raise StatelessValidationError(
            "Missing stateless artifacts are only supported for external "
            "benchmark fills"
        )
    if block_exception is not None:
        raise StatelessValidationError(
            "Missing stateless artifacts require a valid benchmark block"
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


def finalize_stateless_artifacts(
    *,
    options: StatelessBlockOptions,
    artifacts: StatelessValidationArtifacts,
    block: StatelessBlockProtocol,
    fork: Fork,
    block_number: int,
    timestamp: int,
    t8n: FillerBackend,
    chain_id: int,
) -> StatelessValidationArtifacts:
    """Verify, mutate, and rerun stateless guest artifacts as needed."""
    stateless_input_bytes = artifacts.stateless_input_bytes
    stateless_output_bytes = artifacts.stateless_output_bytes

    has_witness_modifier = artifacts.execution_witness_mutated
    for modifier_active, modifier_name in (
        (has_witness_modifier, "execution witness"),
        (options.has_public_keys_modifier, "stateless input public-key"),
        (
            options.has_stateless_input_bytes_modifier,
            "stateless input byte",
        ),
    ):
        if modifier_active and options.expected_validation_success is None:
            raise AssertionError(
                f"Mutated {modifier_name} tests must set "
                "expected_stateless_validation_success explicitly"
            )

    public_keys: Tuple[Bytes, ...] | None = None
    if stateless_input_bytes is not None:
        # The block could be invalid because of invalid txs, thus
        # the public keys might not be properly constructed given they
        # can't be decoded and thus provided in the execution witness.
        if block.exception is None:
            t8n.stateless_verify_input_public_keys(
                fork=fork,
                block_number=block_number,
                timestamp=timestamp,
                input_bytes=stateless_input_bytes,
                chain_id=chain_id,
            )
        if options.has_public_keys_modifier:
            public_keys = t8n.stateless_input_public_keys(
                fork=fork,
                block_number=block_number,
                timestamp=timestamp,
                input_bytes=stateless_input_bytes,
            )
    elif options.has_public_keys_modifier:
        raise StatelessValidationError(
            "Stateless input public-key mutation requires stateless "
            "input bytes"
        )

    final_successful_validation: bool | None = None
    if (
        has_witness_modifier
        or options.has_public_keys_modifier
        or options.expected_validation_success is not None
    ):
        if stateless_output_bytes is None:
            raise StatelessValidationError(
                "Stateless guest verification requires stateless output bytes"
            )
        final_successful_validation = t8n.stateless_validation_result(
            fork=fork,
            block_number=block_number,
            timestamp=timestamp,
            output_bytes=stateless_output_bytes,
        )

    has_structured_stateless_overrides = (
        has_witness_modifier or options.has_public_keys_modifier
    )
    if has_structured_stateless_overrides:
        if stateless_input_bytes is None:
            raise StatelessValidationError(
                "Stateless guest rerun requires stateless input bytes"
            )
        if has_witness_modifier and artifacts.execution_witness is None:
            raise StatelessValidationError(
                "Stateless guest witness mutation rerun requires "
                "execution witness"
            )
        modified_public_keys: Tuple[Bytes, ...] | None = None
        if options.public_keys_modifier is not None:
            if public_keys is None:
                raise StatelessValidationError(
                    "Stateless guest rerun requires public keys"
                )
            modified_public_keys = options.public_keys_modifier(public_keys)
        stateless_input_bytes = t8n.stateless_rebuild_input(
            fork=fork,
            block_number=block_number,
            timestamp=timestamp,
            input_bytes=stateless_input_bytes,
            execution_witness=(
                artifacts.execution_witness if has_witness_modifier else None
            ),
            public_keys=modified_public_keys,
        )

    should_rerun_stateless_guest = (
        has_structured_stateless_overrides
        or options.has_stateless_input_bytes_modifier
    )
    if options.has_stateless_input_bytes_modifier:
        if stateless_input_bytes is None:
            raise StatelessValidationError(
                "Stateless guest raw input rerun requires stateless "
                "input bytes"
            )
        stateless_input_bytes_modifier = options.stateless_input_bytes_modifier
        if stateless_input_bytes_modifier is None:
            raise StatelessValidationError(
                "Stateless input bytes modifier is required"
            )
        stateless_input_bytes = stateless_input_bytes_modifier(
            stateless_input_bytes
        )

    if should_rerun_stateless_guest:
        if stateless_input_bytes is None:
            raise StatelessValidationError(
                "Stateless guest rerun requires stateless input bytes"
            )
        (
            stateless_input_bytes,
            stateless_output_bytes,
            final_successful_validation,
        ) = t8n.stateless_run_guest(
            fork=fork,
            block_number=block_number,
            timestamp=timestamp,
            input_bytes=stateless_input_bytes,
        )

    if (
        options.expected_validation_success is not None
        and final_successful_validation != options.expected_validation_success
    ):
        raise AssertionError(
            "Stateless guest validation result mismatch: "
            f"got {final_successful_validation}, "
            f"want {options.expected_validation_success}"
        )

    if stateless_output_bytes is not None:
        if stateless_input_bytes is None:
            raise StatelessValidationError(
                "Stateless output verification requires stateless input bytes"
            )
        t8n.stateless_verify_output(
            fork=fork,
            block_number=block_number,
            timestamp=timestamp,
            chain_id=chain_id,
            input_bytes=stateless_input_bytes,
            output_bytes=stateless_output_bytes,
            input_bytes_modified=options.has_stateless_input_bytes_modifier,
        )

    return replace(
        artifacts,
        stateless_input_bytes=stateless_input_bytes,
        stateless_output_bytes=stateless_output_bytes,
    )


def build_stateless_artifacts(
    *,
    options: StatelessBlockOptions,
    block: StatelessBlockProtocol,
    fork: Fork,
    previous_alloc: Alloc | LazyAlloc,
    env: Environment,
    header: FixtureHeader,
    result: Result,
    block_access_list: BlockAccessList | None,
    t8n: FillerBackend,
    operation_mode: OpMode | None,
    chain_id: int,
) -> StatelessValidationArtifacts:
    """
    Run the post-t8n stateless pipeline for one block.

    Apply witness expectations, gate the trust path for fills whose
    transition tool emits no stateless bytes, collect the serialized
    artifacts, and verify them -- rerunning the guest through the
    backend for mutation tests.
    """
    block_number = int(env.number)
    timestamp = int(env.timestamp)
    execution_witness = result.execution_witness
    artifacts = apply_execution_witness_expectations(
        block=block,
        fork=fork,
        previous_alloc=previous_alloc,
        block_number=block_number,
        timestamp=timestamp,
        parent_hash=header.parent_hash,
        execution_witness=execution_witness,
    )
    require_stateless_artifacts_or_trusted_fill(
        options=options,
        result=result,
        execution_witness=execution_witness,
        block_access_list=block_access_list,
        t8n=t8n,
        operation_mode=operation_mode,
        block_exception=block.exception,
    )
    artifacts = replace(
        artifacts,
        stateless_input_bytes=result.stateless_input_bytes,
        stateless_output_bytes=result.stateless_output_bytes,
    )
    return finalize_stateless_artifacts(
        options=options,
        artifacts=artifacts,
        block=block,
        fork=fork,
        block_number=block_number,
        timestamp=timestamp,
        t8n=t8n,
        chain_id=chain_id,
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
