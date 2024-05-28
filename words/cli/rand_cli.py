"""CLI for words rand command group."""

import click
from more_itertools import flatten
from rich import box
from rich.columns import Columns
from rich.panel import Panel

from words import bp, WordsError  # noqa
from words.cli import ui  # noqa
from words.cli.param_types import RangeType
from words.color import Colors
from words.random import RandomBooks, RandomName, RandomWord
from words.renderers.colors_renderer import ColorsRenderer


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
    metavar="MAX",
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

    with ui.pager:
        ui.console.print(Columns(panels))


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
    metavar="MAX",
    type=int,
    default=1,
    help="Number of colors to print.",
)
def color_cmd(output_format, num):
    """Colors."""
    color_list = Colors(num=num)
    renderer = ColorsRenderer(color_list)
    obj = renderer.render(output_format)

    with ui.pager:
        ui.console.print(obj)


@rand_group.command("word")
@click.option(
    "-n", "--num",
    metavar="MAX",
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

    with ui.pager:
        ui.console.print(panel)


@rand_group.command("text")
@click.option(
    "-u", "--unit",
    help="Unit of text to print.",
    default="sent",
    type=click.Choice(
        ["para", "sent"],
        case_sensitive=False,
    ),
    show_choices=True,
)
@click.option(
    "-n", "--num",
    metavar="MAX",
    type=int,
    default=1,
    help="Number to print.",
)
def text_cmd(unit: str, num: int):
    """Text."""
    books = RandomBooks()
    files = books.get(num)
    items = list(flatten((f.get() for f in files)))

    if unit == "sent":
        items = flatten((p.get() for p in items))

    for item in items:
        panel = Panel(
            item.text,
            padding=(1, 3),
            subtitle=f"-- {item.title}",
            subtitle_align="right",
            box=box.MINIMAL,
            width=80,
        )

        ui.console.print(panel)
    ui.console.line()
