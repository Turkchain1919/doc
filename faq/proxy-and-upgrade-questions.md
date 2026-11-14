# Proxy and Upgrade Questions

A proxy can keep the same public address while delegating to a different implementation after an upgrade. Its admin role can differ from the application owner.

## What to check

Verify proxy and implementation separately, inspect current implementation and roles, and use the correct ABI when reading or writing through the proxy. Source verification before an upgrade does not certify all future behavior.

## Further guidance

[Read the detailed TurkScan guide](../smart-contracts/proxy-contracts.md). If the issue persists, retain the public identifiers and exact error while keeping secrets out of the report.
