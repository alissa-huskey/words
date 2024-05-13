from click.testing import CliRunner

from words.cli.dict_cli import define


def test_words_def_help():
    """
    WHEN: words def --help
    THEN: all arguments should be listed
    """
    runner = CliRunner()
    result = runner.invoke(define, ["--help"])
    assert result.exit_code == 0

    assert "def [OPTIONS] WORD" in result.output
