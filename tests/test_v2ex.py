import json
from datetime import datetime, timezone
from pathlib import Path

import httpx

from src.trend_radar.collectors.v2ex import V2EXCollector
from src.trend_radar.schemas import CollectorConfig


def test_v2ex_normalizes_hot_topics():
    fixture = json.loads(Path("tests/fixtures/v2ex_hot.json").read_text())

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/topics/hot.json"
        return httpx.Response(200, json=fixture)

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://www.v2ex.com",
    )
    collector = V2EXCollector(
        client=client,
        now=lambda: datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
    )

    items = collector.collect(CollectorConfig(limit_per_source=10))

    assert len(items) == 1
    item = items[0]
    assert item.id == "v2ex-9001"
    assert item.title == "大家最近在用哪些 AI Agent 工具？"
    assert str(item.url) == "https://www.v2ex.com/t/9001"
    assert item.source == "V2EX"
    assert item.raw_content == "想了解一下开发者日常使用的 AI Agent 工具。"
    assert item.signals.comments == 18
    assert item.signals.published_at == "2026-07-02T02:40:00+00:00"
    assert item.signals.updated_at == "2026-07-02T03:40:00+00:00"
    assert item.signals.source_specific["node"] == "programmer"
    assert item.eligibility.can_read is True
