"""CLI for words rand command group."""

import click
from rich.table import Table

from words import WordsError, bp  # noqa
from words.cli import ui  # noqa
from words.datamuse_api import DatamuseAPI
from words.definition_request import DefinitionRequest
from words.word import Word
from words.word_presenter import WordPresenter


@click.command("syn")
@click.argument("word")
@click.option("--max", type=int, default=10, help="Max results.")
@click.option("--json", is_flag=True, help="Export as JSON.")
@click.option("--long", is_flag=True, help="Print word list in long format.")
def syn_cmd(word: str, max: int, json: bool, long: bool):
    """Synonyms.

    Look up a synonyms via dict.org and Datamuse APIs.

    Essentially a combination of:

    \b
        words dm --ml WORD
        words dm --rel-syn WORD
        words dict define --db moby-thesaurus WORD
    """
    synonyms = []

    # get synonyms from datamuse
    requests = [
        DatamuseAPI(ml=word, max=max, md="p"),
        DatamuseAPI(rel_syn=word, max=max, md="p"),
    ]

    for r in requests:
        r.get()
        synonyms += (r.words)

    # get synonyms from moby thesaurus
    rsp = DefinitionRequest(word, db="moby-thesaurus")
    rsp.lookup()
    if rsp.definitions:
        entry = rsp.definitions[0]
        _, _, text = entry.partition("\n")
        synonyms += ([Word(word=w.strip()) for w in text.split(",")])

    done = []
    table = Table(*WordPresenter.headers())
    for w in synonyms:
        if w.word in done:
            continue
        word = WordPresenter(w)
        table.add_row(*word.columns)
        done.append(w.word)

    with ui.pager:
        ui.console.print(table)
