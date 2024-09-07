from click.testing import CliRunner

from words import bp, WordsError  # noqa
from words.cli.lookup_cli import lookup_group


def test_cli_lookup_help():
    """
    WHEN: words lookup --help
    THEN: all commands should be listed
    """
    runner = CliRunner()
    result = runner.invoke(lookup_group, ["--help"])
    assert result.exit_code == 0

    assert "Look up a word on a website." in result.output
