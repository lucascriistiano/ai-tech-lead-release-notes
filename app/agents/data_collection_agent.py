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
        """Retorna dados coletados mockados e estruturados."""
        
        github_data = fetch_github_changes.invoke({})
        tasks_data = fetch_tasks_data.invoke({})

        combined_fixes = []
        
        for fix in github_data.get("fixes", []):
            combined_fixes.append(f"[GitHub {fix['id']}] {fix['title']}: {fix['description']}")
            
        for bug in tasks_data.get("bugs", []):
            combined_fixes.append(f"[Jira {bug['ticket_id']}] {bug['summary']} - Resolução: {bug['resolution']}")

        combined_features = []
        for feat in github_data.get("features", []):
            combined_features.append(f"{feat['title']} ({feat['description']})")
        
        for feat in tasks_data.get("features", []):
            combined_features.append(f"{feat['summary']} - Impacto: {feat['business_value']}")

        return {
            "collected_data": CollectedData(
                features=combined_features,
                fixes=combined_fixes,
                breaking_changes=[
                    f"{bc['summary']}: {bc['description']} (Migration: {bc['migration_guide']})"
                    for bc in tasks_data.get("breaking_changes", [])
                ],
            )
        }