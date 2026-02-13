from app.agents.state import ValidationResult, WorkflowState
from app.agents.tools import validate_release_notes_content


class ValidationAgent:
    """Valida qualidade e completude do conteúdo final.

    Responsabilidades:
    - Revisar clareza e completude.
    - Detectar omissões ou redundâncias.
    - Aprovar ou solicitar ajustes.

    Representa um loop de validação com papel de revisão humana.
    """

    tools = [validate_release_notes_content]

    def run(self, state: WorkflowState) -> dict[str, ValidationResult]:
        """Define o status final da validação e anotações de revisão."""
        formatted_release_notes = state.get("formatted_release_notes")
        validation = validate_release_notes_content.invoke(
            {"markdown": formatted_release_notes.markdown if formatted_release_notes else ""}
        )
        return {
            "validation": ValidationResult(
                status=validation["status"],
                notes=validation["notes"],
            )
        }
