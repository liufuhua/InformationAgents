import json
from datetime import datetime, timezone
from pathlib import Path

import httpx

from src.trend_radar.collectors.hacker_news import HackerNewsCollector
from src.trend_radar.schemas import CollectorConfig


def test_hacker_news_normalizes_story_hits():
    fixture = json.loads(Path("tests/fixtures/hacker_news_response.json").read_text())

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/v1/search_by_date"
        assert request.url.params["query"] == "AI agent"
        assert request.url.params["tags"] == "story"
        return httpx.Response(200, json=fixture)

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://hn.algolia.com",
    )
    collector = HackerNewsCollector(
        client=client,
        now=lambda: datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
    )

    items = collector.collect(CollectorConfig(query="AI agent", limit_per_source=10))

    assert len(items) == 1
    item = items[0]
    assert item.id == "hacker-news-401"
    assert item.title == "Show HN: Tiny AI agent debugger"
    assert str(item.url) == "https://example.com/agent-debugger"
    assert item.source == "Hacker News"
    assert item.raw_content == "A small tool for debugging AI agents."
    assert item.signals.comments == 45
    assert item.signals.published_at == "2026-07-02T08:00:00Z"
    assert item.signals.source_specific["points"] == 123
    assert item.signals.source_specific["author"] == "octo"
    assert item.eligibility.can_read is True
