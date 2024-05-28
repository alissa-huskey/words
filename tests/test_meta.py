import pytest
from pytest_socket import SocketBlockedError
from requests import get
from requests.exceptions import ConnectionError

from words import bp, WordsError  # noqa


#  @pytest.mark.skip
def test_no_internet():
    """
    If this fails you need to pass --disable-socket to pytest or add it to your
    pytest config.
    """
    with pytest.raises((SocketBlockedError, ConnectionError)):
        get("http://google.com")
