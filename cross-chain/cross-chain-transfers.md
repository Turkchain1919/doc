# Cross-Chain Transfers

Before transferring, verify the official interface, route contracts, source and destination chains, destination address format, token decimals, quoted fees and minimum received. Ensure you can pay destination gas.

An approval, source-chain lock or burn and destination mint or release are separate operations. A successful source receipt does not mean destination funds have arrived. Save message identifiers and both chains' transaction hashes.

No end-to-end route was exercised during this audit. Do not use example infrastructure addresses as transfer destinations. See [Transfer Tracking](transfer-tracking.md) and [Bridge Security](bridge-security.md).
