from app.agents.state import CollectedData, WorkflowState


class DataCollectionAgent:
    def run(self, state: WorkflowState) -> dict[str, CollectedData]:
        # Placeholder for GitHub/Jira API integrations.
        return {
            "collected_data": CollectedData(
                features=["Feature A", "Feature B"],
                fixes=["Bug Fix C"],
                breaking_changes=[],
            )
        }
