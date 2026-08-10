"""Pytest fixtures for Engine API RPC clients."""

from typing import Generator, Union

import pytest
from hive.client import Client

from execution_testing.exceptions import ExceptionMapper
from execution_testing.fixtures import (
    BlockchainEngineFixture,
    BlockchainEngineXFixture,
)
from execution_testing.rpc import EngineRPC, EngineSszRPC

from .helpers.stateless import skip_unsuitable_stateless_fixture


@pytest.fixture(scope="session")
def stateless(request: pytest.FixtureRequest) -> bool:
    """Return True when `--stateless` was passed on the CLI."""
    return bool(request.config.getoption("--stateless", False))


@pytest.fixture(scope="session")
def use_ssz_transport(request: pytest.FixtureRequest) -> bool:
    """Return True when `--ssz` was passed on the CLI."""
    return bool(request.config.getoption("--ssz", False))


@pytest.fixture(autouse=True)
def _skip_unsuitable_stateless_fixtures(
    stateless: bool,
    fixture: Union[BlockchainEngineFixture, BlockchainEngineXFixture],
) -> None:
    """
    Skip unsuitable fixtures before the client fixture starts a container.

    Autouse fixtures run first within their scope, so unsuitable fixtures
    never pay for client startup.
    """
    if stateless:
        skip_unsuitable_stateless_fixture(fixture)


@pytest.fixture(scope="function")
def engine_rpc(
    client: Client, client_exception_mapper: ExceptionMapper | None
) -> Generator[EngineRPC, None, None]:
    """
    Initialize Engine RPC client for the execution client under test.

    Provide a configured EngineRPC instance that communicates
    with the client's Engine API endpoint (port 8551). If an
    exception mapper is available, it will be used for response
    validation to map client-specific error messages to standard
    exception types.

    The session is closed on teardown.

    Args:
        client: The Hive client instance to connect to.
        client_exception_mapper: Optional exception mapper.

    Yields:
        Configured EngineRPC instance for making Engine API calls.

    """
    if client_exception_mapper:
        rpc = EngineRPC(
            f"http://{client.ip}:8551",
            response_validation_context={
                "exception_mapper": client_exception_mapper,
            },
        )
    else:
        rpc = EngineRPC(f"http://{client.ip}:8551")
    with rpc:
        yield rpc


@pytest.fixture(scope="function")
def engine_ssz_rpc(
    client: Client, client_exception_mapper: ExceptionMapper | None
) -> EngineSszRPC:
    """
    Initialize the Engine SSZ REST client for the client under test.

    Provide a configured EngineSszRPC instance that communicates
    with the client's REST POST /new-payload-with-witness endpoint
    (port 8551), used by the `--stateless --ssz` witness transport.
    If an exception mapper is available, it will be used for response
    validation to map client-specific error messages to standard
    exception types.

    Args:
        client: The Hive client instance to connect to.
        client_exception_mapper: Optional exception mapper.

    Returns:
        Configured EngineSszRPC instance for witness endpoint calls.

    """
    if client_exception_mapper:
        return EngineSszRPC(
            f"http://{client.ip}:8551",
            response_validation_context={
                "exception_mapper": client_exception_mapper,
            },
        )
    return EngineSszRPC(f"http://{client.ip}:8551")
