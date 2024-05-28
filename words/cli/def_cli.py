"""CLI for words def command."""

import click
from rich.traceback import install as rich_tracebacks

from words import bp, WordsError  # noqa
from words.cli import ui  # noqa
from words.cli.dict_cli import define_cmd

rich_tracebacks(show_locals=True, suppress=[click])


@click.command("def")
@click.argument("word")
@click.option(
    "-n", "--num",
    type=int,
    default=1,
    metavar="MAX",
    show_default=True,
    help="Number of definitions to print.",
)
@click.pass_context
def def_cmd(ctx, *args, **kwargs):
    """Definition lookup.

    Look up a word in the common english word dictionaries using dict.org.

    This is essentially a shorthand with sensible defaults to the command:

    \b
        words dict define WORD
    """
    ctx.invoke(define_cmd, *args, db=None, **kwargs)
