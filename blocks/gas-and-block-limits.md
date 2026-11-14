# Gas Usage and Block Limits

Block gas used is the sum of execution gas recorded in that block. Block gas limit is a separate cap. The usage percentage is meaningful only relative to the actual limit returned for that block.

Fetch [block details](../api-documentation/blocks-api.md) or `eth_getBlockByNumber` rather than hard-coding a limit. Empty blocks can legitimately have zero gas used.

Explorer charts aggregate indexed data over time and can be delayed or unavailable. A high configured gas limit is not a measured throughput benchmark.
