"""DatamuseAPI API Wrapper."""

import click
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install as rich_tracebacks

from words.compat import BdbQuit
from words.datamuse_api import DatamuseAPI
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


#  @run.command()
#  @click.option("--ml", help="Reverse dictionary search.", metavar="WORD")
#  @click.option("--sl", help="Pronounced similarly.", metavar="WORD")
#  @click.option("--sp", help="Text and pattern search.", metavar="PATTERN")
#  @click.option("--rel-jja", help="Nouns that can be described by the given adjective.", metavar="ADJECTIVE")
#  @click.option("--rel-jjb", help="Adjectives that can be used to described the given noun.", metavar="NOUN")
#  @click.option("--rel-syn", help="Synonyms.", metavar="WORD")
#  @click.option("--rel-ant", help="Antonyms.", metavar="WORD")
#  @click.option("--rel-trg", help="Words often said together.", metavar="WORD")
#  @click.option("--rel-spc", help="Broad categories, general concepts or umbrella terms that cover the more specific given term. (hypernyms)", metavar="SUBTYPE")
#  @click.option("--rel-gen", help="Specific examples, instances, or subtypes that falls within the broader given term. (hyponyms)", metavar="SUPERTYPE")
#  @click.option("--rel-com", help="Parts or members that belong to something whole. (holonyms)", metavar="WHOLE")
#  @click.option("--rel-par", help="A whole thing where the given term is a parts or member. (meronyms)", metavar="PART")
#  @click.option("--rel-bga", help="Words often said after.", metavar="WORD BEFORE")
#  @click.option("--rel-bgb", help="Words often said before.", metavar="WORD AFTER")
#  @click.option("--rel-hom", help="Different words that sound exactly the same. (homophones)", metavar="WORD")
#  @click.option("--rel-cns", help="Words with the same consonant phoneme sounds.", metavar="WORD")
#  @click.option("--md", multiple=True,
#                type=click.Choice(["d", "p", "s", "r", "f"]),
#                help="Additional metadata to include.",)
#  @click.option("--max", type=int, help="Max results", default=30)
#  @click.option("--ipa", is_flag=True,
#                help="Use International Phonetic Alphabet pronunciation format.")
#  @click.option("--json", is_flag=True, help="Export as raw JSON.")
#  @click.option("--long", is_flag=True, help="Print word list in long format.")
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

    if api.args.json:
        rprint(api.data)
        return

    if api.args.long:
        table = Table(*WordPresenter.headers())
        for w in api.words:
            word = WordPresenter(w)
            table.add_row(*word.columns)
        console.print(table)
    else:
        for word in api.words:
            print(word)

run.add_command(click.Command("dm", callback=dm, help=dm.__doc__, params=[
    click.Option(["--ml"], help="Reverse dictionary search.", metavar="WORD"),
    click.Option(["--sl"], help="Pronounced similarly.", metavar="WORD"),
    click.Option(["--sp"], help="Text and pattern search.", metavar="PATTERN"),
    click.Option(["--rel-jja"], help="Nouns that can be described by the given adjective.", metavar="ADJECTIVE"),
    click.Option(["--rel-jjb"], help="Adjectives that can be used to described the given noun.", metavar="NOUN"),
    click.Option(["--rel-syn"], help="Synonyms.", metavar="WORD"),
    click.Option(["--rel-ant"], help="Antonyms.", metavar="WORD"),
    click.Option(["--rel-trg"], help="Words often said together.", metavar="WORD"),
    click.Option(["--rel-spc"], help="Broad categories, general concepts or umbrella terms that cover the more specific given term. (hypernyms)", metavar="SUBTYPE"),
    click.Option(["--rel-gen"], help="Specific examples, instances, or subtypes that falls within the broader given term. (hyponyms)", metavar="SUPERTYPE"),
    click.Option(["--rel-com"], help="Parts or members that belong to something whole. (holonyms)", metavar="WHOLE"),
    click.Option(["--rel-par"], help="A whole thing where the given term is a parts or member. (meronyms)", metavar="PART"),
    click.Option(["--rel-bga"], help="Words often said after.", metavar="WORD BEFORE"),
    click.Option(["--rel-bgb"], help="Words often said before.", metavar="WORD AFTER"),
    click.Option(["--rel-hom"], help="Different words that sound exactly the same. (homophones)", metavar="WORD"),
    click.Option(["--rel-cns"], help="Words with the same consonant phoneme sounds.", metavar="WORD"),
    click.Option(["--md"], multiple=True,
                type=click.Choice(["d", "p", "s", "r", "f"]),
                help="Additional metadata to include.",),
    click.Option(["--max"], type=int, help="Max results", default=30),
    click.Option(["--ipa"], is_flag=True,
                help="Use International Phonetic Alphabet pronunciation format."),
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
