from __future__ import annotations

import os
from typing import Annotated

import typer

from src.trend_radar.runner import run_trend_radar
from src.trend_radar.schemas import CollectorConfig

app = typer.Typer(help="Run AI Trend Radar once.")


@app.command()
def collect(
    query: Annotated[str, typer.Option(help="GitHub Search query.")] = "AI agent",
    source: Annotated[
        list[str],
        typer.Option(help="Source key. Use multiple --source flags for multiple sources."),
    ] = ["github_search", "github_trending"],
    limit: Annotated[int, typer.Option(help="Max items per source.")] = 20,
    output_dir: Annotated[str, typer.Option(help="Directory for run JSON files.")] = "data/runs",
) -> None:
    """Run AI Trend Radar once and save one JSON artifact."""

    config = CollectorConfig(
        enabled_sources=source,
        query=query,
        limit_per_source=limit,
        output_dir=output_dir,
        github_token=os.getenv("GITHUB_TOKEN"),
    )
    run, output_path = run_trend_radar(config)
    typer.echo(
        f"Collected {run.item_count} items with {run.error_count} errors. "
        f"Saved to {output_path}"
    )


if __name__ == "__main__":
    app()
