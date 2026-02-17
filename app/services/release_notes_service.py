# app/services/release_notes_service.py
from app.graphs.release_notes_graph import build_release_notes_graph
from app.models.release_notes import ReleaseNotesRequest
from app.util.file_handler import save_html_report

class ReleaseNotesService:
    def __init__(self) -> None:
        self.graph = build_release_notes_graph()

    def generate(self, payload: ReleaseNotesRequest) -> dict:
        result = self.graph.invoke(payload.model_dump())

        validation = result.get("validation")
        formatted_release_notes = result.get("formatted_release_notes")
        
        status = validation.status if validation else None
        release_notes = formatted_release_notes.markdown if formatted_release_notes else None

        if not status or not release_notes:
            raise RuntimeError("Failed to generate release notes")

        html_path = None
        html_url = None
        
        if validation and validation.html_report:
            # Salva o arquivo fisicamente
            saved_path = save_html_report(
                html_content=validation.html_report, 
                version=payload.version
            )
            html_path = saved_path
            # Gera uma URL simulada para retorno (opcional)
            html_url = f"http://localhost:8000/{saved_path}"

        return {
            "status": status,
            "release_notes": release_notes,
            "html_report": validation.html_report, # Conteúdo raw (se quiser exibir no front)
            "html_url": html_url,                  # Link clicável (se quiser abrir o arquivo)
            "score": validation.score
        }