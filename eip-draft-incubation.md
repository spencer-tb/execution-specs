---
eip: XXXX
title: EIP Incubation
description: A fork-agnostic status for EIPs under active prototyping ahead of network upgrade planning.
author: Spencer (@spencer-tb)
discussions-to: https://ethereum-magicians.org/t/TBD
status: Draft
type: Meta
created: 2026-08-21
requires: 7723
---

## Abstract

This document defines "Incubating", a status for EIPs under active
engineering ahead of any network upgrade's planning process. Incubation is
fork-agnostic: it attaches to the EIP itself, persists across network
upgrades, and composes with the per-upgrade inclusion stages defined in
EIP-7723. It grants a sanctioned home for executable specifications, test
fixtures, and devnets produced before an upgrade meta-EIP exists, while
explicitly conferring no inclusion status.

## Motivation

EIP-7723 expects an executable specification with tests when an EIP is
Considered for Inclusion, and mandates one when Scheduled for Inclusion.
Its stages, however, are scoped to a single upgrade and reset between
upgrades: there is no defined home for the engineering work that produces
this evidence before an upgrade's meta-EIP exists. In practice such work
happens anyway — ad hoc, on personal branches and one-off devnets — and
inclusion decisions are made before its results are visible.

The consensus layer resolves this with in-tree feature specifications that
ship alongside scheduled forks without implying scheduling. The execution
layer has no equivalent. Incubation defines one, for both layers.

The aim is to let important future features progress in parallel with the
current upgrade: a public acknowledgment that these R&D efforts are being
worked on optimistically for future upgrades, without touching upgrade
scheduling.

## Specification

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" in this
document are to be interpreted as described in RFC 2119 and RFC 8174.

### Incubating

An Incubating EIP is one whose champion and implementing client teams are
actively producing engineering evidence — an executable specification,
tests, benchmarks, or devnets — ahead of the EIP being Proposed for
Inclusion in a specific network upgrade. An Incubating EIP may be a
candidate future headliner, or supporting work for one.

Incubation is a property of the EIP, not of a network upgrade. It persists
across upgrades and across EIP-7723 stage changes, including Declined for
Inclusion.

Incubation is tracked separately for the execution and consensus layers.
An EIP affecting both layers enters, maintains, and exits incubation on
each layer independently.

Incubation MUST NOT be interpreted as a commitment to include the EIP in
any network upgrade. It is not a Proposed, Considered, or Scheduled for
Inclusion status for a future upgrade: inclusion in any upgrade follows
the separate per-upgrade process defined in EIP-7723.

### Entering incubation

An EIP MAY be added to the incubation register for a layer when all of
the following hold:

* The EIP exists and has a named champion who is not a maintainer of
  that layer's specification or testing repositories.
* More than 40% of that layer's mainnet client teams are actively working
  on it. For the execution layer as of 2026 — Geth, Erigon, Besu,
  Nethermind, Reth, Ethrex, Nimbus — this means at least three teams.
* Its champion has proposed incubation on an AllCoreDevs Testing (ACDT)
  call, with no sustained objection.

### While Incubating

The layer's specification and testing repositories — execution-specs
(EELS) for the execution layer, consensus-specs for the consensus layer —
MAY publish artifacts for Incubating EIPs — executable specifications,
test fixture releases, and devnet configurations — within their regular
release processes, alongside mainnet and current-upgrade development
artifacts. Each repository defines its own incubation tier; artifact
naming and release notes MUST label these artifacts as incubation-tier.

While these repositories' maintainers cannot champion an EIP into
incubation, once incubation is acknowledged they MAY actively help
produce and release its artifacts.

Evidence produced during incubation SHOULD be considered when evaluating
the EIP for Considered for Inclusion under EIP-7723.

Headliner candidates for a network upgrade SHOULD be Incubating at the
time of headliner selection, and their incubation evidence SHOULD inform
that selection. Presence in the register is not itself an endorsement of
any EIP as a future headliner.

### Freshness

An Incubating EIP's executable specification MUST be maintained against
the latest development fork of the relevant specification repository, with
its tests passing, within three months of a change to that fork.
Repositories MAY require a shorter window for their incubation tier.

An EIP that fails the freshness requirement moves to Parked.

### Parked

A Parked EIP's artifacts are retained but excluded from releases. A Parked
EIP returns to Incubating by restoring freshness; no new announcement is
required. An EIP whose champion withdraws it, or which reaches Final or
Withdrawn, is removed from the register.

### Register

The incubation register is maintained in this EIP and updated by pull
request.

| EIP | Layer | Champion | Status | Artifacts |
| --- | ----- | -------- | ------ | --------- |
| TBD | TBD   | TBD      | TBD    | TBD       |

## Rationale

### Why not a new EIP-7723 stage

The EIP-7723 stages live in a specific upgrade's meta-EIP; a stage for a
future upgrade has no meta-EIP to live in, and an EIP under incubation may
target an upgrade two or three forks out whose composition is unknown. A
per-upgrade stage would also read as a rung on the inclusion ladder, which
is precisely the signal incubation must not carry.

### Why a client-activity threshold

Sustained R&D from a large minority of a layer's client teams is revealed
preference: it signals the teams themselves likely want the feature,
without asking anyone to vote on scheduling. The threshold is a fraction
rather than a fixed count so its meaning holds as the client set evolves
and differs between layers, and it sits deliberately below a majority:
incubation acknowledges interest, it does not measure consensus.

### Why champions cannot be specification maintainers

The maintainers of the specification and testing repositories operate the
incubation tier itself; requiring an external champion separates advocacy
for a feature from gatekeeping of the tier that hosts it. Maintainer
effort is what an acknowledgment unlocks, not what proposes it.

### Why incubation is per-layer

Client sets, specification repositories, and coordination calls differ
between the execution and consensus layers, and a cross-layer EIP's
readiness can differ substantially between them.

### Why a freshness requirement

The historical objection to off-schedule specification work is maintenance
cost against a moving base. Modern tooling has substantially reduced that
cost, and the freshness requirement makes the claim enforceable rather
than rhetorical: an incubation tier is self-cleaning, holding only
features with an active champion and passing tests against the current
development fork.

### A worked example

Purely illustrative, using the binary state tree (EIP-7864):

1. The EIP exists with a named champion who maintains neither
   execution-specs nor consensus-specs. More than 40% of execution-layer
   mainnet client teams have active binary tree R&D branches.
2. The champion proposes incubation on an ACDT call. With no sustained
   objection, the EIP enters the register as Incubating on the execution
   layer.
3. execution-specs publishes the executable specification and fixture
   releases for the feature, labeled incubation-tier, alongside its
   mainnet and current-upgrade test releases; its maintainers now
   actively help produce them.
4. When the next upgrade's meta-EIP opens, the champion proposes the EIP
   for inclusion under EIP-7723; the incubation evidence informs the CFI
   and headliner discussions. Incubation continues regardless of the
   outcome.
5. If the specification falls more than three months behind the current
   development fork, the EIP moves to Parked and out of releases,
   returning once freshness is restored.

### Why the register lives here

Upgrade meta-EIPs already track their inclusion lists in-document; keeping
the fork-agnostic register in this document follows the same pattern and
avoids a normative dependency on any external repository.

## Backwards Compatibility

This EIP does not alter the Ethereum protocol. It documents a coordination
practice and composes with, without modifying, the stages defined in
EIP-7723.

## Security Considerations

None.

## Copyright

Copyright and related rights waived via [CC0](../LICENSE.md).
