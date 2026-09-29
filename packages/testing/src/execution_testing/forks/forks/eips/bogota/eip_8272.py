"""
EIP-8272: Recent Roots for Frame Transactions.

Add the recent root contract, a system contract that stores application
roots by slot and lets a frame transaction verify recent roots through an
ordinary `VERIFY` frame targeting it. The transaction payload, gas rules
and opcodes are unchanged; the fork installs the contract at activation.

https://eips.ethereum.org/EIPS/eip-8272
"""

from typing import Mapping

from ....base_fork import BaseFork

RECENT_ROOT_ADDRESS = 0x0000000000000000000000000000000000008272
RECENT_ROOT_BYTECODE = bytes.fromhex(
    "34600858015760095801565b60006000fd5b6040361461010e5801576104"
    "8036116048360617361517600858015760095801565b60006000fd5b6000"
    "6080525b608051356020526020608051013560c01c60a0524b60a0511015"
    "600858015760095801565b60006000fd5b611fff60a0514b031160085801"
    "5760095801565b60006000fd5b7f8f42481679c8e6fefa040974b3c905e0"
    "ce3f2e464ba93acdb074a41181617efc60005260a05160c01b6040526028"
    "608051013560485260686000207fbdc897da2177d260ff5f4be5d4b2aad4"
    "3f89c3347a305b584fa5a2546d053daa60005261200060a0510660c01b60"
    "40526048600020541415600858015760095801565b60006000fd5b604860"
    "805101608052366080511063000000df5803570060855801565b3360601b"
    "60005260003560145260346000206020527f8f42481679c8e6fefa040974"
    "b3c905e0ce3f2e464ba93acdb074a41181617efc6000524b60c01b604052"
    "60203560485260686000207fbdc897da2177d260ff5f4be5d4b2aad43f89"
    "c3347a305b584fa5a2546d053daa6000526120004b0660c01b6040526048"
    "60002055005b"
)
"""
Candidate runtime code of the recent root contract: the EIP leaves the
code to be determined, and this value mirrors the spec's constant.
"""
RECENT_ROOT_NONCE = 1


class EIP8272(BaseFork):
    """EIP-8272 class."""

    @classmethod
    def pre_allocation(cls) -> Mapping:
        """Pre-allocate the recent root contract."""
        return {
            RECENT_ROOT_ADDRESS: {
                "nonce": RECENT_ROOT_NONCE,
                "code": RECENT_ROOT_BYTECODE,
            }
        } | super(EIP8272, cls).pre_allocation()  # type: ignore

    @classmethod
    def activation_code_installs(cls) -> Mapping:
        """
        Initialize the recent root contract when the fork activates.

        The install writes the runtime code and raises the nonce to one,
        keeping a higher existing nonce and the balance; blockchain tests
        get the account from this hook at the fork block, so a fixture
        crossing the boundary exercises the initialization itself.
        """
        return {
            RECENT_ROOT_ADDRESS: {
                "code": RECENT_ROOT_BYTECODE,
                "nonce": RECENT_ROOT_NONCE,
            },
        } | super(EIP8272, cls).activation_code_installs()  # type: ignore
