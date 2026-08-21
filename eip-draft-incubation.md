---
eip: XXXX
title: EIP Incubation
description: A fork-agnostic engineering designation for EIPs under active prototyping.
author: Spencer (@spencer-tb)
discussions-to: https://ethereum-magicians.org/t/TBD
status: Draft
type: Meta
created: 2026-08-21
requires: 7723
---

## Abstract

This document defines incubation, a fork-agnostic engineering designation
for EIPs under active prototyping ahead of any network upgrade's planning
process. Incubation attaches to the EIP, persists across network upgrades,
and composes with the per-upgrade inclusion stages defined in EIP-7723. It
makes executable specifications, test fixtures, benchmarks, and devnets
produced before an upgrade meta-EIP exists visible through the relevant
layer's regular engineering processes, while explicitly conferring no
inclusion status or entitlement to repository resources.

## Motivation

EIP-7723 expects an executable specification with tests when an EIP is
Considered for Inclusion, and mandates tests when an EIP is Scheduled for
Inclusion. Its stages, however, are scoped to a single upgrade and reset
between upgrades: there is no defined home for the engineering work that
produces this evidence before an upgrade's meta-EIP exists. In practice such
work happens anyway -- on personal branches and one-off devnets -- and
inclusion decisions may be made before its results are visible.

The consensus layer resolves part of this problem with in-tree feature
specifications that can ship alongside scheduled forks without implying
scheduling. The execution layer has no equivalent shared designation.
Incubation defines one for both layers.

The aim is to let important future features progress in parallel with the
current upgrade: a public acknowledgment that these research and development
efforts are being worked on optimistically for future upgrades, without
altering upgrade scheduling or creating a prerequisite for future proposal.

## Specification

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" in this
document are to be interpreted as described in RFC 2119 and RFC 8174.

### Terminology and scope

"Incubating" and "Parked" are designations in the incubation register. They
are not EIP lifecycle statuses defined by EIP-1 and are not network-upgrade
inclusion stages defined by EIP-7723.

Incubation is available to Standards Track Core EIPs whose implementation
requires coordinated work by execution-layer or consensus-layer mainnet
client teams. An Incubating EIP may be a candidate future headliner or
supporting work for one.

Incubation is tracked separately for the execution and consensus layers. An
EIP affecting both layers enters, maintains, and exits incubation on each
layer independently.

Incubation MUST NOT be interpreted as:

* a commitment or preference to include the EIP in a network upgrade;
* a Proposed, Considered, or Scheduled for Inclusion stage;
* a guarantee that an artifact will be merged or released by a specification,
  testing, client, or infrastructure repository; or
* a commitment of maintainer, continuous-integration, audit, or devnet
  capacity.

Inclusion in any upgrade remains exclusively governed by the separate
per-upgrade process defined in EIP-7723 and its corresponding AllCoreDevs
Execution (ACDE) or AllCoreDevs Consensus (ACDC) decisions.

### Eligible client teams

For each layer, AllCoreDevs Testing (ACDT) MUST maintain or reference a public
list of teams that operate production mainnet clients. The list and its size
MUST be recorded in each admission or periodic review so the denominator
cannot change retrospectively.

A client team counts as actively working on an EIP only if, during the
preceding 90 days, it has publicly identified itself with at least one
material implementation, testing, benchmarking, specification, or devnet
artifact for the EIP. A branch that only imports another team's work, an
unimplemented statement of interest, or attendance at a call is not
sufficient. The team's evidence MUST be linked from the register.

Where this document requires more than 40% of eligible client teams, the
smallest qualifying integer is the smallest number strictly greater than
`0.4 * N`, where `N` is the recorded number of eligible teams.

### Entering incubation

An EIP MAY enter incubation for a layer when all of the following hold:

* The EIP exists, is not Stagnant or Withdrawn, and has a named champion and
  a named artifact owner. One person MAY hold both roles.
* A public executable specification and normative test seed have been
  submitted as a branch or pull request against a declared baseline of the
  relevant specification or testing repository. The designated tests pass
  in public continuous integration.
* More than 40% of the layer's eligible client teams are actively working on
  the EIP, as defined above.
* The maintainers of each repository expected to host or release artifacts
  have published a feasibility assessment describing the proposed artifact
  location, isolation model, release treatment, and known capacity costs.
  This assessment is not an endorsement and MAY decline any requested use of
  repository resources.
* The champion has opened a public incubation request linking the evidence
  above at least seven days before the ACDT call at which acknowledgment is
  requested.

ACDT acknowledges incubation when the criteria above are met and there is
rough consensus that the work is suitable for the incubation tier. An
objection MUST identify a failed eligibility criterion or a concrete
technical, security, repository-capacity, or process risk. The call
facilitator MUST record the acknowledgment, each objection, and its
disposition. An objection is input to rough consensus and is not an
individual veto.

ACDT acknowledgment is an engineering coordination decision only. It does
not require ratification by ACDE or ACDC and MUST NOT determine an EIP-7723
stage. ACDE and ACDC retain exclusive authority over network-upgrade
inclusion decisions.

Following acknowledgment, the register MUST be updated by pull request. If a
champion or artifact owner is also a maintainer of a hosting repository,
they MUST disclose that role and MUST NOT be the sole approver of the
feasibility assessment or artifact merge.

### While Incubating

The layer's specification and testing repositories -- including
execution-specs for the execution layer and consensus-specs for the
consensus layer -- MAY publish executable specifications, test fixture
releases, and devnet configurations for Incubating EIPs. Each repository
defines its own incubation tier and retains authority over what it accepts,
maintains, and releases. ACDT acknowledgment cannot compel a repository to
merge or release an artifact.

Artifact names, manifests, and release notes MUST identify the EIP and label
the artifacts as experimental incubation-tier material. Incubation artifacts
MUST be isolated from mainnet and scheduled-upgrade artifacts so downstream
consumers cannot mistake them for canonical or deployment-ready outputs.
Each artifact set MUST identify its EIP revision, repository baseline, known
incompatibilities with other incubating work, and last passing continuous-
integration run.

Evidence produced during incubation MAY be considered when evaluating the
EIP under EIP-7723. Incubation evidence MAY also inform headliner selection,
but incubation MUST NOT be a prerequisite for proposing or selecting a
headliner.

### Periodic review and freshness

Each Incubating EIP MUST be reviewed by ACDT at least once every 90 days. The
review MUST confirm that:

* the champion and artifact owner remain active;
* the active-client threshold remains satisfied using the current eligible
  client list and publicly linked evidence from the preceding 90 days;
* the executable specification and tests describe the current normative EIP
  revision;
* the declared repository baseline is no more than 90 days behind the latest
  development fork of the relevant repository;
* the designated tests pass in public continuous integration; and
* hosting repositories continue to consider the artifact isolation and
  maintenance costs feasible.

Repositories MAY require a shorter review or rebasing window. A repository
maintainer MAY record that an intervening development-fork change is
irrelevant to an artifact; such a determination does not waive the 90-day
review.

The review result, denominator, qualifying client evidence, baseline, and
date MUST be recorded in the register.

### Parked and removed

An EIP becomes Parked for a layer when any periodic-review requirement is no
longer satisfied. Parked artifacts MUST be retained in a publicly accessible
form but MUST be excluded from new releases and active devnet configurations.
Repositories MAY move them out of active development branches.

A Parked EIP returns to Incubating after ACDT verifies that all periodic
review requirements have been restored and the register is updated. A new
seven-day request period is required only when the EIP has been Parked for
more than twelve months or a substantive objection remains unresolved.

An EIP is removed from a layer's register when it is Withdrawn, superseded,
has been Parked for twelve months without an active champion, or is removed
by rough consensus on ACDT. When a Core EIP reaches Final because it has been
deployed, its incubation entry SHOULD be replaced by a link to the upgrade in
which it was Included.

Removal from incubation does not alter the EIP's EIP-1 status and does not
prevent a later incubation request, except where EIP-1 makes the underlying
EIP terminal.

### Registers

Each layer's operational register MUST be maintained in a publicly versioned,
machine-readable file owned by the relevant specification or testing
repository. This EIP indexes the canonical registers but does not duplicate
their changing contents.

| Layer | Register | Custodian |
| --- | --- | --- |
| Execution | TBD | execution-specs maintainers |
| Consensus | TBD | consensus-specs maintainers |

Each entry MUST contain at least:

* EIP number and layer;
* champion and artifact owner;
* Incubating or Parked designation;
* admission and last-review dates;
* the eligible-client denominator and linked evidence for each qualifying
  team;
* EIP revision and repository baseline;
* artifact, continuous-integration, and ACDT decision-record links; and
* known incompatibilities or resource constraints.

## Rationale

### Why not a new EIP-7723 stage

The EIP-7723 stages live in a specific upgrade's meta-EIP; a stage for a
future upgrade has no meta-EIP to live in, and an EIP under incubation may
target an upgrade two or three forks out whose composition is unknown. A
per-upgrade stage would also read as a rung on the inclusion ladder, which is
precisely the signal incubation must not carry.

### Why ACDT acknowledges incubation

Incubation evaluates active implementations, executable specifications,
tests, benchmarks, and devnets. ACDT is the venue where the people producing
and consuming that evidence coordinate their work. Requiring ACDE or ACDC
ratification would blur incubation with roadmap selection and create the
inclusion signal this designation is intended to avoid. Repository
maintainers independently retain control of repository resources, while
ACDE and ACDC retain control of upgrade inclusion.

### Why a client-activity threshold

Sustained engineering work from a large minority of a layer's client teams
is revealed preference: it demonstrates that the proposal can produce useful
cross-client evidence without purporting to measure consensus about
inclusion. The threshold is a fraction rather than a fixed count so its
meaning can survive changes to the client set and differences between
layers. Public evidence and periodic reassessment prevent dormant or nominal
implementations from satisfying it indefinitely.

### Why repository feasibility is separate from acknowledgment

Specification and testing repositories bear the ongoing costs of review,
continuous integration, rebasing, storage, and releases. Client interest
does not create unlimited repository capacity. A feasibility assessment
makes those costs visible while preserving maintainers' authority over
their repositories. ACDT acknowledges an engineering effort; it does not
compel a merge or release.

### Why maintainers may champion an EIP

Repository maintainers are often among the people best equipped to develop
executable specifications and tests. Excluding them would remove useful
expertise without preventing informal influence. Disclosure, independent
approval, and repository discretion address the conflict more directly.

### Why incubation is per-layer

Client sets, specification repositories, and coordination needs differ
between the execution and consensus layers, and a cross-layer EIP's
readiness can differ substantially between them.

### Why periodic review and freshness are required

The historical objection to off-schedule specification work is maintenance
cost against a moving base. A fixed review interval makes continuing client
interest, ownership, EIP synchronization, and passing tests auditable. The
Parked designation retains useful work without presenting stale artifacts
as actively supported.

### Why operational registers live with their repositories

The repositories hosting incubation artifacts are best positioned to
validate baselines, continuous-integration results, and artifact ownership.
A machine-readable register also permits automated freshness checks. This
Meta EIP defines the stable process and indexes those registers without
requiring EIP editors to merge routine operational updates indefinitely.

### A worked example

Purely illustrative, using the binary state tree (EIP-7864):

1. The EIP champion opens an incubation request containing an executable
   specification, a normative test seed, public work from more than 40% of
   eligible execution-layer client teams, and an execution-specs feasibility
   assessment.
2. After the public review period, ACDT reviews the technical evidence and
   acknowledges execution-layer incubation by rough consensus. No ACDE
   inclusion decision is implied or required.
3. The execution-layer register records the evidence, owners, baseline, and
   review deadline. execution-specs may publish isolated releases labeled as
   incubation-tier artifacts at its maintainers' discretion.
4. Every 90 days the owners refresh the evidence, EIP revision, baseline, and
   passing tests. The results remain available to later headliner and
   inclusion discussions without granting the EIP inclusion preference.
5. If client activity, ownership, repository feasibility, or artifact
   freshness lapses, the entry becomes Parked and its artifacts leave active
   releases. It returns after ACDT verifies that the requirements are again
   satisfied.

## Backwards Compatibility

This EIP does not alter the Ethereum protocol. It documents a coordination
practice and composes with, without modifying, the stages defined in
EIP-7723 or the lifecycle statuses defined in EIP-1.

## Security Considerations

Incubation gives experimental work greater visibility and can therefore be
mistaken for technical endorsement or an inclusion commitment. Required
labels, artifact isolation, decision records, and the prohibition on using
incubation as an inclusion prerequisite reduce this risk but cannot eliminate
social signaling.

Ambiguous client counting or unverifiable implementation claims could permit
governance capture. Public eligibility lists, snapshotted denominators,
linked evidence, periodic review, and layer-specific acknowledgment make
such claims auditable.

Incubating many proposals can exhaust maintainer, continuous-integration,
release, and devnet capacity. Repository feasibility assessments and
continued repository discretion permit maintainers to reject, isolate,
deprioritize, or Park work that cannot be supported safely.

Implementations and tests may share an incorrect assumption, and passing
incubation tests is not evidence of production safety. Incubation artifacts
MUST remain experimental and MUST NOT bypass the independent review,
multi-client interoperability, audit, and upgrade-inclusion requirements
normally applied before mainnet deployment.

Public prototype artifacts can also expose denial-of-service or consensus
failure techniques before mitigations are ready. Repository security and
responsible-disclosure policies continue to apply; incubation does not
require premature public disclosure of an embargoed vulnerability.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
