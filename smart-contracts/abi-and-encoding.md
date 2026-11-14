# Contract ABI and Encoding

An ABI describes function names, argument types, outputs, events and custom errors. Clients use it to encode calls and decode returned data. It does not enforce the behavior of deployed code.

Use the ABI produced by the exact build, or the verified contract response when available. Preserve integer precision with big integers. A selector can collide with another signature, so decoding by selector alone is insufficient.

Constructor arguments are ABI-encoded after creation bytecode. See [Constructor Arguments](constructor-arguments.md) and [Proxy Contracts](proxy-contracts.md).
