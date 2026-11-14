# Read Contract and Write Contract

Read Contract uses the available ABI to encode view or pure calls. Enter parameters in the correct units; address and integer types must match the method signature. A read can revert, and its output depends on the state queried.

Write Contract prepares a transaction for a connected wallet. Confirm network `1919`, target contract, method, arguments, payable TURK value and gas before approving. A wallet rejection is not a mined failure.

For proxies, use the implementation ABI only after confirming the proxy's current implementation and upgrade pattern. A source-verified contract can still contain privileged or harmful behavior.
