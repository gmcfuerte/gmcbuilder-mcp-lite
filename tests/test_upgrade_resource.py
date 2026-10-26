"""The MCP resource must be consumable Markdown, including line boundaries."""
import asyncio

from gmcbuilder_mcp_lite.__main__ import mcp


def test_upgrade_resource_has_real_markdown_lines():
    resources = asyncio.run(mcp.read_resource("gmc://lite/pro-features"))
    markdown = "".join(item.content for item in resources)
    assert markdown.splitlines()[0] == "# Upgrade to Pro — GMC Builder MCP"
    assert "\n| Capability | Lite | Separate Pro product |\n" in markdown
    assert "\\n" not in markdown
