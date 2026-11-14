# GitBook Publication and Synchronization

The documentation source is `https://github.com/Turkchain1919/doc`; its default branch is `main`. The starting commit was `5b803354f7422ff179d60b774a9d6dd6e753d3d5` (`GITBOOK-60`, 24 September 2026). Existing Markdown paths, navigation entries and the three repository images are retained. No existing Changelog file was found in the starting tracked tree.

The live `https://doc.turkscan.com` returned GitBook HTML and the title “Welcome to TurkScan | Turkchain 1919”. Public page metadata identified existing site `site_ewjLm` and space `EuttlyFczPL5bpa9qKna`. Its content matched the repository's former welcome page. These observations establish the existing published site, but not the current Git Sync repository/branch configuration.

The GitHub token permits repository content work, but webhook inspection returned 403 with its current scope. A skipped Mintlify check was also present on the starting commit; that is not proof of a GitBook sync. No other publishing platform was configured by this task.

In the **existing** GitBook space, inspect Git Sync and confirm repository `Turkchain1919/doc`, branch `main`, root directory and latest imported commit. Do not initialize a new project or overwrite current space content. A “Synced” indicator alone is insufficient unless those settings match. After an authorized merge, confirm the imported commit and inspect the new pages on the existing domain.

For the custom domain, open the existing site's domain settings and confirm `doc.turkscan.com`. GitBook supplies the exact DNS Type, Name and Target for that site. The authoritative target must be read there; this audit does not invent a CNAME target. Public DNS is proxied through Cloudflare and does not expose the original target as a CNAME. Use GitBook hosting and TLS, with no docs Docker image, Nginx reverse proxy or separate server.

The `.gitbook.yaml` file declares the repository's existing README/SUMMARY structure. It does not change the site's logo, theme or domain settings. See [GitBook custom-domain instructions](https://gitbook.com/docs/publish/custom-domain).
