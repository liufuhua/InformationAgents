from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone

import httpx

from src.trend_radar.collectors.github_readme import GitHubReadmeFetcher
from src.trend_radar.schemas import (
    CollectorConfig,
    SourceEligibility,
    SourceItem,
    SourceSignals,
)


class GitHubSearchCollector:
    name = "GitHub Search"

    def __init__(
        self,
        client: httpx.Client | None = None,
        readme_fetcher: GitHubReadmeFetcher | None = None,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self.client = client or httpx.Client(base_url="https://api.github.com")
        self.readme_fetcher = readme_fetcher or GitHubReadmeFetcher(client=self.client)
        self.now = now or (lambda: datetime.now(timezone.utc))

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        headers = {"Accept": "application/vnd.github+json"}
        if config.github_token:
            headers["Authorization"] = f"Bearer {config.github_token}"

        response = self.client.get(
            "/search/repositories",
            params={
                "q": config.query,
                "sort": "stars",
                "order": "desc",
                "per_page": config.limit_per_source,
            },
            headers=headers,
            timeout=config.request_timeout_seconds,
        )
        response.raise_for_status()

        collected_at = self.now()
        items = []
        for repo in response.json().get("items", []):
            owner_repo = repo["full_name"]
            item_id = "github-search-" + owner_repo.replace("/", "-").lower()
            description = repo.get("description") or ""
            signals = SourceSignals(
                stars=repo.get("stargazers_count"),
                forks=repo.get("forks_count"),
                language=repo.get("language"),
                owner_repo=owner_repo,
                updated_at=repo.get("updated_at"),
            )
            raw_content = description
            if config.fetch_readme:
                readme = self.readme_fetcher.fetch(owner_repo, config)
                if readme:
                    raw_content = readme.content
                    signals.source_specific.update(
                        {
                            "readme_fetched": True,
                            "readme_truncated": readme.truncated,
                            "readme_size": readme.size,
                            "readme_path": readme.path,
                        }
                    )
                else:
                    signals.source_specific["readme_fetched"] = False
            items.append(
                SourceItem(
                    id=item_id,
                    title=owner_repo,
                    source=self.name,
                    url=repo["html_url"],
                    collected_at=collected_at,
                    category="AI Project",
                    raw_content=raw_content,
                    signals=signals,
                    eligibility=SourceEligibility(
                        can_read=bool(repo.get("html_url") and owner_repo),
                        reason="Has repository URL and metadata",
                    ),
                )
            )
        return items
