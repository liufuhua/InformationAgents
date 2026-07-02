from datetime import datetime, timezone

from src.trend_radar.dedupe import dedupe_source_items
from src.trend_radar.schemas import SourceEligibility, SourceItem, SourceSignals


def make_item(source: str, item_id: str, url: str, owner_repo: str) -> SourceItem:
    return SourceItem(
        id=item_id,
        title=owner_repo,
        source=source,
        url=url,
        collected_at=datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
        category="AI Project",
        raw_content=f"{owner_repo} description",
        signals=SourceSignals(owner_repo=owner_repo, stars=10),
        eligibility=SourceEligibility(can_read=True, reason="Has metadata"),
    )


def test_dedupe_merges_same_github_repo_and_preserves_evidence():
    search_item = make_item(
        "GitHub Search",
        "github-search-octo-agent-demo",
        "https://github.com/octo/agent-demo",
        "octo/agent-demo",
    )
    trending_item = make_item(
        "GitHub Trending",
        "github-trending-octo-agent-demo",
        "https://github.com/octo/agent-demo",
        "octo/agent-demo",
    )

    result = dedupe_source_items([search_item, trending_item])

    assert len(result) == 1
    merged = result[0]
    assert merged.id == "github-search-octo-agent-demo"
    assert merged.signals.owner_repo == "octo/agent-demo"
    assert len(merged.evidence) == 2
    assert {e.source for e in merged.evidence} == {"GitHub Search", "GitHub Trending"}


def test_dedupe_keeps_distinct_repositories():
    first = make_item(
        "GitHub Search",
        "github-search-octo-agent-demo",
        "https://github.com/octo/agent-demo",
        "octo/agent-demo",
    )
    second = make_item(
        "GitHub Search",
        "github-search-octo-agent-tool",
        "https://github.com/octo/agent-tool",
        "octo/agent-tool",
    )

    assert len(dedupe_source_items([first, second])) == 2
