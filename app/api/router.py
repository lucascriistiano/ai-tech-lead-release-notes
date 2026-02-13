from fastapi import APIRouter

from app.api.v1.release_notes import router as release_notes_router


api_router = APIRouter()
api_router.include_router(release_notes_router, tags=["release-notes"])
