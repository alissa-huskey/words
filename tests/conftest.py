"""Global pytest config and fixtures."""

import pytest
from dictionary_client import DictionaryClient

from tests import fake_response
from tests.mock_socket import MockSocket
from words.definition_request import DefinitionRequest


@pytest.fixture
def dict_request(dict_client, dict_databases):
    """."""
    def wrapped(word=None, response_file=None, **kwargs):
        """Return a DefinitionRequest object.

        The client will fake a connection with a a MockSocket which will respond
        with the contents of response_file.
        """
        params = []
        word and params.append(word)
        if response_file:
            params.append(dict_client(response_file))

        response = fake_response(response_file)
        request = DefinitionRequest(*params, **kwargs)
        request.databases = dict_databases
        request.response = response
        return request
    return wrapped


@pytest.fixture
def dict_databases():
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


@pytest.fixture
def dict_client():
    """."""
    def wrapped(response_file):
        """Return a DictionaryClient object.

        The client will fake a connection with a a MockSocket which will respond
        with the contents of response_file.
        """
        MockSocket.set_responses(response_file)
        client = DictionaryClient(sock_class=MockSocket)
        return client
    return wrapped
