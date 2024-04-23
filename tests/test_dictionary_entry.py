from words.dictionary_entry import DictionaryEntry


def test_dictionary_entry():
    entry = DictionaryEntry(
        "head",
        "gcide",
        "-head \\-head\\ (-h[e^]d), suffix.\n   "
        "A variant of {-hood}.\n   [1913 Webster]"
    )
    assert entry
