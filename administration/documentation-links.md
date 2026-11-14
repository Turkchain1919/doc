# Documentation Labels, URLs and Icons

TurkScan® administrators manage footer categories and links from the authenticated Appearance → Footer screen. Each record has a name, visible label, HTTPS URL, icon platform, optional light/dark icon URLs, order, language, enabled state and link-opening options.

## Documentation entries

| Visible label | Target | Icon platform |
| --- | --- | --- |
| API Documentation | `https://turkscan.com/api-docs` | `api` → `navigation/api_docs` |
| Developer Guides | `https://doc.turkscan.com/developers/network-configuration` | `docs` |
| Documentation | `https://doc.turkscan.com` | `docs` |
| API Reference | `https://doc.turkscan.com/api-documentation/introduction` | `api` |
| Help Center | `https://doc.turkscan.com/faq/frequently-asked-questions` | `help` → `docs` |
| Network Information | `https://doc.turkscan.com/introduction/network-information` | `docs` |

These targets use established main-site routes so the explorer does not depend on the operator finishing a separate API/Help space sync. The dedicated GitBook spaces use the same content through the `api-reference` and `help-center` project directories.

## Editing and verification

Keep existing record IDs, ordering and link behavior unless a change is intended. Save an accurate label and the complete HTTPS target. Choose the built-in API or documentation icon for these resources; no remote icon download is required. Custom light/dark images must be reachable and appropriate for each theme.

Check the public footer after saving and confirm the actual link and icon, not only the form values. Changes are audited. Database-managed settings take precedence over seed defaults, so changing a source default alone does not update an existing record.

Token logos, public address tags, token Verified decisions and contract Certified labels have separate administrator workflows. An icon or label is not a source-code match, and an administrator decision must not fabricate verified source. Preserve authentication, MFA, ownership checks and audit history when using those workflows.
