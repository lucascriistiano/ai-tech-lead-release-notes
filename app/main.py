from fastapi import FastAPI

from app.api.router import api_router


app = FastAPI(
    title="Multi-Agent Release Notes Generator",
    version="0.1.0",
    description="REST API for generating release notes using a LangGraph multi-agent workflow.",
)

app.include_router(api_router, prefix="/v1")


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
