from click.testing import CliRunner

from words import bp, WordsError  # noqa
from words.cli.dict_cli import (
    dbs_cmd,
    define_cmd,
    dict_group,
    match_cmd,
    strategies_cmd,
)


def test_cli_dict_help():
    """
    WHEN: words dict --help
    THEN: all commands should be listed
    """
    runner = CliRunner()
    result = runner.invoke(dict_group, ["--help"])
    assert result.exit_code == 0

    for cmd in ("dbs", "strategies"):
        assert f"\n  {cmd} " in result.output


def test_cli_dict_dbs_help():
    """
    WHEN: words dict dbs --help
    THEN: all options should be listed
    """
    runner = CliRunner()
    result = runner.invoke(dbs_cmd, ["--help"])
    assert result.exit_code == 0

    for opt in ("--search PHRASE", "--default"):
        assert f"\n  {opt} " in result.output


def test_cli_dict_strategies_help():
    """
    WHEN: words dict strategies --help
    THEN: it should work
    """
    runner = CliRunner()
    result = runner.invoke(strategies_cmd, ["--help"])
    assert result.exit_code == 0


def test_cli_dict_define_help():
    """
    WHEN: words dict define --help
    THEN: all arguments should be listed
    """
    runner = CliRunner()
    result = runner.invoke(define_cmd, ["--help"])

    assert result.exit_code == 0
    assert "define [OPTIONS] WORD" in result.output
    for opt in ("--db DB", "--num MAX"):
        assert opt in result.output


def test_cli_dict_match_help():
    """
    WHEN: words dict match --help
    THEN: it should workd
    AND: all arguments should be listed
    """
    runner = CliRunner()
    result = runner.invoke(match_cmd, ["--help"])

    assert result.exit_code == 0
    assert "match [OPTIONS] WORD" in result.output
    options = (
        "-s, --strat STRATEGY",
        "-d, --db DB",
    )

    for opt in options:
        assert opt in result.output
