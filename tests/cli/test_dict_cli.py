from click.testing import CliRunner

from words.cli.dict_cli import dbs_cmd, define_cmd, dict_group, strategies_cmd


def test_words_dict_help():
    """
    WHEN: words dict --help
    THEN: all commands should be listed
    """
    runner = CliRunner()
    result = runner.invoke(dict_group, ["--help"])
    assert result.exit_code == 0

    for cmd in ("dbs", "strategies"):
        assert f"\n  {cmd} " in result.output


def test_words_dict_dbs_help():
    """
    WHEN: words dict dbs --help
    THEN: all options should be listed
    """
    runner = CliRunner()
    result = runner.invoke(dbs_cmd, ["--help"])
    assert result.exit_code == 0

    for opt in ("--search PHRASE", "--default"):
        assert f"\n  {opt} " in result.output


def test_words_dict_strategies_help():
    """
    WHEN: words dict strategies --help
    THEN: it should work
    """
    runner = CliRunner()
    result = runner.invoke(strategies_cmd, ["--help"])
    assert result.exit_code == 0


def test_words_define_help():
    """
    WHEN: words define --help
    THEN: all arguments should be listed
    """
    runner = CliRunner()
    result = runner.invoke(define_cmd, ["--help"])

    assert result.exit_code == 0
    assert "define [OPTIONS] WORD" in result.output
    for opt in ("--db DB", "--num INTEGER"):
        assert opt in result.output
