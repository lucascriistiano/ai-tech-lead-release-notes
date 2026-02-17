from langchain_core.tools import tool
from typing import Optional
from app.core.llm import chatgpt_text
import json

@tool
def fetch_github_changes(input_data: Optional[dict] = None) -> dict:
    """
    Simula a busca de PRs e Commits do GitHub.
    Retorna dados técnicos brutos categorizados.
    """
    # Simulando um delay de rede para realismo nos logs
    # time.sleep(0.5)
    
    return {
        "features": [
            {
                "id": "PR-452",
                "title": "feat(api): Implement Idempotency Key support",
                "description": "Adds support for Idempotency-Key header in POST /transactions to prevent double charges on network failures.",
                "author": "backend-ninja",
                "files_changed": ["app/core/middleware.py", "app/api/v1/transactions.py"]
            },
            {
                "id": "PR-455",
                "title": "feat(dashboard): Dark Mode Toggle",
                "description": "Implements system-wide dark mode based on user preference using Tailwind classes.",
                "author": "frontend-wizard",
                "files_changed": ["frontend/src/theme.ts", "frontend/src/components/*"]
            },
            {
                "id": "PR-470",
                "title": "feat(auth): 2FA with Authenticator App",
                "description": "Adds TOTP support (Google/Microsoft Authenticator) for user login.",
                "author": "security-team",
                "files_changed": ["app/auth/totp.py", "app/models/user.py"]
            },
            {
                "id": "PR-472",
                "title": "feat(reports): Export transactions to PDF",
                "description": "New endpoint to generate PDF statements for merchants.",
                "author": "junior-dev",
                "files_changed": ["app/services/pdf_generator.py"]
            },
            {
                "id": "PR-475",
                "title": "feat(integrations): Slack Webhooks for payments",
                "description": "Allows merchants to receive Slack notifications on successful payments.",
                "author": "backend-ninja",
                "files_changed": ["app/integrations/slack.py"]
            },
            {
                "id": "PR-480",
                "title": "feat(mobile): Biometric login support",
                "description": "React Native bridge for FaceID/TouchID.",
                "author": "mobile-team",
                "files_changed": ["mobile/src/auth/Biometrics.ts"]
            }
        ],
        "fixes": [
            {
                "id": "PR-460",
                "title": "fix(db): Resolve deadlock in wallet transfer",
                "description": "Fixes a critical race condition where simultaneous transfers could lock the row indefinitely. Applied SELECT FOR UPDATE SKIP LOCKED.",
                "author": "db-admin",
                "files_changed": ["app/services/transfer_service.py"],
                "severity": "high"
            },
            {
                "id": "PR-461",
                "title": "fix(ui): Correct decimal rounding on invoice PDF",
                "description": "Invoices were showing 10.999 instead of 11.00. Fixed formatting utility.",
                "author": "junior-dev",
                "files_changed": ["app/utils/formatters.py"]
            },
            {
                "id": "PR-465",
                "title": "fix(security): Patch SQL Injection vulnerability in Search",
                "description": "Sanitized inputs on the global search bar. Critical fix.",
                "author": "security-team",
                "files_changed": ["app/api/search.py"],
                "severity": "critical"
            },
            {
                "id": "PR-466",
                "title": "fix(api): Handle null phone numbers in webhook payload",
                "description": "Prevents 500 error when phone number is missing in legacy payloads.",
                "author": "backend-dev",
                "files_changed": ["app/schemas/webhook.py"]
            },
            {
                "id": "PR-468",
                "title": "fix(ios): Fix crash on startup iOS 17",
                "description": "Updated splash screen library to support newer iOS versions.",
                "author": "mobile-team",
                "files_changed": ["mobile/ios/Podfile"]
            },
            {
                "id": "PR-490",
                "title": "fix(ui): Alignment issue on Settings page",
                "description": "Fixed 2px misalignment in the submit button.",
                "author": "frontend-wizard",
                "files_changed": ["frontend/src/pages/Settings.tsx"]
            }
        ],
        "performance": [
            {
                "id": "PR-449",
                "title": "perf(cache): Redis caching for user permissions",
                "description": "Reduces latency on all authenticated requests by 150ms.",
                "author": "ops-lead"
            },
            {
                "id": "PR-485",
                "title": "perf(db): Index on transaction_date column",
                "description": "Speeds up monthly reporting queries by 80%.",
                "author": "db-admin"
            },
             {
                "id": "PR-488",
                "title": "perf(frontend): Lazy load dashboard charts",
                "description": "Reduces initial bundle size by 200kb.",
                "author": "frontend-wizard"
            }
        ],
        "chore": [
             {
                "id": "PR-492",
                "title": "chore(deps): Bump boto3 to 1.28",
                "description": "Routine dependency update.",
                "author": "dependabot"
            },
            {
                "id": "PR-493",
                "title": "chore(ci): Fix flaky test in pipeline",
                "description": "Increased timeout for integration tests.",
                "author": "ops-lead"
            },
            {
                "id": "PR-495",
                "title": "refactor(utils): Cleanup old date formatting code",
                "description": "Removed unused functions.",
                "author": "junior-dev"
            }
        ]
    }


@tool
def fetch_tasks_data(input_data: Optional[dict] = None) -> dict:
    """
    Simula a busca de tasks, user stories e epics no Jira.
    Foca no 'porquê' e no impacto para o cliente.
    """
    
    return {
        "features": [
            {
                "ticket_id": "JIRA-1024",
                "type": "Story",
                "summary": "Suporte a PIX Automático",
                "business_value": "High demand from Brazilian customers. Expected to increase transaction volume by 15%.",
                "status": "Done"
            },
            {
                "ticket_id": "JIRA-1040",
                "type": "Story",
                "summary": "Painel de Controle de Fraude",
                "business_value": "Allows admins to block suspicious IPs manually. Reduces chargeback risks.",
                "status": "Done"
            },
            {
                "ticket_id": "JIRA-1055",
                "type": "Story",
                "summary": "Integração com Slack",
                "business_value": "Requested by 3 major enterprise clients for workflow automation.",
                "status": "Done"
            },
            {
                "ticket_id": "JIRA-1060",
                "type": "Story",
                "summary": "Suporte a Multi-moeda (USD/EUR)",
                "business_value": "Expands market reach to international merchants.",
                "status": "Done"
            },
            {
                "ticket_id": "JIRA-1080",
                "type": "Story",
                "summary": "Login Biométrico Mobile",
                "business_value": "Improves user retention and login speed on mobile apps.",
                "status": "Done"
            }
        ],
        "bugs": [
            {
                "ticket_id": "JIRA-998",
                "type": "Bug",
                "summary": "Erro 500 ao exportar CSV gigante",
                "root_cause": "Memory overflow on large datasets.",
                "resolution": "Implemented streaming response.",
                "customer_impact": "Medium - affects only enterprise users."
            },
             {
                "ticket_id": "JIRA-1002",
                "type": "Bug",
                "summary": "Vulnerabilidade de SQL Injection na busca",
                "root_cause": "Missing input sanitization.",
                "resolution": "Applied parameter binding.",
                "customer_impact": "Critical - Security risk."
            },
            {
                "ticket_id": "JIRA-1015",
                "type": "Bug",
                "summary": "App trava ao abrir no iOS 17",
                "root_cause": "Incompatible library version.",
                "resolution": "Library upgrade.",
                "customer_impact": "High - iOS users cannot access the app."
            },
            {
                "ticket_id": "JIRA-1033",
                "type": "Bug",
                "summary": "Cobrança duplicada em oscilação de rede",
                "root_cause": "Missing idempotency key.",
                "resolution": "Implemented idempotency logic.",
                "customer_impact": "High - Financial loss and support tickets."
            }
        ],
        "breaking_changes": [
            {
                "ticket_id": "JIRA-1100",
                "type": "Technical Task",
                "summary": "Deprecation of XML API Endpoints",
                "description": "The old XML endpoints /api/xml/charge are now removed. Clients must switch to JSON.",
                "migration_guide": "Use standard JSON payload. See docs v2.1.",
                "mandatory": True
            },
            {
                "ticket_id": "JIRA-1105",
                "type": "Technical Task",
                "summary": "Python 3.11 Upgrade",
                "description": "Backend is now running on Python 3.11.",
                "migration_guide": "No action needed for clients, but self-hosted instances need to upgrade runtime.",
                "mandatory": True
            }
        ],
        "improvements": [
            {
                "ticket_id": "JIRA-1045",
                "type": "Improvement",
                "summary": "Redução de Latência no Dashboard",
                "business_value": "Better UX for power users.",
                "status": "Done"
            },
             {
                "ticket_id": "JIRA-1046",
                "type": "Improvement",
                "summary": "Melhoria mensagens de erro API",
                "business_value": "Reduces integration support time.",
                "status": "Done"
            }
        ]
    }


@tool
def compute_release_metrics(features: list[str], fixes: list[str], bugs: list[str]) -> dict:
    """Compute release-level quantitative metrics."""
    return {
        "features_count": len(features),
        "fixes_count": len(fixes),
        "bugs_count": len(bugs),
        "contributors_count": 0,
    }

@tool
def build_release_notes_markdown(
    version: str,
    audience: str,
    features: list[str],
    fixes: list[str],
    level: str,
    technical_risk: str,
    recommendations: list[str],
    summary: str,
) -> str:
    """Build Markdown text for release notes."""
    features_md = "\n".join(f"- {item}" for item in features) or "- None"
    fixes_md = "\n".join(f"- {item}" for item in fixes) or "- None"
    level_md = level or "Unknown"
    technical_risk_md = technical_risk or "- None"
    recommendations_md = "\n".join(f"- {item}" for item in recommendations) or "- None"
    return (
        f"## Release {version}\n\n"
        f"Audience: {audience}\n\n"
        "### New Features\n"
        f"{features_md}\n\n"
        "### Fixes\n"
        f"{fixes_md}\n\n"
        "### Risks\n"
        f"Level: {level_md}\n\n"
        f"{technical_risk_md}\n\n"
        "### Recommendations\n"
        f"{recommendations_md}\n\n"
        "### Summary\n"
        f"{summary or 'No summary generated.'}"
    )

@tool
def validate_release_notes_content(markdown: str, version: str, audience: str) -> dict:
    """
    Analisa a qualidade do conteúdo, consistência e tom do Release Note.
    Retorna uma nota (0-10) e uma lista de críticas.
    """
    
    if not markdown or len(markdown) < 50:
        return {
            "status": "needs_revision",
            "score": 0,
            "notes": ["O conteúdo está vazio ou insuficiente para análise."]
        }

    audit_system_prompt = (
        "You are a Senior QA Manager & Tech Editor. "
        "Your job is to strictly review Release Notes based on: Clarity, Completeness (Features vs Fixes), and Risk Assessment accuracy. "
        "Scoring Rules:\n"
        "- Below 5: Critical info missing or bad formatting.\n"
        "- 5-6: Good content but needs polish (typos, vague descriptions).\n"
        "- 7+: Ready for publication.\n"
        "Output JSON only: {score: int, status: 'approved'|'needs_revision', critique: list[str]}."
    )
    
    audit_user_prompt = (
        f"Context: Version {version} for Audience {audience}.\n"
        f"Content to Audit:\n---\n{markdown}\n---"
    )

    try:
        audit_raw = chatgpt_text(system_prompt=audit_system_prompt, user_prompt=audit_user_prompt)
        # Limpeza para garantir JSON válido
        audit_json = audit_raw.replace("```json", "").replace("```", "").strip()
        audit_data = json.loads(audit_json)
        
        # Garante estrutura mínima
        return {
            "status": "approved" if audit_data.get("score", 0) > 6 else "needs_revision",
            "score": audit_data.get("score", 0),
            "notes": audit_data.get("critique", [])
        }
    except Exception as e:
        return {
            "status": "needs_revision", 
            "score": 0, 
            "notes": [f"Erro na validação LLM: {str(e)}"]
        }

@tool
def generate_release_notes_html(markdown: str, version: str, audience: str) -> str:
    """
    Transforma o Markdown aprovado em um Dashboard HTML Executivo e Moderno.
    Usa Tailwind CSS, Cards e Gráficos CSS puros.
    """
    
    html_system_prompt = (
        "You are a World-Class Frontend Developer specialized in Tailwind CSS. "
        "Your goal is to convert Markdown Release Notes into a stunning, single-file HTML Dashboard. "
        "Do NOT use simple bullet lists. Use a Card-based Grid layout. "
        "Aesthetic: Stripe-like, clean, modern typography (Inter), with 'Glassmorphism' elements."
    )

    html_user_prompt = f"""
    TRANSFORM THIS DATA INTO A HIGH-FIDELITY HTML DASHBOARD.

    CONTEXT:
    - Version: {version}
    - Audience: {audience}
    - Content Source: {markdown}

    VISUAL REQUIREMENTS (STRICT):
    1. **Setup**: 
       - Use `<script src="https://cdn.tailwindcss.com"></script>`.
       - Import Google Font 'Inter'. Body font-family: 'Inter'.
       - Background: `bg-slate-50`.

    2. **Header**: 
       - Dark Slate background (`bg-slate-900`) with a subtle gradient text for the title.
       - Add a 'Status: Production' badge.

    3. **KPI Row (Top Section)**:
       - Extract these numbers from text: Total Features, Total Fixes, Risk Level.
       - Display them as 3 Big Cards (`bg-white shadow-lg rounded-xl`).
       - **Risk Logic**: If High -> Text Red. If Low -> Text Green.

    4. **Visual Chart (CSS Only)**:
       - Inside a card, create a CSS `conic-gradient` circle (Donut Chart) representing Features vs Fixes ratio.
       - Add a small legend (Green=Features, Red=Fixes).

    5. **Main Grid (The Content)**:
       - Layout: 2 Columns (1 col on mobile).
       - **Column 1 (New Features)**: 
         - Do NOT use `<ul>`. Create individual `<div class="bg-white p-4 rounded-lg shadow-sm border-l-4 border-emerald-500 mb-3">` cards for each feature.
         - Include an SVG check icon.
       - **Column 2 (Fixes)**: 
         - Create individual `<div class="bg-white p-4 rounded-lg shadow-sm border-l-4 border-rose-500 mb-3">` cards for each fix.
         - Include an SVG bug icon.

    6. **Risk & Recommendations**:
       - A full-width banner at the bottom using `bg-orange-50` and `border-orange-200`.

    7. **Output**:
       - Return ONLY raw HTML code. No markdown fences (```html).
    """

    try:
        html_content = chatgpt_text(system_prompt=html_system_prompt, user_prompt=html_user_prompt)
        return html_content.replace("```html", "").replace("```", "").strip()
    except Exception:
        return ""