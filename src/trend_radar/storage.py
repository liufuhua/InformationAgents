from __future__ import annotations

from pathlib import Path

from src.trend_radar.schemas import CollectorRun


def save_collector_run(run: CollectorRun, output_dir: str | Path) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    file_path = output_path / f"{run.run_id}.json"
    file_path.write_text(run.model_dump_json(indent=2), encoding="utf-8")
    return file_path
