#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# ///
"""
Resolve the nightly fill run to promote to a draft `tests@` release.

Usage: `promote_nightly.py` (all inputs come from the environment).

The scheduled nightly runs of `release_fixtures.yaml` fill the mainnet
`tests` feature and upload a release-shaped `fixtures_tests` artifact,
but never tag or draft a release. Promotion turns the newest such
artifact into a draft `tests@<version>` release without refilling:
this script validates the requested version, finds the nightly run to
promote, and pins the exact commit that run built so the workflow can
download its artifact and target the release tag at the right SHA.

Checks performed, failing fast on the first violation:

- `INPUT_VERSION` matches `vX.Y.Z` and is greater than the newest
  existing `tests@` tag (promotion always moves forward; anything
  unusual belongs in a full `release_fixtures.yaml` dispatch).
- The promoted run is a successful *scheduled* run of
  `release_fixtures.yaml` with a live (unexpired) `fixtures_tests`
  artifact. By default the newest such run wins; `INPUT_RUN_ID`
  promotes a specific run instead.
- The promoted commit is an ancestor of the current branch head.
  Commits after it are listed in the step summary so the releaser can
  see what the release will NOT contain.

Read `GITHUB_REPOSITORY`, `GITHUB_SHA`, `INPUT_VERSION` and the
optional `INPUT_RUN_ID` from the environment and query the GitHub API
via the `gh` CLI (authenticated by `GH_TOKEN`). Print `run_id`,
`target_sha` and `prev_tag` (empty when no `tests@` tag exists yet) as
`key=value` lines for `$GITHUB_OUTPUT`.
"""

import json
import os
import re
import subprocess
import sys
from typing import NoReturn

WORKFLOW_FILE = "release_fixtures.yaml"

# The combined-tarball artifact a nightly `tests` fill uploads; only
# this artifact is ever promoted to a mainnet release.
ARTIFACT_NAME = "fixtures_tests"

VERSION_RE = re.compile(r"^v([0-9]+)\.([0-9]+)\.([0-9]+)$")


def fail(message: str) -> NoReturn:
    """Print an error to stderr and exit non-zero."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def gh_api(path: str) -> str:
    """Return the stdout of `gh api <path>`, exiting non-zero on error."""
    result = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error: gh api {path} failed:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)
    return result.stdout


def append_summary(text: str) -> None:
    """Append *text* to the GitHub step summary, or stderr if unset."""
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as f:
            f.write(text + "\n")
    else:
        print(text, file=sys.stderr)


def parse_version(version: str) -> tuple[int, int, int]:
    """Return the (major, minor, patch) tuple of a `vX.Y.Z` version."""
    m = VERSION_RE.match(version)
    if not m:
        fail(f"version '{version}' must match vX.Y.Z (e.g. v5.0.0)")
    major, minor, patch = (int(g) for g in m.groups())
    return major, minor, patch


def newest_tests_tag(repository: str) -> str:
    """
    Return the newest existing `tests@vX.Y.Z` tag, or "" when none.

    The `tests@` ref prefix cannot match any other feature's tags
    (those are namespaced `tests-<feature>@`), so every match is a
    mainnet tests release.
    """
    refs = json.loads(
        gh_api(f"repos/{repository}/git/matching-refs/tags/tests@")
    )
    tags = [ref["ref"].removeprefix("refs/tags/") for ref in refs]
    versioned = [
        (parse_version(tag.removeprefix("tests@")), tag)
        for tag in tags
        if VERSION_RE.match(tag.removeprefix("tests@"))
    ]
    if not versioned:
        return ""
    return max(versioned)[1]


def has_live_tests_artifact(repository: str, run_id: str) -> bool:
    """Return whether *run_id* has a live `fixtures_tests` artifact."""
    artifacts = json.loads(
        gh_api(f"repos/{repository}/actions/runs/{run_id}/artifacts")
    )["artifacts"]
    return any(
        a["name"] == ARTIFACT_NAME and not a["expired"] for a in artifacts
    )


def promotable_run(repository: str, run_id: str) -> tuple[str, str]:
    """
    Return the (run id, head SHA) of the nightly run to promote.

    With an explicit *run_id*, verify it is a successful scheduled run
    of the release workflow with a live artifact. Otherwise take the
    newest such run (skip-runs upload no artifacts and expired fills
    cannot be downloaded, so both are passed over).
    """
    if run_id:
        run = json.loads(gh_api(f"repos/{repository}/actions/runs/{run_id}"))
        if (
            run.get("event") != "schedule"
            or run.get("conclusion") != "success"
            or not str(run.get("path", "")).endswith(WORKFLOW_FILE)
        ):
            fail(
                f"run {run_id} is not a successful scheduled run of "
                f"{WORKFLOW_FILE}"
            )
        if not has_live_tests_artifact(repository, run_id):
            fail(f"run {run_id} has no live `{ARTIFACT_NAME}` artifact")
        # Echo back the id from the API response, not the raw input.
        return str(run["id"]), str(run["head_sha"])

    runs = json.loads(
        gh_api(
            f"repos/{repository}/actions/workflows/{WORKFLOW_FILE}"
            "/runs?status=success&event=schedule&per_page=10"
        )
    )["workflow_runs"]
    for run in runs:
        if has_live_tests_artifact(repository, str(run["id"])):
            return str(run["id"]), str(run["head_sha"])
    fail(
        f"no scheduled run of {WORKFLOW_FILE} with a live "
        f"`{ARTIFACT_NAME}` artifact found; dispatch a full release instead"
    )


def commits_after(
    repository: str, target_sha: str, head_sha: str
) -> list[str]:
    """
    Return `- <sha> <subject>` lines for commits after *target_sha*.

    Fail when *target_sha* is not an ancestor of *head_sha*: a nightly
    built from a rewritten or foreign branch must not be promoted.
    """
    compare = json.loads(
        gh_api(f"repos/{repository}/compare/{target_sha}...{head_sha}")
    )
    if compare["status"] not in ("identical", "ahead"):
        fail(
            f"nightly commit {target_sha} is not an ancestor of "
            f"{head_sha} (compare status: {compare['status']})"
        )
    return [
        f"- {c['sha'][:7]} {(c['commit']['message'].splitlines() or [''])[0]}"
        for c in compare["commits"]
    ]


def main() -> None:
    """Print the resolved run for `$GITHUB_OUTPUT` and the summary."""
    repository = os.environ["GITHUB_REPOSITORY"]
    head_sha = os.environ["GITHUB_SHA"]
    version = os.environ["INPUT_VERSION"]

    requested = parse_version(version)
    prev_tag = newest_tests_tag(repository)
    prev_version = (
        parse_version(prev_tag.removeprefix("tests@")) if prev_tag else None
    )
    if prev_version and requested <= prev_version:
        fail(
            f"version '{version}' must be greater than the newest "
            f"tests release ({prev_tag})"
        )

    run_id, target_sha = promotable_run(
        repository, os.environ.get("INPUT_RUN_ID", "")
    )
    missing = commits_after(repository, target_sha, head_sha)

    print(f"run_id={run_id}")
    print(f"target_sha={target_sha}")
    print(f"prev_tag={prev_tag}")

    run_url = f"https://github.com/{repository}/actions/runs/{run_id}"
    append_summary(
        f"Promoting nightly run [{run_id}]({run_url}) "
        f"(built at `{target_sha}`) to a draft `tests@{version}` release."
    )
    if missing:
        append_summary(
            "### Commits NOT included in this release\n"
            + "\n".join(missing)
            + "\n\nDispatch a full release to include them."
        )
    else:
        append_summary(
            "The nightly is up to date with the current branch head."
        )


if __name__ == "__main__":
    main()
