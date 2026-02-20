from datetime import date

from pydantic import BaseModel, Field, field_validator
from typing import Optional


class ReleaseNotesRequest(BaseModel):
    version: str = Field(..., examples=["v1.4.0"])
    from_date: date = Field(..., examples=["2026-01-01"])
    to_date: date = Field(..., examples=["2026-02-01"])
    audience: str = Field(..., examples=["clientes"])

    @field_validator("to_date")
    @classmethod
    def validate_dates(cls, value: date, info) -> date:
        from_date = info.data.get("from_date")
        if from_date and value < from_date:
            raise ValueError("to_date must be greater than or equal to from_date")
        return value


class ReleaseNotesResponse(BaseModel):
    status: str = Field(..., examples=["approved"])
    release_notes: str
    html_report: Optional[str] = None
    score: Optional[int] = None
