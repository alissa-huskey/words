"""Wordnik API Client."""

from functools import cached_property
from os import environ

from wordnik.swagger import ApiClient as WordnikApiClient
from wordnik.WordApi import WordApi
from wordnik.WordsApi import WordsApi

from words import bp, WordsError  # noqa


class WordnikClient():
    """Wordnik API Client."""

    BASE = "http://api.wordnik.com/v4"
    ENV_VAR = "WORDNIK_API_KEY"

    _key = None
    _base = None

    def __init__(self, base: str = None, key: str = None):
        """Create the object."""
        self.key = key
        self.base = base

    @property
    def base(self):
        """Get base URL."""
        return self._base or environ.get(self.ENV_VAR)

    @base.setter
    def base(self, value):
        """Set base URL."""
        self._base = value

    @property
    def key(self):
        """Get API Key."""
        return self._key or environ.get(self.ENV_VAR)

    @key.setter
    def key(self, value):
        """Set API Key."""
        self._key = value

    @cached_property
    def client(self):
        """Return the underlying client."""
        return WordnikApiClient(self.key, self.BASE)

    @cached_property
    def words(self):
        """Return the words API object."""
        return WordsApi(self.client)

    @cached_property
    def word(self):
        """Return the word API object."""
        return WordApi(self.client)
