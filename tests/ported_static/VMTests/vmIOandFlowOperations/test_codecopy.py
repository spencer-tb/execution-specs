"""
Ori Pomerantz qbzzt1@gmail.com.

Ported from:
tests/static/state_tests/VMTests/vmIOandFlowOperations/codecopyFiller.yml
"""

import pytest
from execution_testing import (
    Account,
    Address,
    Alloc,
    Environment,
    Hash,
    StateTestFiller,
    Transaction,
)

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/VMTests/vmIOandFlowOperations/codecopyFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex(
                        "6040600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "6001600003600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex(
                        "611000600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "6010600f600e600d600c600b600a60096008600760066005600460036002600101010101010101010101010101010161010052602060006000396040602060203960005160005560205160015560405160025500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "3860ff5560ff5460006000396160a76000556160a76001556160a760025560005160005560205160015560405160025560605160035560805160045560a0516005550061deadff60ff546000f360aa60bb60cc60dd60ee60fff400"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={
                        0: 0x6040600060003960005160005560205160015500000000000000000000000000  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "60006000600060006004356110000162fffffff400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex(
                        "6040600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "6001600003600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex(
                        "611000600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "6010600f600e600d600c600b600a60096008600760066005600460036002600101010101010101010101010101010161010052602060006000396040602060203960005160005560205160015560405160025500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "3860ff5560ff5460006000396160a76000556160a76001556160a760025560005160005560205160015560405160025560605160035560805160045560a0516005550061deadff60ff546000f360aa60bb60cc60dd60ee60fff400"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={
                        0: 0x6010600F600E600D600C600B600A600960086007600660056004600360026001,  # noqa: E501
                        1: 0x101010101010101010101010101016101005260206000600039604060206020,  # noqa: E501
                        2: 0x3960005160005560205160015560405160025500000000000000000000000000,  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "60006000600060006004356110000162fffffff400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000002",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex(
                        "6040600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "6001600003600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex(
                        "611000600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "6010600f600e600d600c600b600a60096008600760066005600460036002600101010101010101010101010101010161010052602060006000396040602060203960005160005560205160015560405160025500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "3860ff5560ff5460006000396160a76000556160a76001556160a760025560005160005560205160015560405160025560605160035560805160045560a0516005550061deadff60ff546000f360aa60bb60cc60dd60ee60fff400"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={
                        0: 0x6110006000600039600051600055602051600155000000000000000000000000  # noqa: E501
                    },
                    code=bytes.fromhex(
                        "60006000600060006004356110000162fffffff400"
                    ),
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex(
                        "6040600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "6001600003600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex(
                        "611000600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "6010600f600e600d600c600b600a60096008600760066005600460036002600101010101010101010101010101010161010052602060006000396040602060203960005160005560205160015560405160025500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "3860ff5560ff5460006000396160a76000556160a76001556160a760025560005160005560205160015560405160025560605160035560805160045560a0516005550061deadff60ff546000f360aa60bb60cc60dd60ee60fff400"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    code=bytes.fromhex(
                        "60006000600060006004356110000162fffffff400"
                    )
                ),
            },
        ),
        (
            "693c61390000000000000000000000000000000000000000000000000000000000000004",  # noqa: E501
            {
                Address("0x0000000000000000000000000000000000001000"): Account(
                    code=bytes.fromhex(
                        "6040600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001001"): Account(
                    code=bytes.fromhex(
                        "6001600003600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001002"): Account(
                    code=bytes.fromhex(
                        "611000600060003960005160005560205160015500"
                    )
                ),
                Address("0x0000000000000000000000000000000000001003"): Account(
                    code=bytes.fromhex(
                        "6010600f600e600d600c600b600a60096008600760066005600460036002600101010101010101010101010101010161010052602060006000396040602060203960005160005560205160015560405160025500"  # noqa: E501
                    )
                ),
                Address("0x0000000000000000000000000000000000001004"): Account(
                    code=bytes.fromhex(
                        "3860ff5560ff5460006000396160a76000556160a76001556160a760025560005160005560205160015560405160025560605160035560805160045560a0516005550061deadff60ff546000f360aa60bb60cc60dd60ee60fff400"  # noqa: E501
                    )
                ),
                Address("0xcccccccccccccccccccccccccccccccccccccccc"): Account(
                    storage={
                        0: 0x3860FF5560FF5460006000396160A76000556160A76001556160A76002556000,  # noqa: E501
                        1: 0x5160005560205160015560405160025560605160035560805160045560A05160,  # noqa: E501
                        2: 0x5550061DEADFF60FF546000F360AA60BB60CC60DD60EE60FFF4000000000000,  # noqa: E501
                        255: 91,
                    },
                    code=bytes.fromhex(
                        "60006000600060006004356110000162fffffff400"
                    ),
                ),
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3", "case4"],
)
@pytest.mark.pre_alloc_mutable
def test_codecopy(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Ori Pomerantz qbzzt1@gmail.com."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
    contract = Address("0xcccccccccccccccccccccccccccccccccccccccc")
    callee = Address("0x0000000000000000000000000000000000001000")
    callee_1 = Address("0x0000000000000000000000000000000000001001")
    callee_2 = Address("0x0000000000000000000000000000000000001002")
    callee_3 = Address("0x0000000000000000000000000000000000001003")
    callee_4 = Address("0x0000000000000000000000000000000000001004")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=100000000,
    )

    pre[callee] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("6040600060003960005160005560205160015500"),
    )
    pre[callee_1] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("6001600003600060003960005160005560205160015500"),
    )
    pre[callee_2] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("611000600060003960005160005560205160015500"),
    )
    pre[callee_3] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "6010600f600e600d600c600b600a60096008600760066005600460036002600101010101"  # noqa: E501
            "010101010101010101010161010052602060006000396040602060203960005160005560"  # noqa: E501
            "205160015560405160025500"
        ),
    )
    pre[callee_4] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex(
            "3860ff5560ff5460006000396160a76000556160a76001556160a7600255600051600055"  # noqa: E501
            "60205160015560405160025560605160035560805160045560a0516005550061deadff60"  # noqa: E501
            "ff546000f360aa60bb60cc60dd60ee60fff400"
        ),
    )
    pre[sender] = Account(balance=0xBA1A9CE0BA1A9CE, nonce=0)
    pre[contract] = Account(
        balance=0xBA1A9CE0BA1A9CE,
        nonce=0,
        code=bytes.fromhex("60006000600060006004356110000162fffffff400"),
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8"  # noqa: E501
        ),
        to=contract,
        data=tx_data,
        gas_limit=16777216,
        gas_price=10,
        nonce=0,
        value=1,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
