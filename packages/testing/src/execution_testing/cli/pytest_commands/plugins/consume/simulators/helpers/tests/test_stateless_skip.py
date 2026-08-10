"""Tests for stateless engine mode skip handling."""

from types import SimpleNamespace
from typing import Any, cast

import pytest

from execution_testing.cli.pytest_commands.plugins.consume.simulators.engine_api import (  # noqa: E501
    skip_unsuitable_stateless_fixture,
)


def test_mutated_execution_witness_fixture_is_skipped() -> None:
    """Fixtures with deliberately mutated witnesses are not consumable."""
    fixture = cast(
        Any,
        SimpleNamespace(
            payloads=[
                SimpleNamespace(
                    execution_witness=object(),
                    execution_witness_mutated=True,
                )
            ]
        ),
    )

    with pytest.raises(
        pytest.skip.Exception,
        match="fixture contains a deliberately mutated executionWitness",
    ):
        skip_unsuitable_stateless_fixture(fixture)


def test_witnessless_fixture_is_skipped() -> None:
    """Fixtures without any executionWitness carry nothing to verify."""
    fixture = cast(
        Any,
        SimpleNamespace(
            payloads=[
                SimpleNamespace(
                    execution_witness=None,
                    execution_witness_mutated=None,
                )
            ]
        ),
    )

    with pytest.raises(
        pytest.skip.Exception,
        match="fixture has no executionWitness on any payload",
    ):
        skip_unsuitable_stateless_fixture(fixture)


def test_witness_carrying_fixture_is_not_skipped() -> None:
    """Any payload with a witness makes the fixture consumable."""
    fixture = cast(
        Any,
        SimpleNamespace(
            payloads=[
                SimpleNamespace(
                    execution_witness=None,
                    execution_witness_mutated=None,
                ),
                SimpleNamespace(
                    execution_witness=object(),
                    execution_witness_mutated=None,
                ),
            ]
        ),
    )

    skip_unsuitable_stateless_fixture(fixture)


def test_one_mutated_payload_skips_the_whole_fixture() -> None:
    """A single mutated payload makes the entire fixture unconsumable."""
    fixture = cast(
        Any,
        SimpleNamespace(
            payloads=[
                SimpleNamespace(
                    execution_witness=object(),
                    execution_witness_mutated=None,
                ),
                SimpleNamespace(
                    execution_witness=object(),
                    execution_witness_mutated=True,
                ),
            ]
        ),
    )

    with pytest.raises(pytest.skip.Exception, match="deliberately mutated"):
        skip_unsuitable_stateless_fixture(fixture)
