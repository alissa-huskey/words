"""DefinitionRequest module for interacting with dict.org."""

from socket import gaierror

from dictionary_client import DictionaryClient as DictClient
from dictionary_client.response import DefineWordResponse

from words.dictionary_entry import DictionaryEntry
from words.object import Object
from words.response_status import ResponseStatus
from words import WordsError


class DefinitionRequest(Object):
    """A request to dict.org via a DictionaryCient."""

    HOST = "dict.org"
    PORT = 2628

    _client: DictClient = None

    response: DefineWordResponse = None

    def __init__(self, word=None, client=None, send_request=True, **kwargs):
        """Initialize and make request unless send_request is False."""
        self.word = word
        self.client = client
        super().__init__(**kwargs)

        if word and send_request:
            self.response = self.lookup()

    def lookup(self) -> DefineWordResponse:
        """Query dict.com for a definition."""
        try:
            self.response = self.client.define(self.word)
        except BrokenPipeError:
            self._client = None
            self.lookup()
        return self.response

    def dbs(self, search=None):
        """Return a list of databases."""
        dbs = self.client.databases
        if search:
            dbs = {k: v for k, v in dbs.items() if search.lower() in v.lower()}
        return dbs

    @property
    def count(self) -> int:
        """Number of matches found."""
        return len(self.entries)

    @property
    def client(self) -> DictClient:
        """Return or create DictClient object."""
        if not self._client:
            try:
                self._client = DictClient(self.HOST)
            except gaierror:
                raise WordsError("No internet connection?")
        return self._client

    @client.setter
    def client(self, value):
        """Get client."""
        self._client = value

    @property
    def definitions(self) -> list:
        """Return list of definition strings."""
        return [d.definition for d in self.entries]

    @property
    def entries(self) -> list:
        """Return a list of DefinitionEntry objects from response."""
        if not self.response.content:
            return []
        return [DictionaryEntry(word=self.word, **d) for d in self.response.content]

    @property
    def status(self) -> ResponseStatus:
        """Return the status code and message from the response."""
        if not self.response:
            return ResponseStatus()
        lines = self.response.response_text.splitlines()
        lines.append("")  # in case it's empty

        return ResponseStatus(lines[0])

    @property
    def ok(self):
        """Return True for a successful request."""
        if not self.response:
            return

        status = str(self.response.status_code)

        return (status[0] not in ("4", "5"))
