"""CLI for words def command."""

import click
from rich.traceback import install as rich_tracebacks

from words.cli.dict_cli import define_cmd

rich_tracebacks(show_locals=True, suppress=[click])
bp = breakpoint


@click.command("def")
@click.argument("word")
@click.option(
    "-n", "--num",
    type=int,
    default=1,
    show_default=True,
    help="Number of definitions to print.",
)
@click.pass_context
def def_cmd(ctx, *args, **kwargs):
    """Get the definition of a word."""
    ctx.invoke(define_cmd, *args, db=None, **kwargs)
