import json
from datetime import datetime, timezone
from pathlib import Path

import httpx

from src.trend_radar.collectors.hugging_face import HuggingFaceCollector
from src.trend_radar.schemas import CollectorConfig


def test_hugging_face_normalizes_model_results():
    fixture = json.loads(Path("tests/fixtures/hugging_face_models.json").read_text())

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/models"
        assert request.url.params["search"] == "AI agent"
        return httpx.Response(200, json=fixture)

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://huggingface.co",
    )
    collector = HuggingFaceCollector(
        client=client,
        now=lambda: datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
    )

    items = collector.collect(CollectorConfig(query="AI agent", limit_per_source=10))

    assert len(items) == 1
    item = items[0]
    assert item.id == "hugging-face-octo-agent-model"
    assert item.title == "octo/agent-model"
    assert str(item.url) == "https://huggingface.co/octo/agent-model"
    assert item.source == "Hugging Face"
    assert item.raw_content == "octo/agent-model"
    assert item.signals.updated_at == "2026-07-02T07:00:00.000Z"
    assert item.signals.source_specific["likes"] == 77
    assert item.signals.source_specific["downloads"] == 12345
    assert item.signals.source_specific["pipeline_tag"] == "text-generation"
    assert item.eligibility.can_read is True
