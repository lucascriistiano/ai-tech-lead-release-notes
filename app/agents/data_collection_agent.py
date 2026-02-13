from app.agents.state import CollectedData, WorkflowState
from app.agents.tools import fetch_github_changes, fetch_tasks_data


class DataCollectionAgent:
    """Coleta e normaliza os dados necessários para o release.

    Responsabilidades:
    - Interagir com APIs externas.
    - Buscar commits, PRs, issues e bugs.
    - Normalizar os dados coletados.
    """

    tools = [fetch_github_changes, fetch_tasks_data]

    def run(self, state: WorkflowState) -> dict[str, CollectedData]:
        """Retorna dados coletados em uma estrutura semântica compartilhada no estado."""
        github_data = fetch_github_changes.invoke(
            {
                "version": state["version"],
                "from_date": state["from_date"].isoformat(),
                "to_date": state["to_date"].isoformat(),
            }
        )
        tasks_data = fetch_tasks_data.invoke(
            {
                "version": state["version"],
                "from_date": state["from_date"].isoformat(),
                "to_date": state["to_date"].isoformat(),
            }
        )

        combined_fixes = list(dict.fromkeys(github_data.get("fixes", []) + tasks_data.get("bugs", [])))
        return {
            "collected_data": CollectedData(
                features=github_data.get("features", []),
                fixes=combined_fixes,
                breaking_changes=tasks_data.get("breaking_changes", []),
            )
        }
