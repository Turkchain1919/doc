# TurkScan® API Documentation

TurkScan® exposes indexed explorer data and separate network RPC access.

| Interface | Base URL | Purpose |
| --- | --- | --- |
| Explorer API V2 | `https://turkscan.com/api/v2` | Indexed resources, cursor pagination |
| Explorer compatibility API | `https://turkscan.com/api` | Selected module/action requests |
| Network JSON-RPC | `https://rpc.turkscan.com` | EVM node reads and signed transaction submission |
| Interactive documentation | `https://turkscan.com/api-docs` | Explorer API interface |
| Live OpenAPI | `https://turkscan.com/api/v2/openapi` | Deployed machine-readable contract |

The bare `/api/v2` path returns an unknown-action error; request a resource such as `/api/v2/stats`. The audited backend reports version `12.0.1` and chain type `default`.

The reference is based on the deployed OpenAPI and read-only HTTP observations from 14 November 2026. It separates working reads, unsuccessful observations and operations not exercised. A declared upstream route alone is not treated as proof of support.

Start with [API V2](api-v2.md), [Compatibility Matrix](compatibility-matrix.md), [Pagination](pagination.md), [Errors](error-handling.md) and [Examples](request-examples.md). Raw [audit evidence](../reference/endpoint-evidence.json) is stored in this repository; examples are dated snapshots, not current balances or endorsements.
