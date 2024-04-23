import pytest
from pytest_socket import SocketBlockedError
from requests import get


def test_no_internet():
    """
    If this fails you need to pass --disable-socket to pytest or add it to your
    pytest config.
    """
    with pytest.raises(SocketBlockedError):
        get("http://google.com")
