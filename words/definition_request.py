"""DefinitionRequest module for interacting with dict.org."""

from socket import gaierror

from dictionary_client import DictionaryClient as DictClient
from dictionary_client.response import DefineWordResponse

from words import WordsError
from words.dictionary_entry import DictionaryEntry
from words.object import Object
from words.response_status import ResponseStatus


class DefinitionRequest(Object):
    """A request to dict.org via a DictionaryCient."""

    HOST = "dict.org"
    PORT = 2628
    DEFAULT_DBS = ["gcide", "wn"]

    _client: DictClient = None
    _databases: dict = {}

    response: DefineWordResponse = None

    def __init__(self, word=None, client=None, db="*", send_request=True, **kwargs):
        """Initialize and make request unless send_request is False."""
        self.word = word
        self.db = db
        self.client = client
        super().__init__(**kwargs)

        if word and send_request:
            self.response = self.lookup()

    def lookup(self) -> DefineWordResponse:
        """Query dict.com for a definition."""
        try:
            self.response = self.client.define(self.word, self.db)
        except BrokenPipeError:
            self._client = None
            self.lookup()
        return self.response

    @property
    def databases(self):
        """Get databases."""
        if not self._databases:
            self._databases = self.client.databases
        return self._databases

    @databases.setter
    def databases(self, value):
        """Set databases."""
        self._databases = value

    def dbs(self, search=None, default=False):
        """Return a list of databases."""
        dbs = self.databases
        if search:
            dbs = {k: v for k, v in dbs.items() if search.lower() in v.lower()}
        if default:
            dbs = {k: v for k, v in dbs.items() if k in self.DEFAULT_DBS}
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
        return [DictionaryEntry(word=self.word, **d, dbname=self.databases.get(d["db"]))
                for d in self.response.content]

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
