# Hardhat Contract Verification

Use a verification plugin compatible with the project's installed Hardhat major version. Configure the custom chain as `1919`, the explorer API as `https://turkscan.com/api` and the browser URL as `https://turkscan.com` where the plugin supports custom explorer definitions.

Keep compiler version, optimizer, EVM target, libraries and constructor arguments identical to deployment. Plugin configuration formats vary across versions; consult the installed plugin's primary documentation before applying a configuration example.

An API key field in a tool's configuration does not prove that an unrelated provider's key is accepted by TurkScan. See [Authentication](../../api-documentation/authentication-and-api-keys.md). Original compiler Standard JSON Input can be submitted through the [verification workflow](../../smart-contracts/contract-verification.md).
