from __future__ import annotations

import os

from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.trend_radar.runner import run_trend_radar
from src.trend_radar.schemas import CollectorConfig, CollectorRun

app = FastAPI(title="InformationAgents API")


class TrendRadarCollectRequest(BaseModel):
    query: str = "AI agent"
    sources: list[str] = Field(
        default_factory=lambda: ["github_search", "github_trending"]
    )
    limit: int = 20
    output_dir: str = "data/runs"


class TrendRadarCollectResponse(BaseModel):
    run: CollectorRun
    output_path: str


@app.post("/api/trend-radar/collect", response_model=TrendRadarCollectResponse)
def collect_trend_radar(request: TrendRadarCollectRequest) -> TrendRadarCollectResponse:
    config = CollectorConfig(
        enabled_sources=request.sources,
        query=request.query,
        limit_per_source=request.limit,
        output_dir=request.output_dir,
        github_token=os.getenv("GITHUB_TOKEN"),
    )
    run, output_path = run_trend_radar(config)
    return TrendRadarCollectResponse(run=run, output_path=str(output_path))
