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


class HuggingFaceCollector:
    name = "Hugging Face"

    def __init__(
        self,
        client: httpx.Client | None = None,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self.client = client or httpx.Client(base_url="https://huggingface.co")
        self.now = now or (lambda: datetime.now(timezone.utc))

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        response = self.client.get(
            "/api/models",
            params={
                "search": config.query,
                "sort": "downloads",
                "direction": -1,
                "limit": config.limit_per_source,
            },
            timeout=config.request_timeout_seconds,
        )
        response.raise_for_status()

        collected_at = self.now()
        items: list[SourceItem] = []
        for model in response.json()[: config.limit_per_source]:
            model_id = model["modelId"]
            items.append(
                SourceItem(
                    id="hugging-face-" + model_id.replace("/", "-").lower(),
                    title=model_id,
                    source=self.name,
                    url=f"https://huggingface.co/{model_id}",
                    collected_at=collected_at,
                    category="AI Model",
                    raw_content=model_id,
                    signals=SourceSignals(
                        published_at=model.get("createdAt"),
                        updated_at=model.get("lastModified"),
                        source_specific={
                            "likes": model.get("likes"),
                            "downloads": model.get("downloads"),
                            "pipeline_tag": model.get("pipeline_tag"),
                            "library_name": model.get("library_name"),
                        },
                    ),
                    eligibility=SourceEligibility(
                        can_read=bool(model_id),
                        reason="Has Hugging Face model ID",
                    ),
                )
            )
        return items
