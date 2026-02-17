from app.agents.state import SynthesisResult, WorkflowState
from app.core.llm import chatgpt_text


class SynthesisAgent:
    """Consolida os resultados produzidos pelos agentes paralelos.

    Responsabilidades:
    - Consolidar as análises paralelas.
    - Unificar perspectivas técnicas, de risco e de impacto.
    - Criar uma visão coerente do release.
    """

    def run(self, state: WorkflowState) -> dict[str, SynthesisResult]:
        """Gera um resumo executivo unificado a partir das análises anteriores."""
        impact = state.get("impact_analysis")
        risk = state.get("risk_analysis")
        metrics = state.get("metrics_analysis")

        parts = [
            f"Impact ({impact.level}): {impact.user_impact}" if impact else "",
            f"Risk ({risk.level}): {risk.technical_risk}" if risk else "",
            (
                f"Metrics: Features {metrics.features_count}, "
                f"Fixes {metrics.fixes_count}, Contributors {metrics.contributors_count}"
                if metrics
                else ""
            ),
        ]

        fallback_summary = " ".join(part for part in parts if part).strip()
        llm_summary = chatgpt_text(
            system_prompt=(
                "You are a software release analyst. "
                "Create an executive summary that balances impact, risk, and metrics."
            ),
            user_prompt=(
                "Use the following analysis details and return a concise paragraph in plain text:\n"
                f"{fallback_summary}"
            ),
        )

        return {"synthesis": SynthesisResult(executive_summary=llm_summary or fallback_summary)}
