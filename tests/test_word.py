import pytest

from words.word import Word


def test_word():
    """
    WHEN: a word object is made
    THEN: it should work
    """
    word = Word()
    assert word


def test_word_str():
    """
    GIVEN: a Word object with a word attribute
    WHEN: str(word) is called
    THEN: it should return the word
    """
    word = Word(word="hello")
    assert str(word) == "hello"


def test_word_str_no_word():
    """
    GIVEN: a Word object with no word attribute
    WHEN: str(word) is called
    THEN: it should return the word repr
    """
    word = Word()
    assert str(word) == repr(word)


def test_word_():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    word = Word()
    assert word


@pytest.mark.parametrize(("tags", "parts", "skip"), (
        (["n"], ["n"], False),
        (["n", "a"], ["n", "a"], False),
        (["n", "pron:K R IY1 M "], ["n"], False),
        (['syn', 'v'], ["v"], "TODO"),
))
def test_word_parts(tags, parts, skip):
    """
    GIVEN: a tags list containing some number of parts of speech
           {"score": 20051203, "tags": ["n", "pron:K R IY1 M "], "word": "cream"},
    WHEN: word.tags is assigned
    THEN: word.parts should return a list of those parts
    """

    if skip:
        pytest.skip(skip)
    word = Word(tags=tags)
    assert word.parts == parts


def test_word_tags_kvp():
    """
    GIVEN: a tags list containing values in the form of "key: value"
    WHEN: word.tags is assigned
    THEN: each should be set as attrs
    """
    word = Word(tags=["n", "pron:K R IY1 M "])
    assert word.pron == "K R IY1 M "
