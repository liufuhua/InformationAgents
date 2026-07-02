from datetime import datetime, timezone

from src.trend_radar.schemas import (
    CollectorConfig,
    CollectorError,
    CollectorRun,
    SourceEligibility,
    SourceItem,
    SourceSignals,
)


def test_source_item_serializes_required_fields():
    item = SourceItem(
        id="github-search-owner-repo",
        title="owner/repo",
        source="GitHub Search",
        url="https://github.com/owner/repo",
        collected_at=datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
        category="AI Project",
        raw_content="A useful AI project.",
        signals=SourceSignals(stars=1200, published_at="2026-07-01"),
        eligibility=SourceEligibility(can_read=True, reason="Has repository metadata"),
    )

    dumped = item.model_dump(mode="json")

    assert dumped["id"] == "github-search-owner-repo"
    assert dumped["signals"]["stars"] == 1200
    assert dumped["eligibility"]["can_read"] is True


def test_collector_config_defaults_to_single_run_data_path():
    config = CollectorConfig()

    assert config.enabled_sources == ["github_search", "github_trending"]
    assert config.output_dir == "data/runs"
    assert config.limit_per_source == 20


def test_collector_run_counts_items_and_errors():
    run = CollectorRun(
        run_id="2026-07-02-trend-radar",
        collected_at=datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
        enabled_sources=["github_search"],
        items=[],
        errors=[
            CollectorError(
                source="GitHub Search",
                message="rate limited",
            )
        ],
    )

    assert run.item_count == 0
    assert run.error_count == 1


from src.trend_radar.collectors.base import SourceCollector


def test_source_collector_protocol_shape():
    assert hasattr(SourceCollector, "collect")
    assert SourceCollector.__annotations__["name"] is str
