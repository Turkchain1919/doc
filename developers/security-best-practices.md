# Developer Security Best Practices

Keep keys in wallet, hardware or keystore systems; never in frontend bundles, Git repositories or API examples. Restrict server credentials and rotate them through secure operational procedures.

Validate user input, use exact integer arithmetic, bound approvals, simulate sensitive calls and inspect receipt status. Audit upgrade authority and external dependencies. Protect authenticated explorer integrations against session theft, CSRF and accidental exposure of private tags or keys.

Implement retries only where semantics are safe. Verify external metadata before rendering it and do not treat an explorer label as an authorization decision. See [User Safety](../security/user-safety-best-practices.md).
