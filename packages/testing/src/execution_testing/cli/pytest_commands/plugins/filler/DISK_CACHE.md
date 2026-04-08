# T8n Disk Cache

Persists t8n results to disk across fill runs. Content-addressed by input hash + spec source hash.

## Benchmarks

All benchmarks: Amsterdam fork, `-n 8`, `--ignore=tests/ported_static`, M-series Mac.

### `blockchain_test` only (14,300 tests)

| Run | Time | vs No Cache |
|---|---|---|
| No cache | 1:48 | baseline |
| Cache cold | 1:41 | 6% faster (32% hits within run) |
| Cache warm | 0:39 | **64% faster** (96% hit rate) |

### Default formats (35,716 tests)

| Run | Time | vs No Cache |
|---|---|---|
| No cache | 2:44 | baseline |
| Cache cold | 2:39 | 3% faster (28% hits within run) |
| Cache warm | 1:08 | **59% faster** (95% hit rate) |

### `--generate-all-formats` (50,035 tests)

| Run | Time | vs No Cache |
|---|---|---|
| No cache | 33:53 | baseline |
| Cache cold | 29:40 | 12% faster (36% hits within run) |
| Cache warm | **13:07** | **61% faster** (95% hit rate) |

### All results

| Test set | Tests | No Cache | Cold | Warm | Speedup | Hit rate | Disk |
|---|---|---|---|---|---|---|---|
| `blockchain_test` | 14,300 | 1:48 | 1:41 | 0:39 | 64% | 96% | ~3GB |
| Default formats | 35,716 | 2:44 | 2:39 | 1:08 | 59% | 95% | ~5GB |
| `--generate-all-formats` | 50,035 | 33:53 | 29:40 | 13:07 | 61% | 95% | ~48GB |

## Disk usage

Cache size: **~48GB** for Amsterdam `--generate-all-formats`.
9,611 files over 1MB account for 47.4GB — these are entries with large post-state allocs
(engine tests with pre-alloc groups, tests with many accounts).

## Design

### Content hash (blake2b)

Hashes: fork + chain_id + reward + **alloc identity** + env + txs + blob_params + state_test.

Alloc hashing strategy:
- `LazyAlloc` (from previous t8n output or disk cache hit): uses `_state_root` — a 32-byte
  hash already computed by the t8n tool. **0.0004ms**, essentially free.
- `Alloc` (genesis, first block only): `model_dump()` + `json.dumps(sort_keys=True)`.
  **0.02-0.5ms** for typical tests (5-20 accounts).

### Key design decisions

- **Alloc must be in the hash** — omitting it caused collisions (tests with same txs/env but
  different allocs got wrong cached results).
- **`_state_root` is the key insight** — it's a cryptographic hash of the full alloc state,
  already available on `LazyAlloc` at zero cost. Only genesis `Alloc` needs serialization.
- **`sort_keys=True` is required** — `model_dump_json()` preserves dict insertion order, which
  varies with xdist worker ordering. Must sort for deterministic hashes.
- **`LazyAllocStr` deserialization** — disk cache returns `LazyAllocStr` so subsequent block
  hashing and `model_dump()` calls work correctly.
- **Skip `BlockchainEngineXFixture`** — uses pre-alloc groups with huge combined allocs.
  In-memory cache already deduplicates from `blockchain_test`.

### Spec hash

Per-fork hash of EELS source code (`src/ethereum/`). Shared modules + fork directory.
Transition forks (e.g. `ShanghaiToCancunAtTime15k`) hash both source and target fork directories.

### Serialization

Direct byte concatenation avoids re-parsing alloc JSON. Output stored as plain JSON.

### Approaches tried

| Approach | Disk | Warm speedup | Issue |
|---|---|---|---|
| Content hash with `model_dump()` | 48GB | 31% | Expensive hash for large allocs |
| Content hash without alloc | 3GB | 64% | **Collisions** — wrong results |
| Content hash with `_state_root` | 48GB | **61%** | Current approach |
| 512KB size limit | 3GB | ~0% | Filters out most valuable entries |
| gzip level 1 | ~10GB | ~31% | Cold run write overhead |

## Open issues

1. **Disk usage** — 48GB for all-formats. Large post-state allocs dominate.
   Compression or delta storage could help.
2. **5% warm misses** — 2,245 misses on warm run. Likely genesis `Alloc` with
   non-deterministic `model_dump` ordering, or tests with no `_state_root`.
3. **Cold run overhead** — writing 48GB of cache entries adds ~4min vs no-cache.

## Where the remaining time goes

The disk cache eliminates t8n execution but the fill still needs to:

1. Collect tests (~5s fixed)
2. Build fixture JSON (block headers, RLP encoding, etc.)
3. Write fixture files to disk
4. xdist coordination overhead

These dominate the warm-cache runtime. Further speedup requires caching final fixture output.

## Usage

Opt-in with `--cache`. Custom directory with `--cache-dir <path>`.

Cache directory: `.t8n-cache/` (gitignored).
