"""Module for web resources."""

from string import Template

from words import bp, WordsError  # noqa
from words.object import Object


class Resource(Object):
    """Resource belonging to a web word reference.

    A specific search associated with a URL.
    """

    _template: str = None
    """URL template for web search.

    For example: "https://example.com/search=${WORD}"
    """

    def __init__(self, template=None, **kwargs):
        """Create object.

        Keyword Args:
            template (str): URL template for web search.
            name (str): Name of the type of search.
            option (str): CLI option name.

        Example:
            >>> Resource(name="Define", option="def", template="http://d.com/q=${WORD}")
        """
        self.template = template
        super().__init__(**kwargs)

    @property
    def template(self):
        """Get template."""
        if not self._template:
            return
        return Template(self._template)

    @template.setter
    def template(self, value):
        """Set template."""
        self._template = value

    def url(self, word):
        """Return the URL to search for `word`."""
        if not self.template:
            return

        return self.template.substitute(WORD=word)


RESOURCES = {
    "https://www.wordhippo.com/what-is/another-word-for/${WORD}.html"
}
