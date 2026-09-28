"""
The Bogota fork is the development fork after Amsterdam. EIPs targeting it are
prototyped on their own ``eips/bogota/*`` branches and land here once
accepted.

### Changes

- [EIP-8141: Frame Transactions][EIP-8141]

### Releases

[EIP-8141]: https://eips.ethereum.org/EIPS/eip-8141
"""

from ethereum.fork_criteria import ForkCriteria, Unscheduled

FORK_CRITERIA: ForkCriteria = Unscheduled(order_index=4)
