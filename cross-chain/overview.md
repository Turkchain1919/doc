# Turkchain® Bridge and Cross-Chain Status

The 14 November 2026 audit verified Turkchain metadata and deployment addresses in the Hyperlane registry. It did not execute a cross-chain transfer or establish a complete supported-asset list.

| Capability | Evidence / status |
| --- | --- |
| Turkchain EVM network | Live RPC chain ID `1919` verified |
| Hyperlane metadata | Registry lists chain ID and domain ID `1919` |
| Hyperlane deployment addresses | Registry records mailbox and supporting contracts; see [integration](hyperlane-integration.md) |
| Warp routes and supported assets | No end-to-end route or redemption test established in this audit |
| Ethereum transfers | Depend on a verified asset route and active relaying; not certified here |
| Solana integration | Roadmap only; no live deployment or transfer support established |

An infrastructure registry entry is not proof of bridge availability. See [Transfers](cross-chain-transfers.md), [Tracking](transfer-tracking.md) and [Security](bridge-security.md).
