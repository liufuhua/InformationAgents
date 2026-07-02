from datetime import datetime, timezone
from pathlib import Path

import httpx

from src.trend_radar.collectors.arxiv import ArxivCollector
from src.trend_radar.schemas import CollectorConfig


def test_arxiv_normalizes_atom_entries():
    xml = Path("tests/fixtures/arxiv_response.xml").read_text()

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/query"
        assert "AI agent" in request.url.params["search_query"]
        return httpx.Response(200, text=xml)

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://export.arxiv.org",
    )
    collector = ArxivCollector(
        client=client,
        now=lambda: datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
    )

    items = collector.collect(CollectorConfig(query="AI agent", limit_per_source=10))

    assert len(items) == 1
    item = items[0]
    assert item.id == "arxiv-2607.00001v1"
    assert item.title == "Agentic Evaluation for AI Systems"
    assert str(item.url) == "http://arxiv.org/abs/2607.00001v1"
    assert item.source == "arXiv"
    assert item.raw_content == "This paper studies evaluation methods for AI agents."
    assert item.signals.published_at == "2026-07-01T00:00:00Z"
    assert item.signals.updated_at == "2026-07-02T00:00:00Z"
    assert item.signals.source_specific["authors"] == ["Alice Example", "Bob Example"]
    assert item.signals.source_specific["categories"] == ["cs.AI", "cs.LG"]
    assert item.eligibility.can_read is True
