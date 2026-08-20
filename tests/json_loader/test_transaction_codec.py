"""Test that decode_transaction handles legacy transactions as bytes."""

import pytest
from ethereum_rlp import rlp
from ethereum_types.bytes import Bytes
from ethereum_types.numeric import U256, Uint

from ethereum.exceptions import EthereumException
from ethereum.forks.amsterdam.transactions import (
    LegacyTransaction,
    decode_transaction,
)
from ethereum.state import Address


def test_decode_legacy_from_bytes() -> None:
    """Decode a legacy transaction from both bytes and object form."""
    tx = LegacyTransaction(
        nonce=U256(0),
        gas_price=Uint(1),
        gas=Uint(21000),
        to=Address(b"\x00" * 20),
        value=U256(0),
        data=Bytes(b""),
        v=U256(27),
        r=U256(1),
        s=U256(2),
    )
    encoded = rlp.encode(tx)
    assert encoded[0] >= 0xC0
    assert decode_transaction(encoded) == tx
    assert decode_transaction(tx) is tx


@pytest.mark.parametrize(
    "raw",
    [
        pytest.param(b"", id="empty"),
        pytest.param(b"\xff", id="reserved_first_byte"),
        pytest.param(b"\x05", id="unknown_type"),
        pytest.param(b"\xbf", id="not_a_list_prefix"),
    ],
)
def test_decode_malformed_bytes_raises_catchable(raw: bytes) -> None:
    """
    Malformed transaction bytes raise an `EthereumException`.

    The inclusion list validator skips entries that fail to decode by
    catching `EthereumException`, so no input may escape as a bare
    `IndexError` or `AssertionError`.
    """
    with pytest.raises(EthereumException):
        decode_transaction(Bytes(raw))
