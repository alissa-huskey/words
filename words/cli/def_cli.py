"""CLI for words def command."""

import click
from rich import print as rprint
from rich.panel import Panel
from rich.traceback import install as rich_tracebacks

from words.definition_request import DefinitionRequest

rich_tracebacks(show_locals=True, suppress=[click])
bp = breakpoint


@click.command("def")
@click.argument("word")
@click.option(
    "-n", "--num",
    type=int,
    default=1,
    help="Number of definitions to print.",
)
def def_cmd(word: str, num: int):
    """Get the definition of a word."""
    rsp = DefinitionRequest(word, default=True)
    rsp.lookup()

    if not rsp.count:
        rprint("Not found.")
    for i, e in enumerate(rsp.entries):
        bp()
        panel = Panel(e.definition, title=e.dbname)
        rprint(panel)
        if i >= num:
            break
