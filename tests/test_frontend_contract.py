from pathlib import Path


def test_frontend_uses_design_tokens_and_one_time_collection_language():
    tokens = Path("web/src/styles/tokens.css").read_text(encoding="utf-8")
    app = Path("web/src/App.tsx").read_text(encoding="utf-8")

    assert "--color-canvas: #faf9f5" in tokens
    assert "--color-primary: #cc785c" in tokens
    assert "--color-surface-dark: #181715" in tokens
    assert "Run once" in app
    assert "setInterval" not in app
    assert "manual URL" not in app
    assert "loadLatestTrendRadar" in app
    assert "useEffect" in app


def test_frontend_proxies_api_requests_to_backend():
    vite_config = Path("web/vite.config.ts").read_text(encoding="utf-8")

    assert '"/api"' in vite_config
    assert "http://127.0.0.1:8000" in vite_config


def test_frontend_has_required_workbench_components():
    required_paths = [
        "web/src/components/SourceRail.tsx",
        "web/src/components/RunSummary.tsx",
        "web/src/components/ResultTable.tsx",
        "web/src/components/DetailDrawer.tsx",
        "web/src/api/trendRadar.ts",
    ]

    for path in required_paths:
        assert Path(path).exists(), path
