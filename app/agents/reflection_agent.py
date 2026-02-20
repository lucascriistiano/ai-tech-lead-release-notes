from app.core.llm import chatgpt_text
from app.agents.state import PlanningResult, WorkflowState
import json

class ReflectionAgent:
    """
    Planejador Estratégico (The Orchestrator).
    
    Ele não apenas resume, ele define a 'Estratégia Editorial' do Release Note.
    Ele analisa a versão (Major/Minor/Patch) e o público para ditar o tom.
    """

    def run(self, state: WorkflowState) -> dict[str, PlanningResult]:
        system_prompt = """
        <role>
        You are the Chief Technical Editor and Architect responsible for planning the release notes strategy.
        Your goal is to analyze the input metadata and dictate the guidelines for the Data Collection, Impact Analysis, and Risk agents.
        </role>

        <context>
        We are generating release notes for a software product. The downstream agents depend on your strategic direction to know what to filter and emphasize.
        </context>

        <rules>
        1. Analyze the version number (SemVer):
        - Major (e.g., 2.0.0): Focus on new features, migration guides, and high impact.
        - Minor (e.g., 1.2.0): Focus on improvements and non-breaking features.
        - Patch (e.g., 1.2.1): Focus on bug fixes, stability, and security.
        2. Analyze the Audience:
        - "Stakeholders/Execs": Focus on business value, ROI, and high-level metrics. Tone: Professional & Celebratory.
        - "Developers/Internal": Focus on technical details, refactoring, APIs, and breaking changes. Tone: Technical & Direct.
        - "Clients/Users": Focus on usability, new capabilities, and fixed annoyances. Tone: Helpful & Welcoming.
        </rules>

        <output_format>
        Return a structured JSON with the following keys:
        - "strategy_summary": A high-level 2-sentence summary of the release goal.
        - "data_collection_focus": Specific keywords or ticket types the DataCollectionAgent should prioritize (e.g., "urgent bugs", "API changes").
        - "tone_voice": The adjective describing the writing style.
        - "highlight_criteria": What constitutes a "highlight" for this specific release.
        </output_format>
        """

        user_prompt = f"""
        <input_data>
            <version>{state['version']}</version>
            <date_range>{state['from_date']} to {state['to_date']}</date_range>
            <audience>{state['audience']}</audience>
        </input_data>
        """

        llm_response = chatgpt_text(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        try:
            plan_data = json.loads(llm_response.replace("```json", "").replace("```", ""))
            
            final_summary = json.dumps(plan_data, indent=2)
        except:
            final_summary = llm_response
            
        return {
            "planning": PlanningResult(
                summary=final_summary
            )
        }