"""
This test checks that the returndata buffer is changed when a subcall REVERTs.  In each test case, a non-empty returndata buffer is set up, and then calls into a contract that REVERTs.

Ported from:
tests/static/state_tests/stRevertTest/RevertOpcodeInCallsOnNonEmptyReturnDataFiller.json
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
from execution_testing.vm import Op

REFERENCE_SPEC_GIT_PATH = "N/A"
REFERENCE_SPEC_VERSION = "N/A"


@pytest.mark.ported_from(
    ["tests/static/state_tests/stRevertTest/RevertOpcodeInCallsOnNonEmptyReturnDataFiller.json"],
)
@pytest.mark.valid_from("Prague")
@pytest.mark.parametrize(
    "tx_data_hex, tx_gas_limit, expected_post",
    [
        ("000000000000000000000000e73611b5b479b30c93ac377aeb3bfb199764f3c3", 860000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(storage={2: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
        ("000000000000000000000000e73611b5b479b30c93ac377aeb3bfb199764f3c3", 28000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 255}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
        ("000000000000000000000000c9da6cd8413f64323f12cd44c99671f280f15e1c", 860000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(storage={2: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
        ("000000000000000000000000c9da6cd8413f64323f12cd44c99671f280f15e1c", 28000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 255}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
        ("000000000000000000000000f20ccaf271beaa36e7cf4c9ced2867fac9558f14", 860000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(storage={2: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
        ("000000000000000000000000f20ccaf271beaa36e7cf4c9ced2867fac9558f14", 28000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 255}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
        ("0000000000000000000000006bacdfa8216dbb2a09819f8739e57ae3574c9fff", 860000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(storage={0: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(storage={5: 1}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
        ("0000000000000000000000006bacdfa8216dbb2a09819f8739e57ae3574c9fff", 28000, {Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01"): Account(code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP), Address("0x172a8f572404293aa810685dfdc6f740c300cc4b"): Account(storage={10: 255}, code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.STOP), Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b"): Account(code=Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1) + Op.SSTORE(key=0x3, value=0xd) + Op.STOP), Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP), Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14"): Account(code=Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0)) + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP)}),
    ],
    ids=['case0', 'case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7'],
)
@pytest.mark.pre_alloc_mutable
def test_revert_opcode_in_calls_on_non_empty_return_data(
    state_test: StateTestFiller,
    pre: Alloc,
    tx_data_hex: str,
    tx_gas_limit: int,
    expected_post: dict,
) -> None:
    """This test checks that the returndata buffer is changed when a subcall REVERTs.  In each test case, a non-empty returndata buffer is set up, and then calls into a contract that REVERTs.."""
    coinbase = Address("0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba")
    sender = Address("0xfaa10b404ab607779993c016cd5da73ae1f29d7e")
    contract = Address("0x172a8f572404293aa810685dfdc6f740c300cc4b")
    callee = Address("0x127eaf7e31d691a8393b7a2f84a6e94372190c01")
    callee_1 = Address("0x6bacdfa8216dbb2a09819f8739e57ae3574c9fff")
    callee_2 = Address("0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b")
    callee_3 = Address("0xc9da6cd8413f64323f12cd44c99671f280f15e1c")
    callee_4 = Address("0xe73611b5b479b30c93ac377aeb3bfb199764f3c3")
    callee_5 = Address("0xea519c47889074e6378b0d83747f2c3ea0b9cbc9")
    callee_6 = Address("0xf20ccaf271beaa36e7cf4c9ced2867fac9558f14")

    env = Environment(
        fee_recipient=coinbase,
        number=1,
        timestamp=1000,
        prev_randao=0x20000,
        base_fee_per_gas=10,
        gas_limit=10000000,
    )

    pre[callee] = Account(
        balance=1,
        nonce=0,
        code=Op.MSTORE(offset=0x1, value=0xc) + Op.RETURN(offset=0x0, size=0x40) + Op.STOP,
    )
    pre[contract] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0xa, value=Op.CALL(gas=0x3f7a0, address=Op.CALLDATALOAD(offset=0x0), value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.STOP
    ),
        storage={0xa: 0xff},
    )
    pre[callee_1] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x0, value=Op.CALL(gas=0x186a0, address=0xea519c47889074e6378b0d83747f2c3ea0b9cbc9, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP
    ),
    )
    pre[callee_2] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.SSTORE(key=0x1, value=0xc) + Op.REVERT(offset=0x0, size=0x1)
        + Op.SSTORE(key=0x3, value=0xd) + Op.STOP
    ),
    )
    pre[callee_3] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x0, value=Op.CALLCODE(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP
    ),
    )
    pre[callee_4] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x0, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP
    ),
    )
    pre[callee_5] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x4, value=Op.CALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x5, value=Op.RETURNDATASIZE) + Op.STOP
    ),
    )
    pre[callee_6] = Account(
        balance=1,
        nonce=0,
        code=(
        Op.POP(Op.CALL(gas=0x0, address=0x127eaf7e31d691a8393b7a2f84a6e94372190c01, value=0x0, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x0, value=Op.DELEGATECALL(gas=0xc350, address=0x93a599bde9a3b6390afdb06952aa5ec0b8c44f3b, args_offset=0x0, args_size=0x0, ret_offset=0x0, ret_size=0x0))
        + Op.SSTORE(key=0x2, value=Op.RETURNDATASIZE) + Op.STOP
    ),
    )
    pre[sender] = Account(balance=0xe8d4a51000, nonce=0)

    tx_data = bytes.fromhex(tx_data_hex) if tx_data_hex else b""

    tx = Transaction(
        secret_key=Hash(
            "0x4f31b3206fbf0e0e598b9b1a7d8ac86302a0ff1d8930738f1bebae9b67173e52"
        ),
        to=contract,
        data=tx_data,
        gas_limit=tx_gas_limit,
        gas_price=10,
        nonce=0,
        value=0,
    )

    post = expected_post

    state_test(env=env, pre=pre, post=post, tx=tx)
