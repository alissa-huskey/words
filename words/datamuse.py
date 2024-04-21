"""Datamuse API."""

from requests import get, Response

from words.object import Object

class Word(Object):
    """Word class."""

    def __gt__(self, other):
        return (self.word > other.word)


class Datamuse(Object):
    """Class for the Datamuse API."""

    URL = "https://api.datamuse.com/words"
    # ?ml=ringing+in+the+ears

    response: response = None

    def get(self):
        self.response = get(self.URL, params=self.__dict__)
        return self. response

    @property
    def words(self):
        if not self.response:
            return
        return [Word(**word) for word in self.response.json()]




