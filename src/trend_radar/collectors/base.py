from typing import Protocol

from src.trend_radar.schemas import CollectorConfig, SourceItem


class SourceCollector(Protocol):
    name: str

    def collect(self, config: CollectorConfig) -> list[SourceItem]:
        ...
