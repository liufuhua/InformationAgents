from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.trend_radar.runner import run_trend_radar
from src.trend_radar.schemas import CollectorConfig, CollectorRun
from src.trend_radar.storage import load_latest_collector_run

app = FastAPI(title="InformationAgents API")


class TrendRadarCollectRequest(BaseModel):
    query: str = "AI agent"
    sources: list[str] = Field(
        default_factory=lambda: ["github_search", "github_trending"]
    )
    limit: int = 20
    output_dir: str = "data/runs"
    fetch_readme: bool = True
    readme_max_chars: int = 20000


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
        fetch_readme=request.fetch_readme,
        readme_max_chars=request.readme_max_chars,
    )
    run, output_path = run_trend_radar(config)
    return TrendRadarCollectResponse(run=run, output_path=str(output_path))


@app.get("/api/trend-radar/latest", response_model=TrendRadarCollectResponse)
def get_latest_trend_radar(output_dir: str = "data/runs") -> TrendRadarCollectResponse:
    latest = load_latest_collector_run(output_dir)
    if latest is None:
        raise HTTPException(status_code=404, detail="No trend radar run found")

    run, output_path = latest
    return TrendRadarCollectResponse(run=run, output_path=str(output_path))
