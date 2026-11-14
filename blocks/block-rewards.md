# Block Rewards

TurkScan® may return block reward-related fields as part of its EVM-compatible schema. Their presence does not establish a fixed TURK issuance schedule or a payout to the address shown as the block producer.

No reward schedule or reward distribution mechanism was established by the API audit. Do not calculate validator yield from null, zero or generic reward fields. Use chain monetary-policy and consensus evidence before reporting issuance.

See [Supply Metrics](../network-statistics/supply-metrics.md) for the same distinction between schema fields and validated monetary totals.
