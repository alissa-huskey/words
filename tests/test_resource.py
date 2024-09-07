from words import bp, WordsError  # noqa
from words.resource import Resource


def test_resource():
    r = Resource()
    assert r


def test_resource_url():
    template = "https://example.com/search=${WORD}"
    word = "hello"

    r = Resource(template)
    url = r.url(word)
    assert url == f"https://example.com/search={word}"
