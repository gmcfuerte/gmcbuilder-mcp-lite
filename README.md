# GMC Builder MCP Lite

Free limited companion to the GMC Pro product. This is a separate **0.1.2**
client with a fresh history and only four read-only MCP tools. The Pro
implementation is absent from this repository.

## Lite and Pro

| Capability | Lite | Pro product |
| --- | --- | --- |
| Configured site aliases | Yes | Yes |
| Authenticated connection probe | Yes | Yes |
| Up to 10 element types per call | Yes | Extended tools |
| Local supplied JSON: node counts/types | Yes, input up to 64 KiB | Detailed inspection |
| Create/edit/publish layouts or documents | No | Paid functionality |
| Full export/import, bulk editing, backups | No | Paid functionality |
| Private Pro implementation or CMS companion source | Absent | Separately distributed |

Contact **gmcfuerte@gmail.com** for the Pro product and current annual plans; see the [GMC catalogue](https://fuerteventuratv.net/en/cms).

Lite is free to use under the [limited commercial licence](LICENSE).
Source visibility does not grant redistribution or resale rights.

## Upgrade to Pro in your MCP client

Open the resource **Upgrade to Pro** (`gmc://lite/pro-features`) to see the
capability comparison and the product's current plans. Editing, publishing,
full import/export, bulk editing and restoration are labelled **unavailable
in Lite**. They are informational previews; no Pro code or executable Pro
tools are bundled. The free tools keep working without an upgrade.

MCP clients decide how resources are displayed, so this is not a guaranteed
popup or a graphical settings panel. Ask your assistant to read the resource
if its client does not expose a resource browser.

[Read the practical Lite guide](https://fuerteventuratv.net/en/joomla-app/1887-gmc-mcp-lite-practical-guide).

## Prerequisites

Python 3.10 or newer. GMC Builder installed on the target site: WordPress authoring API (2.0.0+) with an Application Password, or Joomla remote API (2.0.1+) with the shared X-Gmc-Builder-Key. This repository does not distribute GMC Builder. Obtain the CMS product through GMC; no layout-export endpoint is included in Lite.

## Install from GitHub

```console
git clone https://github.com/gmcfuerte/gmcbuilder-mcp-lite.git
cd gmcbuilder-mcp-lite
python -m venv .venv
```

Windows:

```console
.venv\Scripts\python.exe -m pip install .
```

macOS/Linux:

```console
.venv/bin/python -m pip install .
```

This Lite edition is distributed through this GitHub repository; it has
not been published to PyPI. Do not install the separate full Pro package
as a substitute for Lite.

## Configure

1. Copy `sites.example.json` to a **local** `sites.json` and keep only the
   sites you own or are authorized to access. The file is ignored by Git.
2. Set the credential environment variables named by `username_env`,
   `password_env`, and the applicable Joomla token/key field. Never put
   credential values in committed JSON or an MCP chat.
3. Set `GMCBUILDER_MCP_LITE_SITES` to the absolute path of that local JSON file.
4. Add the server using `mcp.example.json`: replace the placeholders with
   the absolute Python executable and configuration file paths. Ensure
   the MCP client passes the credential variables to its child process.
5. Start with `gmcbuilder_lite_list_sites`, then `gmcbuilder_lite_ping_site`.

`rest_mode: "query"` supports WordPress without pretty REST URLs; otherwise
use `pretty`. Subdirectory installations are supported in the base URL.

## Tools

- `gmcbuilder_lite_list_sites`: aliases and platforms only.
- `gmcbuilder_lite_ping_site`: one authenticated GET, sanitized status only.
- `gmcbuilder_lite_list_element_types`: List at most ten builder element type names; no schema or kit export.
- `gmcbuilder_lite_summarize_layout`: pass the text from `layout.example.json`
  as `layout_json`. Returns counts and types; no settings or content.

The server runs locally using **stdio**. No remote HTTP server, uploads,
arbitrary URLs, SSH, license switch or Pro modules are included. Online
tools use a fixed GET allowlist, verified TLS, no redirects, at most one
request at a time per configured base URL, a two-second interval, and a
1 MiB response limit. HTTP is accepted only for exact loopback hosts.
HTTP 403/415 stops subsequent requests to that base URL until restart.

## Release status

Initial Lite release: source and package contents inspected and Python
compiled. Site integration and runtime tests have not been performed.
Do not treat this initial release as a production integration certification.

## Contact

[GMC](https://fuerteventuratv.net/en/cms) · gmcfuerte@gmail.com.
Independent GMC software; product names belong to their respective owners.
