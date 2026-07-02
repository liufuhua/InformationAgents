from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone

import httpx

from src.trend_radar.schemas import (
    CollectorConfig,
    SourceEligibility,
    SourceItem,
    SourceSignals,
)


class HackerNewsCollector:
    name = "Hacker News"

    def __init__(
        self,
        client: httpx.Client | None = None,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self.client = client or httpx.Client(base_url="https://hn.algolia.com")
        self.now = now or (lambda: datetime.now(timezone.utc))

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        response = self.client.get(
            "/api/v1/search_by_date",
            params={
                "query": config.query,
                "tags": "story",
                "hitsPerPage": config.limit_per_source,
            },
            timeout=config.request_timeout_seconds,
        )
        response.raise_for_status()

        collected_at = self.now()
        items: list[SourceItem] = []
        for hit in response.json().get("hits", [])[: config.limit_per_source]:
            object_id = str(hit["objectID"])
            title = hit.get("title") or hit.get("story_title") or ""
            url = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"
            created_at = hit.get("created_at")
            signals = SourceSignals(
                comments=hit.get("num_comments"),
                published_at=created_at,
                source_specific={
                    "points": hit.get("points"),
                    "author": hit.get("author"),
                    "object_id": object_id,
                },
            )
            items.append(
                SourceItem(
                    id=f"hacker-news-{object_id}",
                    title=title,
                    source=self.name,
                    url=url,
                    collected_at=collected_at,
                    category="Developer Discussion",
                    raw_content=hit.get("story_text") or title,
                    signals=signals,
                    eligibility=SourceEligibility(
                        can_read=bool(title and url),
                        reason="Has Hacker News story title and URL",
                    ),
                )
            )
        return items
