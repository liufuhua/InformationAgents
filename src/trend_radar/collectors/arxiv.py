from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone
from xml.etree import ElementTree

import httpx

from src.trend_radar.schemas import (
    CollectorConfig,
    SourceEligibility,
    SourceItem,
    SourceSignals,
)


ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


class ArxivCollector:
    name = "arXiv"

    def __init__(
        self,
        client: httpx.Client | None = None,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self.client = client or httpx.Client(base_url="https://export.arxiv.org")
        self.now = now or (lambda: datetime.now(timezone.utc))

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        response = self.client.get(
            "/api/query",
            params={
                "search_query": f'all:"{config.query}"',
                "start": 0,
                "max_results": config.limit_per_source,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            },
            timeout=config.request_timeout_seconds,
        )
        response.raise_for_status()

        root = ElementTree.fromstring(response.text)
        collected_at = self.now()
        items: list[SourceItem] = []
        for entry in root.findall("atom:entry", ATOM_NS)[: config.limit_per_source]:
            url = self._text(entry, "atom:id")
            title = " ".join(self._text(entry, "atom:title").split())
            summary = " ".join(self._text(entry, "atom:summary").split())
            published_at = self._text(entry, "atom:published")
            updated_at = self._text(entry, "atom:updated")
            authors = [
                self._text(author, "atom:name")
                for author in entry.findall("atom:author", ATOM_NS)
            ]
            categories = [
                category.attrib["term"]
                for category in entry.findall("atom:category", ATOM_NS)
                if category.attrib.get("term")
            ]
            arxiv_id = url.rsplit("/", 1)[-1]
            items.append(
                SourceItem(
                    id="arxiv-" + arxiv_id,
                    title=title,
                    source=self.name,
                    url=url,
                    collected_at=collected_at,
                    category="AI Paper",
                    raw_content=summary,
                    signals=SourceSignals(
                        published_at=published_at,
                        updated_at=updated_at,
                        source_specific={
                            "authors": authors,
                            "categories": categories,
                            "arxiv_id": arxiv_id,
                        },
                    ),
                    eligibility=SourceEligibility(
                        can_read=bool(title and url and summary),
                        reason="Has arXiv title, abstract, and URL",
                    ),
                )
            )
        return items

    def _text(self, entry: ElementTree.Element, path: str) -> str:
        node = entry.find(path, ATOM_NS)
        return node.text.strip() if node is not None and node.text else ""
