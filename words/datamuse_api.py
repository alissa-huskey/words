"""Datamuse API."""

from functools import cached_property

from datamuse import Datamuse as DatamuseClient

from words.object import Object
from words.word import Word


class DatamuseAPI(Object):
    """DatamuseAPI API Client."""

    PARAMS = [
        "ml",
        "sl",
        "sp",
        "v",
        "md",
        "ipa",
        "topics",
        "lc",
        "rc",
        "max",
        "md",
        "qe",
        "ipa",
    ]

    @property
    def query(self):
        """Return a dictionary of params to include in request."""
        return {k: getattr(self, k) for k in self.PARAMS if hasattr(self, k)}

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
            return
        return [Word(**data) for data in self.data]
