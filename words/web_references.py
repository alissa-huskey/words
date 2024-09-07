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
    WebReference(
        name="Wordnik",
        options=("wn", "wordnik"),
        resources=(
            Resource(name="lookup", option="l", template="https://wordnik.com/words/${WORD}"),
        )
    ),
    WebReference(
        name="OneLook",
        options=("ol", "onelook"),
        help="? any letter, * any number of letters, # consonant, @ vowel, -abcd disallow letters, +abcd restrict to letters, //abcd// unscramble, expand:, reverse acronym pattern:meaning",
        resources=(
            Resource(name="Query", option="query", template="https://onelook.com/?w=${WORD}"),
            Resource(name="Related Words", option="rel", template="https://onelook.com/?w=${WORD}&related=1"),
            Resource(name="Mentions", option="men", template="https://onelook.com/?w=${WORD}&mentions=1"),
            Resource(name="Lyrics", option="lyr", template="https://onelook.com/?w=${WORD}&verses=1"),
            Resource(name="History", option="his", template="https://onelook.com/?w=${WORD}&history=1"),
            Resource(name="Thesaurus", option="thes", template="https://onelook.com/thesaurus/?s=${WORD}"),
        )
    ),
    WebReference(
        name="Merriam-Webster",
        options=("mw", "webster"),
        resources=(
            Resource(name="Dictionary", option="dict", template="https://www.merriam-webster.com/dictionary/${WORD}"),
            Resource(name="Thesaurus", option="thes", template="https://www.merriam-webster.com/thesaurus/${WORD}"),
        )
    ),
    WebReference(
        name="Wiktionary",
        options=("wt", "wik"),
        resources=(
            Resource(name="Wiki", option="wiki", template="https://en.wiktionary.org/wiki/${WORD}"),
        )
    ),
    WebReference(
        name="Wikipedia",
        options=("wp", "wikipedia"),
        resources=(
            Resource(name="Wiki", option="wiki", template="https://en.wikipedia.org/wiki/${WORD}"),
        )
    ),
    WebReference(
        name="Power Thesaurus",
        options=("pt", "power"),
        resources=(
            Resource(name="Synonyms", option="syn", template="https://www.powerthesaurus.org/${WORD}/synonyms"),
            Resource(name="Antonyms", option="ant", template="https://www.powerthesaurus.org/${WORD}/antonyms"),
            Resource(name="Definitions", option="def", template="https://www.powerthesaurus.org/${WORD}/definitions"),
            Resource(name="Sentences", option="sent", template="https://www.powerthesaurus.org/${WORD}/sentences"),
            Resource(name="Thesaurus", option="thes", template="https://www.powerthesaurus.org/${WORD}"),
        )
    ),
    WebReference(
        name="Rhyme Zone",
        options=("rz", "rhyme"),
        resources=(
            Resource(name="Rhymes", option="rhy", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&typeofrhyme=perfect&org1=syl&org2=l&org3=y"),
            Resource(name="Near Rhymes", option="near", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=nry"),
            Resource(name="Thesaurus", option="thes", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=syn"),
            Resource(name="Phrases", option="phrase", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=phr"),
            Resource(name="Phrase Rhymes", option="ph-rhy", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=pry"),
            Resource(name="Descriptive Words", option="desc", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=jjb"),
            Resource(name="Definitions", option="def", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=def"),
            Resource(name="Similar Sounds", option="sound", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=sim"),
            Resource(name="Same Consonants", option="cons", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&org1=syl&org2=l&org3=y&typeofrhyme=cons"),
            Resource(name="Anagrams", option="ana", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&typeofrhyme=ana&org1=syl&org2=l&org3=y"),
            Resource(name="Homophones", option="hom", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&typeofrhyme=hom&org1=syl&org2=l&org3=y"),
            Resource(name="Similarly Spelled", option="spell", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&typeofrhyme=spell&org1=syl&org2=l&org3=y"),
            Resource(name="Find", option="find", template="https://www.rhymezone.com/r/rhyme.cgi?Word=${WORD}&typeofrhyme=sub&org1=syl&org2=l&org3=y"),
        )
    ),
)
