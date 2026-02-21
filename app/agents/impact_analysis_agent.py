from app.agents.state import ImpactAnalysisResult, WorkflowState
from app.core.llm import chatgpt_text
import json

class ImpactAnalysisAgent:
    """Analisa o impacto das mudanças para usuários finais.

    Responsabilidades:
    - Avaliar o 'valor de negócio' ou 'melhoria de UX' das entregas.
    - Classificar o impacto (high, medium, low) de forma inteligente.
    - Gerar um resumo direcionado ao público (audience).
    """

    def run(self, state: WorkflowState) -> dict[str, ImpactAnalysisResult]:
        data = state.get("collected_data")
        audience = state.get("audience", "General")

        system_prompt = """
        <role>
        You are a Senior Product Manager analyzing a new software release.
        </role>
        
        <rules>
        1. Evaluate the semantic business impact of the provided features and fixes.
        2. Classify the impact level as "high", "medium", or "low". (e.g., A new payment method is High; a typo fix is Low).
        3. Write a concise, 1-2 sentence summary of the main impact tailored to the target audience.
        </rules>
        
        <output_format>
        Return valid JSON only:
        {
            "level": "high|medium|low",
            "user_impact": "Summary string here"
        }
        </output_format>
        """

        user_prompt = f"""
        <input_data>
            <audience>{audience}</audience>
            <features>{data.features if data else []}</features>
        </input_data>
        """

        try:
            response = chatgpt_text(system_prompt=system_prompt, user_prompt=user_prompt)
            clean_json = response.replace("```json", "").replace("```", "").strip()
            result = json.loads(clean_json)
            
            level = result.get("level", "medium")
            user_impact = result.get("user_impact", "Routine updates and improvements.")
        except Exception:
            # Fallback determinístico caso o LLM falhe (Zero Side Effects)
            features_count = len(data.features) if data else 0
            level = "high" if features_count >= 3 else "medium" if features_count > 0 else "low"
            user_impact = f"Main impact for {audience}: {features_count} feature(s) delivered."

        return {
            "impact_analysis": ImpactAnalysisResult(
                level=level,
                user_impact=user_impact
            )
        }