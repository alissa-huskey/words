"""Datamuse API Wrapper."""

from typing_extensions import Annotated

from rich import print
from rich.console import Console
from rich.traceback import install as rich_tracebacks
from typer import Typer, Option

from words.datamuse import Datamuse

cli = Typer()
console = Console(stderr=True)
rich_tracebacks(show_locals=True)


@cli.command()
def words(
    ml: Annotated[str, Option(help="Meaning like.")] = "",
    max: Annotated[str, Option(help="Max results.")] = "",
):
    """Print results from the primary datamuse endpoint."""
    doc = Datamuse(ml=ml, max=max)
    doc.get()

    for word in doc.words:
        print(word.word)


def run():
    """Command line runner."""
    try:
        cli()
    except SystemExit:
        ...
    #  except BaseException as e:
    #      print("[red]Error[/red]", e)
    #      exit(1)


if __name__ == "__main__":
    run()
