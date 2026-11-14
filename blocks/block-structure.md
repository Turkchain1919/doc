# Block Details, Height and Hash

A block groups executed transactions and references its parent. TurkScan® exposes height, hash, parent hash, timestamp, gas limit, gas used and related transactions where indexed.

Use block number for sequential queries and block hash for exact identity. JSON-RPC quantities are hexadecimal; REST V2 generally uses JSON numbers or decimal strings according to each field schema.

Do not infer proof-of-work mining from an EVM field named `miner` or `difficulty`. Chain adapters can retain those field names for compatibility. A field that is null or zero is not evidence of a reward or economic value.
