# Amsterdam Static Test Failures (EIP-8037 branch)

**Total failures:** 1475
**Unique test files:** 698
**Test directories affected:** 47

## Summary by Directory

| Directory | Failures |
|-----------|----------|
| `stStackTests` | 209 |
| `stRandom` | 200 |
| `stRandom2` | 134 |
| `stZeroKnowledge` | 134 |
| `stEIP2930` | 122 |
| `stSStoreTest` | 89 |
| `stPreCompiledContracts` | 57 |
| `stCreate2` | 55 |
| `stCreateTest` | 49 |
| `stMemoryTest` | 43 |
| `stStaticCall` | 41 |
| `stRevertTest` | 34 |
| `stExample` | 32 |
| `stEIP150singleCodeGasPrices` | 28 |
| `stCallCreateCallCodeTest` | 21 |
| `stEIP1559` | 20 |
| `stReturnDataTest` | 20 |
| `stInitCodeTest` | 16 |
| `stZeroCallsRevert` | 16 |
| `Cancun` | 13 |
| `stSystemOperationsTest` | 13 |
| `stPreCompiledContracts2` | 12 |
| `stNonZeroCallsTest` | 10 |
| `stCallCodes` | 9 |
| `stEIP3607` | 9 |
| `stExtCodeHash` | 8 |
| `stCallDelegateCodesHomestead` | 7 |
| `stEIP150Specific` | 7 |
| `stCallDelegateCodesCallCodeHomestead` | 7 |
| `stSelfBalance` | 7 |
| `stRefundTest` | 7 |
| `stDelegatecallTestHomestead` | 6 |
| `stTransactionTest` | 5 |
| `stBadOpcode` | 4 |
| `stMemExpandingEIP150Calls` | 4 |
| `stSolidityTest` | 4 |
| `stSpecialTest` | 4 |
| `Shanghai` | 3 |
| `stMemoryStressTest` | 3 |
| `stTransitionTest` | 3 |
| `stChainId` | 2 |
| `stCodeCopyTest` | 2 |
| `stQuadraticComplexityTest` | 2 |
| `VMTests` | 1 |
| `stAttackTest` | 1 |
| `stEIP158Specific` | 1 |
| `stSLoadTest` | 1 |

## All Failures

### `stStackTests` (209 failures)

- `shallowStack` (81 variants)
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
- `stackOverflowDUP` (16 variants)
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
- `stackOverflow` (16 variants)
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
- `stackOverflowM1DUP` (16 variants)
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
- `stackOverflowM1` (16 variants)
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
- `stackOverflowM1PUSH` (31 variants)
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
- `stackOverflowPUSH` (31 variants)
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
- `stackOverflowSWAP[fork_Amsterdam-blockchain_test_from_state_test-]`
- `stacksanitySWAP[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stRandom` (200 failures)

- `randomStatetest100[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest102[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest104[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest105[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest106[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest107[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest110[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest112[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest114[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest115[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest116[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest117[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest118[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest119[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest11[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest120[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest121[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest122[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest124[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest129[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest12[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest130[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest131[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest137[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest138[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest139[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest142[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest143[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest145[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest147[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest148[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest14[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest153[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest155[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest156[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest158[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest15[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest161[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest162[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest164[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest166[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest167[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest169[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest173[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest174[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest175[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest179[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest17[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest180[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest183[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest184[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest187[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest188[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest191[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest192[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest194[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest195[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest196[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest198[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest199[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest19[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest200[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest201[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest202[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest204[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest206[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest207[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest208[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest210[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest212[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest214[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest215[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest216[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest217[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest219[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest220[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest221[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest222[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest225[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest227[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest228[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest22[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest231[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest232[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest236[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest237[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest238[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest23[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest242[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest243[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest244[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest245[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest246[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest247[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest248[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest249[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest254[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest259[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest264[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest267[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest268[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest269[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest26[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest270[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest273[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest276[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest278[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest279[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest27[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest280[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest281[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest283[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest28[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest290[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest291[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest293[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest297[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest298[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest299[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest29[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest301[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest305[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest30[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest310[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest311[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest315[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest316[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest318[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest322[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest325[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest329[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest332[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest333[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest334[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest337[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest338[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest339[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest342[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest343[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest348[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest349[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest351[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest354[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest356[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest358[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest360[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest361[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest362[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest363[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest364[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest365[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest366[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest367[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest368[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest369[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest371[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest372[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest376[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest379[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest37[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest380[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest381[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest382[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest383[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest39[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest3[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest41[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest43[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest47[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest49[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest52[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest58[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest59[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest60[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest62[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest63[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest64[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest66[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest67[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest69[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest6[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest73[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest74[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest75[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest77[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest80[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest81[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest83[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest85[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest87[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest88[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest89[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest90[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest92[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest95[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest96[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest98[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest9[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stRandom2` (134 failures)

- `randomStatetest384[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest385[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest386[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest388[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest389[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest395[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest398[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest399[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest402[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest405[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest406[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest407[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest408[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest409[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest411[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest412[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest413[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest416[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest419[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest421[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest424[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest425[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest426[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest429[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest430[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest435[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest436[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest437[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest438[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest439[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest440[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest442[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest446[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest447[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest450[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest451[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest452[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest455[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest457[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest460[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest461[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest462[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest464[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest465[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest466[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest470[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest471[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest473[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest474[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest475[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest477[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest480[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest482[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest483[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest487[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest488[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest489[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest491[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest493[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest495[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest497[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest500[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest501[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest502[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest503[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest505[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest506[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest511[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest512[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest514[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest516[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest517[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest518[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest519[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest520[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest521[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest526[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest532[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest533[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest534[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest535[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest537[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest539[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest541[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest542[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest544[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest545[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest546[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest548[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest550[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest552[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest553[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest555[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest556[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest559[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest564[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest565[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest571[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest574[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest577[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest578[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest580[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest581[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest584[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest585[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest586[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest587[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest588[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest592[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest596[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest599[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest600[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest602[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest603[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest605[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest607[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest608[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest610[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest612[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest615[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest616[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest620[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest621[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest627[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest628[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest629[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest630[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest633[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest635[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest637[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest638[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest641[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest643[fork_Amsterdam-blockchain_test_from_state_test-]`
- `randomStatetest[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stZeroKnowledge` (134 failures)

- `pointAdd` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9-g3]`
- `pointAddTrunc` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d8-g3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d9-g3]`
- `pointMulAdd2` (98 variants)
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
- `pointMulAdd` (24 variants)
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

- `addressOpcodes` (48 variants)
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
- `coinbaseT01` (3 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-T0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-T1baseInList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-T1baseNotInList]`
- `coinbaseT2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-T2baseInList]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-T2baseNotInList]`
- `manualCreate` (3 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-addrGoodCellBad]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-allBad]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-allGood]`
- `storageCosts` (36 variants)
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
- `variedContext` (30 variants)
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

- `sstoreGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `sstore_0to0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0to0to0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0to0toX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXto0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXto0toX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXtoX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_0toXtoY` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0to0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0toX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0toXto0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_Xto0toY` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoXto0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoXtoX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoXtoY` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoY` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYto0` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYtoX` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYtoY` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`
- `sstore_XtoYtoZ` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4-g1]`

### `stPreCompiledContracts` (57 failures)

- `precompsEIP2929Cancun` (57 variants)
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

- `CREATE2_FirstByte_loop[fork_Amsterdam-blockchain_test_from_state_test-firstHalf]`
- `Create2OOGFromCallRefunds` (8 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-LogOp_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_CallCode_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Call_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create2_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_DelegateCall_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SelfDestruct_Refund_NoOoG]`
- `Create2OOGafterInitCodeReturndata2[fork_Amsterdam-blockchain_test_from_state_test--g0]`
- `CreateMessageReverted[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `CreateMessageRevertedOOGInInit2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `RevertDepthCreate2OOGBerlin` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertDepthCreate2OOG` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertDepthCreateAddressCollisionBerlin` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertDepthCreateAddressCollision` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertOpcodeCreate[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `RevertOpcodeInCreateReturnsCreate2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `call_outsize_then_create2_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]`
- `call_then_create2_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]`
- `create2SmartInitCode` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `create2callPrecompiles` (8 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d7]`
- `returndatacopy_0_0_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]`
- `returndatacopy_afterFailing_create[fork_Amsterdam-blockchain_test_from_state_test-]`
- `returndatacopy_following_revert_in_create[fork_Amsterdam-blockchain_test_from_state_test-]`
- `returndatasize_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stCreateTest` (49 failures)

- `CREATE_EContractCreateNEContractInInitOOG_Tr[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `CREATE_EContract_ThenCALLToNonExistentAcc[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CREATE_EmptyContractAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CREATE_EmptyContractAndCallIt_1wei[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CREATE_EmptyContract[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CREATE_EmptyContractWithBalance[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CREATE_EmptyContractWithStorageAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CREATE_EmptyContractWithStorageAndCallIt_1wei[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CREATE_EmptyContractWithStorage[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CodeInConstructor` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `CreateAddressWarmAfterFail` (16 variants)
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
- `CreateCollisionResults` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `CreateCollisionToEmpty2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
- `CreateOOGFromCallRefunds` (8 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-LogOp_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create2_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Create_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SStore_Refund_NoOoG]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-SelfDestruct_Refund_NoOoG]`
- `CreateOOGafterInitCodeReturndata2[fork_Amsterdam-blockchain_test_from_state_test--g0]`
- `CreateOOGafterInitCodeRevert2[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `CreateResults` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d6]`
- `TransactionCollisionToEmpty2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1-v1]`

### `stMemoryTest` (43 failures)

- `calldatacopy_dejavu2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem0b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem31b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb+1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb+31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb+32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb+33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb-1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb-31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb-32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb-33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte+1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte+31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte+32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte+33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte-1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte-31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte-32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte-33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem32kb_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem33b_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb+1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb+31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb+32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb+33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb-1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb-31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb-32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb-33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte+1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte+31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte+32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte+33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte-1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte-31[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte-32[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte-33[fork_Amsterdam-blockchain_test_from_state_test-]`
- `mem64kb_singleByte[fork_Amsterdam-blockchain_test_from_state_test-]`
- `oog` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-15]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-16]`

### `stStaticCall` (41 failures)

- `static_ABAcalls3[fork_Amsterdam-blockchain_test_from_state_test-d0]`
- `static_CREATE_EmptyContractAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_CREATE_EmptyContractWithStorageAndCallIt_0wei[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_Call1024OOG` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `static_Call10` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `static_CallContractToCreateContractOOG[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_CallContractToCreateContractWhichWouldCreateContractIfCalled[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_CallLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_CheckOpcodes5` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `static_RETURN_Bounds[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_RETURN_BoundsOOG[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `static_ReturnTest2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcallcodecall_ABCB_RECURSIVE2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcallcodecallcode_ABCB_RECURSIVE2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcode_checkPC[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcodecallcall_ABCB_RECURSIVE2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcodecallcallcode_ABCB_RECURSIVE2` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-v1]`
- `static_callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_callcodecallcodecall_110_SuicideEnd2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcodecall_110_SuicideEnd` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcodecall_ABCB_RECURSIVE2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--v1]`
- `static_callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `static_contractCreationMakeCallThatAskMoreGasThenTransactionProvided` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`

### `stRevertTest` (34 failures)

- `RevertDepth2` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `RevertDepthCreateAddressCollision` (8 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v1]`
- `RevertDepthCreateOOG` (6 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0-v1]`
- `RevertInCreateInInit_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RevertOpcodeCalls` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1]`
- `RevertOpcodeCreate[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `RevertOpcodeDirectCall[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `RevertOpcodeInCreateReturns[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RevertOpcodeMultipleSubCalls` (8 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2-g1-v1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1-v0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3-g1-v1]`
- `RevertSubCallStorageOOG2[fork_Amsterdam-blockchain_test_from_state_test--g0-v0]`
- `RevertSubCallStorageOOG[fork_Amsterdam-blockchain_test_from_state_test--g0-v0]`

### `stExample` (32 failures)

- `add11[fork_Amsterdam-blockchain_test_from_state_test-]`
- `add11_yml[fork_Amsterdam-blockchain_test_from_state_test-]`
- `basefeeExample[fork_Amsterdam-blockchain_test_from_state_test-declaredKeyWrite]`
- `indexesOmitExample[fork_Amsterdam-blockchain_test_from_state_test-]`
- `labelsExample` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction3-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-transaction3]`
- `rangesExample` (24 variants)
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

- `RawCallCodeGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallCodeGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallCodeGasMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallCodeGasMemory[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallCodeGasValueTransferAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallCodeGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallCodeGasValueTransferMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallCodeGasValueTransferMemory[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallGasValueTransferAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallGasValueTransferMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallGasValueTransferMemory[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallMemoryGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCallMemoryGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCreateFailGasValueTransfer2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCreateFailGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCreateGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCreateGasMemory[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCreateGasValueTransfer[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawCreateGasValueTransferMemory[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawDelegateCallGasAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawDelegateCallGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawDelegateCallGasMemoryAsk[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RawDelegateCallGasMemory[fork_Amsterdam-blockchain_test_from_state_test-]`
- `gasCostBerlin[fork_Amsterdam-blockchain_test_from_state_test-d40]`
- `gasCost[fork_Amsterdam-blockchain_test_from_state_test-d40]`

### `stCallCreateCallCodeTest` (21 failures)

- `Call1024OOG` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g3]`
- `CallLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test-]`
- `Callcode1024OOG` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `CallcodeLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test--g2]`
- `callWithHighValueOOGinCall[fork_Amsterdam-blockchain_test_from_state_test-]`
- `contractCreationMakeCallThatAskMoreGasThenTransactionProvided[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `createFailBalanceTooLow[fork_Amsterdam-blockchain_test_from_state_test--v0]`
- `createInitFailBadJumpDestination2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createInitFailBadJumpDestination[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createInitFailStackSizeLargerThan1024[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createInitFailStackUnderflow[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createInitFailUndefinedInstruction2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createInitFailUndefinedInstruction[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createNameRegistratorPerTxs[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createNameRegistratorPerTxsNotEnoughGas` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `createNameRegistratorPreStore1NotEnoughGas[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stEIP1559` (20 failures)

- `baseFeeDiffPlaces` (10 variants)
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
- `gasPriceDiffPlaces` (10 variants)
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

- `call_outsize_then_create_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]`
- `call_then_create_successful_then_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]`
- `create_callprecompile_returndatasize[fork_Amsterdam-blockchain_test_from_state_test-]`
- `modexp_modsize0_returndatasize` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
- `returndatacopy_0_0_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]`
- `returndatacopy_afterFailing_create[fork_Amsterdam-blockchain_test_from_state_test-]`
- `returndatacopy_following_revert_in_create[fork_Amsterdam-blockchain_test_from_state_test-]`
- `returndatasize_after_successful_callcode[fork_Amsterdam-blockchain_test_from_state_test-]`
- `returndatasize_following_successful_create[fork_Amsterdam-blockchain_test_from_state_test-]`
- `tooLongReturnDataCopy` (8 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-10]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-7]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-8]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-success-9]`

### `stInitCodeTest` (16 failures)

- `CallContractToCreateContractAndCallItOOG[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallContractToCreateContractOOGBonusGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallContractToCreateContractWhichWouldCreateContractIfCalled[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallContractToCreateContractWhichWouldCreateContractInInitCode[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallTheContractToCreateEmptyContract[fork_Amsterdam-blockchain_test_from_state_test-]`
- `OutOfGasContractCreation` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0-g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1-g1]`
- `OutOfGasPrefundedContractCreation` (3 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g2]`
- `ReturnTest2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `StackUnderFlowContractCreation[fork_Amsterdam-blockchain_test_from_state_test-]`
- `TransactionCreateRandomInitCode[fork_Amsterdam-blockchain_test_from_state_test-]`
- `TransactionCreateSuicideInInitcode[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stZeroCallsRevert` (16 failures)

- `ZeroValue_CALLCODE_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_CALLCODE_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_CALLCODE_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_CALLCODE_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_CALL_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_CALL_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_CALL_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_CALL_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_DELEGATECALL_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_DELEGATECALL_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_DELEGATECALL_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_DELEGATECALL_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_SUICIDE_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_SUICIDE_ToEmpty_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_SUICIDE_ToNonZeroBalance_OOGRevert[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ZeroValue_SUICIDE_ToOneStorageKey_OOGRevert_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`

### `Cancun` (13 failures)

- `10_revertUndoesStoreAfterReturn[fork_Amsterdam-blockchain_test_from_state_test-]`
- `14_revertAfterNestedStaticcall[fork_Amsterdam-blockchain_test_from_state_test-]`
- `17_tstoreGas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createBlobhashTx[fork_Amsterdam-blockchain_test_from_state_test-]`
- `MCOPY_copy_cost` (9 variants)
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

- `ABAcalls3[fork_Amsterdam-blockchain_test_from_state_test-]`
- `Call10[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallRecursiveBomb3[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallToNameRegistratorZeorSizeMemExpansion[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `callcodeToNameRegistratorZeroMemExpanion[fork_Amsterdam-blockchain_test_from_state_test--g0]`
- `doubleSelfdestructTest` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-caller-self-destruct-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-caller-self-destruct]`
- `extcodecopy[fork_Amsterdam-blockchain_test_from_state_test-]`
- `multiSelfdestruct` (5 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`

### `stPreCompiledContracts2` (12 failures)

- `CallEcrecover_Overflow` (8 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-4]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail-5]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-fail]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-pass01]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-pass02]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-pass03]`
- `ecrecoverShortBuff[fork_Amsterdam-blockchain_test_from_state_test-]`
- `modexp_0_0_0_22000[fork_Amsterdam-blockchain_test_from_state_test--g0]`
- `modexp_0_0_0_25000[fork_Amsterdam-blockchain_test_from_state_test--g0]`
- `modexp_0_0_0_35000[fork_Amsterdam-blockchain_test_from_state_test--g0]`

### `stNonZeroCallsTest` (10 failures)

- `NonZeroValue_CALLCODE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_CALLCODE_ToEmpty_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_CALLCODE_ToOneStorageKey_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_CALL[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_CALL_ToEmpty_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_CALL_ToOneStorageKey_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_DELEGATECALL[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_DELEGATECALL_ToEmpty_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_DELEGATECALL_ToNonNonZeroBalance[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NonZeroValue_DELEGATECALL_ToOneStorageKey_Paris[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stCallCodes` (9 failures)

- `callcallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcode_checkPC[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stEIP3607` (9 failures)

- `initCollidingWithNonEmptyAccount` (5 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d4]`
- `transactionCollidingWithNonEmptyAccount_init_Paris` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`

### `stExtCodeHash` (8 failures)

- `callToNonExistent` (4 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d3]`
- `callToSuicideThenExtcodehash` (3 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
- `createEmptyThenExtcodehash[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stCallDelegateCodesHomestead` (7 failures)

- `callcallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stEIP150Specific` (7 failures)

- `CallAskMoreGasOnDepth2ThenTransactionHas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CreateAndGasInsideCreate[fork_Amsterdam-blockchain_test_from_state_test-]`
- `DelegateCallOnEIP[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NewGasPriceForCodes[fork_Amsterdam-blockchain_test_from_state_test-]`
- `Transaction64Rule_d64e0[fork_Amsterdam-blockchain_test_from_state_test-]`
- `Transaction64Rule_d64m1[fork_Amsterdam-blockchain_test_from_state_test-]`
- `Transaction64Rule_d64p1[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stCallDelegateCodesCallCodeHomestead` (7 failures)

- `callcallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcodecall_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`
- `callcodecallcodecallcode_ABCB_RECURSIVE[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stSelfBalance` (7 failures)

- `selfBalanceCallTypes` (3 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d2]`
- `selfBalanceEqualsBalance[fork_Amsterdam-blockchain_test_from_state_test-]`
- `selfBalance[fork_Amsterdam-blockchain_test_from_state_test-]`
- `selfBalanceGasCost[fork_Amsterdam-blockchain_test_from_state_test-]`
- `selfBalanceUpdate[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stRefundTest` (7 failures)

- `refund50_2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `refund50percentCap[fork_Amsterdam-blockchain_test_from_state_test-]`
- `refund600[fork_Amsterdam-blockchain_test_from_state_test-]`
- `refundSuicide50procentCap` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-d0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-d1]`
- `refund_CallA[fork_Amsterdam-blockchain_test_from_state_test-]`
- `refund_TxToSuicide[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stDelegatecallTestHomestead` (6 failures)

- `Call1024OOG` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g0]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `CallLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallcodeLoseGasOOG[fork_Amsterdam-blockchain_test_from_state_test--g2]`
- `Delegatecall1024OOG[fork_Amsterdam-blockchain_test_from_state_test-]`
- `delegatecallOOGinCall[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stTransactionTest` (5 failures)

- `CreateMessageSuccess[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CreateTransactionSuccess[fork_Amsterdam-blockchain_test_from_state_test-]`
- `InternalCallHittingGasLimit2[fork_Amsterdam-blockchain_test_from_state_test-]`
- `StoreGasOnCreate[fork_Amsterdam-blockchain_test_from_state_test-]`
- `SuicidesAndInternalCallSuicidesOOG[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stBadOpcode` (4 failures)

- `measureGas` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE]`
- `operationDiffGas` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE2]`
  - `[fork_Amsterdam-blockchain_test_from_state_test-CREATE]`

### `stMemExpandingEIP150Calls` (4 failures)

- `CallAskMoreGasOnDepth2ThenTransactionHasWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CallGoesOOGOnSecondLevelWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]`
- `CreateAndGasInsideCreateWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]`
- `NewGasPriceForCodesWithMemExpandingCalls[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stSolidityTest` (4 failures)

- `CallLowLevelCreatesSolidity[fork_Amsterdam-blockchain_test_from_state_test-]`
- `RecursiveCreateContractsCreate4Contracts[fork_Amsterdam-blockchain_test_from_state_test-]`
- `TestOverflow[fork_Amsterdam-blockchain_test_from_state_test-]`
- `TestStructuresAndVariabless[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stSpecialTest` (4 failures)

- `FailedCreateRevertsDeletionParis[fork_Amsterdam-blockchain_test_from_state_test-]`
- `deploymentError[fork_Amsterdam-blockchain_test_from_state_test-]`
- `makeMoney[fork_Amsterdam-blockchain_test_from_state_test-]`
- `selfdestructEIP2929[fork_Amsterdam-blockchain_test_from_state_test-]`

### `Shanghai` (3 failures)

- `push0Gas[fork_Amsterdam-blockchain_test_from_state_test-]`
- `create2InitCodeSizeLimit[fork_Amsterdam-blockchain_test_from_state_test-valid]`
- `createInitCodeSizeLimit[fork_Amsterdam-blockchain_test_from_state_test-valid]`

### `stMemoryStressTest` (3 failures)

- `RETURN_Bounds` (2 variants)
  - `[fork_Amsterdam-blockchain_test_from_state_test--g1]`
  - `[fork_Amsterdam-blockchain_test_from_state_test--g2]`
- `SSTORE_Bounds[fork_Amsterdam-blockchain_test_from_state_test--g1]`

### `stTransitionTest` (3 failures)

- `createNameRegistratorPerTxsAfter[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createNameRegistratorPerTxsAt[fork_Amsterdam-blockchain_test_from_state_test-]`
- `createNameRegistratorPerTxsBefore[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stChainId` (2 failures)

- `chainId[fork_Amsterdam-blockchain_test_from_state_test-]`
- `chainIdGasCost[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stCodeCopyTest` (2 failures)

- `ExtCodeCopyTargetRangeLongerThanCodeTests[fork_Amsterdam-blockchain_test_from_state_test-]`
- `ExtCodeCopyTestsParis[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stQuadraticComplexityTest` (2 failures)

- `Call20KbytesContract50_1[fork_Amsterdam-blockchain_test_from_state_test--g1]`
- `Return50000[fork_Amsterdam-blockchain_test_from_state_test--g1]`

### `VMTests` (1 failures)

- `twoOps[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stAttackTest` (1 failures)

- `CrashingTransaction[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stEIP158Specific` (1 failures)

- `EXP_Empty[fork_Amsterdam-blockchain_test_from_state_test-]`

### `stSLoadTest` (1 failures)

- `sloadGasCost[fork_Amsterdam-blockchain_test_from_state_test-]`
