"""A dict response status."""

from re import compile as re_compile

from words import WordsError, bp  # noqa


class ResponseStatus():
    """Status and message from a dict response."""

    STATUS_PARSER = re_compile(r'(\d+) ([^[]+)')

    _code: int = None
    _message: str = None

    def __init__(self, code=None, message=None):
        """Assign the code and message.

        Parse the code and message from a status line string or assign the
        values as passed.
        """
        if not self.parse(code):
            self.code = code
            self.message = message

    def parse(self, line):
        """Assign code and message from a parsed line.

        If line looks like a status line string then assign self.code and
        self.message from the parsed result.
        """
        # stop if this doesn't look like a status line
        if not line or len(str(line)) == 3:
            return

        found = self.STATUS_PARSER.search(line)
        self.code, self.message = found and found.groups() or (None, None)

        return True

    @property
    def code(self):
        """Get the code."""
        return self._code

    @code.setter
    def code(self, value):
        """Set the code as an int if valid."""
        # don't bother if nothing was passed
        if not value:
            return

        # raise an error unless it's a 3 digit number
        value = str(value)
        if not (len(value) == 3 and value.isnumeric()):
            raise ValueError(f"Status code should be a 3 digit number not: {value!r}.")

        self._code = int(value)

    @property
    def message(self):
        """Get the message."""
        return self._message

    @message.setter
    def message(self, value):
        """Set the stripped message."""
        self._message = value and value.strip()
