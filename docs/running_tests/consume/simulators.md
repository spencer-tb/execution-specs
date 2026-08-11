# Consume Simulators

The `engine` and `rlp` simulators test clients by importing blocks through different interfaces. These simulators run within the Hive testing framework to provide containerized, isolated testing environments.

## Command Syntax

```bash
uv run consume <engine|rlp> [OPTIONS]
```

## Stateless Witness Mode

The engine simulators accept `--stateless` to execute payloads through the witness-emitting `engine_newPayloadWithWitnessVX` endpoint and verify the client-generated execution witness against the fixture. Pass `--ssz` to use the REST `POST /new-payload-with-witness` endpoint with an SSZ-encoded response instead of JSON-RPC. In this mode the hive test suite name gains a `-stateless` suffix (e.g. `eels/consume-engine-stateless`), and fixtures without a witness — or with a deliberately mutated one — are skipped before client startup.

```bash
uv run consume engine --stateless [--ssz] [OPTIONS]
```

## Relevant Information

- To install the `consume` command, see [Installation](../../getting_started/installation.md).
- Help [setting up](../hive/index.md) and [starting Hive in dev mode](../hive/dev_mode.md).
- For an explanation of how the `consume` simulators work, see the [Engine](../running.md#engine) and [RLP](../running.md#rlp) sections in [Running Tests](../running.md).
- Help for relevant options can be found in [Consume Cache and Fixture Inputs](./cache.md) and [Useful Pytest Options](../useful_pytest_options.md).

## Related: Block Building

A separate hive simulator [`build-block`](../running.md#block-building) is also fixture-driven but tests the client's **producer-side** path via the `testing_buildBlockV1` engine-API testing-namespace endpoint, rather than the consumer-side import path that the simulators above exercise.
