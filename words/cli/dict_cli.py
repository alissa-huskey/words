"""CLI for words dict group."""

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
    """Dict.org API wrapper."""


@dict_group.command("dbs")
@click.option("--search", metavar="PHRASE", help="Filter results.")
@click.option("--default", is_flag=True,
              help="Display the default databases used for for definition searches.")
def dbs_cmd(search=None, default=False):
    """SHOW DATABASES command."""
    rsp = DefinitionRequest()
    dbs = rsp.dbs(search, default).items()

    table = Table("Name", "Description")
    for db in dbs:
        table.add_row(*db)
    rprint(table)


@dict_group.command("strategies")
def strategies_cmd():
    """SHOW DATABASES command."""
    rsp = DefinitionRequest()
    strategies = rsp.client.strategies.items()

    header("Strategies")
    table = Table("Name", "Description")
    for db in strategies:
        table.add_row(*db)
    rprint(table)


@dict_group.command("define")
@click.argument("word")
@click.option(
    "-n", "--num",
    type=int,
    default=None,
    show_default="all",
    help="Number of definitions to print.",
)
@click.option(
    "-d", "--db",
    default="*",
    metavar="DB",
    show_default="all",
    help="Database to search.",
)
def define_cmd(word: str, num: int, db: str):
    """DEFINE command."""
    args = []
    if db == "defaults":
        args = {"default": True}
    elif db:
        args = {"db": db}
    else:
        args = {}

    rsp = DefinitionRequest(word, **args)
    rsp.lookup()

    if not rsp.count:
        rprint("Not found.")
    for i, e in enumerate(rsp.entries, 1):
        panel = Panel(e.definition, title=e.dbname)
        rprint(panel)
        if num and i >= num:
            break
