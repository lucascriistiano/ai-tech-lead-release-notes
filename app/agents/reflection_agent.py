from app.core.llm import chatgpt_text
from app.agents.state import PlanningResult, WorkflowState


class ReflectionAgent:
    """Planeja o release antes da execução dos demais agentes.

    Responsabilidades:
    - Interpretar o contexto do release.
    - Definir escopo, foco e critérios.
    - Planejar quais dados devem ser coletados.

    Simula o raciocínio inicial de um Tech Lead.
    """

    def run(self, state: WorkflowState) -> dict[str, PlanningResult]:
        """Gera o resultado de planejamento com base nos dados de entrada do release."""
        llm_summary = chatgpt_text(
            system_prompt=(
                "You are a senior tech lead planner. "
                "Generate a concise release planning summary with scope and data collection priorities."
            ),
            user_prompt=(
                f"Release version: {state['version']}\n"
                f"Window: {state['from_date']} to {state['to_date']}\n"
                f"Audience: {state['audience']}\n"
                "Return plain text only."
            ),
        )

        fallback_summary = (
            f"Generate release notes for {state['version']} from {state['from_date']} to {state['to_date']} "
            f"for audience '{state['audience']}'."
        )

        return {
            "planning": PlanningResult(
                summary=llm_summary or fallback_summary
            )
        }
