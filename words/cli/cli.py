"""DatamuseAPI API Wrapper."""
import click
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install as rich_tracebacks

from words import WordsError
from words.compat import BdbQuit
from words.datamuse_api import DatamuseAPI
from words.datamuse_options import DatamuseOptions
from words.definition_request import DefinitionRequest
from words.word_presenter import WordPresenter

rich_tracebacks(show_locals=True)
console = Console(stderr=True)
bp = breakpoint


def err(message):
    """Print an error message and exit."""
    rprint(f"[red]Error[/red] {message}")
    exit(1)


def header(title):
    """Print a section header."""
    console.rule(f"[bold green]{title}")


@click.group()
def run():
    """Command line thesaurus, dictionary and more."""
    pass


@run.group("dict")
def dict_api():
    """Dict.org API commands."""


@dict_api.command()
@click.option("--search", metavar="PHRASE", help="Filter results.")
@click.option("--default", is_flag=True,
              help="Display the default databases used for for definition searches.")
def dbs(search=None, default=False):
    """List databases."""
    rsp = DefinitionRequest()
    dbs = rsp.dbs(search, default).items()

    table = Table("Name", "Description")
    for db in dbs:
        table.add_row(*db)
    rprint(table)


@dict_api.command()
def strategies():
    """List strategies."""
    rsp = DefinitionRequest()
    strategies = rsp.client.strategies.items()

    header("Strategies")
    table = Table("Name", "Description")
    for db in strategies:
        table.add_row(*db)
    rprint(table)


@run.command("def")
@click.argument("word")
@click.option("--db", default="*", help="Database(s) to search.")
def define(word: str, db: None):
    """Get the definition of a word."""
    rsp = DefinitionRequest(word, db=db)

    if not rsp.count:
        rprint("Not found.")
    for e in rsp.entries:
        panel = Panel(e.definition, title=e.dbname)
        rprint(panel)


def dm(**kwargs):
    """Datamuse word search."""
    has_required = filter(None, map(kwargs.get, DatamuseOptions.cli_required))
    if not tuple(has_required):
        err("No search option provided.")
        return

    api = DatamuseAPI(**kwargs)
    api.get()

    if api.json:
        rprint(api.data)
        return

    if api.long:
        table = Table(*WordPresenter.headers())
        for w in api.words:
            word = WordPresenter(w)
            table.add_row(*word.columns)
        console.print(table)
    else:
        for word in api.words:
            print(word)


run.add_command(click.Command("dm", callback=dm, help=dm.__doc__, params=[
    *DatamuseOptions.cli_options,
    click.Option(["--json"], is_flag=True, help="Export as raw JSON."),
    click.Option(["--long"], is_flag=True, help="Print word list in long format."),
]))


def main():
    """CLI entrypoint."""
    try:
        run()
    except (SystemExit, BdbQuit):
        ...
    except WordsError as e:
        err(e)
