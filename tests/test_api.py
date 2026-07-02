from datetime import datetime, timezone
from pathlib import Path

from fastapi.testclient import TestClient

from api import main
from api.main import app
from src.trend_radar.schemas import CollectorRun


def test_collect_endpoint_triggers_one_run_and_returns_artifact(monkeypatch, tmp_path):
    calls = {"count": 0}

    def fake_run_trend_radar(config):
        calls["count"] += 1
        output_path = tmp_path / "2026-07-02-trend-radar.json"
        output_path.write_text("{}", encoding="utf-8")
        return (
            CollectorRun(
                run_id="2026-07-02-trend-radar",
                collected_at=datetime(2026, 7, 2, 10, 0, tzinfo=timezone.utc),
                enabled_sources=config.enabled_sources,
                items=[],
                errors=[],
            ),
            output_path,
        )

    monkeypatch.setattr(main, "run_trend_radar", fake_run_trend_radar)
    client = TestClient(app)

    response = client.post(
        "/api/trend-radar/collect",
        json={
            "query": "AI agent",
            "sources": ["github_search", "github_trending"],
            "limit": 20,
            "output_dir": str(tmp_path),
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert calls["count"] == 1
    assert payload["run"]["run_id"] == "2026-07-02-trend-radar"
    assert payload["output_path"] == str(Path(tmp_path) / "2026-07-02-trend-radar.json")
