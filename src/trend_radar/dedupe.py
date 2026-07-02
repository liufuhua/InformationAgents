from __future__ import annotations

from src.trend_radar.schemas import SourceEvidence, SourceItem


def dedupe_source_items(items: list[SourceItem]) -> list[SourceItem]:
    merged: dict[str, SourceItem] = {}

    for item in items:
        key = _dedupe_key(item)
        evidence = SourceEvidence(
            source=item.source,
            url=item.url,
            collected_at=item.collected_at,
            signals=item.signals,
        )

        if key not in merged:
            merged[key] = item.model_copy(update={"evidence": [evidence]})
            continue

        existing = merged[key]
        merged[key] = existing.model_copy(
            update={"evidence": [*existing.evidence, evidence]}
        )

    return list(merged.values())


def _dedupe_key(item: SourceItem) -> str:
    if item.signals.owner_repo:
        return f"github:{item.signals.owner_repo.lower()}"
    return f"url:{str(item.url).rstrip('/').lower()}"
