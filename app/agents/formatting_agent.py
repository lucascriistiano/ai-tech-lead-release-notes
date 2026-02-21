from app.agents.state import CollectedData, FormattedReleaseNotes, WorkflowState
from app.agents.tools import build_release_notes_markdown
from app.core.llm import chatgpt_text

class FormattingAgent:
    """Transforma a síntese em texto final de release notes.

    Responsabilidades:
    - Gerar o texto final em Markdown de alta qualidade.
    - Ajustar a linguagem e o jargão técnico ao público-alvo (Audience).
    """

    def run(self, state: WorkflowState) -> dict[str, FormattedReleaseNotes]:
        collected_data = state.get("collected_data") or CollectedData(features=[], fixes=[], breaking_changes=[])
        synthesis = state.get("synthesis")
        risks = state.get("risk_analysis")
        
        fallback_markdown = build_release_notes_markdown.invoke(
            {
                "version": state.get("version", "v0.0.0"),
                "audience": state.get("audience", "General"),
                "features": collected_data.features,
                "fixes": collected_data.fixes,
                "level": risks.level if risks else "Unknown",
                "technical_risk": risks.technical_risk if risks else "",
                "recommendations": risks.recommendations if risks else [],
                "summary": synthesis.executive_summary if synthesis else "",
            }
        )

        system_prompt = """
        <role>
        You are an Expert Technical Writer specialized in software release documentation.
        </role>

        <context>
        You are formatting the final Release Notes document. The document must be pristine, easy to read, and tailored to the audience.
        </context>

        <rules>
        1. Tone: Adjust your writing style strictly to the target <audience>. (e.g., Use business terms for Stakeholders, technical terms for Developers).
        2. Structure: Use the exact markdown sections requested.
        3. Readability: Polish the raw feature/bug descriptions to sound professional.
        </rules>

        <output_format>
        Return ONLY valid Markdown text.
        </output_format>
        """

        user_prompt = f"""
        <input_data>
            <version>{state.get('version')}</version>
            <audience>{state.get('audience')}</audience>
            <summary>{synthesis.executive_summary if synthesis else ''}</summary>
            <features>{collected_data.features}</features>
            <fixes>{collected_data.fixes}</fixes>
            <risk_level>{risks.level if risks else 'Unknown'}</risk_level>
            <technical_risk>{risks.technical_risk if risks else 'N/A'}</technical_risk>
            <recommendations>{risks.recommendations if risks else []}</recommendations>
        </input_data>

        <formatting_instructions>
        Use the following sections exactly:
        ## Release {state.get('version')}
        **Audience:** {state.get('audience')}
        
        ### Executive Summary
        [Insert summary here]
        
        ### New Features
        [Format as bullet points]
        
        ### Bug Fixes
        [Format as bullet points]
        
        ### Risks & Recommendations
        **Risk Level:** [Level]
        [Technical Risk]
        [Format recommendations as bullet points]
        </formatting_instructions>
        """

        try:
            llm_markdown = chatgpt_text(system_prompt=system_prompt, user_prompt=user_prompt)
            final_markdown = llm_markdown.strip()
        except Exception:
            final_markdown = fallback_markdown

        return {"formatted_release_notes": FormattedReleaseNotes(markdown=final_markdown)}