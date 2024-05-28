"""CLI for words wordnik group."""

import click

from words import bp, WordsError  # noqa
from words.clients.wordnik.wordnik_client import WordnikClient


@click.group(
    "wordnik",
    epilog="http://wordnik.com/"
)
def wordnik_group():
    """Wordnik.com API wrapper."""


@wordnik_group.group("words")
def words_group():
    """Query the words resource."""


@words_group.command("rand")
def rand_cmd():
    """Return a single random WordObject."""
    client = WordnikClient()
    response = client.words.getRandomWord()

    print(response.word)
