# Contract Security Considerations

Review access controls, upgrade paths, reentrancy, oracle dependencies, token approvals and external calls. Test expected failures as well as happy paths. Use maintained libraries and independent review for contracts that control valuable assets.

Verify source and bytecode, but do not treat a source match or Certified label as an audit. Inspect proxy implementations and admin permissions. Simulate sensitive transactions and use bounded allowances when practical.

Never enter a seed phrase or private key into a verification form. Avoid publishing credentials in source, deployment scripts or compiler inputs. See [Developer Security](../developers/security-best-practices.md).
