from fastapi import APIRouter, HTTPException

from app.models.release_notes import ReleaseNotesRequest, ReleaseNotesResponse
from app.services.release_notes_service import ReleaseNotesService


router = APIRouter()
service = ReleaseNotesService()


@router.post("/release-notes", response_model=ReleaseNotesResponse)
def generate_release_notes(payload: ReleaseNotesRequest) -> ReleaseNotesResponse:
    try:
        result = service.generate(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return ReleaseNotesResponse(**result)
