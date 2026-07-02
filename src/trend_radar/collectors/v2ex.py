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


class V2EXCollector:
    name = "V2EX"

    def __init__(
        self,
        client: httpx.Client | None = None,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self.client = client or httpx.Client(base_url="https://www.v2ex.com")
        self.now = now or (lambda: datetime.now(timezone.utc))

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        response = self.client.get(
            "/api/topics/hot.json",
            timeout=config.request_timeout_seconds,
        )
        response.raise_for_status()

        collected_at = self.now()
        items: list[SourceItem] = []
        for topic in response.json()[: config.limit_per_source]:
            topic_id = str(topic["id"])
            node = topic.get("node") or {}
            member = topic.get("member") or {}
            items.append(
                SourceItem(
                    id=f"v2ex-{topic_id}",
                    title=topic.get("title") or "",
                    source=self.name,
                    url=topic["url"],
                    collected_at=collected_at,
                    category="Developer Discussion",
                    raw_content=topic.get("content") or topic.get("title") or "",
                    signals=SourceSignals(
                        comments=topic.get("replies"),
                        published_at=self._from_unix(topic.get("created")),
                        updated_at=self._from_unix(topic.get("last_modified")),
                        source_specific={
                            "node": node.get("name"),
                            "node_title": node.get("title"),
                            "member": member.get("username"),
                        },
                    ),
                    eligibility=SourceEligibility(
                        can_read=bool(topic.get("title") and topic.get("url")),
                        reason="Has V2EX topic title and URL",
                    ),
                )
            )
        return items

    def _from_unix(self, value: int | None) -> str | None:
        if value is None:
            return None
        return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()
