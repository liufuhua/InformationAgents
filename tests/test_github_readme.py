import httpx

from src.trend_radar.collectors.github_readme import GitHubReadmeFetcher
from src.trend_radar.schemas import CollectorConfig


def test_github_readme_fetcher_returns_truncated_raw_readme():
    markdown = "# Agent Demo\n\n" + "A" * 30

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/repos/octo/agent-demo/readme"
        assert request.headers["accept"] == "application/vnd.github.raw"
        return httpx.Response(
            200,
            content=markdown.encode("utf-8"),
            headers={"x-github-readme-path": "README.md"},
        )

    client = httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://api.github.com",
    )
    fetcher = GitHubReadmeFetcher(client=client)

    result = fetcher.fetch(
        "octo/agent-demo",
        CollectorConfig(readme_max_chars=20),
    )

    assert result is not None
    assert result.content == markdown[:20]
    assert result.truncated is True
    assert result.size == len(markdown)
    assert result.path == "README.md"


def test_github_readme_fetcher_returns_none_when_readme_is_missing():
    client = httpx.Client(
        transport=httpx.MockTransport(lambda request: httpx.Response(404)),
        base_url="https://api.github.com",
    )
    fetcher = GitHubReadmeFetcher(client=client)

    assert fetcher.fetch("octo/missing-readme", CollectorConfig()) is None


def test_github_readme_fetcher_returns_none_when_github_errors():
    client = httpx.Client(
        transport=httpx.MockTransport(lambda request: httpx.Response(500)),
        base_url="https://api.github.com",
    )
    fetcher = GitHubReadmeFetcher(client=client)

    assert fetcher.fetch("octo/error-readme", CollectorConfig()) is None
