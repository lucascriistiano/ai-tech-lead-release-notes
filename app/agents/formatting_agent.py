from app.agents.state import CollectedData, FormattedReleaseNotes, WorkflowState
from app.agents.tools import build_release_notes_markdown


class FormattingAgent:
    """Transforma a síntese em texto final de release notes.

    Responsabilidades:
    - Gerar o texto final das release notes.
    - Aplicar formatação em Markdown.
    - Ajustar linguagem ao público-alvo.
    """

    tools = [build_release_notes_markdown]

    def run(self, state: WorkflowState) -> dict[str, FormattedReleaseNotes]:
        """Monta o documento final em Markdown usando os dados do estado."""
        collected_data = state.get("collected_data") or CollectedData(features=[], fixes=[], breaking_changes=[])
        synthesis = state.get("synthesis")
        risks = state.get("risk_analysis")
        markdown = build_release_notes_markdown.invoke(
            {
                "version": state["version"],
                "audience": state["audience"],
                "features": collected_data.features,
                "fixes": collected_data.fixes,
                "level": risks.level if risks else "Unknown",
                "technical_risk": risks.technical_risk,
                "recommendations": risks.recommendations or [],
                "summary": synthesis.executive_summary if synthesis else "",
            }
        )

        return {
            "formatted_release_notes": FormattedReleaseNotes(
                markdown=markdown
            )
        }
