from words import bp, WordsError  # noqa
from words.clients.wordnik.wordnik_client import WordnikClient


def test_wordnik_client():
    """
    WHEN: a WordnikClient object is created
    THEN: it should work
    """

    client = WordnikClient()
    assert client
    assert client.base
