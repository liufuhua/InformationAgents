from __future__ import annotations

from dataclasses import dataclass

import httpx

from src.trend_radar.schemas import CollectorConfig


@dataclass(frozen=True)
class GitHubReadmeResult:
    content: str
    truncated: bool
    size: int
    path: str | None = None


class GitHubReadmeFetcher:
    def __init__(self, client: httpx.Client | None = None) -> None:
        self.client = client or httpx.Client(base_url="https://api.github.com")

    def fetch(
        self,
        owner_repo: str,
        config: CollectorConfig,
    ) -> GitHubReadmeResult | None:
        headers = {"Accept": "application/vnd.github.raw"}
        if config.github_token:
            headers["Authorization"] = f"Bearer {config.github_token}"

        try:
            response = self.client.get(
                f"/repos/{owner_repo}/readme",
                headers=headers,
                timeout=config.request_timeout_seconds,
            )
            response.raise_for_status()
        except httpx.HTTPError:
            return None

        content = response.text
        size = len(content)
        truncated = size > config.readme_max_chars
        if truncated:
            content = content[: config.readme_max_chars]

        return GitHubReadmeResult(
            content=content,
            truncated=truncated,
            size=size,
            path=response.headers.get("x-github-readme-path"),
        )
