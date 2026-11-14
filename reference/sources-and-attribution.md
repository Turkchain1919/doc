# Sources and Technical Provenance

This content is authored for TurkScan® from deployment inspection, protocol facts and read-only live observations dated 14 November 2026. No Etherscan prose or screenshots were copied and relabeled.

| Source | Use |
| --- | --- |
| [Deployed OpenAPI](https://turkscan.com/api/v2/openapi) | Parameter and response contract; [local snapshot](openapi.json) |
| [Backend version](https://turkscan.com/api/v2/config/backend-version) | Observed `12.0.1` |
| [Backend source release](https://github.com/blockscout/blockscout/tree/v12.0.1) | Route/controller comparison with inspected deployment source |
| [Frontend source](https://github.com/blockscout/frontend) | Explorer features and documentation-link mapping; deployed tree has operator modifications |
| [Blockscout documentation](https://docs.blockscout.com) | Feature organization and source-verification concepts |
| [Documentation archive](https://github.com/blockscout/docs-archive) | Historical path comparison; root license file not found in inspected inventory |
| [Etherscan documentation](https://docs.etherscan.io) | Category coverage and compatibility comparison only |
| [Viem public client](https://viem.sh/docs/clients/public) | Public read-client API |
| [Ethers 6](https://docs.ethers.org/v6/getting-started/) | Provider and bigint examples |
| [MetaMask RPC reference](https://docs.metamask.io/metamask-connect/evm/reference/json-rpc-api/) | Wallet network methods |
| [Hyperlane registry](https://github.com/hyperlane-xyz/hyperlane-registry/tree/main/chains/turkchain) | Chain metadata and registry addresses, not an end-to-end bridge test |

The inspected backend and frontend LICENSE files identify `LicenseRef-Blockscout`, effective 22 April 2026. They must not be described as universally MIT licensed. This audit does not publish or interpret private commercial-license terms. Existing source license files and notices remain in their source repositories. A separate clear permission to copy the current documentation corpus was not established, so the guide text is original rather than a wholesale documentation copy.

Protocol names, module/action identifiers, source-repository links and technical provenance are kept accurate. They are not replaced with fictional TurkScan protocol names. The visible product documentation describes TurkScan® and Turkchain®.
