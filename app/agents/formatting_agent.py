from app.agents.state import CollectedData, FormattedReleaseNotes, WorkflowState


class FormattingAgent:
    def run(self, state: WorkflowState) -> dict[str, FormattedReleaseNotes]:
        data = state.get("collected_data") or CollectedData(features=[], fixes=[], breaking_changes=[])
        synthesis = state.get("synthesis")
        features = "\n".join(f"- {item}" for item in data.features) or "- None"
        fixes = "\n".join(f"- {item}" for item in data.fixes) or "- None"

        return {
            "formatted_release_notes": FormattedReleaseNotes(
                markdown=(
                    f"## Release {state['version']}\n\n"
                    f"Audience: {state['audience']}\n\n"
                    "### New Features\n"
                    f"{features}\n\n"
                    "### Fixes\n"
                    f"{fixes}\n\n"
                    "### Summary\n"
                    f"{synthesis.executive_summary if synthesis else 'No summary generated.'}"
                )
            )
        }
