from app.agents.state import ImpactAnalysisResult, WorkflowState


class ImpactAnalysisAgent:
    def run(self, state: WorkflowState) -> dict[str, ImpactAnalysisResult]:
        return {
            "impact_analysis": ImpactAnalysisResult(
                level="medium",
                user_impact="Onboarding flow improved for end users.",
            )
        }
