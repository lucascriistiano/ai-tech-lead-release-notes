from app.agents.state import PlanningResult, WorkflowState


class ReflectionAgent:
    def run(self, state: WorkflowState) -> dict[str, PlanningResult]:
        return {
            "planning": PlanningResult(
                summary=(
                    f"Generate release notes for {state['version']} from {state['from_date']} to {state['to_date']} "
                    f"for audience '{state['audience']}'."
                )
            )
        }
