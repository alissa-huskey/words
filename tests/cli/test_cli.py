from click.testing import CliRunner

from words import bp, WordsError  # noqa
from words.cli.cli import run


def test_cli_words_help():
    """
    WHEN: words --help
    THEN: all commands should be listed
    """
    runner = CliRunner()
    result = runner.invoke(run, ["--help"])
    assert result.exit_code == 0

    for cmd in ("def", "dict", "dm", "rand"):
        assert f"\n  {cmd} " in result.output
