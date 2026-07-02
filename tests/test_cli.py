from typer.testing import CliRunner

from cli.trend_radar import app


def test_cli_help_shows_one_time_collection_command():
    runner = CliRunner()

    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Run AI Trend Radar once" in result.output
    assert "--source" in result.output
