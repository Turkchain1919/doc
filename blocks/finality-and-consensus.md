# Finality & Consensus

A transaction receipt records inclusion in a block. Explorer confirmations count subsequent indexed blocks; they do not independently prove the network's consensus guarantees.

This documentation does not promise irreversible or instant finality from an EVM receipt alone. Applications should define their acceptance policy from Turkchain® node consensus data and their own risk requirements. Cross-chain systems also have route-specific confirmation and relayer policies.

Track canonical block hashes and reconcile changes. See [Bridge Security](../cross-chain/bridge-security.md) before treating source-chain inclusion as completed destination delivery.
