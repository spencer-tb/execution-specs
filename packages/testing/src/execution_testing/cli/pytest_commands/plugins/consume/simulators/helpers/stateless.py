"""Fixture suitability checks for the stateless consume mode."""

from typing import Union

import pytest

from execution_testing.fixtures import (
    BlockchainEngineFixture,
    BlockchainEngineXFixture,
)


def skip_unsuitable_stateless_fixture(
    fixture: Union[BlockchainEngineFixture, BlockchainEngineXFixture],
) -> None:
    """Skip fixtures the stateless engine mode cannot consume."""
    if any(p.execution_witness_mutated for p in fixture.payloads):
        pytest.skip("fixture contains a deliberately mutated executionWitness")
    if not any(p.execution_witness is not None for p in fixture.payloads):
        pytest.skip("fixture has no executionWitness on any payload")
