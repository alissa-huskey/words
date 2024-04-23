import pytest
from dictionary_client import DictionaryClient
from dictionary_client.response import DefineWordResponse

from tests import read_file
from tests.mock_socket import MockSocket
from words.definition_request import DefinitionRequest


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
    GIVEN: ...
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


@pytest.mark.skip
def test_definition_request_matches():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    request = DefinitionRequest()
    assert request


@pytest.mark.skip
def test_definition_request_client():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    request = DefinitionRequest()
    assert request


@pytest.mark.skip
def test_definition_request_definitions():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    request = DefinitionRequest()
    assert request


@pytest.mark.skip
def test_definition_request_entries():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    request = DefinitionRequest()
    assert request


@pytest.mark.skip
def test_definition_request_status():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    request = DefinitionRequest()
    assert request


@pytest.mark.skip
def test_definition_request_ok():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    request = DefinitionRequest()
    assert request
