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
    """Audita a qualidade do conteúdo."""
    
    if not markdown or len(markdown) < 50:
        return {
            "status": "needs_revision",
            "score": 0,
            "notes": ["O conteúdo está vazio ou insuficiente para análise."]
        }

    audit_system_prompt = """
    <role>You are a Senior QA Manager & Tech Editor.</role>
    <context>Strictly review Release Notes for clarity, completeness, and formatting.</context>
    <rules>
    1. Score from 0 to 10.
    2. Below 7 is rejected ('needs_revision'), 7 or above is 'approved'.
    3. Output valid JSON only.
    </rules>
    <output_format>
    {
        "score": int,
        "status": "approved" | "needs_revision",
        "critique": ["list of strings"]
    }
    </output_format>
    """
    
    audit_user_prompt = f"""
    <input_data>
        <version>{version}</version>
        <audience>{audience}</audience>
        <markdown_content>{markdown}</markdown_content>
    </input_data>
    """

    try:
        audit_raw = chatgpt_text(system_prompt=audit_system_prompt, user_prompt=audit_user_prompt)
        audit_json = audit_raw.replace("```json", "").replace("```", "").strip()
        audit_data = json.loads(audit_json)
        
        return {
            "status": "approved" if audit_data.get("score", 0) > 6 else "needs_revision",
            "score": audit_data.get("score", 0),
            "notes": audit_data.get("critique", [])
        }
    except Exception as e:
        return {"status": "needs_revision", "score": 0, "notes": [f"Erro na validação LLM: {str(e)}"]}


@tool
def generate_release_notes_html(markdown: str, version: str, audience: str) -> str:
    """Transforma o Markdown aprovado em um Dashboard HTML Tailwind."""
    
    html_system_prompt = """
    <role>You are an award-winning UI/UX Designer and Lead Frontend Engineer expert in Tailwind CSS.</role>
    <context>
    Your task is to convert Markdown Release Notes into a breathtaking, single-file HTML Executive Dashboard. 
    It will be presented on a large screen, so it requires a highly polished Dark Mode aesthetic, excellent readability, and a structured layout.
    </context>
    <rules>
    1. Theme: Premium Deep Dark Mode. Use `bg-slate-950` for the body, `bg-slate-900` for cards, and `border-slate-800` for subtle card outlines. 
    2. Typography: Import and use the 'Inter' font. Use generous font sizes (`text-slate-300` for body, `text-white` for headings). KPIs must have HUGE text (`text-5xl` or `text-6xl font-extrabold`).
    3. Layout: Use a Card-based CSS Grid (`grid-cols-1 lg:grid-cols-2`). Never use plain bullet lists (`<ul>`).
    4. Anti-Truncation: You MUST render EVERY SINGLE feature and EVERY SINGLE fix from the input content. DO NOT summarize, omit, or use "..." to shorten the lists. Map 100% of the items into their respective cards.
    5. Output ONLY raw, valid HTML5 starting with <!DOCTYPE html>. Absolutely no markdown code fences like ```html.
    </rules>
    """

    html_user_prompt = f"""
    <input_data>
        <version>{version}</version>
        <audience>{audience}</audience>
        <content>{markdown}</content>
    </input_data>

    <visual_requirements>
    1. **Imports**: `<script src="https://cdn.tailwindcss.com"></script>` and Google Fonts 'Inter'. Add a custom `<style>` block for a pure CSS Donut Chart (using `conic-gradient` masked with a dark inner circle).
    2. **Header**: Clean and impactful. Make the Version Title a glowing text gradient (`bg-clip-text text-transparent bg-gradient-to-r from-indigo-400 via-purple-400 to-cyan-400`). Add a pill-shaped badge: 'Status: Production' (`bg-emerald-500/20 text-emerald-400`).
    3. **Top Section (KPIs & Chart)**: 
       - Display 3 prominent KPI Cards side-by-side: Total Features, Total Fixes, and Risk Level. Center the numbers and make them massive. Risk text should be Red if high, Emerald if low.
       - Next to them, render the beautiful CSS-only Donut Chart representing the Features vs Fixes ratio.
    4. **Main Content (The Grid)**:
       - Two distinct columns: "New Features" (Left) and "Bug Fixes" (Right).
       - Encase EVERY item in its own card: `bg-slate-900 p-5 rounded-xl border border-slate-800 shadow-lg mb-4`.
       - Features get a left accent border: `border-l-4 border-emerald-500`.
       - Fixes get a left accent border: `border-l-4 border-rose-500`.
       - Bold the title/ID of the item in white, put the description below in `text-slate-400`.
    5. **Risks & Recommendations**:
       - Full-width block at the bottom of the page.
       - Styling: `bg-amber-950/30 border border-amber-700/50 rounded-xl p-6 text-amber-200`.
       - Show the Risk Level, then format the recommendations clearly with icons or styled bullets.
    </visual_requirements>
    """

    try:
        html_content = chatgpt_text(system_prompt=html_system_prompt, user_prompt=html_user_prompt)
        # Limpeza para garantir que o output seja puro HTML, removendo formatações do LLM
        clean_html = html_content.replace("```html", "").replace("```", "").strip()
        return clean_html
    except Exception:
        return ""