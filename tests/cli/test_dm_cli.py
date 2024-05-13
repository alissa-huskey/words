from click.testing import CliRunner

from words.cli.dm_cli import dm_command


def test_words_dm_help():
    """
    WHEN: words dm --help
    THEN: all options should be listed
    """
    runner = CliRunner()
    result = runner.invoke(dm_command, ["--help"])
    assert result.exit_code == 0

    options = (
        "--ml WORD",
        "--sl WORD",
        "--sp PATTERN",
        "--rel-jja ADJECTIVE",
        "--rel-jjb NOUN",
        "--rel-syn WORD",
        "--rel-ant WORD",
        "--rel-trg WORD",
        "--rel-spc SUBTYPE",
        "--rel-gen SUPERTYPE",
        "--rel-com WHOLE",
        "--rel-par PART",
        "--rel-bga WORD BEFORE",
        "--rel-bgb WORD AFTER",
        "--rel-hom WORD",
        "--rel-cns WORD",
        "--max INTEGER",
        "--md [d|p|s|r|f]",
        "--ipa",
        "--json",
        "--long",
    )

    for opt in options:
        assert f"\n  {opt} " in result.output
