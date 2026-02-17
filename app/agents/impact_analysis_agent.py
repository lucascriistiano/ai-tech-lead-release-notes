from app.agents.state import ImpactAnalysisResult, WorkflowState


class ImpactAnalysisAgent:
    """Analisa o impacto das mudanças para usuários finais.

    Responsabilidades:
    - Avaliar impacto das mudanças para usuários finais.
    - Classificar impacto (alto, médio, baixo).
    - Sugerir destaques para o release.
    """

    def run(self, state: WorkflowState) -> dict[str, ImpactAnalysisResult]:
        """Produz a análise de impacto do release em formato estruturado."""
        data = state["collected_data"]
        level = "high" if len(data.features) >= 3 else "medium" if data.features else "low"
        return {
            "impact_analysis": ImpactAnalysisResult(
                level=level,
                user_impact=f"Main impact for {state['audience']}: {len(data.features)} feature(s) delivered.",
            )
        }
