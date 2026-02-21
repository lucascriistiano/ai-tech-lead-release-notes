from app.agents.state import SynthesisResult, WorkflowState
from app.core.llm import chatgpt_text

class SynthesisAgent:
    """Consolida os resultados produzidos pelos agentes paralelos.

    Responsabilidades:
    - Unificar perspectivas técnicas (métricas), de risco e de impacto.
    - Criar um Resumo Executivo coerente e agradável de ler.
    """

    def run(self, state: WorkflowState) -> dict[str, SynthesisResult]:
        impact = state.get("impact_analysis")
        risk = state.get("risk_analysis")
        metrics = state.get("metrics_analysis")

        parts = [
            f"Impact ({impact.level}): {impact.user_impact}" if impact else "",
            f"Risk ({risk.level}): {risk.technical_risk}" if risk else "",
            (
                f"Metrics: Features {metrics.features_count}, "
                f"Fixes {metrics.fixes_count}, Contributors {metrics.contributors_count}"
                if metrics else ""
            ),
        ]
        fallback_summary = " ".join(part for part in parts if part).strip()

        system_prompt = """
        <role>
        You are a Lead Software Release Analyst. Your job is to write the Executive Summary for the release notes.
        </role>

        <context>
        You will receive raw data containing Impact, Risk, and Metrics. You must weave these facts into a cohesive, professional narrative.
        </context>

        <rules>
        1. Keep it concise: Maximum 1 paragraph (3-4 sentences).
        2. Balance the tone: Celebrate the features/impact, but be transparent about the risks.
        3. Do not use bullet points or lists. Write a flowing paragraph.
        4. Do not invent data; strictly use the numbers and facts provided in the input.
        </rules>

        <output_format>
        Return ONLY the plain text paragraph. No markdown, no titles.
        </output_format>
        """

        user_prompt = f"""
        <input_data>
        {fallback_summary}
        </input_data>
        """

        try:
            llm_summary = chatgpt_text(system_prompt=system_prompt, user_prompt=user_prompt)
            final_summary = llm_summary.strip()
        except Exception:
            final_summary = fallback_summary

        return {"synthesis": SynthesisResult(executive_summary=final_summary)}