from app.agents.state import ValidationResult, WorkflowState


class ValidationAgent:
    def run(self, state: WorkflowState) -> dict[str, ValidationResult]:
        formatted_release_notes = state.get("formatted_release_notes")
        has_release_notes = bool(formatted_release_notes and formatted_release_notes.markdown)
        notes = [] if has_release_notes else ["Release notes content is empty."]
        return {
            "validation": ValidationResult(
                status="approved" if has_release_notes else "needs_revision",
                notes=notes,
            )
        }
