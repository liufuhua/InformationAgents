from typer.testing import CliRunner

from cli.trend_radar import app


def test_cli_root_help_shows_collect_command():
    runner = CliRunner()

    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "AI Trend Radar command line tools" in result.output
    assert "collect" in result.output


def test_cli_collect_help_shows_collection_options():
    runner = CliRunner()

    result = runner.invoke(app, ["collect", "--help"])

    assert result.exit_code == 0
    assert "Run AI Trend Radar once" in result.output
    assert "--source" in result.output
