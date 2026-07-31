"""
Conftest for ported static tests.

Enforce the fork-folder layout: every ported static test lives under
`tests/ported_static/<fork>/<legacy_suite>/`, where `<fork>` is the fork
that introduced the subject the test exercises. The fork folder is
organizational — a test's `valid_from` marker is an independent property
and may be earlier or later than the folder's fork.
"""

from pathlib import Path

import pytest

_BASE = Path(__file__).parent

_FORK_DIRS = frozenset(
    {
        "frontier",
        "homestead",
        "tangerine_whistle",
        "spurious_dragon",
        "byzantium",
        "constantinople",
        "istanbul",
        "berlin",
        "london",
        "paris",
        "shanghai",
        "cancun",
        "prague",
        "osaka",
        "amsterdam",
    }
)


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """Fail collection for tests outside a recognized fork directory."""
    for item in items:
        path = Path(str(item.path))
        try:
            rel = path.relative_to(_BASE)
        except ValueError:
            continue
        if rel.parts[0] not in _FORK_DIRS:
            raise pytest.UsageError(
                f"{rel} is not under a recognized fork directory; ported "
                "static tests live in tests/ported_static/<fork>/<suite>/ "
                f"(known forks: {', '.join(sorted(_FORK_DIRS))})"
            )
