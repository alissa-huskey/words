"""CLI for words dict and def commands."""

import click
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install as rich_tracebacks

from words.cli import header
from words.definition_request import DefinitionRequest

rich_tracebacks(show_locals=True, suppress=[click])
bp = breakpoint


@click.group("dict")
def dict_group():
    """Dict.org API commands."""


@dict_group.command("dbs")
@click.option("--search", metavar="PHRASE", help="Filter results.")
@click.option("--default", is_flag=True,
              help="Display the default databases used for for definition searches.")
def dbs_cmd(search=None, default=False):
    """List databases."""
    rsp = DefinitionRequest()
    dbs = rsp.dbs(search, default).items()

    table = Table("Name", "Description")
    for db in dbs:
        table.add_row(*db)
    rprint(table)


@dict_group.command("strategies")
def strategies_cmd():
    """List strategies."""
    rsp = DefinitionRequest()
    strategies = rsp.client.strategies.items()

    header("Strategies")
    table = Table("Name", "Description")
    for db in strategies:
        table.add_row(*db)
    rprint(table)


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
