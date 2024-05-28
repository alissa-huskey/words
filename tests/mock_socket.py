from words import bp, WordsError  # noqa

r"""Module for creating mock socket.socket objects.

Example:
    >>> from tests import MockSocket
    >>> MockSocket.set_responses("moon.def")
    >>> sock = MockSocket()
    >>> sock.recv(200)
    b'220 dict.dict.org dictd 1.12.1/rf on Linux 4.19.0-10-amd64 <auth.mime> <298764503.11281.1713863891@dict.dict.org>\r\n'
    >>> sock.sendall("FAUX COMMAND")
    >>> sock.recv(200)
    >>> sock.sendall("FAUX COMMAND")
    >>> sock.recv(200)
    b'250 ok\r\n'
    >>> sock.sendall("FAUX COMMAND")
    >>> sock.recv(200)
    b'150 6 definitions retrieved\r\n'
    >>> sock.recv(200)
    b'151 "Moon" gcide "The Collaborative International Dictionary of English v.0.48"\r\n'
    >>> sock.recv(200)
    b'Moon \\Moon\\ (m[=oo]n), n. [OE. mone, AS. m[=o]na; akin to D.\r\n'
    >>> sock.close()
"""

from pathlib import Path


class MockSocket(object):
    """Mock of a socket object for DictionaryClient."""

    path = Path(__file__).parent / "data"
    """Root directory for the response files."""

    headers = ("header-1", "header-2")
    """Files that contain the response to the initial handshake requests."""

    responses = []
    """Files that contain the all response filenames, set dynamically."""

    _fp = None
    """Private attr for the current open file pointer."""

    @classmethod
    def set_responses(cls, *responses):
        """Set a list of one or more response files.

        Set the list of response files at the class level instead of the
        instance, since we can't control that.
        """
        cls.responses = list(cls.headers + responses)

    def __init__(self, *args, **kwargs):
        """Make the object."""

    @property
    def fp(self):
        """Open (if needed) and return a file stream.

        If self._fp is empty, fetch the next file from the self.responses stack,
        open a new stream, and return it.
        """
        if not self._fp:
            if not self.responses:
                raise Exception("MockSocket has run out of response files.")
            name = self.responses.pop(0)
            self.filepath = self.path / name
            self._fp = self.filepath.open("rb")
        return self._fp

    def sendall(self, content):
        """Close and clear the current stream.

        This triggers the next response file in the stack to be opened and read
        on the next recv() call, effictively mimicking a series of responses.
        """
        self.fp.close()
        self._fp = None

    def recv(self, size):
        """Return one line of up to size bytes from the file."""
        return self.fp.readline(size)

    def fileno(self):
        """Return the file descriptor number."""
        return self.fp.fileno()

    def close(self):
        """Close the file stream."""
        return self.fp.close()

    def connect(self, *args, **kwargs):
        """Do nothing."""
