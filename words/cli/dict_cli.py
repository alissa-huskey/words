"""CLI for words dict group."""

import click
from rich import print as rprint
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
