# Foundry Contract Verification

Preserve the exact compiler version, optimizer runs, EVM target, library addresses and constructor arguments from deployment. Confirm the deployed contract is on Turkchain® chain `1919`.

The compatibility verification URL is `https://turkscan.com/api`. Foundry's verifier integration can use a Blockscout-compatible verifier backend; the backend identifier is a tool configuration value and must not be renamed to a nonexistent provider. Use the options supported by your installed Foundry version.

For reproducibility, export the build's Standard JSON Input and submit it through TurkScan's verified-source workflow. See [Contract Verification](../../smart-contracts/contract-verification.md) and [Verification API](../../api-documentation/contract-verification-api.md).

The audit did not broadcast a deployment or submit a verification job. Do not interpret configuration guidance as proof of a completed verification.
