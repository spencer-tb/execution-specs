"""
A hive based simulator that executes blocks against clients using the
`engine_newPayloadVX` method from the Engine API.

The unified test function in this module supports both:
- `BlockchainEngineFixtures`, the original engine mode with a
  1-to-1 relationship between client instance and test, i.e.,
  each test is executed against a fresh client instance.
- `BlockchainEngineXFixtures`, enginex mode with client reuse
  across tests with shared pre-alloc groups.

Each `engine_newPayloadVX` is verified against the appropriate VALID/INVALID
responses.
"""

from typing import Union

import pytest
from hive.client import Client

from execution_testing.fixtures import (
    BlockchainEngineFixture,
    BlockchainEngineXFixture,
)
from execution_testing.fixtures.blockchain import (
    FixtureEngineNewPayload,
    FixtureHeader,
)
from execution_testing.logging import get_logger
from execution_testing.rpc import (
    EngineRPC,
    EngineSszRPC,
    EngineWitnessEndpointNotImplementedError,
    EthRPC,
    ForkchoiceUpdateTimeoutError,
)
from execution_testing.rpc.rpc_types import (
    ForkchoiceState,
    JSONRPCError,
    NewPayloadWithWitnessResponse,
    PayloadStatusEnum,
)

from ..helpers.exceptions import (
    GenesisBlockMismatchExceptionError,
    LoggedError,
)
from ..helpers.rejected_blocks import (
    BlockRejectionTracker,
    verify_block_rejection,
)
from ..helpers.timing import TimingData
from ..helpers.witness_diff import (
    WitnessMismatchError,
    assert_witness_matches,
)

logger = get_logger(__name__)

_JSONRPC_METHOD_NOT_FOUND = -32601


def skip_unsuitable_stateless_fixture(
    fixture: Union[BlockchainEngineFixture, BlockchainEngineXFixture],
) -> None:
    """Skip fixtures the stateless engine mode cannot consume."""
    if any(p.execution_witness_mutated for p in fixture.payloads):
        pytest.skip("fixture contains a deliberately mutated executionWitness")
    if not any(p.execution_witness is not None for p in fixture.payloads):
        pytest.skip("fixture has no executionWitness on any payload")


def _witness_endpoint_label(
    payload: FixtureEngineNewPayload,
    *,
    use_ssz_transport: bool,
) -> str:
    """Return the timing label for the selected witness endpoint."""
    if use_ssz_transport:
        return "POST /new-payload-with-witness"
    return f"engine_newPayloadWithWitnessV{payload.new_payload_version}"


def _send_payload_with_witness(
    *,
    use_ssz_transport: bool,
    engine_rpc: EngineRPC,
    engine_ssz_rpc: EngineSszRPC,
    payload: FixtureEngineNewPayload,
) -> NewPayloadWithWitnessResponse | JSONRPCError:
    """
    Execute one payload through the configured witness endpoint.

    Return the response, or the caught Engine API error for the assertion to
    validate against the fixture's expected ``error_code``.
    """
    try:
        if use_ssz_transport:
            return engine_ssz_rpc.new_payload_with_witness(*payload.params)
        return engine_rpc.new_payload_with_witness(
            *payload.params,
            version=payload.new_payload_version,
        )
    except EngineWitnessEndpointNotImplementedError as e:
        pytest.skip(str(e))
    except JSONRPCError as e:
        # An unimplemented endpoint is a transport skip, but only when no
        # error was expected; otherwise the error is a result to assert.
        if payload.error_code is None and e.code == _JSONRPC_METHOD_NOT_FOUND:
            pytest.skip(
                "client does not support "
                f"engine_newPayloadWithWitnessV"
                f"{payload.new_payload_version}: {e.message}"
            )
        return e


def _assert_witness_response(
    *,
    payload: FixtureEngineNewPayload,
    payload_number: int,
    result: NewPayloadWithWitnessResponse | JSONRPCError,
    payload_timing: TimingData,
    use_ssz_transport: bool,
) -> None:
    """Assert one witness result (response or error) matches the fixture."""
    if isinstance(result, JSONRPCError):
        # The client raised an Engine API error; a negative test expects it.
        if payload.error_code is None:
            raise LoggedError(
                f"Payload {payload_number}: unexpected error: "
                f"{result.code} - {result.message}"
            )
        if result.code != payload.error_code:
            raise LoggedError(
                f"Payload {payload_number}: unexpected error code: "
                f"got {result.code}, expected {payload.error_code}"
            )
        return

    if payload.error_code is not None:
        # Negative test expected an Engine API error, but got a response.
        raise LoggedError(
            f"Payload {payload_number}: client did not raise the expected "
            f"Engine API error code {payload.error_code}"
        )

    response = result
    expected_status = (
        PayloadStatusEnum.VALID
        if payload.valid()
        else PayloadStatusEnum.INVALID
    )
    if response.status != expected_status:
        raise LoggedError(
            f"unexpected status: want {expected_status}, got {response.status}"
        )

    if response.status != PayloadStatusEnum.VALID:
        if use_ssz_transport and response.witness is not None:
            raise LoggedError(
                f"Payload {payload_number}: {response.status} status but "
                "client returned a non-empty witness; the REST+SSZ endpoint "
                "requires an empty witness when not VALID"
            )
        return

    expected_witness = payload.execution_witness
    if expected_witness is None:
        logger.warning(
            f"Payload {payload_number}: fixture has no executionWitness; "
            "skipping witness diff"
        )
        return

    actual_witness = response.witness
    if actual_witness is None:
        raise LoggedError(
            f"Payload {payload_number}: VALID status but client returned "
            "no witness"
        )

    with payload_timing.time("Witness diff"):
        try:
            assert_witness_matches(
                expected=expected_witness,
                actual=actual_witness,
            )
        except WitnessMismatchError as e:
            raise LoggedError(str(e)) from e


def test_blockchain_via_engine(
    timing_data: TimingData,
    eth_rpc: EthRPC,
    engine_rpc: EngineRPC,
    engine_ssz_rpc: EngineSszRPC,
    client: Client,
    genesis_verified_clients: set[str],
    block_rejection_tracker: BlockRejectionTracker,
    fixture: Union[BlockchainEngineFixture, BlockchainEngineXFixture],
    strict_exception_matching: bool,
    genesis_header: FixtureHeader,
    stateless: bool,
    use_ssz_transport: bool,
) -> None:
    """
    Execute blockchain test fixtures against a client using the Engine API.

    This function supports both engine mode (`BlockchainEngineFixture`)
    with per-test clients and enginex mode (`BlockchainEngineXFixture`)
    with client reuse across tests sharing a pre-alloc group.

    With `--stateless`, payloads execute through the witness-emitting
    `engine_newPayloadWithWitnessVX` endpoint instead (or the REST+SSZ
    transport with `--ssz`), and the client-generated execution witness
    is verified against the fixture witness.

    Both modes follow the same test sequence for equivalence:

    1. Send initial FCU to genesis to establish the chain head.
    2. Verify the client genesis block hash matches genesis_header. Genesis
       is immutable per client, so in shared-client (enginex) mode this is
       done once per client and skipped for later tests in the group.
    3. Execute test fixture blocks using engine_newPayloadVX.
    4. For valid payloads, send FCU to advance the chain head.

    A client's bad-block cache persists across the tests of a pre-alloc
    group in enginex mode: a block that an earlier test already got
    rejected may be rejected again with a generic cache error (e.g. reth's
    "links to previously rejected block") instead of being re-validated.
    When the returned error does not match the expected exception, it is
    therefore verified against the error from the client's first rejection
    of the same block before failing the test.
    """
    if stateless:
        skip_unsuitable_stateless_fixture(fixture)
        transport_label = "REST+SSZ" if use_ssz_transport else "JSON-RPC+RLP"
        logger.info(f"Using {transport_label} witness transport")

    with timing_data.time("Initial forkchoice update"):
        logger.info("Sending initial forkchoice update to genesis block...")
        try:
            response = engine_rpc.forkchoice_updated_with_retry(
                forkchoice_state=ForkchoiceState(
                    head_block_hash=genesis_header.block_hash,
                ),
                forkchoice_version=fixture.payloads[
                    0
                ].forkchoice_updated_version,
                max_attempts=30,
                wait_fixed=1.0,
            )
            if response.payload_status.status != PayloadStatusEnum.VALID:
                raise LoggedError(
                    f"Unexpected status on forkchoice updated to genesis: "
                    f"{response.payload_status.status}"
                )
        except ForkchoiceUpdateTimeoutError as e:
            raise LoggedError(
                f"Timed out waiting for forkchoice update to genesis: {e}"
            ) from None

    if client.id not in genesis_verified_clients:
        with timing_data.time("Get genesis block"):
            logger.info("Calling getBlockByNumber to get genesis block...")
            genesis_block = eth_rpc.get_block_by_number(0)
            assert genesis_block is not None, "genesis_block is None"
            if genesis_block["hash"] != str(genesis_header.block_hash):
                expected = genesis_header.block_hash
                got = genesis_block["hash"]
                logger.fail(
                    f"Genesis block hash mismatch. "
                    f"Expected: {expected}, Got: {got}"
                )
                raise GenesisBlockMismatchExceptionError(
                    expected_header=genesis_header,
                    got_genesis_block=genesis_block,
                )
        # Genesis is immutable per client, so verify it once per client. In
        # shared-client (enginex) mode the same client serves every test in a
        # pre-alloc group, so later tests skip the redundant getBlockByNumber
        # round-trip; per-test clients get a fresh id each test and re-verify.
        genesis_verified_clients.add(client.id)

    with timing_data.time("Payloads execution") as total_payload_timing:
        logger.info(
            f"Starting execution of {len(fixture.payloads)} payloads..."
        )
        for i, payload in enumerate(fixture.payloads):
            logger.info(
                f"Processing payload {i + 1}/{len(fixture.payloads)}..."
            )
            witness_errored = False
            with total_payload_timing.time(
                f"Payload {i + 1}"
            ) as payload_timing:
                if stateless:
                    with payload_timing.time(
                        _witness_endpoint_label(
                            payload,
                            use_ssz_transport=use_ssz_transport,
                        )
                    ):
                        witness_result = _send_payload_with_witness(
                            use_ssz_transport=use_ssz_transport,
                            engine_rpc=engine_rpc,
                            engine_ssz_rpc=engine_ssz_rpc,
                            payload=payload,
                        )
                    _assert_witness_response(
                        payload=payload,
                        payload_number=i + 1,
                        result=witness_result,
                        payload_timing=payload_timing,
                        use_ssz_transport=use_ssz_transport,
                    )
                    # A raised error means the block was rejected, so there
                    # is no canonical block to advance the forkchoice to.
                    witness_errored = isinstance(witness_result, JSONRPCError)
                else:
                    with payload_timing.time(
                        f"engine_newPayloadV{payload.new_payload_version}"
                    ):
                        version = payload.new_payload_version
                        logger.info(f"Sending engine_newPayloadV{version}...")
                        try:
                            payload_response = engine_rpc.new_payload(
                                *payload.params,
                                version=payload.new_payload_version,
                            )
                            status = payload_response.status
                            logger.info(f"Payload response status: {status}")
                            expected_validity = (
                                PayloadStatusEnum.VALID
                                if payload.valid()
                                else PayloadStatusEnum.INVALID
                            )
                            if payload_response.status != expected_validity:
                                raise LoggedError(
                                    f"unexpected status: want "
                                    f"{expected_validity}, got "
                                    f"{payload_response.status}"
                                )
                            if payload.error_code is not None:
                                raise LoggedError(
                                    "Client failed to raise expected "
                                    "Engine API error code: "
                                    f"{payload.error_code}"
                                )
                            elif (
                                payload_response.status
                                == PayloadStatusEnum.INVALID
                            ):
                                if payload_response.validation_error is None:
                                    raise LoggedError(
                                        "Client returned INVALID but no "
                                        "validation error was provided."
                                    )
                                block_hash = payload.params[0].block_hash
                                first_rejection = (
                                    block_rejection_tracker.track(
                                        client.id,
                                        block_hash,
                                        payload_response.validation_error,
                                    )
                                )
                                verify_block_rejection(
                                    payload.validation_error,
                                    payload_response.validation_error,
                                    first_rejection,
                                    block_hash,
                                    strict_exception_matching,
                                )

                        except JSONRPCError as e:
                            logger.info(
                                f"JSONRPC error encountered: "
                                f"{e.code} - {e.message}"
                            )
                            if payload.error_code is None:
                                raise LoggedError(
                                    f"Unexpected error: {e.code} - {e.message}"
                                ) from e
                            if e.code != payload.error_code:
                                raise LoggedError(
                                    f"Unexpected error code: {e.code}, "
                                    f"expected: {payload.error_code}"
                                ) from e

                if payload.valid() and not witness_errored:
                    with payload_timing.time(
                        f"engine_forkchoiceUpdatedV{payload.forkchoice_updated_version}"
                    ):
                        # Send a forkchoice update to the engine
                        version = payload.forkchoice_updated_version
                        logger.info(
                            f"Sending engine_forkchoiceUpdatedV{version}..."
                        )
                        forkchoice_response = engine_rpc.forkchoice_updated(
                            forkchoice_state=ForkchoiceState(
                                head_block_hash=payload.params[0].block_hash,
                            ),
                            payload_attributes=None,
                            version=payload.forkchoice_updated_version,
                        )
                        status = forkchoice_response.payload_status.status
                        logger.info(f"Forkchoice update response: {status}")
                        if (
                            forkchoice_response.payload_status.status
                            != PayloadStatusEnum.VALID
                        ):
                            status = forkchoice_response.payload_status.status
                            raise LoggedError(
                                f"unexpected status: want "
                                f"{PayloadStatusEnum.VALID}, got {status}"
                            )
        logger.info("All payloads processed successfully.")
