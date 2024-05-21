from re import compile as re_compile

import pytest
from click.testing import CliRunner

from words.cli.rand_cli import color_cmd, name_cmd, rand_group, word_cmd

from .. import Stub

bp = breakpoint
HEX_FINDER = re_compile(r'#[A-Z0-9]{6}')
HEADER_FINDER = re_compile(r'─ ([A-Z][a-z]+ )+─')


class Params(Stub):
    """Stub class for parametrization."""

    options: tuple = tuple()
    content: tuple = tuple()
    exclude: tuple = tuple()
    patterns: dict = {}
    size: int = None
    skip: bool = False
    message: str = None


def test_cli_rand_help():
    """
    WHEN: words rand --help
    THEN: all commands should be listed
    """
    runner = CliRunner()
    result = runner.invoke(rand_group, ["--help"])
    assert result.exit_code == 0

    for cmd in ("color", "name"):
        assert f"\n  {cmd} " in result.output


def test_cli_rand_color_help():
    """
    WHEN: words rand --help
    THEN: all options should be listed
    """
    runner = CliRunner()
    result = runner.invoke(color_cmd, ["--help"])
    assert result.exit_code == 0

    options = (
        "-s, --simple",
        "-v, --verbose",
        "-n, --num MAX",
    )

    for opt in options:
        assert f"\n  {opt} " in result.output


def test_cli_rand_name_help():
    """
    WHEN: words rand --help
    THEN: all commands should be listed
    """
    runner = CliRunner()
    result = runner.invoke(name_cmd, ["--help"])
    assert result.exit_code == 0

    options = (
        "-b, --boy",
        "-g, --girl",
        "-l, --last",
        "-f, --full",
        "-n, --num INTEGER",
        "-m, --max MAX",
    )

    for opt in options:
        assert f"\n  {opt} " in result.output


@pytest.mark.parametrize("params", [
    Params(options=("--boy",), content=("Boy Names",), size=3),
    Params(options=("--girl",), content=("Girl Names",), size=3),
    Params(options=("--last",), content=("Last Names",), size=3),
    Params(
        options=("--girl", "--max", "100"),
        content=("Girl Names",),
        size=3,
    ),
    Params(
        options=("--boy", "--num", "5"),
        content=("Boy Names",),
        size=7,
    ),
    Params(
        options=("--boy", "--girl", "--last"),
        content=("Boy Names", "Girl Names", "Last Names"),
        size=3,
    ),
    Params(
        options=("--girl", "--full"),
        content=("Girl Full Names",),
    ),
    Params(
        options=("--girl", "--full"),
        content=("Girl Full Names",),
    ),
    Params(
        options=("--girl", "--boy", "--full"),
        content=("Girl Full Names", "Boy Full Names"),
    ),
    Params(
        options=("--girl", "--boy", "--full", "--last"),
        content=("Girl Full Names", "Boy Full Names"),
        exclude=("Girl Names",),
    ),
])
def test_cli_rand_name_gender(params):
    """
    WHEN: words rand name [OPTIONS]
    THEN: the results should be as expected
    """
    runner = CliRunner()
    result = runner.invoke(name_cmd, [*params.options,])
    assert result.exit_code == 0

    if params.size:
        assert len(result.output.splitlines()) == params.size

    for text in params.content:
        assert text in result.output

    for text in params.exclude:
        assert text not in result.output


@pytest.mark.parametrize("params", [
    Params(
        message="Need at least one of: --girl, --boy, or --last",
    ),
    Params(
        options=("--full",),
        message="With --full, need at least one of: --girl or --boy.",
    ),
    Params(
        options=("--last", "--full"),
        message="With --full, need at least one of: --girl or --boy.",
    ),
    Params(
        options=("--last", "--num", "-1"),
        message="--num must be a positive number",
        skip="TODO"
    ),
    Params(
        options=("--last", "--num", "0"),
        message="--num must be a positive number",
        skip="TODO"
    ),
])
def test_cli_rand_name_errors(params):
    """
    WHEN: invalid options are passed to words rand name
    THEN: the the program should exit with a non-zero exit code
    """
    if params.skip:
        pytest.skip(reason=params.skip)

    runner = CliRunner()
    result = runner.invoke(name_cmd, [*params.options,])
    assert result.exit_code != 0
    assert params.message in result.output


@pytest.mark.parametrize("params", [
    Params(
        content=("─ Colors ─",),
        size=3,
    ),
    Params(
        options=("--simple",),
        content=("─ Colors ─",),
        patterns={HEX_FINDER: False},
        size=3,
    ),
    Params(
        options=("--simple", "--num", "10"),
        size=12,
        desc="Colors are printed in one panel with additional header and footer lines.",
    ),
    Params(
        options=("--verbose", "--num", "4"),
        size=6,
        desc="Colors panels are in cols so the height stays the same until they wrap.",
    ),
    Params(
        options=("--verbose",),
        patterns={HEX_FINDER: True, HEADER_FINDER: True},
        exclude=("─ Colors ─",),
        size=6,
        desc="Colors panels 6 lines high, title is name, and include the hex code.",
    ),
])
def test_cli_rand_name_verbosity(params):
    """
    WHEN: words rand color [OPTIONS]
    THEN: the results should be as expected
    """
    if params.skip:
        pytest.skip(reason=params.skip)

    runner = CliRunner()
    result = runner.invoke(color_cmd, [*params.options,])

    assert result.exit_code == 0

    assert len(result.output.splitlines()) == params.size

    for text in params.content:
        assert text in result.output

    for text in params.exclude:
        assert text not in result.output

    for pattern, should_match in params.patterns.items():
        assert bool(pattern.search(result.output)) == should_match


def test_cli_rand_word_help():
    """
    WHEN: words rand word
    THEN: it should work
    AND: all of the options should be present
    """
    runner = CliRunner()
    result = runner.invoke(word_cmd, ["--help"])

    assert result.exit_code == 0

    for opt in ("-n, --num MAX", "-l, --len [MIN]-[MAX]"):
        assert f"\n  {opt} " in result.output


def test_cli_rand_word_num():
    """
    WHEN: words rand word --num INT
    THEN: it should work
    AND: INT random number should be printed
    """
    runner = CliRunner()
    result = runner.invoke(word_cmd, ["--num", 10])

    assert result.exit_code == 0

    assert len(result.output.splitlines()) == 12


@pytest.mark.parametrize(
    ["input_length", "pred", "input_msg", "output_msg"], [
        ["5", lambda x: len(x) <= 5, "MAX_INT", "less than or equal to MAX_INT"],
        ["-10", lambda x: len(x) <= 10, "-MAX_INT", "less than or equal to MAX_INT"],
        ["10-", lambda x: len(x) >= 10, "MIN_INT-", "greater than or equal to MIN_INT"],
        [
            "5-10",
            lambda x: len(x) >= 5 and len(x) <= 10,
            "MIN_INT-MAX_INT",
            "between MIN_INT and MAX_INT inclusive",
        ],
    ]
)
def test_cli_rand_word_length(
    input_length, pred, input_msg, output_msg
):
    """
    WHEN: words rand word --len RANGE
    THEN: it should work
    AND: the length of all words should be constrained to the values within RANGE
    """
    runner = CliRunner()
    result = runner.invoke(word_cmd, ["--len", input_length])

    lines = result.output.splitlines()[1:-1]
    words = (line[2:-2].strip() for line in lines)

    assert result.exit_code == 0
    assert all(map(pred, words)), (
        f"When input range is {input_msg}, "
        f"the length of all words should be {output_msg}"
    )
