# Amsterdam Static Test Failures (EIP-8037 branch)

**Branch:** `test-eip8037` (commit `3bc3d8018`)
**Command:** `uv run fill tests/static --fork Amsterdam --fill-static-tests -n 12 --clean -m 'blockchain_test and not slow' --output=fixtures_static`
**Total failures:** 1475
**Unique filler files:** 698
**Test directories affected:** 47

## Root Cause Analysis

All 1475 failures are **post-state mismatches** — the expected storage/balance values
(from `>=Cancun` expect sections) don't match the actual t8n output because Amsterdam
introduces breaking gas cost changes via **EIP-8037**.

### Breaking EIPs

#### EIP-8037: Two-Dimensional Gas Metering (State Gas)

The primary breaking change. Introduces `state_gas` as a separate gas dimension
charged for state-growing operations. The `cost_per_state_byte` (cpsb) is derived
from the block gas limit: **cpsb = 1174** at the default 120M block gas limit.

**Changed gas costs (Osaka -> Amsterdam):**

| Gas Constant | Osaka | Amsterdam | Delta | Affected Operations |
|-------------|-------|-----------|-------|-------------------|
| `G_STORAGE_SET` | 20,000 | 40,468 | +102% | SSTORE (0 -> nonzero) |
| `G_NEW_ACCOUNT` | 25,000 | 131,488 | +426% | CALL to new account, SELFDESTRUCT beneficiary |
| `G_CREATE` | 32,000 | 140,488 | +339% | CREATE, CREATE2 |
| `G_TRANSACTION_CREATE` | 32,000 | 140,488 | +339% | Contract creation transactions (intrinsic) |
| `G_AUTHORIZATION` | 25,000 | 165,990 | +564% | EIP-7702 authorization list entries |
| `R_AUTHORIZATION_EXISTING_AUTHORITY` | 12,500 | 131,488 | +952% | Refund for existing authority |

**State gas parameters:**
- `cost_per_state_byte`: 1174 (at 120M block gas limit)
- `STATE_BYTES_PER_STORAGE_SET`: 32
- `STATE_BYTES_PER_NEW_ACCOUNT`: 112
- `STATE_BYTES_PER_AUTH_BASE`: 23
- Intrinsic state gas (contract creation): 131,488
- Intrinsic state gas (per authorization): 158,490

**How EIP-8037 breaks tests:**
- State gas is deducted from `state_gas_reservoir` first, then from `gas_left`
- `gas_left` is capped at `TX_MAX_GAS_LIMIT - intrinsic_regular_gas` (EIP-7825)
- Excess execution gas goes to `state_gas_reservoir`
- Since most failing tests have gas_limit <= 16M and low intrinsic state gas,
  the reservoir is 0 and state gas costs eat into `gas_left` directly
- This reduces available execution gas, changing call depths, storage outcomes,
  and whether operations OOG

#### EIP-7825: Transaction Gas Limit Cap (inherited from Osaka)

Caps transaction gas at `TX_MAX_GAS_LIMIT = 16,777,216` (2^24). Already present in
Osaka, but interacts with EIP-8037's gas splitting. Not directly causing failures
here (all test gas limits are <= 16M).

### Failure Breakdown by EIP-8037 Mechanism

| Mechanism | Files | Description |
|-----------|-------|-------------|
| Changed `gas_left` available | 541 | State gas costs reduce available execution gas, changing outcomes |
| CREATE/CREATE2 cost increase | 133 | `G_CREATE` jumped from 32K to 140K, creation often OOGs |
| SSTORE cost increase | 24 | `G_STORAGE_SET` doubled, storage writes consume more gas |

### Failure Context

- **Gas limits above TX_MAX_GAS_LIMIT (16M):** 0 of 789 gas limit values
- **All gas limits are at or below 16M** — this is NOT a gas cap issue
- **Network constraints:** 695 files use `>=Cancun`, 2 use `>=Osaka`
- **Transaction types:** 692 legacy, 6 EIP-1559/4844
- **Contract creation transactions:** 57 files

## Fix Plan

### Approach: Prepend Amsterdam-specific expect sections to filler files

The existing `>=Cancun` expect sections remain **untouched**. New `>=Amsterdam` expect
sections are **prepended** (inserted before existing expects) so the test runner's
first-match ordering works:

- **Amsterdam** → matches new `>=Amsterdam` section first, uses Amsterdam-correct post-state
- **Cancun/Prague/Osaka** → skips `>=Amsterdam`, matches existing `>=Cancun` as before

No existing test behavior changes. Amsterdam gets its own correct expectations.

### Steps

1. **Capture actual Amsterdam post-states**: For each failing test variant, run t8n for
   Amsterdam to get the actual post-state (storage, balances, nonces, code)
2. **Build `>=Amsterdam` expect sections**: Group results by (filler_file, indexes) and
   construct expect entries matching the filler format
3. **Prepend to each filler**: Insert the new expect sections before existing ones
4. **Verify**: Re-run `fill tests/static --fork Amsterdam` — all 1475 should pass

## Summary by Directory

| Directory | Failures | Files |
|-----------|----------|-------|
| `stStackTests` | 209 | 9 |
| `stRandom` | 200 | 200 |
| `stRandom2` | 134 | 134 |
| `stZeroKnowledge` | 134 | 4 |
| `stEIP2930` | 122 | 6 |
| `stSStoreTest` | 89 | 23 |
| `stPreCompiledContracts` | 57 | 1 |
| `stCreate2` | 55 | 19 |
| `stCreateTest` | 49 | 18 |
| `stMemoryTest` | 43 | 42 |
| `stStaticCall` | 41 | 26 |
| `stRevertTest` | 34 | 11 |
| `stExample` | 32 | 6 |
| `stEIP150singleCodeGasPrices` | 28 | 28 |
| `stCallCreateCallCodeTest` | 21 | 16 |
| `stEIP1559` | 20 | 2 |
| `stReturnDataTest` | 20 | 10 |
| `stInitCodeTest` | 16 | 11 |
| `stZeroCallsRevert` | 16 | 16 |
| `Cancun` | 13 | 5 |
| `stSystemOperationsTest` | 13 | 8 |
| `stPreCompiledContracts2` | 12 | 5 |
| `stNonZeroCallsTest` | 10 | 10 |
| `stCallCodes` | 9 | 9 |
| `stEIP3607` | 9 | 2 |
| `stExtCodeHash` | 8 | 3 |
| `stCallDelegateCodesHomestead` | 7 | 7 |
| `stEIP150Specific` | 7 | 7 |
| `stCallDelegateCodesCallCodeHomestead` | 7 | 7 |
| `stSelfBalance` | 7 | 5 |
| `stRefundTest` | 7 | 6 |
| `stDelegatecallTestHomestead` | 6 | 5 |
| `stTransactionTest` | 5 | 5 |
| `stBadOpcode` | 4 | 2 |
| `stMemExpandingEIP150Calls` | 4 | 4 |
| `stSolidityTest` | 4 | 4 |
| `stSpecialTest` | 4 | 4 |
| `Shanghai` | 3 | 3 |
| `stMemoryStressTest` | 3 | 2 |
| `stTransitionTest` | 3 | 3 |
| `stChainId` | 2 | 2 |
| `stCodeCopyTest` | 2 | 2 |
| `stQuadraticComplexityTest` | 2 | 2 |
| `VMTests` | 1 | 1 |
| `stAttackTest` | 1 | 1 |
| `stEIP158Specific` | 1 | 1 |
| `stSLoadTest` | 1 | 1 |

## All Failures (by directory)

### `stStackTests` (209 failures)

- `shallowStack` (81 variants) — gas_limit=[300000] net=[>=Cancun] [CREATE] env_gas=42949672960
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d16]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d17]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d18]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d19]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d20]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d21]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d22]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d23]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d26]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d30]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d31]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d32]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d33]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d34]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d35]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d36]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d37]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d38]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d39]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d40]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d41]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d42]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d43]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d44]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d45]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d46]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d47]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d48]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d49]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d50]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d51]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d52]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d53]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d54]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d55]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d56]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d57]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d58]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d59]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d60]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d61]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d62]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d63]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d64]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d65]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d66]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d67]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d68]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d69]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d70]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d71]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d72]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d73]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d74]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d75]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d76]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d77]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d78]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d79]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d80]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9]`
- `stackOverflowDUP` (16 variants) — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9]`
- `stackOverflow` (16 variants) — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9]`
- `stackOverflowM1DUP` (16 variants) — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9]`
- `stackOverflowM1` (16 variants) — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9]`
- `stackOverflowM1PUSH` (31 variants) — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d16]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d17]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d18]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d19]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d20]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d21]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d22]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d23]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d26]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d30]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9]`
- `stackOverflowPUSH` (31 variants) — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d16]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d17]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d18]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d19]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d20]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d21]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d22]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d23]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d26]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d30]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9]`
- `stackOverflowSWAP[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960
- `stacksanitySWAP[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[6000000] net=[>=Cancun] [CREATE] env_gas=42949672960

### `stRandom` (200 failures)

- `randomStatetest100[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest102[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest104[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest105[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest106[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest107[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest110[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest112[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest114[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest115[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[3202574] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest116[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest117[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest118[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest119[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest11[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest120[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest121[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest122[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest124[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest129[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest12[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest130[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest131[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest137[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest138[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest139[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest142[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest143[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest145[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest147[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest148[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest14[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest153[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest155[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest156[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest158[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest15[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest161[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest162[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest164[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest166[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest167[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest169[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest173[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest174[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest175[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest179[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest17[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest180[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest183[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest184[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=69449279085
- `randomStatetest187[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest188[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest191[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest192[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest194[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest195[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest196[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest198[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest199[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest19[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest200[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest201[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest202[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest204[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest206[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest207[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest208[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest210[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest212[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest214[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest215[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest216[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest217[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest219[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest220[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest221[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest222[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest225[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest227[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest228[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest22[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest231[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest232[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest236[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest237[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest238[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest23[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest242[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest243[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest244[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest245[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest246[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest247[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest248[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest249[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest254[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest259[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest264[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest267[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest268[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest269[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest26[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest270[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest273[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest276[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest278[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest279[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest27[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest280[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest281[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest283[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest28[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest290[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest291[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest293[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest297[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest298[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest299[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest29[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest301[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest305[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest30[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest310[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest311[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest315[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest316[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest318[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest322[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest325[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest329[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest332[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest333[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest334[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest337[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest338[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest339[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest342[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest343[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest348[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest349[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest351[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest354[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest356[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest358[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest360[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest361[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest362[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest363[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest364[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest365[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest366[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest367[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest368[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest369[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest371[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest372[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest376[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest379[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest37[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest380[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest381[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest382[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest383[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest39[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest3[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest41[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest43[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest47[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest49[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest52[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest58[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest59[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest60[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest62[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest63[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest64[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest66[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest67[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest69[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest6[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest73[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest74[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest75[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest77[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest80[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest81[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest83[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest85[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest87[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest88[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest89[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest90[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest92[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest95[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest96[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest98[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest9[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807

### `stRandom2` (134 failures)

- `randomStatetest384[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest385[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest386[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest388[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest389[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest395[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest398[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest399[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest402[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest405[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest406[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest407[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest408[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest409[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest411[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest412[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest413[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest416[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest419[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest421[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest424[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest425[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest426[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest429[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest430[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest435[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest436[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest437[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest438[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest439[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest440[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest442[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest446[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest447[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest450[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest451[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest452[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest455[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest457[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest460[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest461[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest462[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest464[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest465[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest466[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[14265563] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest470[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest471[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest473[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest474[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest475[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest477[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest480[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest482[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest483[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest487[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest488[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest489[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest491[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest493[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest495[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest497[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest500[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest501[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest502[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest503[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest505[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest506[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest511[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest512[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest514[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest516[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest517[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest518[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest519[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest520[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest521[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest526[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest532[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest533[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest534[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest535[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest537[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest539[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest541[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest542[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest544[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest545[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest546[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest548[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest550[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest552[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest553[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest555[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest556[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest559[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest564[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest565[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest571[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest574[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest577[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest578[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest580[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest581[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest584[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest585[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest586[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest587[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest588[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest592[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest596[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest599[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest600[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest602[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest603[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest605[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest607[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest608[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest610[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest612[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest615[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest616[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest620[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest621[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest627[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest628[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest629[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest630[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest633[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest635[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest637[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest638[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest641[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `randomStatetest643[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[9840869] net=[>=Cancun] [CREATE] env_gas=35761922600709271
- `randomStatetest[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807

### `stZeroKnowledge` (134 failures)

- `pointAdd` (6 variants) — gas_limit=[1000000, 110000, 150000, 70000] net=[>=Cancun] env_gas=4012015
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9-g3]`
- `pointAddTrunc` (6 variants) — gas_limit=[1000000, 110000, 200000, 80000] net=[>=Cancun] env_gas=4012015
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9-g3]`
- `pointMulAdd2` (98 variants) — gas_limit=[2000000, 90000, 110000, 150000] net=[>=Cancun] env_gas=4012015
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d10-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d11-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d12-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d13-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d14-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d15-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d16-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d16-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d16-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d17-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d17-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d18-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d18-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d18-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d19-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d19-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d19-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d20-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d20-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d20-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d21-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d21-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d22-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d22-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d22-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d23-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d23-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d23-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d26-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d26-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d30-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d30-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d31-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d31-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d31-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d32-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d32-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d32-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d33-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d33-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d33-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d34-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d34-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d35-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d35-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d35-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d36-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d36-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d36-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d37-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d37-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d37-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9-g2]`
- `pointMulAdd` (24 variants) — gas_limit=[2000000, 90000, 110000, 192000] net=[>=Cancun] env_gas=4012015
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g2]`

### `stEIP2930` (122 failures)

- `addressOpcodes` (48 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid-6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid-7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid-8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-invalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-16]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-17]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-18]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-19]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-20]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-21]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-22]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-23]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-24]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-25]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-26]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-27]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-28]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-29]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-30]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-31]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-32]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-33]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-34]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-35]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-36]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-37]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-38]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-39]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-40]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid-9]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-valid]`
- `coinbaseT01` (3 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-T0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-T1baseInList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-T1baseNotInList]`
- `coinbaseT2` (2 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-T2baseInList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-T2baseNotInList]`
- `manualCreate` (3 variants) — gas_limit=[400000] net=[>=Cancun] [CREATE] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-addrGoodCellBad]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-allBad]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-allGood]`
- `storageCosts` (36 variants) — gas_limit=[400000] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyDel]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyNOP0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyNOP]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyRead]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyRead_postSLOAD]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyRead_postSSTORE]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyUpdate]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyWrite-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyWrite]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyWrite_postSLOAD]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyWrite_postSSTORE]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-declaredTo]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyDel-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyDel-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyDel]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyNOP-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyNOP-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyNOP0-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyNOP0-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyNOP0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyNOP]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyRead-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyRead-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyRead]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyRead_postSLOAD]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyRead_postSSTORE]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyUpdate-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyUpdate-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyUpdate]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyWrite-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyWrite-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyWrite]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyWrite_postSLOAD]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredKeyWrite_postSSTORE]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredTo-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-undeclaredTo]`
- `variedContext` (30 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-callCalleeInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callCallerInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callCreate2edInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callCreate2edValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callCreatedInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callCreatedValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callReadSuicideInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callReadSuicideValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callRevertCalleeInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callRevertCallerInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callTwiceInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callTwiceValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callWriteSuicideInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callWriteSuicideValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callcodeCalleeInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-callcodeCallerInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2AndCallInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2AndCallValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2Invalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2Valid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-createAndCallInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-createAndCallValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-createInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-createValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-delegateCalleeInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-delegateCallerInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-recurseInvalid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-recurseValid]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-staticcallCalleeInAccessList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-staticcallCallerInAccessList]`

### `stSStoreTest` (89 failures)

- `sstoreGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[16777216] net=[>=Cancun] env_gas=100000000
- `sstore_0to0` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0to0to0` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0to0toX` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toX` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXto0` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXto0toX` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXtoX` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXtoY` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0` (4 variants) — gas_limit=[3000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0to0` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0toX` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0toXto0` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0toY` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoX` (4 variants) — gas_limit=[3000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoXto0` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoXtoX` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoXtoY` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoY` (4 variants) — gas_limit=[3000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYto0` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYtoX` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYtoY` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYtoZ` (4 variants) — gas_limit=[1000000, 400000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`

### `stPreCompiledContracts` (57 failures)

- `precompsEIP2929Cancun` (57 variants) — gas_limit=[16777216] net=[>=Cancun, >=Prague, Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-all-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all-6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-16]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-17]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-18]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-19]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-20]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-21]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague-9]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-all_then_yes_from_prague]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-11]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-14]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-16]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-17]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-18]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-19]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-20]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-21]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-22]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-23]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new-9]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-new]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-yes-12]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-yes-13]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-yes-26]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-yes-27]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-yes-28]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-yes-41]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-yes-42]`

### `stCreate2` (55 failures)

- `CREATE2_FirstByte_loop[fork_Amsterdam-blockchain_test_from_state_test-firstHalf]` — gas_limit=[16777216] net=[>=Cancun] env_gas=89128960
- `Create2OOGFromCallRefunds` (8 variants) — gas_limit=[400000] net=[>=Cancun] env_gas=4294967296
  - `[fork_Amsterdam-blockchain_test_from_state_test-LogOp_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_CallCode_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Call_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create2_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_DelegateCall_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SelfDestruct_Refund_NoOoG]`
- `Create2OOGafterInitCodeReturndata2[fork_Amsterdam-blockchain_test_from_state_test--g0]` — gas_limit=[54000, 95000] net=[>=Cancun] env_gas=10000000
- `CreateMessageReverted[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[80000, 150000] net=[>=Cancun] env_gas=1000000000000
- `CreateMessageRevertedOOGInInit2` (2 variants) — gas_limit=[110000, 150000] net=[>=Cancun] [CREATE] env_gas=1000000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `RevertDepthCreate2OOGBerlin` (6 variants) — gas_limit=[110000, 170000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertDepthCreate2OOG` (6 variants) — gas_limit=[110000, 170000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertDepthCreateAddressCollisionBerlin` (6 variants) — gas_limit=[110000, 170000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertDepthCreateAddressCollision` (6 variants) — gas_limit=[110000, 170000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertOpcodeCreate[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[460000, 70000] net=[>=Cancun] env_gas=10000000
- `RevertOpcodeInCreateReturnsCreate2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=47244640256
- `call_outsize_then_create2_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=47244640256
- `call_then_create2_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=47244640256
- `create2SmartInitCode` (2 variants) — gas_limit=[400000] net=[>=Cancun] env_gas=47244640256
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `create2callPrecompiles` (8 variants) — gas_limit=[15000000] net=[>=Cancun] [CREATE] env_gas=1000000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
- `returndatacopy_0_0_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=47244640256
- `returndatacopy_afterFailing_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=47244640256
- `returndatacopy_following_revert_in_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=47244640256
- `returndatasize_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=47244640256

### `stCreateTest` (49 failures)

- `CREATE_EContractCreateNEContractInInitOOG_Tr[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[160000, 60000] net=[>=Cancun] [CREATE] env_gas=10000000
- `CREATE_EContract_ThenCALLToNonExistentAcc[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CREATE_EmptyContractAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CREATE_EmptyContractAndCallIt_1wei[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CREATE_EmptyContract[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CREATE_EmptyContractWithBalance[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CREATE_EmptyContractWithStorageAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CREATE_EmptyContractWithStorageAndCallIt_1wei[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CREATE_EmptyContractWithStorage[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CodeInConstructor` (2 variants) — gas_limit=[9437184] net=[>=Cancun] env_gas=4294967296
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `CreateAddressWarmAfterFail` (16 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=3000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-0xef-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-code-too-big-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-contructor-revert-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-high-nonce-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-high-nonce-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-invalid-opcode-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-ok-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-oog-constructor-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create-oog-post-constr-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2-0xef-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2-code-too-big-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2-contructor-revert-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2-invalid-opcode-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2-ok-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2-oog-constructor-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-create2-oog-post-constr-v1]`
- `CreateCollisionResults` (2 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=4294967296
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `CreateCollisionToEmpty2` (2 variants) — gas_limit=[600000, 54000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
- `CreateOOGFromCallRefunds` (8 variants) — gas_limit=[400000] net=[>=Cancun] env_gas=4294967296
  - `[fork_Amsterdam-blockchain_test_from_state_test-LogOp_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create2_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SelfDestruct_Refund_NoOoG]`
- `CreateOOGafterInitCodeReturndata2[fork_Amsterdam-blockchain_test_from_state_test--g0]` — gas_limit=[54000, 95000] net=[>=Cancun] env_gas=10000000
- `CreateOOGafterInitCodeRevert2[fork_Amsterdam-blockchain_test_from_state_test-d1]` — gas_limit=[175000] net=[>=Cancun] env_gas=10000000
- `CreateResults` (6 variants) — gas_limit=[9437184] net=[>=Cancun] env_gas=4294967296
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
- `TransactionCollisionToEmpty2` (2 variants) — gas_limit=[600000, 54000] net=[>=Cancun] [CREATE] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1-v1]`

### `stMemoryTest` (43 failures)

- `calldatacopy_dejavu2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=52949672960
- `mem0b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem31b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb+1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb+31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb+32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb+33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb-1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb-31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb-32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb-33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte+1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte+31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte+32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte+33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte-1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte-31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte-32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte-33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem32kb_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem33b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb+1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb+31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb+32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb+33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb-1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb-31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb-32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb-33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte+1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte+31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte+32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte+33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte-1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte-31[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte-32[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte-33[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `mem64kb_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `oog` (2 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=100000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-16]`

### `stStaticCall` (41 failures)

- `static_ABAcalls3[fork_Amsterdam-blockchain_test_from_state_test-d0]` — gas_limit=[10000000] net=[>=Cancun] env_gas=1000000000
- `static_CREATE_EmptyContractAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `static_CREATE_EmptyContractWithStorageAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `static_Call1024OOG` (2 variants) — gas_limit=[15720826] net=[>=Cancun] env_gas=9223372036854775807
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `static_Call10` (2 variants) — gas_limit=[200000] net=[>=Cancun] env_gas=9223372036854775807
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `static_CallContractToCreateContractOOG[fork_Amsterdam-blockchain_test_from_state_test--v1]` — gas_limit=[100000] net=[>=Cancun] env_gas=100000000
- `static_CallContractToCreateContractWhichWouldCreateContractIfCalled[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[300000] net=[>=Cancun] env_gas=100000000
- `static_CallLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=9223372036854775807
- `static_CheckOpcodes5` (4 variants) — gas_limit=[50000, 335000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `static_RETURN_Bounds[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[15000000] net=[>=Cancun] env_gas=9223372036854775807
- `static_RETURN_BoundsOOG[fork_Amsterdam-blockchain_test_from_state_test-d1]` — gas_limit=[15000000] net=[>=Cancun] env_gas=9223372036854775807
- `static_ReturnTest2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[250000] net=[>=Cancun] env_gas=1000000000
- `static_callcallcodecall_ABCB_RECURSIVE2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `static_callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `static_callcallcodecallcode_ABCB_RECURSIVE2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `static_callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `static_callcode_checkPC[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[1100000] net=[>=Cancun] env_gas=3000000000
- `static_callcodecallcall_ABCB_RECURSIVE2` (2 variants) — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `static_callcodecallcallcode_ABCB_RECURSIVE2` (4 variants) — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-v1]`
- `static_callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `static_callcodecallcodecall_110_SuicideEnd2` (2 variants) — gas_limit=[3000000] net=[>=Cancun] env_gas=30000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcodecall_110_SuicideEnd` (2 variants) — gas_limit=[3000000] net=[>=Cancun] env_gas=30000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcodecall_ABCB_RECURSIVE2` (2 variants) — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `static_contractCreationMakeCallThatAskMoreGasThenTransactionProvided` (4 variants) — gas_limit=[96000] net=[>=Cancun] [CREATE] env_gas=100000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`

### `stRevertTest` (34 failures)

- `RevertDepth2` (2 variants) — gas_limit=[170685, 136685] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `RevertDepthCreateAddressCollision` (8 variants) — gas_limit=[110000, 160000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v1]`
- `RevertDepthCreateOOG` (6 variants) — gas_limit=[110000, 180000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertInCreateInInit_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] [CREATE] env_gas=42949672960
- `RevertOpcodeCalls` (4 variants) — gas_limit=[460000, 83622] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1]`
- `RevertOpcodeCreate[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[460000, 70000] net=[>=Cancun] env_gas=10000000
- `RevertOpcodeDirectCall[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[460000, 62912] net=[>=Cancun] env_gas=10000000
- `RevertOpcodeInCreateReturns[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=42949672960
- `RevertOpcodeMultipleSubCalls` (8 variants) — gas_limit=[800000, 126200, 160000, 50000] net=[>=Cancun] env_gas=10000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1-v1]`
- `RevertSubCallStorageOOG2[fork_Amsterdam-blockchain_test_from_state_test--g0-v0]` — gas_limit=[61500, 181000] net=[>=Cancun] env_gas=10000000
- `RevertSubCallStorageOOG[fork_Amsterdam-blockchain_test_from_state_test--g0-v0]` — gas_limit=[81000, 181000] net=[>=Cancun] env_gas=10000000

### `stExample` (32 failures)

- `add11[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=71794957647893862
- `add11_yml[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=71794957647893862
- `basefeeExample[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyWrite]` — gas_limit=[4000000] net=[>=Cancun] env_gas=68719476736
- `indexesOmitExample[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=71794957647893862
- `labelsExample` (4 variants) — gas_limit=[400000] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction3-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction3]`
- `rangesExample` (24 variants) — gas_limit=[400000, 1400000, 2400000] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g2-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g2-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g2-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g2-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g2-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g2-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1-g2-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1-g2-v1]`

### `stEIP150singleCodeGasPrices` (28 failures)

- `RawCallCodeGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallCodeGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallCodeGasMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallCodeGasMemory[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallCodeGasValueTransferAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallCodeGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallCodeGasValueTransferMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallCodeGasValueTransferMemory[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallGasValueTransferAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallGasValueTransferMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallGasValueTransferMemory[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallMemoryGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCallMemoryGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCreateFailGasValueTransfer2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCreateFailGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCreateGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCreateGasMemory[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCreateGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawCreateGasValueTransferMemory[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawDelegateCallGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawDelegateCallGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawDelegateCallGasMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `RawDelegateCallGasMemory[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[500000] net=[>=Cancun] env_gas=10000000
- `gasCostBerlin[fork_Amsterdam-blockchain_test_from_state_test-d40]` — gas_limit=[16777216] net=[>=Cancun] env_gas=100000000
- `gasCost[fork_Amsterdam-blockchain_test_from_state_test-d40]` — gas_limit=[16777216] net=[>=Cancun] env_gas=100000000

### `stCallCreateCallCodeTest` (21 failures)

- `Call1024OOG` (4 variants) — gas_limit=[13120826, 9320826, 15720826, 11220826] net=[>=Cancun] env_gas=9223372036854775807
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g3]`
- `CallLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=9223372036854775807
- `Callcode1024OOG` (2 variants) — gas_limit=[15720826, 13120826] net=[>=Cancun] env_gas=9223372036854775807
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `CallcodeLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test--g2]` — gas_limit=[166262, 156262, 170000] net=[>=Cancun] env_gas=9223372036854775807
- `callWithHighValueOOGinCall[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[3000000] net=[>=Cancun] env_gas=30000000
- `contractCreationMakeCallThatAskMoreGasThenTransactionProvided[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[96000, 60000] net=[>=Cancun] [CREATE] env_gas=10000000
- `createFailBalanceTooLow[fork_Amsterdam-blockchain_test_from_state_test--v0]` — gas_limit=[253021] net=[>=Cancun] env_gas=100000000
- `createInitFailBadJumpDestination2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[2200000] net=[>=Cancun] env_gas=1000000000
- `createInitFailBadJumpDestination[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[2200000] net=[>=Cancun] env_gas=1000000000
- `createInitFailStackSizeLargerThan1024[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[2200000] net=[>=Cancun] env_gas=1000000000
- `createInitFailStackUnderflow[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[2200000] net=[>=Cancun] env_gas=1000000000
- `createInitFailUndefinedInstruction2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[2200000] net=[>=Cancun] env_gas=1000000000
- `createInitFailUndefinedInstruction[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[900000] net=[>=Cancun] env_gas=1000000000
- `createNameRegistratorPerTxs[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[1250528] net=[>=Cancun] [CREATE] env_gas=10000000000
- `createNameRegistratorPerTxsNotEnoughGas` (2 variants) — gas_limit=[56157, 86157] net=[>=Cancun] [CREATE] env_gas=10000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `createNameRegistratorPreStore1NotEnoughGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[73071] net=[>=Cancun] env_gas=100000000

### `stEIP1559` (20 failures)

- `baseFeeDiffPlaces` (10 variants) — gas_limit=[1000000] net=[>=Osaka] env_gas=4503599627370496
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d26]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d30]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d31]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d32]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d33]`
- `gasPriceDiffPlaces` (10 variants) — gas_limit=[1000000] net=[>=Osaka] env_gas=4503599627370496
  - `[fork_Amsterdam-blockchain_test_from_state_test-d24]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d25]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d26]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d27]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d28]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d29]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d30]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d31]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d32]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d33]`

### `stReturnDataTest` (20 failures)

- `call_outsize_then_create_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `call_then_create_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `create_callprecompile_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `modexp_modsize0_returndatasize` (4 variants) — gas_limit=[10000000] net=[>=Cancun] env_gas=100000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
- `returndatacopy_0_0_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `returndatacopy_afterFailing_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `returndatacopy_following_revert_in_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `returndatasize_after_successful_callcode[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `returndatasize_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=111669149696
- `tooLongReturnDataCopy` (8 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=4503599627370496
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-9]`

### `stInitCodeTest` (16 failures)

- `CallContractToCreateContractAndCallItOOG[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[203000] net=[>=Cancun] env_gas=100000000
- `CallContractToCreateContractOOGBonusGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=1000000000
- `CallContractToCreateContractWhichWouldCreateContractIfCalled[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=1000000000
- `CallContractToCreateContractWhichWouldCreateContractInInitCode[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=1000000000
- `CallTheContractToCreateEmptyContract[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=100000000
- `OutOfGasContractCreation` (4 variants) — gas_limit=[56000, 150000] net=[>=Cancun] [CREATE] env_gas=100000000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
- `OutOfGasPrefundedContractCreation` (3 variants) — gas_limit=[154000, 65000, 95000] net=[>=Cancun] [CREATE] env_gas=1000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g2]`
- `ReturnTest2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[250000] net=[>=Cancun] env_gas=1000000000
- `StackUnderFlowContractCreation[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[72000] net=[>=Cancun] [CREATE] env_gas=1000000000000000
- `TransactionCreateRandomInitCode[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[64599] net=[>=Cancun] [CREATE] env_gas=10000000000
- `TransactionCreateSuicideInInitcode[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[155000] net=[>=Cancun] [CREATE] env_gas=100000000

### `stZeroCallsRevert` (16 failures)

- `ZeroValue_CALLCODE_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_CALLCODE_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_CALLCODE_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_CALLCODE_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_CALL_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_CALL_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_CALL_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_CALL_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_DELEGATECALL_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_DELEGATECALL_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_DELEGATECALL_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_DELEGATECALL_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[135000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_SUICIDE_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_SUICIDE_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[75000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_SUICIDE_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[75000] net=[>=Cancun] env_gas=10000000
- `ZeroValue_SUICIDE_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[75000] net=[>=Cancun] env_gas=10000000

### `Cancun` (13 failures)

- `10_revertUndoesStoreAfterReturn[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=4503599627370496
- `14_revertAfterNestedStaticcall[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=4503599627370496
- `17_tstoreGas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=4503599627370496
- `createBlobhashTx[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[4000000] net=[>=Cancun] [CREATE] env_gas=68719476736
- `MCOPY_copy_cost` (9 variants) — gas_limit=[100000, 55697] net=[>=Cancun] env_gas=1000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-src1_size44767-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src1_size44768-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src1_size44769-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src31_size44767-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src31_size44768-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src31_size44769-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src32_size44767-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src32_size44768-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-src32_size44769-g1]`

### `stSystemOperationsTest` (13 failures)

- `ABAcalls3[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[10000000] net=[>=Cancun] env_gas=100000000
- `Call10[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=9223372036854775807
- `CallRecursiveBomb3[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[1000000] net=[>=Cancun] env_gas=10000000
- `CallToNameRegistratorZeorSizeMemExpansion[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[500000, 50000] net=[>=Cancun] env_gas=10000000
- `callcodeToNameRegistratorZeroMemExpanion[fork_Amsterdam-blockchain_test_from_state_test--g0]` — gas_limit=[50000, 1000000] net=[>=Cancun] env_gas=10000000
- `doubleSelfdestructTest` (2 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=10000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-caller-self-destruct-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-caller-self-destruct]`
- `extcodecopy[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=1478962728
- `multiSelfdestruct` (5 variants) — gas_limit=[10000000] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`

### `stPreCompiledContracts2` (12 failures)

- `CallEcrecover_Overflow` (8 variants) — gas_limit=[100000] net=[>=Cancun] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-pass01]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-pass02]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-pass03]`
- `ecrecoverShortBuff[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[7400000] net=[>=Cancun] env_gas=71794957647893862
- `modexp_0_0_0_22000[fork_Amsterdam-blockchain_test_from_state_test--g0]` — gas_limit=[48136, 90000, 110000, 200000] net=[>=Cancun] env_gas=100000000
- `modexp_0_0_0_25000[fork_Amsterdam-blockchain_test_from_state_test--g0]` — gas_limit=[47040, 90000, 110000, 200000] net=[>=Cancun] env_gas=100000000
- `modexp_0_0_0_35000[fork_Amsterdam-blockchain_test_from_state_test--g0]` — gas_limit=[57040, 90000, 110000, 200000] net=[>=Cancun] env_gas=100000000

### `stNonZeroCallsTest` (10 failures)

- `NonZeroValue_CALLCODE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_CALLCODE_ToEmpty_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_CALLCODE_ToOneStorageKey_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_CALL[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_CALL_ToEmpty_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_CALL_ToOneStorageKey_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_DELEGATECALL[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_DELEGATECALL_ToEmpty_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_DELEGATECALL_ToNonNonZeroBalance[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NonZeroValue_DELEGATECALL_ToOneStorageKey_Paris[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000

### `stCallCodes` (9 failures)

- `callcallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcode_checkPC[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[1100000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000

### `stEIP3607` (9 failures)

- `initCollidingWithNonEmptyAccount` (5 variants) — gas_limit=[400000] net=[>=Cancun] [CREATE] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
- `transactionCollidingWithNonEmptyAccount_init_Paris` (4 variants) — gas_limit=[400000] net=[>=Cancun] [CREATE] env_gas=71794957647893862
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`

### `stExtCodeHash` (8 failures)

- `callToNonExistent` (4 variants) — gas_limit=[100000] net=[>=Cancun] env_gas=3000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
- `callToSuicideThenExtcodehash` (3 variants) — gas_limit=[300000] net=[>=Cancun] env_gas=3000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
- `createEmptyThenExtcodehash[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[300000] net=[>=Cancun] env_gas=47244640256

### `stCallDelegateCodesHomestead` (7 failures)

- `callcallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000

### `stEIP150Specific` (7 failures)

- `CallAskMoreGasOnDepth2ThenTransactionHas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CreateAndGasInsideCreate[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `DelegateCallOnEIP[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NewGasPriceForCodes[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `Transaction64Rule_d64e0[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[160062] net=[>=Cancun] env_gas=10000000
- `Transaction64Rule_d64m1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[160061] net=[>=Cancun] env_gas=10000000
- `Transaction64Rule_d64p1[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[160063] net=[>=Cancun] env_gas=10000000

### `stCallDelegateCodesCallCodeHomestead` (7 failures)

- `callcallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000
- `callcodecallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=3000000000

### `stSelfBalance` (7 failures)

- `selfBalanceCallTypes` (3 variants) — gas_limit=[1000000] net=[>=Cancun] env_gas=10000000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
- `selfBalanceEqualsBalance[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=10000000000
- `selfBalance[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=10000000000
- `selfBalanceGasCost[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=10000000000
- `selfBalanceUpdate[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=10000000000

### `stRefundTest` (7 failures)

- `refund50_2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=1000000
- `refund50percentCap[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=1000000
- `refund600[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=1000000
- `refundSuicide50procentCap` (2 variants) — gas_limit=[10000000] net=[>=Cancun] env_gas=100000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `refund_CallA[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=1000000
- `refund_TxToSuicide[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[61003] net=[>=Cancun] env_gas=10000000

### `stDelegatecallTestHomestead` (6 failures)

- `Call1024OOG` (2 variants) — gas_limit=[13120826, 15720826] net=[>=Cancun] env_gas=9223372036854775807
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `CallLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] env_gas=9223372036854775807
- `CallcodeLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test--g2]` — gas_limit=[166262, 156262, 600000] net=[>=Cancun] env_gas=9223372036854775807
- `Delegatecall1024OOG[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[15720826] net=[>=Cancun] env_gas=9223372036854775807
- `delegatecallOOGinCall[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[3000000] net=[>=Cancun] env_gas=30000000

### `stTransactionTest` (5 failures)

- `CreateMessageSuccess[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[131882] net=[>=Cancun] env_gas=1000000000000
- `CreateTransactionSuccess[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[70000] net=[>=Cancun] [CREATE] env_gas=1000000000000
- `InternalCallHittingGasLimit2[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[47766] net=[>=Cancun] env_gas=47766
- `StoreGasOnCreate[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[131882] net=[>=Cancun] env_gas=1000000
- `SuicidesAndInternalCallSuicidesOOG[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[50000] net=[>=Cancun] env_gas=1000000

### `stBadOpcode` (4 failures)

- `measureGas` (2 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=100000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE]`
- `operationDiffGas` (2 variants) — gas_limit=[16777216] net=[>=Cancun] env_gas=100000000
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE]`

### `stMemExpandingEIP150Calls` (4 failures)

- `CallAskMoreGasOnDepth2ThenTransactionHasWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `CallGoesOOGOnSecondLevelWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[220000] net=[>=Cancun] env_gas=10000000
- `CreateAndGasInsideCreateWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000
- `NewGasPriceForCodesWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000

### `stSolidityTest` (4 failures)

- `CallLowLevelCreatesSolidity[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[350000] net=[>=Cancun] env_gas=100000000
- `RecursiveCreateContractsCreate4Contracts[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[300000] net=[>=Cancun] env_gas=100000000
- `TestOverflow[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=9223372036854775807
- `TestStructuresAndVariabless[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[350000] net=[>=Cancun] env_gas=9223372036854775807

### `stSpecialTest` (4 failures)

- `FailedCreateRevertsDeletionParis[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] [CREATE] env_gas=43218108416
- `deploymentError[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[5000000] net=[>=Cancun] [CREATE] env_gas=314159200
- `makeMoney[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[228500] net=[>=Cancun] env_gas=1000000
- `selfdestructEIP2929[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[8000000] net=[>=Cancun] env_gas=10944489199640098

### `Shanghai` (3 failures)

- `push0Gas[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=89128960
- `create2InitCodeSizeLimit[fork_Amsterdam-blockchain_test_from_state_test-valid]` — gas_limit=[15000000] net=[>=Cancun] env_gas=20000000
- `createInitCodeSizeLimit[fork_Amsterdam-blockchain_test_from_state_test-valid]` — gas_limit=[15000000] net=[>=Cancun] env_gas=20000000

### `stMemoryStressTest` (3 failures)

- `RETURN_Bounds` (2 variants) — gas_limit=[150000, 500000, 15000000] net=[>=Cancun] env_gas=9223372036854775807
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g2]`
- `SSTORE_Bounds[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[150000, 16777216] net=[>=Cancun] env_gas=9223372036854775807

### `stTransitionTest` (3 failures)

- `createNameRegistratorPerTxsAfter[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] [CREATE] env_gas=10000000000
- `createNameRegistratorPerTxsAt[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] [CREATE] env_gas=10000000000
- `createNameRegistratorPerTxsBefore[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[200000] net=[>=Cancun] [CREATE] env_gas=10000000000

### `stChainId` (2 failures)

- `chainId[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=10000000000
- `chainIdGasCost[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=10000000000

### `stCodeCopyTest` (2 failures)

- `ExtCodeCopyTargetRangeLongerThanCodeTests[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807
- `ExtCodeCopyTestsParis[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[400000] net=[>=Cancun] env_gas=9223372036854775807

### `stQuadraticComplexityTest` (2 failures)

- `Call20KbytesContract50_1[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[150000, 12500000] net=[>=Cancun] env_gas=882500000000
- `Return50000[fork_Amsterdam-blockchain_test_from_state_test--g1]` — gas_limit=[150000, 16000000] net=[>=Cancun] env_gas=8825000000

### `VMTests` (1 failures)

- `twoOps[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[16777216] net=[>=Cancun] env_gas=100000000

### `stAttackTest` (1 failures)

- `CrashingTransaction[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[4657786] net=[>=Cancun] [CREATE] env_gas=4712388

### `stEIP158Specific` (1 failures)

- `EXP_Empty[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[600000] net=[>=Cancun] env_gas=10000000

### `stSLoadTest` (1 failures)

- `sloadGasCost[fork_Amsterdam-blockchain_test_from_state_test-]` — gas_limit=[100000] net=[>=Cancun] env_gas=10000000000
