from __future__ import annotations

import re
from collections.abc import Callable
from datetime import datetime, timezone

import httpx
from bs4 import BeautifulSoup

from src.trend_radar.schemas import (
    CollectorConfig,
    SourceEligibility,
    SourceItem,
    SourceSignals,
)


class GitHubTrendingCollector:
    name = "GitHub Trending"

    def __init__(
        self,
        client: httpx.Client | None = None,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self.client = client or httpx.Client(base_url="https://github.com")
        self.now = now or (lambda: datetime.now(timezone.utc))

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        response = self.client.get(
            "/trending",
            params=self._build_params(config),
            timeout=config.request_timeout_seconds,
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        collected_at = self.now()
        items: list[SourceItem] = []
        for article in soup.select("article.Box-row")[: config.limit_per_source]:
            link = article.select_one("h2 a")
            if not link or not link.get("href"):
                continue

            owner_repo = self._normalize_owner_repo(link.get_text(" ", strip=True))
            url = "https://github.com" + link["href"]
            description_tag = article.select_one("p")
            raw_content = (
                description_tag.get_text(" ", strip=True) if description_tag else ""
            )
            language_tag = article.select_one('[itemprop="programmingLanguage"]')
            language = language_tag.get_text(" ", strip=True) if language_tag else None
            stars = self._number_from_text(article, "stargazers")
            forks = self._number_from_text(article, "forks")
            star_growth = self._stars_today(article.get_text(" ", strip=True))

            signals = SourceSignals(
                stars=stars,
                forks=forks,
                star_growth=star_growth,
                language=language,
                owner_repo=owner_repo,
            )
            items.append(
                SourceItem(
                    id="github-trending-" + owner_repo.replace("/", "-").lower(),
                    title=owner_repo,
                    source=self.name,
                    url=url,
                    collected_at=collected_at,
                    category="AI Project",
                    raw_content=raw_content,
                    signals=signals,
                    eligibility=SourceEligibility(
                        can_read=True,
                        reason="Has repository URL from GitHub Trending",
                    ),
                )
            )
        return items

    def _build_params(self, config: CollectorConfig) -> dict[str, str]:
        params: dict[str, str] = {"since": "daily"}
        if config.language:
            params["spoken_language_code"] = config.language
        return params

    def _normalize_owner_repo(self, text: str) -> str:
        return re.sub(r"\s+", "", text)

    def _number_from_text(self, article: object, href_part: str) -> int | None:
        tag = article.select_one(f'a[href*="{href_part}"]')
        if not tag:
            return None
        digits = re.sub(r"[^0-9]", "", tag.get_text())
        return int(digits) if digits else None

    def _stars_today(self, text: str) -> int | None:
        match = re.search(r"([0-9,]+)\s+stars?\s+today", text)
        if not match:
            return None
        return int(match.group(1).replace(",", ""))
