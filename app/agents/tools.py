from langchain_core.tools import tool


@tool
def fetch_github_changes(version: str, from_date: str, to_date: str) -> dict:
    """Fetch changes from GitHub for a target release window."""
    _ = (version, from_date, to_date)
    return {
        "features": ["Feature A", "Feature B"],
        "fixes": ["Bug Fix C"],
    }


@tool
def fetch_tasks_data(version: str, from_date: str, to_date: str) -> dict:
    """Fetch tasks/issues data from external tracker services."""
    _ = (version, from_date, to_date)
    return {
        "bugs": ["Bug Fix C"],
        "breaking_changes": [],
    }


@tool
def compute_release_metrics(features: list[str], fixes: list[str], bugs: list[str]) -> dict:
    """Compute release-level quantitative metrics."""
    return {
        "features_count": len(features),
        "fixes_count": len(fixes),
        "bugs_count": len(bugs),
        "contributors_count": 0,
    }

@tool
def build_release_notes_markdown(
    version: str,
    audience: str,
    features: list[str],
    fixes: list[str],
    level: str,
    technical_risk: str,
    recommendations: list[str],
    summary: str,
) -> str:
    """Build Markdown text for release notes."""
    features_md = "\n".join(f"- {item}" for item in features) or "- None"
    fixes_md = "\n".join(f"- {item}" for item in fixes) or "- None"
    level_md = level or "Unknown"
    technical_risk_md = technical_risk or "- None"
    recommendations_md = "\n".join(f"- {item}" for item in recommendations) or "- None"
    return (
        f"## Release {version}\n\n"
        f"Audience: {audience}\n\n"
        "### New Features\n"
        f"{features_md}\n\n"
        "### Fixes\n"
        f"{fixes_md}\n\n"
        "### Risks\n"
        f"Level: {level_md}\n\n"
        f"{technical_risk_md}\n\n"
        "### Recommendations\n"
        f"{recommendations_md}\n\n"
        "### Summary\n"
        f"{summary or 'No summary generated.'}"
    )


@tool
def validate_release_notes_content(markdown: str) -> dict:
    """Validate release notes clarity/completeness for final approval."""
    has_content = bool(markdown and markdown.strip())
    return {
        "status": "approved" if has_content else "needs_revision",
        "notes": [] if has_content else ["Release notes content is empty."],
    }
