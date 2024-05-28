from click.testing import CliRunner

from words import bp, WordsError  # noqa
from words.cli.def_cli import def_cmd


def test_cli_def_help():
    """
    WHEN: words def --help
    THEN: all arguments should be listed
    """
    runner = CliRunner()
    result = runner.invoke(def_cmd, ["--help"])

    assert result.exit_code == 0
    assert "def [OPTIONS] WORD" in result.output
    for opt in ("--num MAX"):
        assert opt in result.output
