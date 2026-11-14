# Transfer Tracking

Track source approval separately from the actual dispatch transaction. Confirm the source receipt, derive the bridge message identifier using the route's protocol, and check delivery on the destination chain.

Record the route, domains, asset addresses, recipient, amount and fees. Verify the destination mint or release event against the expected contract. An explorer's successful source receipt is only one stage.

For a delayed transfer, avoid sending again until its state is reconciled. Relayer delays, incorrect route enrollment, insufficient gas or security-module failures require route-specific diagnosis. See [Bridge Troubleshooting](../faq/bridge-troubleshooting.md).
