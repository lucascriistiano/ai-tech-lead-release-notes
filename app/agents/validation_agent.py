from app.agents.state import ValidationResult, WorkflowState
from app.agents.tools import validate_release_notes_content, generate_release_notes_html

class ValidationAgent:
    """
    Guardião da Qualidade e Editor de Design.
    
    Fluxo:
    1. Audita o conteúdo (Texto -> Nota/Crítica).
    2. Se Aprovado (>6), gera o Dashboard HTML (Texto -> HTML).
    3. Retorna o resultado composto.
    """

    def run(self, state: WorkflowState) -> dict[str, ValidationResult]:
        formatted_notes = state.get("formatted_release_notes")
        markdown_content = formatted_notes.markdown if formatted_notes else ""
        
        version = state.get("version", "v0.0.0")
        audience = state.get("audience", "General")

        validation_output = validate_release_notes_content.invoke({
            "markdown": markdown_content,
            "version": version,
            "audience": audience
        })

        status = validation_output["status"]
        score = validation_output["score"]
        notes = validation_output["notes"]
        html_report = None

        if status == "approved":
            html_report = generate_release_notes_html.invoke({
                "markdown": markdown_content,
                "version": version,
                "audience": audience
            })
        else:
            # Opcional: Se quiser HTML mesmo reprovado, remova o 'else' e idente o invoke acima
            html_report = ""

        return {
            "validation": ValidationResult(
                status=status,
                score=score,
                notes=notes,
                html_report=html_report
            )
        }