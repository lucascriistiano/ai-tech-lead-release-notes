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
        return {
            "planning": PlanningResult(
                summary=(
                    f"Generate release notes for {state['version']} from {state['from_date']} to {state['to_date']} "
                    f"for audience '{state['audience']}'."
                )
            )
        }
