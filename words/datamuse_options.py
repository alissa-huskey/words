"""Logic and information related to all Datamuse API options."""

from click import Choice, Option

from words.object import Object

bp = breakpoint


class DatamuseOptions(Object):
    """Contains methods to return options in various configurations."""

    PARAMS = [
        {
            "summary": "Reverse dictionary search.",
            "alt-summary": "Similar meaning.",
            "required": True,
            "click": {
                "metavar": "WORD",
            },
            "by": "semantic",
            "grammatical": "",
            "source": {"name": "", "details": ""},
            "relationship": [{"have": "", "get": ""}],
            "datamuse": {
                "param": "ml",
                "param-long": "means-like",
                "description": (
                    "Words with a related meaning. "
                    "(Effectively the reverse dictionary feature of OneLook.)"
                )
            },
            "options": {
                "natural": ["defined-as"],
                "action": "means",
                "returns": ""
            },
            "examples": {
                "cat": ["hat", "bat"]
            }
        },
        {
            "summary": "Pronounced similarly.",
            "required": True,
            "click": {
                "metavar": "WORD",
            },
            "by": "phonetic",
            "grammatical": "minimal pair",
            "source": {"name": "", "details": ""},
            "relationship": [{"have": "", "get": ""}],
            "datamuse": {
                "param": "sl",
                "param-long": "sounds-like",
                "description": "Words that are pronounced similarly.",
                "behavior": (
                    "If the string of characters doesn't have a known pronunciation, "
                    "the system will make its best guess using a text-to-phonemes "
                    "algorithm."
                )
            },
            "options": {
                "natural": ["sounds-close", "phonetically-close", "pronounced-like"],
                "action": "",
                "returns": ""
            },
            "examples": {
                "": [""]
            }
        },
        {
            "summary": "Text and pattern search.",
            "required": True,
            "click": {
                "metavar": "PATTERN",
            },
            "by": "lexical?",
            "grammatical": "",
            "source": {"name": "", "details": ""},
            "datamuse": {
                "param": "sp",
                "param-long": "spelled-like",
                "description": "Words spelled similarly or match a wildcard pattern.",
                "behavior": (
                    "A pattern can include any combination of alphanumeric characters "
                    "and the symbols described on that page. The most commonly used "
                    "symbols are * (a placeholder for any number of characters) and ? "
                    "(a placeholder for exactly one character). Please be sure that "
                    "your parameters are properly URL encoded when you form your"
                    "request."
                )
            },
            "options": {
                "natural": ["text-search", "spell-search"],
                "action": "search",
                "returns": "match"
            },
            "relationship": [{"have": "", "get": ""}],
            "examples": {
                "": [""]
            }
        },
        {
            "summary": "Nouns that can be described by the given adjective.",
            "required": True,
            "click": {
                "metavar": "ADJECTIVE",
            },
            "by": "semantic",
            "grammatical": "",
            "source": {"name": "Google Books Ngrams", "details": ""},
            "datamuse": {
                "param": "rel-jja",
                "param-long": "",
                "description": "Popular nouns modified by the given adjective."
            },
            "options": {
                "natural": ["described-as"],
                "action": "describes",
                "returns": "nouns"
            },
            "relationship": [
                {"have": "adjective", "get": "nouns"},
                {"have": "description", "get": "subjects"}
            ],
            "examples": {
                "gradual": ["increase"]
            }
        },
        {
            "summary": "Adjectives that can be used to described the given noun.",
            "required": True,
            "click": {
                "metavar": "NOUN",
            },
            "by": "semantic",
            "grammatical": "attributive adjective",
            "source": {"name": "Google Books Ngrams", "details": ""},
            "datamuse": {
                "param": "rel-jjb",
                "param-long": "",
                "description": "Popular adjectives used to modify the given noun."
            },
            "options": {
                "natural": ["descriptions-for", "can-be"],
                "action": "seems",
                "returns": "adjectives"
            },
            "relationship": [
                {"have": "noun", "get": "adjectives"},
                {"have": "subject", "get": "descriptions"}
            ],
            "examples": {
                "beach": ["sandy"]
            }
        },
        {
            "summary": "Synonyms.",
            "required": True,
            "click": {
                "metavar": "WORD",
            },
            "by": "semantic",
            "grammatical": "synonym",
            "opposite": "antonym",
            "source": {"name": "WordNet ", "details": "sysnets"},
            "datamuse": {
                "param": "rel-syn",
                "param-long": "related-synonyms",
                "description": "Synonyms."
            },
            "options": {
                "natural": ["words-for"],
                "action": "like",
                "returns": "synonyms"
            },
            "relationship": [{"have": "", "get": ""}],
            "examples": {
                "ocean": ["sea"]
            }
        },
        {
            "summary": "Antonyms.",
            "required": True,
            "click": {
                "metavar": "WORD",
            },
            "by": "semantic",
            "grammatical": "antonym",
            "opposite": "synonym",
            "source": {"name": "WordNet", "details": ""},
            "datamuse": {
                "param": "rel-ant",
                "param-long": "related-antonyms",
                "description": "Antonyms."
            },
            "options": {
                "natural": ["opposite-of"],
                "action": "unlike",
                "returns": "antonyms"
            },
            "relationship": [{"have": "", "get": ""}],
            "examples": {
                "late": ["early"]
            }
        },
        {
            "summary": "Words often said together.",
            "required": True,
            "click": {
                "metavar": "WORD",
            },
            "by": "stastical",
            "grammatical": "",
            "source": {"name": "", "details": ""},
            "datamuse": {
                "param": "rel-trg",
                "param-long": "related-triggers",
                "description": (
                    "Triggers: Words that are statistically associated with the query "
                    "word in the same piece of text."
                )
            },
            "relationship": [{"have": "", "get": ""}],
            "options": {
                "natural": ["said-with"],
                "action": "with",
                "returns": "neighbor"
            },
            "examples": {
                "cow": ["milking"]
            }
        },
        {
            "summary": (
                "Broad categories, general concepts or umbrella terms that cover the "
                "more specific given term."
            ),
            "required": True,
            "click": {
                "metavar": "SUBTYPE",
            },
            "by": "semantic",
            "grammatical": "hypernym",
            "opposite": "hyponym",
            "source": {"name": "WordNet", "details": ""},
            "datamuse": {
                "param": "rel-spc",
                "param-long": "related-specific",
                "description": "Kind of."
            },
            "options": {
                "natural": ["supertype-of", "archetype-of", "superclass-of"],
                "action": "",
                "returns": "supertype"
            },
            "relationship": [
                {"have": "subclass", "get": "superclass"},
                {"have": "subtype", "get": "supertype"},
                {"have": "specific", "get": "generic"},
                {"have": "hyponym", "get": "hypernym"},
                {"have": "precise", "get": "hypernym"}
            ],
            "examples": {
                "gondola": ["boat"],
                "shirt": ["garment", "apparel", "garb"]
            }
        },
        {
            "summary": (
                "Specific examples, instances, or subtypes that falls within the "
                "broader given term."
            ),
            "required": True,
            "click": {
                "metavar": "SUPERTYPE",
            },
            "by": "semantic",
            "grammatical": "hyponym",
            "opposite": "hypernym",
            "source": {"name": "WordNet", "details": ""},
            "relationship": [{"have": "superclass", "get": "subclass"}],
            "datamuse": {
                "param": "rel-gen",
                "param-long": "related-general",
                "description": "More general than."
            },
            "options": {
                "natural": ["subtype-of"],
                "action": "",
                "returns": "subtype"
            },
            "examples": {
                "boat": ["gondola"],
                "garb": ["jacket", "shoe", "shirt"]
            }
        },
        {
            "summary": "Parts or members that belong to something whole.",
            "required": True,
            "click": {
                "metavar": "WHOLE",
            },
            "grammatical": "holonym",
            "opposite": "meronym",
            "source": {"name": "WordNet", "details": ""},
            "relationship": [
                {"have": "whole", "get": "part"},
                {"have": "holonym", "get": "meronyms"}
            ],
            "datamuse": {
                "param": "rel-com",
                "param-long": "related-comprises",
                "description": "Comprises."
            },
            "options": {
                "natural": ["made-of", "has-members", "comprised-of"],
                "action": "has",
                "returns": ["meronym", "part", "member"]
            },
            "examples": {
                "face": ["eye", "mouth", "nose"]
            }
        },
        {
            "summary": "A whole thing where the given term is a parts or member.",
            "required": True,
            "click": {
                "metavar": "PART",
            },
            "grammatical": "meronym",
            "opposite": "holonym",
            "source": {"name": "WordNet", "details": ""},
            "datamuse": {
                "param": "rel-par",
                "param-long": "related-part-of",
                "description": "Part of."
            },
            "options": {
                "natural": ["belongs-to"],
                "action": "is-a",
                "returns": ["holonym", "whole", "sum"]
            },
            "relationship": [
                {"have": "meronym", "get": "holonym"},
                {"have": "part", "get": "whole"}
            ],
            "examples": {
                "trunk": ["tree"]
            }
        },
        {
            "summary": "Words often said after.",
            "required": True,
            "click": {
                "metavar": "WORD BEFORE",
            },
            "grammatical": "",
            "source": {
                "name": "Google Books Ngrams", "details": "w′ such that P(w′|w) ≥ 0.001"
            },
            "relationship": [
                {"have": "before", "get": "after"}
            ],
            "datamuse": {
                "param": "rel-bga",
                "param-long": "related-bg-after",
                "description": "Frequent followers."
            },
            "options": {
                "natural": ["comes-after", "is-after"],
                "action": "follows",
                "returns": ["follower"]
            },
            "examples": {
                "wreak": ["havoc"]
            }
        },
        {
            "summary": "Words often said before.",
            "required": True,
            "click": {
                "metavar": "WORD AFTER",
            },
            "grammatical": "",
            "source": {
                "name": "Google Books Ngrams", "details": "w′ such that P(w|w′) ≥ 0.001"
            },
            "relationship": [
                {"have": "after", "get": "before"},
                {"have": "word", "get": "predecessors"}
            ],
            "datamuse": {
                "param": "rel-bgb",
                "param-long": "related-bg-before",
                "description": "Frequent predecessors."
            },
            "options": {
                "natural": ["comes-before", "preceeds", "that-precede"],
                "action": "preceeds",
                "returns": ["antecedent", "forerunner", "predecessors"]
            },
            "examples": {
                "wreak": ["havoc"]
            }
        },
        {
            "summary": "Different words that sound exactly the same.",
            "required": True,
            "click": {
                "metavar": "WORD",
            },
            "by": "phonetic",
            "grammatical": "homophones",
            "source": {"name": "", "details": ""},
            "relationship": [
                {"have": "", "get": ""}
            ],
            "datamuse": {
                "param": "rel-hom",
                "param-long": "related-homophones",
                "description": "Sound-alike words."
            },
            "options": {
                "natural": ["same-sound"],
                "action": "",
                "returns": ["pronunciation"]
            },
            "examples": {
                "course": ["coarse"]
            }
        },
        {
            "summary": "Words with the same consonant phoneme sounds.",
            "required": True,
            "click": {
                "metavar": "WORD",
            },
            "by": "phonetic",
            "grammatical": "",
            "source": {"name": "", "details": ""},
            "relationship": [
                {"have": "", "get": ""}
            ],
            "datamuse": {
                "param": "rel-cns",
                "param-long": "related-consonant",
                "description": "Consonant match."
            },
            "options": {
                "natural": ["same-consonants"],
                "action": "",
                "returns": [""]
            },
            "examples": {
                "sample": ["simple"]
            }
        },
        {
            "summary": "Max results",
            "click": {
                "default": 10,
                "type": int,
            },
            "datamuse": {
                "param": "max",
            }
        },
        {
            "summary": "Additional metadata to include.",
            "click": {
                "type": Choice(["d", "p", "s", "r", "f"]),
                "multiple": True,
            },
            "datamuse": {
                "param": "md",
            }
        },
        {
            "summary": "Use International Phonetic Alphabet pronunciation format.",
            "click": {
                "is_flag": True,
            },
            "datamuse": {
                "param": "ipa",
            }
        },
    ]

    @classmethod
    @property
    def params(cls):
        """Return a list of valid Datamuse params."""
        return [p.get("datamuse", {}).get("param", "").replace("-", "_")
                for p in DatamuseOptions.PARAMS]

    @classmethod
    @property
    def cli_options(cls):
        """Return a list of valid Datamuse params."""
        options = [
            Option([f"--{p['datamuse']['param']}"], help=p["summary"], **p["click"])
            for p in cls.PARAMS]
        return options
