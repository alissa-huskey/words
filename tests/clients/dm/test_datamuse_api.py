from words import bp, WordsError  # noqa
from words.clients.dm.datamuse_api import DatamuseAPI


def test_datamuse_api():
    assert DatamuseAPI()


def test_datamuse_params():
    params = DatamuseAPI.params
    assert "ml" in params


def test_datamuse_empty_words():
    """
    GIVEN: A datamuse object with no results.
    WHEN: .data or .words are accessed
    THEN: An empty iter should be returned
    """
    dm = DatamuseAPI()
    assert dm.data == []
    assert dm.words == []
