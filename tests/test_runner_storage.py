import json
from datetime import datetime, timezone

from src.trend_radar.schemas import CollectorRun
from src.trend_radar.storage import save_collector_run


def test_save_collector_run_writes_json(tmp_path):
    run = CollectorRun(
        run_id="2026-07-02-trend-radar",
        collected_at=datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
        enabled_sources=["github_search", "github_trending"],
        items=[],
        errors=[],
    )

    output_path = save_collector_run(run, tmp_path)

    assert output_path.name == "2026-07-02-trend-radar.json"
    payload = json.loads(output_path.read_text())
    assert payload["run_id"] == "2026-07-02-trend-radar"
    assert payload["enabled_sources"] == ["github_search", "github_trending"]
    assert payload["items"] == []


from src.trend_radar.runner import run_trend_radar
from src.trend_radar.runner import default_collectors
from src.trend_radar.schemas import CollectorConfig, SourceEligibility, SourceItem, SourceSignals


class FakeCollector:
    name = "Fake Source"

    def __init__(self) -> None:
        self.calls = 0

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        self.calls += 1
        return [
            SourceItem(
                id="fake-item",
                title="Fake item",
                source=self.name,
                url="https://example.com/fake",
                collected_at=datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
                category="AI Project",
                raw_content="Fake content",
                signals=SourceSignals(),
                eligibility=SourceEligibility(can_read=True, reason="Fake item"),
            )
        ]


def test_run_trend_radar_runs_collectors_once_and_saves(tmp_path):
    collector = FakeCollector()

    run, output_path = run_trend_radar(
        CollectorConfig(enabled_sources=["fake"], output_dir=str(tmp_path)),
        collectors={"fake": collector},
        now=lambda: datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
    )

    assert collector.calls == 1
    assert run.run_id == "2026-07-02-trend-radar"
    assert run.item_count == 1
    assert output_path.exists()


def test_default_collectors_include_all_documented_mvp_sources():
    collectors = default_collectors()

    assert "github_search" in collectors
    assert "github_trending" in collectors
    assert "hacker_news" in collectors
    assert "arxiv" in collectors
    assert "hugging_face" in collectors
    assert "v2ex" in collectors
