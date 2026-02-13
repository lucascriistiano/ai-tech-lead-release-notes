from app.agents.state import CollectedData, MetricsAnalysisResult, WorkflowState


class MetricsAgent:
    def run(self, state: WorkflowState) -> dict[str, MetricsAnalysisResult]:
        data = state.get("collected_data") or CollectedData(features=[], fixes=[], breaking_changes=[])
        return {
            "metrics_analysis": MetricsAnalysisResult(
                features_count=len(data.features),
                fixes_count=len(data.fixes),
                contributors_count=0,
            )
        }
