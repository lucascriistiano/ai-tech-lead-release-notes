from app.agents.state import CollectedData, MetricsAnalysisResult, WorkflowState
from app.agents.tools import compute_release_metrics


class MetricsAgent:
    """Consolida métricas quantitativas do release.

    Responsabilidades:
    - Quantificar o escopo do release.
    - Contabilizar commits, bugs, features e contribuidores.
    - Gerar base para um resumo executivo.

    Útil para comunicação com stakeholders e liderança.
    """

    tools = [compute_release_metrics]

    def run(self, state: WorkflowState) -> dict[str, MetricsAnalysisResult]:
        """Calcula os indicadores principais a partir dos dados coletados."""
        data = state.get("collected_data") or CollectedData(features=[], fixes=[], breaking_changes=[])
        metrics = compute_release_metrics.invoke(
            {
                "features": data.features,
                "fixes": data.fixes,
                "bugs": data.fixes,
            }
        )
        return {
            "metrics_analysis": MetricsAnalysisResult(
                features_count=metrics["features_count"],
                fixes_count=metrics["fixes_count"],
                contributors_count=metrics["contributors_count"],
            )
        }
