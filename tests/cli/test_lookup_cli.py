from click.testing import CliRunner

from words import bp, WordsError  # noqa
from words.cli.lookup_cli import lookup_cmd


def test_cli_lookup_help():
    """
    WHEN: words lookup --help
    THEN: all commands should be listed
    """
    runner = CliRunner()
    result = runner.invoke(lookup_cmd, ["--help"])
    assert result.exit_code == 0

    options = (
        "-l, --list",
    )

    for opt in options:
        assert f"\n  {opt} " in result.output
