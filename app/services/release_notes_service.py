from app.graphs.release_notes_graph import build_release_notes_graph
from app.models.release_notes import ReleaseNotesRequest


class ReleaseNotesService:
    def __init__(self) -> None:
        self.graph = build_release_notes_graph()

    def generate(self, payload: ReleaseNotesRequest) -> dict[str, str]:
        result = self.graph.invoke(payload.model_dump())

        validation = result.get("validation")
        formatted_release_notes = result.get("formatted_release_notes")
        status = validation.status if validation else None
        release_notes = formatted_release_notes.markdown if formatted_release_notes else None

        if not status or not release_notes:
            raise RuntimeError("Failed to generate release notes")

        return {
            "status": status,
            "release_notes": release_notes,
        }
