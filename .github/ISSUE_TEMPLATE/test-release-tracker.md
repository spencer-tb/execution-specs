---
name: Test Release Tracker
about: Track EL test release readiness for a feature or devnet (tests-<feat>@vX.Y.Z)
title: '<feat>@vX.Y.Z Test Release Tracker'
labels: C-tracker, P-high
assignees: ''

---

## `<feat>`@v`X.Y.Z`

> [!NOTE]
> This is an **execution layer (EL) only** tracker — it does not cover
> consensus layer (CL) readiness.

> [!TIP]
> This template covers any EL test release. Lines and checkboxes marked
> _(devnet only)_ apply only when the release targets a specific devnet —
> delete them otherwise.

### Overview

<!--
    Briefly describe the purpose of this test release, its scope, and any
    relevant links (specs repo, ACD notes, configuration / genesis).

    `<feat>` is the full feature slug used in the release tag, and must be
    written out in full — the template appends nothing to it. When the release
    targets a devnet, include `-devnet` in the slug yourself; omit it for a
    feature that is not tied to a specific devnet.

    Examples (slug → resulting tag):
      - `glamsterdam-devnet` → `tests-glamsterdam-devnet@v7.0.0`  (devnet)
      - `fusaka-devnet`      → `tests-fusaka-devnet@v1.0.0`       (devnet)
      - `benchmark`          → `tests-benchmark@v1.0.0`           (no devnet)

    The slug is typically the fork name or headliner feature. The release
    fills all forks until the development fork (e.g. `fill --until Amsterdam`)
    so clients can guard against regressions, and is run in Hive CI under the
    standard naming scheme.
-->

- **Target release tag**: <!-- e.g. tests-glamsterdam-devnet@v7.0.0 -->
- **EELS branch**: <!-- link to the branch being used for this release (for a devnet, e.g. `devnets/<fork>/N`) -->
- **Test release date**: <!-- YYYY-MM-DD or "TBD" -->
- **Devnet launch date** _(devnet only)_: <!-- YYYY-MM-DD or "TBD" -->

> [!NOTE]
> **Versioning** (`vX.Y.Z`): when targeting a devnet, `X` is the devnet number
> (e.g. `7` for `glamsterdam-devnet-7`), making the targeted devnet explicit;
> for a non-devnet feature, `X` is a major version bumped on a rework. `Y`/`Z`
> follow the same semantics as the consensus test releases: `Y` (minor) is
> bumped for a change in behaviour (a spec/test change that alters existing
> fixtures), and `Z` (patch) is bumped for new test additions only.

> [!NOTE]
> _(devnet only)_ Aim to cut the test (fixture) release **at least 5 days
> before** the devnet launch, to give client teams time to integrate and run
> them.

### Follows On From _(optional)_

<!--
    Optional. If there is a previous release tracker, link it here for context
    — even if the scope has changed. If this is a test-only follow-up (most
    updates are test additions and the scope is semantically unchanged), keep
    this issue small and list only what is new below. If there is no
    predecessor (a brand new `<feat>` / first release), remove this section.
-->

This is a follow-up to the `tests-<feat>@vX.Y.Z` tracker (#`<issue>`),
with test additions only.

> [!TIP]
> For a test-only follow-up, the sections below can be trimmed to just what
> changed since the previous tracker.

### Aim

<!--
    A short statement of what we're aiming for in this test release.
    Be explicit that the scope is tentative and will change.
-->

We aim to include the following EIPs in the first `tests-<feat>@vX.Y.Z` EELS
test release. This scope is tentative — EIPs may be added, dropped, or
deferred as decisions land in ACD and during implementation.

### Instructions

- [ ] Add the issue to the target fork milestone if applicable.
- [ ] Link each included
  EIP's [EIP Implementation Tracker](https://github.com/ethereum/execution-specs/issues/new?template=eip-tracker.md)
  below.

> [!IMPORTANT]
> Per-EIP specification and testing progress is tracked in the individual EIP
> Implementation Tracker issues. This issue tracks release-level readiness only.

### EIPs Included

<!--
    The definitive list of the exact spec version each included EIP is frozen
    at for this release. These links are the source of truth used to generate
    the release notes, so keep this list flat and complete — one line per EIP.

    Every link MUST be a commit permalink to the markdown in the canonical
    `ethereum/EIPs` repo (`https://github.com/ethereum/EIPs/blob/<sha>/EIPS/eip-<n>.md`),
    NOT `eips.ethereum.org` and NOT a fork. In-flight EIPs still living in a
    PR will not have a canonical link yet — mark them `TBD` until the change
    merges to `ethereum/EIPs`, then replace `TBD` with the permalink.
-->

> [!IMPORTANT]
> Before closing this issue, every entry below must point to an `ethereum/EIPs`
> commit permalink — no `TBD` values. These links are consumed directly when
> generating the release notes and external automations.

- [ ] EIP-<eip-number>: https://github.com/ethereum/EIPs/blob/<sha>/EIPS/eip-<eip-number>.md
- [ ] EIP-<eip-number>: TBD <!-- in-flight; pin once merged to ethereum/EIPs -->

### Spec Changes

<!--
    List each EIP included in this release as a descending bullet hierarchy.
    Prefix the top-level checkbox with:

      - ✨ New     — an EIP introduced for the first time in this release.
      - 🔄 Updated — an EIP already in a prior release that is being changed.

    🔄 Updated EIPs use a three-level hierarchy:

      1. The EIP being updated (linked) with a checkbox — check it off once
         all of its changes have landed. Use one top-level entry per EIP.
         2. The EIP PR(s) that define the change (plain bullet, no checkbox);
            add a short note after the link if the change is still pending a
            decision.
            3. The execution-specs PR(s) that satisfy that EIP change, each
               with a checkbox — check off as each is merged.

    ✨ New EIPs use a two-level hierarchy (there is no pre-existing spec to
    diff against, so the EIP PR level is dropped):

      1. The EIP (linked) with a checkbox.
         2. The execution-specs PR(s) implementing it, each with a checkbox.

    Note a ✨ New EIP is not necessarily in-flight: it may be a long-merged
    EIP simply being bumped into this release. Link its PR only if the spec is
    still under review; otherwise link the merged markdown permalink.

    Link the top-level EIP to EITHER its PR or a commit permalink to the
    markdown — but always in the canonical `ethereum/EIPs` repo, NEVER an
    author's fork, and never `eips.ethereum.org` (which always renders the
    latest merged version and hides the release's frozen one).

      - Prefer the PR while the change is in-flight: it shows at a glance
        whether the change has merged or is still being discussed. Note that
        the PR lives at `https://github.com/ethereum/EIPs/pull/<n>` even when
        the branch itself is in a fork — so this stays an `ethereum/EIPs` link.
      - Once merged (or for an EIP that merged long ago), a commit permalink
        to the markdown (`https://github.com/ethereum/EIPs/blob/<sha>/EIPS/eip-<n>.md`)
        pins the exact spec text.

    The frozen spec version used for release notes is recorded separately in
    the EIPs Included section above; this section tracks the change itself.
    A single EIP may have several relevant PRs — list them all.
-->

- [ ] 🔄 Updated **[EIP-<eip-number>](https://github.com/ethereum/EIPs/pull/<pr>)
  **: <short description of the change> <!-- in-flight change -->
    - https://github.com/ethereum/EIPs/pull/<pr>: <optional note / decision status>
        - [ ] #<execution-specs-pr>
- [ ] 🔄 Updated **[EIP-<eip-number>](https://github.com/ethereum/EIPs/blob/<sha>/EIPS/eip-<eip-number>.md)
  **: <short description of the change> <!-- change already merged -->
    - https://github.com/ethereum/EIPs/pull/<pr>
        - [ ] #<execution-specs-pr>
- [ ] ✨ New **[EIP-<eip-number>](https://github.com/ethereum/EIPs/pull/<pr>)
  **: <short description> <!-- new EIP still under review -->
    - [ ] #<execution-specs-pr>
- [ ] ✨ New **[EIP-<eip-number>](https://github.com/ethereum/EIPs/blob/<sha>/EIPS/eip-<eip-number>.md)
  **: <short description> <!-- long-merged EIP, just bumped into this release -->
    - [ ] #<execution-specs-pr>

### New Test Cases

<!--
    Test additions for this release that are not tied to a specific EIP spec
    change above. Link the execution-specs PR or issue for each.
-->

- [ ] <description>, #<execution-specs-pr-or-issue>
- [ ] https://github.com/ethereum/execution-specs/pull/<pr>

### Notes & Risks

<!--
    Call out the integration challenges and known hard spots, e.g. cross-EIP
    alignment, ordering dependencies, framework changes.
-->

The most difficult changes are expected to be `<...>`. Highlight any cross-EIP
alignment, ordering dependencies, or testing-framework work that could block the
release here.

### Specification + Testing Status

- [ ] All included EIP specifications merged to the release branch.
- [ ] _(devnet only)_ Devnet branch (e.g. `devnets/<fork>/N`) created and rebased on the target `forks/<fork>` branch.
- [ ] Required testing framework modifications implemented.
- [ ] Sufficient test suites for the included EIPs implemented.
- [ ] No regressions or failures in tests from prior forks (including static tests).
- [ ] Fixtures generated and released.
- [ ] [`hive-tests`](https://github.com/ethpandaops/hive-tests/tree/master/.github/workflows) repo checked/updated to
  run the latest set of fixtures.
- [ ] [`hive-ui`](https://github.com/ethpandaops/hive-ui/blob/master/public/discovery.json) discovery checked/updated to
  the latest workflow file within the `hive-tests` repo.

### Process Status

- [ ] Hive tests passing on at least two implementations.
- [ ] Interop / cross-client testing completed.
- [ ] _(devnet only)_ Devnet launched.
- [ ] Post-launch issues triaged and tracked.

### Closure

<!--
    Before closing this issue, link the test fixture release tag that shipped
    for this release.
-->

- [ ] All [EIPs Included](#eips-included) resolved to `ethereum/EIPs` commit permalinks — no `TBD` entries remain (these
  feed the release notes).
- [ ] Linked the test fixture release tag used for this
  release: <!-- e.g. https://github.com/ethereum/execution-specs/releases/tag/<tag> -->

> [!IMPORTANT]
> After tagging, any future changes must be added to a newly created release
> tracker rather than reopening or amending this one.
