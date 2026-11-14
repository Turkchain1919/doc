# Contract Ownership Proof Problems

An ownership challenge verifies control of the signing address. A contract can have a deployer, factory, proxy admin and separate application roles, none of which are automatically interchangeable.

## What to check

Check the challenged address, selected wallet, chain and message. For factory-created or contract-wallet addresses, use a supported proof method rather than signing from an unrelated account. Do not publish a private key to prove control.

## Further guidance

[Read the detailed TurkScan guide](https://doc.turkscan.com/accounts/address-verification). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
