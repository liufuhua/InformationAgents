from __future__ import annotations

from pathlib import Path

from src.trend_radar.schemas import CollectorRun


def save_collector_run(run: CollectorRun, output_dir: str | Path) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    file_path = output_path / f"{run.run_id}.json"
    file_path.write_text(run.model_dump_json(indent=2), encoding="utf-8")
    return file_path


def load_latest_collector_run(output_dir: str | Path) -> tuple[CollectorRun, Path] | None:
    output_path = Path(output_dir)
    if not output_path.exists():
        return None

    run_paths = sorted(
        output_path.glob("*.json"),
        key=lambda path: (path.stat().st_mtime, path.name),
        reverse=True,
    )
    if not run_paths:
        return None

    latest_path = run_paths[0]
    return (
        CollectorRun.model_validate_json(latest_path.read_text(encoding="utf-8")),
        latest_path,
    )
