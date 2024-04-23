from random import choice
from socket import socket

import pytest
from dictionary_client import DictionaryClient
from dictionary_client.response import DefineWordResponse

from tests import Stub, read_file
from tests.mock_socket import MockSocket
from words.definition_request import DefinitionRequest

DBS = ("gcide", "wn", "moby-thesaurus", "elements", "english", "all", "easton")


def make_client(response_file: str):
    """Return a DictionaryClient object.

    The client will fake a connection with a a MockSocket which will respond
    with the contents of response_file.
    """
    MockSocket.set_responses(response_file)
    client = DictionaryClient(sock_class=MockSocket)
    return client


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


def test_definition_request_word_no_send():
    """
    WHEN: DefinitionRequest is created with a word
    AND: send_request is False
    THEN: request.word should be the word
    AND: request.response should be None
    """
    request = DefinitionRequest("hello", send_request=False)

    assert request
    assert request.word == "hello"
    assert not request.response


def test_definition_request_lookup():
    """
    GIVEN: a DefinitionRequest object with a word
    WHEN: when request.lookup() is called
    THEN: it should return a DefineWordResponse object that has been parsed
          correctly
    """

    response = fake_response("moon.def")
    request = DefinitionRequest(
        "moon",
        make_client("moon.def"),
        send_request=False,
    )
    actual_response = request.lookup()

    assert actual_response.content
    assert actual_response.content == response.content


@pytest.mark.parametrize(("response_file", "count"), [
    ("moon.def", 6), ("xxxxx.def", 0)
])
def test_definition_request_count(response_file, count):
    """
    GIVEN: a DefinitionRequest object with a response
    WHEN: request.count is accessed
    THEN: the correct number of entires should be returned
    """
    response = fake_response(response_file)
    request = DefinitionRequest()
    request.response = response

    assert request.count == count


def test_definition_request_no_client():
    """
    WHEN: a DefinitionRequest object is created with no client
    THEN: a client should be assigned
    """
    request = DefinitionRequest()
    assert request.client
    assert isinstance(request.client.sock, socket)


def test_definition_request_with_client():
    """
    WHEN: a DefinitionRequest object is created with a client
    THEN: that client should be assigned
    """
    request = DefinitionRequest(client=make_client("moon.dict"))
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


def test_definition_request_definitions():
    """
    GIVEN: a DefinitionRequest object with a response with results
    WHEN: request.definitions is accessed
    THEN: the definitions should be returned
    """
    response = fake_response("moon.def")
    request = DefinitionRequest("moon", send_request=False)
    request.response = response
    defn = choice(request.definitions or [None])

    assert len(request.definitions) == 6
    assert "Moon" in defn


def test_definition_request_entries():
    """
    GIVEN: a DefinitionRequest object with a response with results
    WHEN: request.entries is accessed
    THEN: the entires should be returned
    """
    response = fake_response("moon.def")
    request = DefinitionRequest("moon", send_request=False)
    request.response = response
    entry = choice(request.entries or [None])

    assert len(request.entries) == 6
    assert entry.word == "moon"
    assert entry.db in DBS


def test_definition_request_entries_empty():
    """
    GIVEN: a DefinitionRequest object with a response with no results
    WHEN: request.entries is accessed
    THEN: an empty list should be returned
    """
    response = fake_response("xxxxx.def")
    request = DefinitionRequest("xxxxx", send_request=False)
    request.response = response

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
