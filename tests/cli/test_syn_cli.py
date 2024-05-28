#  import pytest
from click.testing import CliRunner

from words import bp, WordsError  # noqa
from words.cli.syn_cli import syn_cmd


def test_cli_syn_help():
    """
    WHEN: words syn --help
    THEN: it should work
    AND: all options should be listed
    """
    runner = CliRunner()
    result = runner.invoke(syn_cmd, ["--help"])
    assert result.exit_code == 0

    for opt in ("--json", "--long", "--max INTEGER"):
        assert f"\n  {opt} " in result.output
