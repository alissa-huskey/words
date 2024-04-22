"""Datamuse API."""

from requests import Response, get

from words.object import Object
from words.word import Word


class Datamuse(Object):
    """Datamuse API Client."""

    URL = "https://api.datamuse.com/words"

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

    response: Response = None

    @property
    def query(self):
        """Return a dictionary of params to include in request."""
        return {k: getattr(self, k) for k in self.PARAMS if hasattr(self, k)}

    def get(self):
        """Send a GET request."""
        self.response = get(self.URL, params=self.query)
        self.data = self.response.json()
        return self.response

    @property
    def words(self) -> list[Word]:
        """Return a list of Word objects."""
        if not self.response:
            return
        return [Word(**data) for data in self.data]
