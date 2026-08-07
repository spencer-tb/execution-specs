"""
Test the `--state-trie` option's session wiring: the override is set
at configure time and restored at unconfigure, so nested in-process
pytest sessions cannot leak the scheme into later sessions in the
same process.
"""

import pytest

from execution_testing.forks.base_fork import BaseFork

FORKS_PLUGIN = "execution_testing.cli.pytest_commands.plugins.forks.forks"


@pytest.mark.parametrize(
    "options, expected",
    [
        pytest.param((), "MPT", id="default_is_mpt"),
        pytest.param(("--state-trie", "pbt"), "PBT", id="pbt_override"),
        pytest.param(("--state-trie", "mpt"), "MPT", id="explicit_mpt"),
    ],
)
def test_state_trie_option_sets_and_resets_the_override(
    pytester: pytest.Pytester, options: tuple, expected: str
) -> None:
    """
    An inner session observes the commitment the option selects, and
    the override is `None` again once the session ends.
    """
    pytester.makepyfile(
        f"""
        from execution_testing.base_types import StateCommitment
        from execution_testing.forks import Amsterdam

        def test_commitment():
            assert (
                Amsterdam.state_commitment()
                is StateCommitment.{expected}
            )
        """
    )

    result = pytester.runpytest(
        "-p", FORKS_PLUGIN, "--fork", "Amsterdam", *options
    )

    leaked = BaseFork._state_commitment_override
    # Reset regardless, so a regression cannot poison sibling tests
    # running later in this process.
    BaseFork.set_state_commitment_override(None)
    result.assert_outcomes(passed=1)
    assert leaked is None
