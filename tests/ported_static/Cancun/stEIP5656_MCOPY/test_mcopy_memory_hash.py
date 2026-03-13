"""
Performs exact the same MCOPY twice and dumps the hash of all memory after...

Ported from:
tests/static/state_tests/Cancun/stEIP5656_MCOPY/MCOPY_memory_hashFiller.yml
"""

import pytest
from execution_testing import (
    EOA,
    Account,
    Address,
    Alloc,
    Environment,
    StateTestFiller,
    Transaction,
)
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    [
        "tests/static/state_tests/Cancun/stEIP5656_MCOPY/MCOPY_memory_hashFiller.yml",  # noqa: E501
    ],
)
@pytest.mark.valid_from("Cancun")
@pytest.mark.parametrize(
    "tx_data_hex, expected_post",
    [
        (
            "000000000000000000000000000000000000000000000000000000000000103000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001020",  # noqa: E501
            {
                Address("0xff4c22cd1d160fdc49c752dfb44b55d318d14113"): Account(
                    storage={
                        1: 0x6216FE67A1C972FC4BF45303AB3449E0E30C6964D2D458CB786233F9F2AFE595,  # noqa: E501
                        2: 0x6216FE67A1C972FC4BF45303AB3449E0E30C6964D2D458CB786233F9F2AFE595,  # noqa: E501
                    }
                )
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020",  # noqa: E501
            {
                Address("0xff4c22cd1d160fdc49c752dfb44b55d318d14113"): Account(
                    storage={
                        1: 0x1A75C0C32A7DC05E25E0F0280E8EE7456EDC0092A13A86ED7D20C8EDC87FCBA9,  # noqa: E501
                        2: 0x1A75C0C32A7DC05E25E0F0280E8EE7456EDC0092A13A86ED7D20C8EDC87FCBA9,  # noqa: E501
                    }
                )
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000102000000000000000000000000000000000000000000000000000000000000010100000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            {
                Address("0xff4c22cd1d160fdc49c752dfb44b55d318d14113"): Account(
                    storage={
                        1: 0x1A75C0C32A7DC05E25E0F0280E8EE7456EDC0092A13A86ED7D20C8EDC87FCBA9,  # noqa: E501
                        2: 0x1A75C0C32A7DC05E25E0F0280E8EE7456EDC0092A13A86ED7D20C8EDC87FCBA9,  # noqa: E501
                    }
                )
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000102000000000000000000000000000000000000000000000000000000000000010400000000000000000000000000000000000000000000000000000000000000010",  # noqa: E501
            {
                Address("0xff4c22cd1d160fdc49c752dfb44b55d318d14113"): Account(
                    storage={
                        1: 0x6A1CF6752C1B8DF514452C3004A65C46B1AFE7E52030E8100ADFB036C180172E,  # noqa: E501
                        2: 0x6A1CF6752C1B8DF514452C3004A65C46B1AFE7E52030E8100ADFB036C180172E,  # noqa: E501
                    }
                )
            },
        ),
        (
            "00000000000000000000000000000000000000000000000000000000000010200000000000000000000000000000000000000000000000000000000000001023000000000000000000000000000000000000000000000000000000000000001d",  # noqa: E501
            {
                Address("0xff4c22cd1d160fdc49c752dfb44b55d318d14113"): Account(
                    storage={
                        1: 0xF6A2C41AD18FF89FEEBF7B54A7BAC01E27EB1FB3C3AE8919E2FDB4B7C704CA70,  # noqa: E501
                        2: 0xDEDD31C55B058C4165CE1DAEC55B4811A781D716FC87E249A4C0B829196ACC2F,  # noqa: E501
                    }
                )
            },
        ),
        (
            "000000000000000000000000000000000000000000000000000000000000102100000000000000000000000000000000000000000000000000000000000010200000000000000000000000000000000000000000000000000000000000000123",  # noqa: E501
            {
                Address("0xff4c22cd1d160fdc49c752dfb44b55d318d14113"): Account(
                    storage={
                        1: 0xB04D651A3B0932C57CB624B7E0BBCC5BC5A546EC5805EBCA5B95CEC66F695DEF,  # noqa: E501
                        2: 0xC10DF02254713FAFE8ED614F51F5E8FA111578A060ECC8BB28E56F4ECE9A82EE,  # noqa: E501
                    }
                )
            },
        ),
    ],
    ids=["case0", "case1", "case2", "case3", "case4", "case5"],
)
@pytest.mark.pre_alloc_mutable
def test_mcopy_memory_hash(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    expected_post: dict,
) -> None:
    """Performs exact the same MCOPY twice and dumps the hash of all..."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = EOA(
        key=0xF79127A3004ABDE26A4CBD80C428CB10F829FA11B54D36E7B326F4F4A5927ACF
    )

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1687174231,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=1000000,
    )

    pre[sender] = Account(balance=0x3B9ACA00)
    # Source: Yul
    # {
    #   function mcopy(dst, src, size) { verbatim_3i_0o(hex"5e", dst, src, size) }  # noqa: E501
    #
    #   // Fill one word of memory at 0x1020 with the pattern of unique bytes.
    #   mstore(0x1020, 0xa0a1a2a3a4a5a6a7a8a9aAaBaCaDaEaFb0b1b2b3b4b5b6b7b8b9bAbBbCbDbEbF)  # noqa: E501
    #
    #   // MCOPY using parameters from CALLDATA.
    #   mcopy(calldataload(0), calldataload(32), calldataload(64))
    #
    #   // Dump the hash of full memory.
    #   sstore(1, keccak256(0, msize()))
    #
    #   // Do exact the same MCOPY once again.
    #   mcopy(calldataload(0), calldataload(32), calldataload(64))
    #
    #   // Dump the hash of full memory again.
    #   sstore(2, keccak256(0, msize()))
    # }
    contract = pre.deploy_contract(
        code=(
            Op.MSTORE(
                offset=0x1020,
                value=0xA0A1A2A3A4A5A6A7A8A9AAABACADAEAFB0B1B2B3B4B5B6B7B8B9BABBBCBDBEBF,  # noqa: E501
            )
            + Op.PUSH1[0x32]
            + Op.CALLDATALOAD(offset=0x40)
            + Op.CALLDATALOAD(offset=0x20)
            + Op.CALLDATALOAD(offset=Op.PUSH0)
            + Op.JUMP(pc=0x4E)
            + Op.JUMPDEST
            + Op.SSTORE(key=0x1, value=Op.SHA3(offset=Op.PUSH0, size=Op.MSIZE))
            + Op.PUSH1[0x46]
            + Op.CALLDATALOAD(offset=0x40)
            + Op.CALLDATALOAD(offset=0x20)
            + Op.CALLDATALOAD(offset=Op.PUSH0)
            + Op.JUMP(pc=0x4E)
            + Op.JUMPDEST
            + Op.SSTORE(key=0x2, value=Op.SHA3(offset=Op.PUSH0, size=Op.MSIZE))
            + Op.STOP
            + Op.JUMPDEST
            + Op.MCOPY
            + Op.JUMP
        ),
        address=Address("0xff4c22cd1d160fdc49c752dfb44b55d318d14113"),  # noqa: E501
    )

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        sender=sender,
        to=contract,
        data=tx_data,
        gas_limit=1000000,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
