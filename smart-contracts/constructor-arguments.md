# Constructor Arguments

Constructor arguments initialize a deployment and are appended to creation bytecode using ABI encoding. They are not ordinary post-deployment function calls.

Retain the deployment transaction, build artifact and original values. Verification must use the original constructor arguments and correct linked-library addresses. Encoding a decimal amount with the wrong units can produce a different initialization.

For proxy deployments, distinguish implementation constructor arguments from proxy constructor and initialization calldata. Never publish a secret as a constructor argument: deployment data is public.
