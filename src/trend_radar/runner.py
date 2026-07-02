from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.trend_radar.collectors.github_search import GitHubSearchCollector
from src.trend_radar.collectors.github_trending import GitHubTrendingCollector
from src.trend_radar.dedupe import dedupe_source_items
from src.trend_radar.schemas import (
    CollectorConfig,
    CollectorError,
    CollectorRun,
    SourceItem,
)
from src.trend_radar.storage import save_collector_run


def default_collectors() -> dict[str, Any]:
    return {
        "github_search": GitHubSearchCollector(),
        "github_trending": GitHubTrendingCollector(),
    }


def run_trend_radar(
    config: CollectorConfig,
    collectors: dict[str, Any] | None = None,
    now: Callable[[], datetime] | None = None,
) -> tuple[CollectorRun, Path]:
    current_time = (now or (lambda: datetime.now(timezone.utc)))()
    collector_map = collectors or default_collectors()
    collected_items: list[SourceItem] = []
    errors: list[CollectorError] = []

    for source_key in config.enabled_sources:
        collector = collector_map[source_key]
        try:
            collected_items.extend(collector.collect(config))
        except Exception as exc:
            errors.append(
                CollectorError(
                    source=getattr(collector, "name", source_key),
                    message=str(exc),
                )
            )

    run = CollectorRun(
        run_id=f"{current_time.date().isoformat()}-trend-radar",
        collected_at=current_time,
        enabled_sources=config.enabled_sources,
        items=dedupe_source_items(collected_items),
        errors=errors,
    )
    output_path = save_collector_run(run, config.output_dir)
    return run, output_path
