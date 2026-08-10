"""Pytest fixtures for Engine API RPC clients."""

from typing import Generator

import pytest
from hive.client import Client

from execution_testing.exceptions import ExceptionMapper
from execution_testing.rpc import EngineRPC, EngineSszRPC


@pytest.fixture(scope="session")
def stateless(request: pytest.FixtureRequest) -> bool:
    """Return True when `--stateless` was passed on the CLI."""
    return bool(request.config.getoption("--stateless", False))


@pytest.fixture(scope="session")
def use_ssz_transport(request: pytest.FixtureRequest) -> bool:
    """Return True when `--ssz` was passed on the CLI."""
    return bool(request.config.getoption("--ssz", False))


@pytest.fixture(scope="function")
def engine_ssz_rpc(
    client: Client, client_exception_mapper: ExceptionMapper | None
) -> EngineSszRPC:
    """Provide the REST client used by the `--ssz` witness transport."""
    if client_exception_mapper:
        return EngineSszRPC(
            f"http://{client.ip}:8551",
            response_validation_context={
                "exception_mapper": client_exception_mapper,
            },
        )
    return EngineSszRPC(f"http://{client.ip}:8551")


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
