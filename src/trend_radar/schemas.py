from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, HttpUrl


class SourceSignals(BaseModel):
    stars: int | None = None
    star_growth: int | None = None
    comments: int | None = None
    forks: int | None = None
    language: str | None = None
    owner_repo: str | None = None
    published_at: str | None = None
    updated_at: str | None = None
    source_specific: dict[str, Any] = Field(default_factory=dict)


class SourceEligibility(BaseModel):
    can_read: bool
    reason: str


class SourceEvidence(BaseModel):
    source: str
    url: HttpUrl
    collected_at: datetime
    signals: SourceSignals = Field(default_factory=SourceSignals)


class SourceItem(BaseModel):
    id: str
    title: str
    source: str
    url: HttpUrl
    collected_at: datetime
    category: str | None = None
    raw_content: str
    signals: SourceSignals
    eligibility: SourceEligibility
    evidence: list[SourceEvidence] = Field(default_factory=list)


class CollectorError(BaseModel):
    source: str
    message: str


class CollectorConfig(BaseModel):
    enabled_sources: list[str] = Field(
        default_factory=lambda: ["github_search", "github_trending"]
    )
    query: str = "AI agent"
    language: str | None = None
    date: str | None = None
    limit_per_source: int = 20
    request_timeout_seconds: float = 20.0
    retry_count: int = 0
    output_dir: str = "data/runs"
    github_token: str | None = None


class CollectorRun(BaseModel):
    run_id: str
    collected_at: datetime
    enabled_sources: list[str]
    items: list[SourceItem]
    errors: list[CollectorError] = Field(default_factory=list)

    @property
    def item_count(self) -> int:
        return len(self.items)

    @property
    def error_count(self) -> int:
        return len(self.errors)
