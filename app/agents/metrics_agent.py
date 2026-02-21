from app.agents.state import CollectedData, MetricsAnalysisResult, WorkflowState
from app.agents.tools import compute_release_metrics

class MetricsAgent:
    """Consolida métricas quantitativas do release.

    Responsabilidades:
    - Quantificar o escopo de forma 100% determinística.
    - NÃO usa LLM para evitar alucinações matemáticas.
    """

    def run(self, state: WorkflowState) -> dict[str, MetricsAnalysisResult]:
        
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
                features_count=metrics.get("features_count", 0),
                fixes_count=metrics.get("fixes_count", 0),
                contributors_count=metrics.get("contributors_count", 0),
            )
        }