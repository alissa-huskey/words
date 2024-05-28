"""Datamuse API."""

from functools import cached_property

from datamuse import Datamuse as DatamuseClient

from words import bp, WordsError  # noqa
from words.clients.dm.word import Word
from words.datamuse_options import DatamuseOptions
from words.object import Object


class DatamuseAPI(Object):
    """DatamuseAPI API Client."""

    data: list = []

    @classmethod
    @property
    def params(cls):
        """Return a list of valid Datamuse params."""
        return DatamuseOptions.params

    @property
    def query(self):
        """Return a dictionary of params to include in request."""
        query_params = {k: getattr(self, k) for k in self.params if hasattr(self, k)}
        return query_params

    def get(self):
        """Send a request to the client."""
        self.data = self.client.words(**self.query)
        return self.data

    @cached_property
    def client(self):
        """Get a DatamuseAPIClient object."""
        return DatamuseClient()

    @property
    def words(self) -> list[Word]:
        """Return a list of Word objects."""
        if not self.data:
            return []
        return [Word(**data) for data in self.data]
