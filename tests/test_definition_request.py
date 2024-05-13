from random import choice
from socket import socket

import pytest

from words import WordsError
from words.definition_request import DefinitionRequest

from . import Stub, fake_response
from .mock_socket import MockSocket

DBS = ("gcide", "wn", "moby-thesaurus", "elements", "english", "all", "easton")
bp = breakpoint


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


def test_definition_request_databases(dict_request, dict_databases):
    """
    GIVEN: a DefinitionRequest object
    WHEN: .databases() is called
    THEN: it should return a dictionary of databases
    """
    request = dict_request(response_file="db.show")
    dbs = request.dbs()

    assert dbs


def test_definition_request_databases_filter(dict_request):
    """
    GIVEN: a DefinitionRequest object
    WHEN: .databases() is called with a search argument
    THEN: it should return a dictionary of databases
    AND: the results should include any databases with names that
         contain the search phrase
    AND: the results should not include any databases with names that do not
         contain the search phrase
    """
    request = dict_request(response_file="db.show")
    dbs = request.dbs("free")

    assert dbs
    assert "gcide" not in dbs
    assert "foldoc" in dbs


def test_definition_request_databases_default(dict_request):
    """
    GIVEN: a DefinitionRequest object
    WHEN: .databases() is called with default=True
    THEN: it should return a truncated dictionary of databases
    """
    request = dict_request(response_file="db.show")
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


def test_definition_request_lookup(dict_request):
    """
    GIVEN: a DefinitionRequest object with a word
    WHEN: when request.lookup() is called
    THEN: it should return a DefineWordResponse object that has been parsed
          correctly
    """

    response = fake_response("moon.def")
    request = dict_request("moon", "moon.def")
    actual_response = request.lookup()

    assert actual_response.content
    assert actual_response.content == response.content


def test_definition_request_lookup_database(dict_request):
    """
    GIVEN: a DefinitionRequest object with a word
    WHEN: when request.lookup() is called with a database
    THEN: responses should be restricted to that database
    """

    response = fake_response("moon.def")
    request = dict_request("moon", "moon.def", db="*")
    actual_response = request.lookup()

    assert actual_response.content
    assert actual_response.content == response.content


@pytest.mark.parametrize(("word", "response_file", "count"), [
    ("moon", "moon.def", 6), ("xxxxx", "xxxxx.def", 0)
])
def test_definition_request_count(word, response_file, count, dict_request):
    """
    GIVEN: a DefinitionRequest object with a response
    WHEN: request.count is accessed
    THEN: the correct number of entires should be returned
    """
    request = dict_request(word, response_file)

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


def test_definition_request_with_client(dict_request):
    """
    WHEN: a DefinitionRequest object is created with a client
    THEN: that client should be assigned
    """
    request = dict_request("moon", "moon.def")

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


def test_definition_request_definitions(dict_request):
    """
    GIVEN: a DefinitionRequest object with a response with results
    WHEN: request.definitions is accessed
    THEN: the definitions should be returned
    """
    request = dict_request("moon", "moon.def")
    defn = choice(request.definitions or [None])

    assert len(request.definitions) == 6
    assert "Moon" in defn


def test_definition_request_entries(dict_request):
    """
    GIVEN: a DefinitionRequest object with a response with results
    WHEN: request.entries is accessed
    THEN: the entires should be returned
    """
    request = dict_request("moon", "moon.def")
    entry = choice(request.entries or [None])

    assert len(request.entries) == 6
    assert entry.word == "moon"
    assert entry.db in DBS


def test_definition_request_entries_empty(dict_request):
    """
    GIVEN: a DefinitionRequest object with a response with no results
    WHEN: request.entries is accessed
    THEN: an empty list should be returned
    """
    request = dict_request("xxxxx", "xxxxx.def")

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
