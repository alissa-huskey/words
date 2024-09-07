from words import bp, WordsError  # noqa
from words.web_reference import WebReference


def test_web_reference():
    ref = WebReference()
    assert ref
    assert ref.resources
