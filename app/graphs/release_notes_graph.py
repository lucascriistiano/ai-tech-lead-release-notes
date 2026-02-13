from langgraph.graph import END, START, StateGraph

from app.agents import (
    DataCollectionAgent,
    FormattingAgent,
    ImpactAnalysisAgent,
    MetricsAgent,
    ReflectionAgent,
    RiskRegressionAgent,
    SynthesisAgent,
    ValidationAgent,
    WorkflowState,
)


def build_release_notes_graph():
    reflection = ReflectionAgent()
    data_collection = DataCollectionAgent()
    impact = ImpactAnalysisAgent()
    risk = RiskRegressionAgent()
    metrics = MetricsAgent()
    synthesis = SynthesisAgent()
    formatting = FormattingAgent()
    validation = ValidationAgent()

    workflow = StateGraph(WorkflowState)

    workflow.add_node("reflection", reflection.run)
    workflow.add_node("data_collection", data_collection.run)
    workflow.add_node("impact", impact.run)
    workflow.add_node("risk", risk.run)
    workflow.add_node("metrics", metrics.run)
    workflow.add_node("synthesis", synthesis.run)
    workflow.add_node("formatting", formatting.run)
    workflow.add_node("validation", validation.run)

    workflow.add_edge(START, "reflection")
    workflow.add_edge("reflection", "data_collection")

    workflow.add_edge("data_collection", "impact")
    workflow.add_edge("data_collection", "risk")
    workflow.add_edge("data_collection", "metrics")

    workflow.add_edge(["impact", "risk", "metrics"], "synthesis")

    workflow.add_edge("synthesis", "formatting")
    workflow.add_edge("formatting", "validation")
    workflow.add_edge("validation", END)

    return workflow.compile()
