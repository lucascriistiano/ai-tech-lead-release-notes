from app.agents.state import RiskAnalysisResult, WorkflowState
from app.core.llm import chatgpt_text
import json

class RiskRegressionAgent:
    """Avalia riscos técnicos e possíveis regressões.

    Responsabilidades:
    - Analisar complexidade de fixes e breaking changes.
    - Sugerir ações preventivas e observações pós-release (Context-aware).
    """

    def run(self, state: WorkflowState) -> dict[str, RiskAnalysisResult]:
        data = state.get("collected_data")

        system_prompt = """
        <role>
        You are a Site Reliability Engineer (SRE) and QA Lead assessing deployment risks.
        </role>
        
        <rules>
        1. Read the fixes and breaking changes to identify technical risks (e.g., database locks, security patches, deprecated APIs).
        2. Classify risk level as "high", "medium", or "low". (Security patches and breaking changes automatically elevate risk).
        3. Write a 1-sentence technical risk summary.
        4. Provide 1 to 3 specific, actionable monitoring recommendations based *only* on the input data.
        </rules>
        
        <output_format>
        Return valid JSON only:
        {
            "level": "high|medium|low",
            "technical_risk": "Risk summary string",
            "recommendations": ["Rec 1", "Rec 2"]
        }
        </output_format>
        """

        user_prompt = f"""
        <input_data>
            <fixes>{data.fixes if data else []}</fixes>
            <breaking_changes>{data.breaking_changes if data else []}</breaking_changes>
        </input_data>
        """

        try:
            response = chatgpt_text(system_prompt=system_prompt, user_prompt=user_prompt)
            clean_json = response.replace("```json", "").replace("```", "").strip()
            result = json.loads(clean_json)
            
            level = result.get("level", "low")
            technical_risk = result.get("technical_risk", "Routine bug fixes and stability improvements.")
            recommendations = result.get("recommendations", ["Monitor system logs post-deployment."])
        except Exception:
            level = "high" if (data and data.breaking_changes) else "medium"
            technical_risk = "Fallback: Unable to parse detailed risk."
            recommendations = ["Monitor application health metrics."]

        return {
            "risk_analysis": RiskAnalysisResult(
                level=level,
                technical_risk=technical_risk,
                recommendations=recommendations
            )
        }