from app.agents.state import RiskAnalysisResult, WorkflowState


class RiskRegressionAgent:
    """Avalia riscos técnicos e possíveis regressões.

    Responsabilidades:
    - Identificar riscos técnicos.
    - Detectar áreas sensíveis do código.
    - Sugerir observações pós-release.

    Simula uma análise combinada de QA e engenharia de confiabilidade.
    """

    def run(self, state: WorkflowState) -> dict[str, RiskAnalysisResult]:
        """Produz a análise de riscos para suporte à validação do release."""
        data = state["collected_data"]
        if data.breaking_changes:
            level = "high"
        elif data.features and data.fixes:
            level = "medium"
        else:
            level = "low"

        recommendations = [
            "Monitor authentication service during rollout.",
            "Monitor billing service during rollout.",
        ]
        return {
            "risk_analysis": RiskAnalysisResult(
                level=level,
                technical_risk=(
                    f"Release includes {len(data.features)} feature(s), {len(data.fixes)} fix(es), "
                    f"and {len(data.breaking_changes)} breaking change(s)."
                ),
                recommendations=recommendations,
            )
        }
