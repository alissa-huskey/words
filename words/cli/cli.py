"""DatamuseAPI API Wrapper."""

import click
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install as rich_tracebacks

from words.compat import BdbQuit
from words.datamuse_api import DatamuseAPI
from words.datamuse_options import DatamuseOptions
from words.definition_request import DefinitionRequest
from words.word_presenter import WordPresenter

console = Console(stderr=True)
rich_tracebacks(show_locals=True)
bp = breakpoint


def err(message):
    """Print an error message and exit."""
    rprint(f"[red]Error[/red] {message}")
    exit(1)


@click.group()
def run():
    """Command line thesaurus, dictionary and more."""
    pass


@run.command()
@click.argument("word")
def define(word: str):
    """Get the definition of a word."""
    rsp = DefinitionRequest(word)
    if not rsp.count:
        rprint("Not found.")
    for e in rsp.entries:
        panel = Panel(e.definition, title=e.db)
        rprint(panel)


def dm(**kwargs):
    """Datamuse search."""
    required = [
        "ml",
        "sl",
        "sp",
        "rel_jja",
        "rel_syn",
        "rel_ant",
        "rel_trg",
        "rel_spc",
        "rel_gen",
        "rel_com",
        "rel_par",
        "rel_bga"
        "rel_bgb",
        "rel_hom",
        "rel-cns",
    ]
    has_required = filter(None, map(kwargs.get, required))
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


if __name__ == "__main__":
    try:
        click()
    except (SystemExit, BdbQuit):
        ...
    #  except BaseException as e:
    #      rprint("[red]Error[/red]", e)
    #      exit(1)
