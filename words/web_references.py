"""List of WebReferences."""

from words import bp, WordsError  # noqa
from words.collection import Collection
from words.resource import Resource
from words.web_reference import WebReference

REFERENCES = Collection(
    "options",
    WebReference(
        name="WordHippo",
        options=("wh", "wordhippo"),
        resources=(
            Resource(name="Synonyms", option="syn", template="https://www.wordhippo.com/what-is/another-word-for/${WORD}.html"),
            Resource(name="Antonyms", option="ant", template="https://www.wordhippo.com/what-is/the-opposite-of/${WORD}.html"),
            Resource(name="Definitions", option="def", template="https://www.wordhippo.com/what-is/the-meaning-of-the-word/${WORD}.html"),
            Resource(name="Rhymes", option="rhy", template="https://www.wordhippo.com/what-is/words-that-rhyme-with/${WORD}.html"),
            Resource(name="Sentences", option="sent", template="https://www.wordhippo.com/what-is/sentences-with-the-word/${WORD}.html"),
            Resource(name="Pronounciations", option="pron", template="https://www.wordhippo.com/what-is/how-do-you-pronounce-the-word/${WORD}.html"),
            #  Resource(
            #      name="Word Forms",
            #      option="forms",
            #      forms=("plural", "singular", "past-tense", "present-tense", "verb", "adjective", "adverb", "noun"),
            #      template="https://www.wordhippo.com/what-is/the-${FORM}-of/${WORD}.html",
            #  ),
            #  Resource(
            #      name="Find Words",
            #      option="find",
            #      template="https://www.wordhippo.com/what-is/words-starting-with/archiv.html",
            #      template="https://www.wordhippo.com/what-is/starting-with/5-letter-words-archiv.html",
            #  ),
        )
    ),
)
