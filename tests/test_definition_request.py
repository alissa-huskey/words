from random import choice
from socket import socket

import pytest
from dictionary_client import DictionaryClient
from dictionary_client.response import DefineWordResponse

from tests import Stub, read_file
from tests.mock_socket import MockSocket
from words import WordsError
from words.definition_request import DefinitionRequest

DBS = ("gcide", "wn", "moby-thesaurus", "elements", "english", "all", "easton")
bp = breakpoint


@pytest.fixture
def make_client():
    def wrapped(response_file):
        """Return a DictionaryClient object.

        The client will fake a connection with a a MockSocket which will respond
        with the contents of response_file.
        """
        MockSocket.set_responses(response_file)
        client = DictionaryClient(sock_class=MockSocket)
        return client
    return wrapped


@pytest.fixture
def make_request(make_client, databases):
    def wrapped(word=None, response_file=None, **kwargs):
        """Return a DefinitionRequest object.

        The client will fake a connection with a a MockSocket which will respond
        with the contents of response_file.
        """
        params = []
        word and params.append(word)
        if response_file:
            params.append(make_client(response_file))

        response = fake_response(response_file)
        request = DefinitionRequest(*params, **kwargs)
        request.databases = databases
        request.response = response
        return request
    return wrapped


@pytest.fixture
def databases():
    """Return a list of databases."""
    databases = {
        'foldoc': 'The Free On-line Dictionary of Computing (30 December 2018)',
        'gcide': 'The Collaborative International Dictionary of English v.0.48',
        'wn': 'WordNet (r) 3.0 (2006)',
        'english': 'English Monolingual Dictionaries',
        'trans': 'Translating Dictionaries',
        'all': 'All Dictionaries (English-Only and Translating)',
    }
    return databases


def fake_response(response_file: str):
    """Return a DefineWordResponse object.

    To parse the contents of the response_file.
    """
    contents = read_file(response_file)
    response = DefineWordResponse(contents)
    return response


def test_definition_request():
    request = DefinitionRequest()
    assert request


def test_definition_no_connection(monkeypatch):
    """
    GIVEN: a DefinitionRequest object
    WHEN: .dbs() is called
    THEN: it should return a dictionary of databases
    """
    monkeypatch.setattr(DefinitionRequest, "HOST", "wrongdict.org")

    with pytest.raises(WordsError):
        client = DefinitionRequest()
        client.dbs()


def test_definition_request_databases(make_request, databases):
    """
    GIVEN: a DefinitionRequest object
    WHEN: .databases() is called
    THEN: it should return a dictionary of databases
    """
    request = make_request(response_file="db.show")
    dbs = request.dbs()

    assert dbs


def test_definition_request_databases_filter(make_request):
    """
    GIVEN: a DefinitionRequest object
    WHEN: .databases() is called with a search argument
    THEN: it should return a dictionary of databases
    AND: the results should include any databases with names that
         contain the search phrase
    AND: the results should not include any databases with names that do not
         contain the search phrase
    """
    request = make_request(response_file="db.show")
    dbs = request.dbs("free")

    assert dbs
    assert "gcide" not in dbs
    assert "foldoc" in dbs


def test_definition_request_databases_default(make_request):
    """
    GIVEN: a DefinitionRequest object
    WHEN: .databases() is called with default=True
    THEN: it should return a truncated dictionary of databases
    """
    request = make_request(response_file="db.show")
    dbs = request.dbs(default=True)

    assert dbs
    assert "fd-spa-ast" not in dbs


def test_definition_request_word_no_send():
    """
    WHEN: DefinitionRequest is created with a word
    THEN: request.word should be the word
    AND: request.response should be None
    """
    request = DefinitionRequest("hello")

    assert request
    assert request.word == "hello"
    assert not request.response


def test_definition_request_lookup(make_request):
    """
    GIVEN: a DefinitionRequest object with a word
    WHEN: when request.lookup() is called
    THEN: it should return a DefineWordResponse object that has been parsed
          correctly
    """

    response = fake_response("moon.def")
    request = make_request("moon", "moon.def")
    actual_response = request.lookup()

    assert actual_response.content
    assert actual_response.content == response.content


def test_definition_request_lookup_database(make_request):
    """
    GIVEN: a DefinitionRequest object with a word
    WHEN: when request.lookup() is called with a database
    THEN: responses should be restricted to that database
    """

    response = fake_response("moon.def")
    request = make_request("moon", "moon.def", db="*")
    actual_response = request.lookup()

    assert actual_response.content
    assert actual_response.content == response.content


@pytest.mark.parametrize(("word", "response_file", "count"), [
    ("moon", "moon.def", 6), ("xxxxx", "xxxxx.def", 0)
])
def test_definition_request_count(word, response_file, count, make_request):
    """
    GIVEN: a DefinitionRequest object with a response
    WHEN: request.count is accessed
    THEN: the correct number of entires should be returned
    """
    request = make_request(word, response_file)

    assert request.count == count


@pytest.mark.skip("can't really test this without internet connection'")
def test_definition_request_no_client():
    """
    WHEN: a DefinitionRequest object is created with no client
    THEN: a client should be assigned
    """
    request = DefinitionRequest()
    assert request.client
    assert isinstance(request.client.sock, socket)


def test_definition_request_with_client(make_request):
    """
    WHEN: a DefinitionRequest object is created with a client
    THEN: that client should be assigned
    """
    request = make_request("moon", "moon.def")

    assert request.client
    assert isinstance(request.client.sock, MockSocket)


def test_definition_request_definitions_no_entries():
    """
    GIVEN: a DefinitionRequest object with a response with results
    WHEN: request.definitions is accessed
    THEN: the definitions should be returned
    """
    response = fake_response("xxxxx.def")
    request = DefinitionRequest()
    request.response = response

    assert len(request.definitions) == 0


def test_definition_request_definitions(make_request):
    """
    GIVEN: a DefinitionRequest object with a response with results
    WHEN: request.definitions is accessed
    THEN: the definitions should be returned
    """
    request = make_request("moon", "moon.def")
    defn = choice(request.definitions or [None])

    assert len(request.definitions) == 6
    assert "Moon" in defn


def test_definition_request_entries(make_request):
    """
    GIVEN: a DefinitionRequest object with a response with results
    WHEN: request.entries is accessed
    THEN: the entires should be returned
    """
    request = make_request("moon", "moon.def")
    entry = choice(request.entries or [None])

    assert len(request.entries) == 6
    assert entry.word == "moon"
    assert entry.db in DBS


def test_definition_request_entries_empty(make_request):
    """
    GIVEN: a DefinitionRequest object with a response with no results
    WHEN: request.entries is accessed
    THEN: an empty list should be returned
    """
    request = make_request("xxxxx", "xxxxx.def")

    assert len(request.entries) == 0


@pytest.mark.parametrize(("response_file", "wanted_status"), [
    ("moon.def", Stub(_code=150, _message="6 definitions retrieved")),
    ("xxxxx.def", Stub(_code=552, _message="no match"))
])
def test_definition_request_status(response_file, wanted_status):
    """
    GIVEN: a DefinitionRequest with a response from dict.org
    WHEN: request.status is accessed
    THEN: it should return the status code and message
    """
    request = DefinitionRequest()
    request.response = fake_response(response_file)
    status = request.status

    assert wanted_status == status


@pytest.mark.parametrize(("response_file", "is_ok"), [
    ("moon.def", True),
    ("xxxxx.def", False)
])
def test_definition_request_ok(response_file, is_ok):
    """
    GIVEN: a DefinitionRequest with a response from dict.org
    WHEN: request.ok is accessed
    THEN: it should return True or False depending of the response succeeded
    """
    request = DefinitionRequest()
    request.response = fake_response(response_file)

    assert request.ok is is_ok
