"""CLI for words rand command group."""

import click
from rich import print as rprint
from rich.columns import Columns
from rich.panel import Panel

from words.cli.param_types import RangeType
from words.color import Colors
from words.random import RandomName, RandomWord

bp = breakpoint


def validate_full(ctx, param, value):
    """Ensure that --boy and/or --girl is passed with --full."""
    if not value:
        return value

    selection = ctx.params.get("selection", tuple())
    if not (("girl" in selection) or ("boy" in selection)):
        raise click.BadOptionUsage(
            "full",
            "With --full, need at least one of: --girl or --boy."
        )
    return value


@click.group("rand")
def rand_group():
    """Random data."""


@rand_group.command("name")
@click.option(
    "-b", "--boy", "selection",
    multiple=True,
    flag_value="boy",
    is_eager=True,
    help="Print boy name(s).",
)
@click.option(
    "-g", "--girl", "selection",
    multiple=True,
    flag_value="girl",
    is_eager=True,
    help="Print girl name(s).",
)
@click.option(
    "-l", "--last", "selection",
    multiple=True,
    flag_value="last",
    help="Print last name(s).",
)
@click.option(
    "-f", "--full",
    is_flag=True,
    callback=validate_full,
    help="Add last name(s) to first name(s).",
)
@click.option(
    "-n", "--num",
    type=int,
    default=1,
    help="Number of names to print.",
)
@click.option(
    "-m", "--max", "limit",
    type=int,
    help="Maximum number of lines from top (most popular names) to include.",
)
def name_cmd(selection, full, num, limit):
    """People names."""
    if not selection:
        raise click.UsageError(
            "Need at least one of: --girl, --boy, or --last"
        )

    selection = (full and (selection + ("last",)) or selection)
    files = {}

    for category in selection:
        files[category] = RandomName(category, max=limit)

    panels = []
    for category, file in files.items():
        if full and category == "last":
            continue

        names = file.get(num)

        if full:
            surnames = files["last"].get(num)
            names = list(map(" ".join, zip(names, surnames)))

        title = category.capitalize() + (full and " Full" or "") + " Names"
        panel = Panel("\n".join(names), title=title)
        panels.append(panel)

    rprint(Columns(panels))


@rand_group.command("color")
@click.option(
    "-s", "--simple", "output_format",
    flag_value="simple",
    default=True,
    show_default="true",
    help="Print a simple list of color names.",
)
@click.option(
    "-v", "--verbose", "output_format",
    flag_value="verbose",
    help="Display color swatches and all details.",
)
@click.option(
    "-n", "--num",
    type=int,
    default=1,
    help="Number of colors to print.",
)
def color_cmd(output_format, num):
    """Colors."""
    clist = Colors(output_format, num=num)
    obj = clist.render()
    rprint(obj)


@rand_group.command("word")
@click.option(
    "-n", "--num",
    type=int,
    default=1,
    help="Number of words to print.",
)
@click.option(
    "-l", "--len", "length",
    type=RangeType(),
    help="Constrain the length of words.",
)
def word_cmd(num: int, length):
    """Words."""
    f = RandomWord(length_range=length)
    wordlist = f.get(num)
    panel = Panel("\n".join(wordlist), title="words", expand=False)
    rprint(panel)
