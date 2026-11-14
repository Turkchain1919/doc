# Block Statistics

Use `GET /api/v2/blocks` for current indexed blocks and `GET /api/v2/stats` for aggregate counters. The statistics response includes total indexed blocks and average block time when available.

The observed average block time is an explorer measurement, not a consensus constant. An empty block can have no transactions or gas usage. Missing charts or null monetary values must remain unavailable in derived reports.

See [Network Statistics](../network-statistics/overview.md).
