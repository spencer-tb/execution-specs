# Ported Static Tests

Tests in this directory were auto-converted from the static fillers in
[ethereum/tests](https://github.com/ethereum/tests) and may be regenerated
by the conversion tooling.

## Layout

Tests live under `tests/ported_static/<fork>/<legacy_suite>/`, where
`<fork>` is the fork that introduced the subject the test exercises
(mirroring the native `tests/<fork>/` suites) and `<legacy_suite>` is the
original `ethereum/tests` directory name (traceability, together with each
file's `ported_from` marker).

The fork folder is organizational: a test's `valid_from` marker is an
independent, empirically-determined property and may be earlier (a
general-behavior test grouped under an EIP-named suite) or later (e.g. a
TangerineWhistle EIP-150 gas test floored at Berlin because it uses
EIP-2929 warm/cold opcode metadata) than the folder's fork. The layout is
enforced at collection time by `conftest.py`.

If you correct a test by hand (e.g. fix its post-state expectations), add
the following docstring so the file is not overwritten on regeneration:

```text
@manually-enhanced: Do not overwrite. Post-state expectations corrected
manually (see PR #2784).
```
