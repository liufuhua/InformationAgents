import json
from datetime import datetime, timezone
from pathlib import Path

import httpx

from src.trend_radar.collectors.github_search import GitHubSearchCollector
from src.trend_radar.schemas import CollectorConfig


def test_github_search_normalizes_repository_items():
    fixture = json.loads(Path("tests/fixtures/github_search_response.json").read_text())

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/search/repositories"
        assert request.url.params["q"] == "AI agent"
        return httpx.Response(200, json=fixture)

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://api.github.com",
    )
    collector = GitHubSearchCollector(
        client=client,
        now=lambda: datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
    )

    items = collector.collect(CollectorConfig(query="AI agent", limit_per_source=10))

    assert len(items) == 1
    item = items[0]
    assert item.id == "github-search-octo-agent-demo"
    assert item.title == "octo/agent-demo"
    assert str(item.url) == "https://github.com/octo/agent-demo"
    assert item.source == "GitHub Search"
    assert item.raw_content == "An AI agent demo project."
    assert item.signals.stars == 1200
    assert item.signals.forks == 88
    assert item.signals.language == "Python"
    assert item.signals.owner_repo == "octo/agent-demo"
    assert item.eligibility.can_read is True


def test_github_search_handles_empty_results():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"total_count": 0, "items": []})

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://api.github.com",
    )
    collector = GitHubSearchCollector(client=client)

    assert collector.collect(CollectorConfig()) == []
