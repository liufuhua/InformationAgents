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
    assert "Hacker News" in app
    assert "arXiv" in app
    assert "Hugging Face" in app
    assert "V2EX" in app
    api_client = Path("web/src/api/trendRadar.ts").read_text(encoding="utf-8")
    assert '"hacker_news"' in api_client
    assert '"arxiv"' in api_client
    assert '"hugging_face"' in api_client
    assert '"v2ex"' in api_client


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


def test_detail_drawer_renders_markdown_content():
    detail_drawer = Path("web/src/components/DetailDrawer.tsx").read_text(encoding="utf-8")
    package_json = Path("web/package.json").read_text(encoding="utf-8")

    assert "react-markdown" in package_json
    assert "remark-gfm" in package_json
    assert "ReactMarkdown" in detail_drawer
    assert "remarkGfm" in detail_drawer
    assert "markdown-body" in detail_drawer


def test_detail_panel_is_wider_and_has_markdown_styles():
    styles = Path("web/src/styles/app.css").read_text(encoding="utf-8")

    assert "minmax(500px, 36vw)" in styles
    assert ".markdown-body" in styles
    assert ".markdown-body pre" in styles
    assert ".markdown-body code" in styles


def test_detail_drawer_scrolls_to_top_when_item_changes():
    detail_drawer = Path("web/src/components/DetailDrawer.tsx").read_text(encoding="utf-8")

    assert "useEffect" in detail_drawer
    assert "useRef" in detail_drawer
    assert "detailPanelRef" in detail_drawer
    assert "scrollTo({ top: 0" in detail_drawer
    assert "[item?.id]" in detail_drawer
