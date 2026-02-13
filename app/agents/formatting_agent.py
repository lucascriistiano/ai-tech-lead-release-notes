from app.agents.state import CollectedData, FormattedReleaseNotes, WorkflowState
from app.agents.tools import build_release_notes_markdown
from app.core.llm import chatgpt_text


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

        llm_markdown = chatgpt_text(
            system_prompt=(
                "You are a technical writer specialized in software release notes. "
                "Return Markdown only."
            ),
            user_prompt=(
                f"Create release notes for version {state['version']} targeting audience {state['audience']}.\n"
                f"Features: {collected_data.features}\n"
                f"Fixes: {collected_data.fixes}\n"
                f"Risk level: {risks.level if risks else 'Unknown'}\n"
                f"Technical risk: {risks.technical_risk if risks else 'N/A'}\n"
                f"Recommendations: {risks.recommendations if risks else []}\n"
                f"Summary: {synthesis.executive_summary if synthesis else ''}\n"
                "Use sections: '## Release <version>', '### New Features', '### Fixes', "
                "'### Risks', '### Recommendations', '### Summary'."
            ),
        )

        return {"formatted_release_notes": FormattedReleaseNotes(markdown=llm_markdown or markdown)}
