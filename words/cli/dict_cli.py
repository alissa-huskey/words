"""CLI for words dict group."""

from functools import reduce

import click
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install as rich_tracebacks

from words import bp, WordsError  # noqa
from words.cli import ui
from words.clients.dict.definition_request import DefinitionRequest

rich_tracebacks(show_locals=True, suppress=[click])


@click.group(
    "dict",
    epilog="https://dict.org/"
)
def dict_group():
    """Dict.org API wrapper.

    Query the dict.org server using the DICT protocol.
    """


@dict_group.command("dbs")
@click.option("--search", metavar="PHRASE", help="Filter results.")
@click.option("--default", is_flag=True,
              help="Display the default databases used for for definition searches.")
def dbs_cmd(search=None, default=False):
    """SHOW DATABASES command.

    List available databases.
    """
    rsp = DefinitionRequest()
    dbs = rsp.dbs(search, default).items()

    table = Table("Name", "Description")
    for db in dbs:
        table.add_row(*db)

    with ui.pager:
        ui.console.print(table)


@dict_group.command("strategies")
def strategies_cmd():
    """SHOW STRATEGIES command.

    List supported search strategies.
    """
    rsp = DefinitionRequest()
    strategies = rsp.client.strategies.items()

    ui.header("Strategies")
    table = Table("Name", "Description")
    for db in strategies:
        table.add_row(*db)

    with ui.pager:
        ui.console.print(table)


@dict_group.command(
    "define",
    epilog="[*]: all databases, [defaults]: default databases",
)
@click.argument("word")
@click.option(
    "-n", "--num",
    type=int,
    metavar="MAX",
    default=None,
    show_default="all",
    help="Number of definitions to print.",
)
@click.option(
    "-d", "--db",
    default="*",
    metavar="DB",
    help="Database to search.",
)
def define_cmd(word: str, num: int, db: str):
    """DEFINE command.

    Look up WORD in the specified DB.

    For a list of valid DB values (available databases) use the command:

    \b
        words dict dbs
    """
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


@dict_group.command(
    "match",
    epilog="[*]: search all databases, [.]: use server's default strategy"
)
@click.argument("word")
@click.option(
    "-d", "--db",
    default="*",
    metavar="DB",
    help="Database to search.",
)
@click.option(
    "-s", "--strat",
    metavar="STRATEGY",
    default=".",
    help="Search strategy.",
)
def match_cmd(word: str, db: str, strat: str):
    """MATCH command.

    Search DB index(/indices) for WORD using STRATEGY.
    """
    client = DefinitionRequest()
    rsp = client.client.match(word, db=db, strategy=strat)

    func = (lambda item, prev: item+[(v, prev[0]) for v in prev[1]])
    flat = reduce(func, rsp.content.items(), [])
    words = sorted(flat, key=lambda w: w[0].lower())

    table = Table("DB", "Word")
    for word, db in words:
        table.add_row(db, word)

    rprint(table)
