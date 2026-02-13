from app.agents.state import RiskAnalysisResult, WorkflowState


class RiskRegressionAgent:
    def run(self, state: WorkflowState) -> dict[str, RiskAnalysisResult]:
        return {
            "risk_analysis": RiskAnalysisResult(
                level="low",
                technical_risk="Overall risk is low with attention needed on auth and billing services.",
                recommendations=[
                    "Monitor authentication service during rollout.",
                    "Monitor billing service during rollout.",
                ],
            )
        }
