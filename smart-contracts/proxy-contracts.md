# Proxy Contracts

A proxy delegates execution to an implementation. The address users call can remain constant while its behavior changes after an upgrade. TurkScan® can show detected implementations where indexed.

Verify the proxy and implementation separately. Inspect upgrade authority, admin roles, initialization state and storage-layout compatibility. Read/write operations normally target the proxy address using the correct implementation ABI.

Detection can be incomplete for custom patterns. A verified implementation does not prove that every proxy using it is correctly initialized or safely administered. Track implementation changes over time.
