"""
EVM replacement for the identity precompile retired by [EIP-7666].

The identity precompile is replaced by an ultra-minimal piece of EVM
code with the same functionality, installed at its address when the
fork activates (see [`apply_fork`]). The bytecode is specified
verbatim by the EIP.

[EIP-7666]: https://eips.ethereum.org/EIPS/eip-7666
[`apply_fork`]: ref:ethereum.forks.amsterdam.fork.apply_fork
"""

from typing import Final

from ethereum_types.bytes import Bytes

from ethereum.state import Address

from .utils.hexadecimal import hex_to_address

IDENTITY_ADDRESS: Final[Address] = hex_to_address("0x04")
"""
Address of the retired identity precompile, now holding
[`IDENTITY_EVM_CODE`][c].

[c]: ref:ethereum.forks.amsterdam.evmified_precompiles.IDENTITY_EVM_CODE
"""

IDENTITY_EVM_CODE: Final[Bytes] = Bytes(bytes.fromhex("365f5f37365ff3"))
"""
Runtime code replacing the identity precompile, as specified by
[EIP-7666]: `CALLDATASIZE PUSH0 PUSH0 CALLDATACOPY CALLDATASIZE PUSH0
RETURN`; keccak256
`0x2fec8f31a9970b0f4ecc5e23be5802c38210902df5c8ae31b251da5b9d0ed416`.

[EIP-7666]: https://eips.ethereum.org/EIPS/eip-7666
"""
