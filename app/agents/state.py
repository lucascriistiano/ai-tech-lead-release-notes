from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import TypedDict, List, Optional
from pydantic import Field

@dataclass
class PlanningResult:
    summary: str

@dataclass
class CollectedData:
    features: list[str]
    fixes: list[str]
    breaking_changes: list[str]

@dataclass
class ImpactAnalysisResult:
    level: str
    user_impact: str

@dataclass
class RiskAnalysisResult:
    level: str
    technical_risk: str
    recommendations: list[str]

@dataclass
class MetricsAnalysisResult:
    features_count: int
    fixes_count: int
    contributors_count: int

@dataclass
class SynthesisResult:
    executive_summary: str

@dataclass
class FormattedReleaseNotes:
    markdown: str

@dataclass
class ValidationResult:
    status: str = Field(..., description="'approved' ou 'needs_revision'")
    score: int = Field(..., description="Nota de 0 a 10 dada pelo auditor")
    notes: List[str] = Field(default_factory=list, description="Críticas e sugestões de melhoria")
    html_report: Optional[str] = Field(None, description="O dashboard HTML gerado para o cliente")

class WorkflowState(TypedDict, total=False):
    version: str
    from_date: date
    to_date: date
    audience: str
    planning: PlanningResult
    collected_data: CollectedData
    impact_analysis: ImpactAnalysisResult
    risk_analysis: RiskAnalysisResult
    metrics_analysis: MetricsAnalysisResult
    synthesis: SynthesisResult
    formatted_release_notes: FormattedReleaseNotes
    validation: ValidationResult
