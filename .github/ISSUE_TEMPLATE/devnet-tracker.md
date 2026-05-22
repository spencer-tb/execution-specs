---
name: Devnet Tracker
about: Track specification, testing, and launch readiness for a devnet
title: '<devnet-name> Tracker'
labels: A-spec-specs, A-spec-tests, C-eip, C-test
assignees: ''

---

## <devnet-name>

### Target Fork

**<fork>**

### Overview

<!--
    Briefly describe the purpose of this devnet, its scope, and any relevant
    links (devnet specs repo, ACD notes, configuration / genesis).
-->

- **Specs**: <!-- link to the devnet specs / config repo -->
- **Target release**: <!-- e.g. v7.3.0 or "TBD" -->
- **Test release date**: <!-- YYYY-MM-DD or "TBD" — aim for 5 days before the devnet -->
- **Devnet launch date**: <!-- YYYY-MM-DD or "TBD" -->

> [!NOTE]
> Aim to cut the test (fixture) release **at least 5 days before** the devnet
> launch, to give client teams time to integrate and run them.

### Aim

<!--
    A short statement of what we're aiming for in this devnet release.
    Be explicit that the scope is tentative and will change.
-->

We aim to include the following EIPs in the first `<devnet-name>` EELS release.
This scope is tentative — EIPs may be added, dropped, or deferred as decisions
land in ACD and during implementation.

### Instructions

- [ ] Assign issue to the devnet coordination owner(s).
- [ ] Add the issue to the target fork milestone if applicable.
- [ ] Link each included EIP's [EIP Implementation Tracker](https://github.com/ethereum/execution-specs/issues/new?template=eip-tracker.md) below.

> [!IMPORTANT]
> Per-EIP specification and testing progress is tracked in the individual EIP
> Implementation Tracker issues. This issue tracks devnet-level readiness only.

### Proposed Scope

<!--
    Group EIPs by confidence. Move EIPs between groups as decisions are made,
    and check an EIP off in "Confirmed" once its tracker issue is stable.
-->

#### Confirmed

- [ ] [EIP-<eip-number>](https://eips.ethereum.org/EIPS/eip-<eip-number>) — #<tracker-issue>
- [ ] [EIP-<eip-number>](https://eips.ethereum.org/EIPS/eip-<eip-number>) — #<tracker-issue>

#### To Be Discussed

<!-- Items pending an ACD / owner decision. Link the relevant EIP PR. -->

- [ ] [EIP-<eip-number>](https://eips.ethereum.org/EIPS/eip-<eip-number>) — <reason / link to discussion PR>

#### At Risk / Likely Dropped

<!-- EIPs that may not make this devnet. -->

- [ ] [EIP-<eip-number>](https://eips.ethereum.org/EIPS/eip-<eip-number>) — <reason>

### Notes & Risks

<!--
    Call out the integration challenges and known hard spots, e.g. cross-EIP
    alignment, ordering dependencies, framework changes.
-->

The most difficult changes are expected to be `<...>`. Highlight any cross-EIP
alignment, ordering dependencies, or testing-framework work that could block the
release here.

#### Guidance for Marking Items Complete

An item should only be checked off once it is considered *stable*. In this
context, stable means:

- No major issues or ambiguities are still being uncovered in the specification or tests.
- There are no open discussion points awaiting resolution.
- Client implementations have been consistently passing the tests for at least a week.

It is ultimately up to the owners' discretion to decide when an item should be
marked as complete, using this guidance as the basis for that decision.

### Specification + Testing Status

- [ ] All included EIP specifications merged to the corresponding `forks/<fork>` branch.
- [ ] Devnet branch (e.g. `devnets/<devnet-name>`) created and rebased on the target fork.
- [ ] Required testing framework modifications implemented.
- [ ] Test suites for all included EIPs implemented.
- [ ] No regressions or failures in tests from prior forks (including static tests).
- [ ] Fixtures generated and released for the devnet.
- [ ] Ran tests using `execute` to ensure compatibility with live networks.

### Client Readiness

<!--
    Track which client implementations are ready for the devnet.
-->

- [ ] geth
- [ ] erigon
- [ ] besu
- [ ] nethermind
- [ ] reth
- [ ] ethrex

### Process Status

- [ ] Hive tests passing on at least two implementations.
- [ ] Interop / cross-client testing completed.
- [ ] Devnet launched.
- [ ] Post-launch issues triaged and tracked.
