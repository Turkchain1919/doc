# GitBook Publication and Synchronization

The documentation source is `https://github.com/Turkchain1919/doc`; its default branch is `main`. The starting commit was `5b803354f7422ff179d60b774a9d6dd6e753d3d5` (`GITBOOK-60`, 24 September 2026). Existing Markdown paths, navigation entries and the three repository images are retained. No existing Changelog file was found in the starting tracked tree.

The live `https://doc.turkscan.com` returned GitBook HTML and the title “Welcome to TurkScan | Turkchain 1919”. Public page metadata identified existing site `site_ewjLm` and space `EuttlyFczPL5bpa9qKna`. Its content matched the repository's former welcome page. These observations establish the existing published site, but not the current Git Sync repository/branch configuration.

The GitHub token permits repository content work, but webhook inspection returned 403 with its current scope. A skipped Mintlify check was also present on the starting commit; that is not proof of a GitBook sync. No other publishing platform was configured by this task.

In the **existing** GitBook space, inspect Git Sync and confirm repository `Turkchain1919/doc`, branch `main`, root directory and latest imported commit. Do not initialize a new project or overwrite current space content. A “Synced” indicator alone is insufficient unless those settings match. After an authorized merge, confirm the imported commit and inspect the new pages on the existing domain.

For the custom domain, open the existing site's domain settings and confirm `doc.turkscan.com`. GitBook supplies the exact DNS Type, Name and Target for that site. The authoritative target must be read there; this audit does not invent a CNAME target. Public DNS is proxied through Cloudflare and does not expose the original target as a CNAME. Use GitBook hosting and TLS, with no docs Docker image, Nginx reverse proxy or separate server.

The `.gitbook.yaml` file declares the repository's existing README/SUMMARY structure. It does not change the site's logo, theme or domain settings. See [GitBook custom-domain instructions](https://gitbook.com/docs/publish/custom-domain).


## Main publication observed after merge

PR #1 was merged to `main` as `d26f8d862859795182629335ece69cdf1ecebf66`. All 146 navigation URLs returned HTTP 200 after following GitBook redirects, and the new chain configuration and compatibility content were checked. The user reports operating GitBook sync manually; this observation does not establish that future sync is automatic.

## Existing API and Help spaces

The site also exposes an existing API Reference section and Help Center. Their sources are prepared as project directories in the **same** repository and branch:

| Existing GitBook area | Repository | Branch | Project directory |
| --- | --- | --- | --- |
| Main documentation | `Turkchain1919/doc` | `main` | `/` (keep current setting) |
| API Reference | `Turkchain1919/doc` | `main` | `api-reference` |
| Help Center | `Turkchain1919/doc` | `main` | `help-center` |

Choose the project directory in each existing space's Git Sync configuration and import in the GitHub → GitBook direction. Each directory has its own README, SUMMARY and GitBook configuration. Keep the existing site-section URLs, logo, theme and Changelog. Do not create a replacement space. The API's previous page slugs (authentication, accounts, blocks, transactions, tokens, logs, stats, rate-limits and error-handling) are retained. Captured previous public content is in [the repository snapshot](previous-gitbook-api-pages.json).

These two directories are generated publication views of the canonical API and FAQ files. Update canonical files and run `python3 tools/generate_spaces.py`; do not maintain competing manual copies. The split is necessary because Git Sync operates per existing space. [GitBook describes monorepo project directories here](https://gitbook.com/docs/changelog/2023-product-updates).


## Explorer integration validation

The existing explorer frontend, backend and administrator service were updated on 14 November 2026. API branding and six administrator-managed documentation links/icons were verified live. The API path, schema, tag and security contracts remained unchanged across 114 paths. See [deployment evidence](deployment-verification.json), [browser results](live-api-browser.json) and [footer icon pairs](live-footer-icons.json). These are explorer application changes; documentation continues to use GitHub and GitBook with no documentation container or reverse proxy.
