from datetime import datetime, timezone
from pathlib import Path

import httpx

from src.trend_radar.collectors.github_readme import GitHubReadmeFetcher
from src.trend_radar.collectors.github_trending import GitHubTrendingCollector
from src.trend_radar.schemas import CollectorConfig


def test_github_trending_normalizes_repository_items():
    html = Path("tests/fixtures/github_trending.html").read_text()
    readme = "# Agent Demo\n\nThis README explains the trending AI agent demo."

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/trending"
        return httpx.Response(200, text=html)

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://github.com",
    )
    readme_client = httpx.Client(
        transport=httpx.MockTransport(lambda request: httpx.Response(200, content=readme.encode("utf-8"))),
        base_url="https://api.github.com",
    )
    collector = GitHubTrendingCollector(
        client=client,
        readme_fetcher=GitHubReadmeFetcher(client=readme_client),
        now=lambda: datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
    )

    items = collector.collect(CollectorConfig(limit_per_source=10))

    assert len(items) == 1
    item = items[0]
    assert item.id == "github-trending-octo-agent-demo"
    assert item.title == "octo/agent-demo"
    assert str(item.url) == "https://github.com/octo/agent-demo"
    assert item.source == "GitHub Trending"
    assert item.raw_content == readme
    assert item.signals.stars == 1200
    assert item.signals.forks == 88
    assert item.signals.star_growth == 42
    assert item.signals.language == "Python"
    assert item.signals.owner_repo == "octo/agent-demo"
    assert item.signals.source_specific["readme_fetched"] is True
    assert item.signals.source_specific["readme_truncated"] is False
    assert item.eligibility.can_read is True


def test_github_trending_empty_page_returns_empty_list():
    client = httpx.Client(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(200, text="<html></html>")
        ),
        base_url="https://github.com",
    )
    collector = GitHubTrendingCollector(client=client)

    assert collector.collect(CollectorConfig()) == []
