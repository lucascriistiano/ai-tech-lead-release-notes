# Multi-Agent Release Notes Generator

Sistema multiagente para gerar release notes automaticamente com Python, FastAPI e LangGraph.

## Objective

Automatizar a criação de release notes claras, completas e rastreáveis com base em dados de desenvolvimento (commits, PRs, issues, bugs), reduzindo trabalho manual e risco de omissões.

## Architecture Overview

Fluxo principal:

`API REST -> Reflection -> Data Collection -> (Impact + Risk + Metrics) -> Synthesis -> Formatting -> Validation -> Release Notes`

## Project Structure

```text
.
├── app/
│   ├── agents/
│   │   ├── state.py
│   │   ├── reflection_agent.py
│   │   ├── data_collection_agent.py
│   │   ├── impact_analysis_agent.py
│   │   ├── risk_regression_agent.py
│   │   ├── metrics_agent.py
│   │   ├── synthesis_agent.py
│   │   ├── formatting_agent.py
│   │   └── validation_agent.py
│   ├── api/
│   │   ├── v1/
│   │   │   └── release_notes.py
│   │   └── router.py
│   ├── core/
│   │   └── config.py
│   ├── graphs/
│   │   └── release_notes_graph.py
│   ├── models/
│   │   └── release_notes.py
│   ├── services/
│   │   └── release_notes_service.py
│   └── main.py
├── tests/
│   ├── test_health.py
│   └── test_release_notes.py
├── .env.example
├── .gitignore
├── Makefile
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Main Dependencies

- `fastapi`
- `uvicorn[standard]`
- `langgraph`
- `langchain`
- `pydantic`
- `pydantic-settings`
- `python-dotenv`
- `httpx`
- `pytest` (dev/test)

## Environment Setup

### Requirements

- Python 3.11+
- `venv`

### 1) Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
make install
```

### 3) Configure environment variables

```bash
cp .env.example .env
```

Fill in:

```env
APP_ENV=development
OPENAI_API_KEY=your_key
GITHUB_TOKEN=your_token
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your_email
JIRA_API_TOKEN=your_token
```

## Run for Development

```bash
make run
```

- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`

## API Endpoint

### `POST /v1/release-notes`

Request:

```json
{
  "version": "v1.4.0",
  "from_date": "2026-01-01",
  "to_date": "2026-02-01",
  "audience": "clientes"
}
```

Response:

```json
{
  "status": "approved",
  "release_notes": "## Release v1.4.0\n..."
}
```

## Tests

```bash
make test
```

## Notes

- O workflow no `app/graphs/release_notes_graph.py` já está conectado com os nós principais de agentes.
- As integrações reais com GitHub/Jira podem ser implementadas no agente de coleta (`DataCollectionAgent`) e em serviços dedicados.
