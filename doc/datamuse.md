Datamuse API
============

Docs taken from the official [Datamuse API](https://www.datamuse.com/api/) website and reformatted/rephrased for my own sanity.

* API version:  1.1
* Queries per second:  29
* Latency (/words):  0.65 ms (median), 79.76 ms (99 %ile)
* Latency (/sug):  4.87 ms (median), 60.58 ms (99 %ile)

Examples
--------

In order to find...	...use https://api.datamuse.com…

* words with a meaning similar to ringing in the ears	`/words?ml=ringing+in+the+ears`
* words related to duck that start with the letter b	`/words?ml=duck&sp=b*`
* words related to spoon that end with the letter a	`/words?ml=spoon&sp=*a`
* words that sound like jirraf	`/words?sl=jirraf`
* words that start with t, end in k, and have two letters in between	`/words?sp=t??k`
* words that are spelled similarly to hipopatamus	`/words?sp=hipopatamus`
* adjectives that are often used to describe ocean	`/words?rel_jjb=ocean`
* adjectives describing ocean sorted by how related they are to temperature	`/words?rel_jjb=ocean&topics=temperature`
* nouns that are often described by the adjective yellow	`/words?rel_jja=yellow`
* words that often follow "drink" in a sentence, that start with the letter w	`/words?lc=drink&sp=w*`
* words that are triggered by (strongly associated with) the word "cow"	`/words?rel_trg=cow`
* suggestions for the user if they have typed in rawand so far	`/sug?s=rawand`

/words endpoint
---------------

This endpoint returns a list of words (and multiword expressions) from a given vocabulary that match a given set of constraints.

All parameters are optional.

### Word constraints

Hard constraints filter the result set.

| Param      | Name         | Description                          |
|------------|--------------|--------------------------------------|
| ml         | Means like   | Words with a related meaning.        |
| sl         | Sounds like  | Words that are pronounced similarly. |
| sp         | Spelled like | Common misspellings                  |
| rel_[code] | Related word |                                      |

### Vocabulary Set

|            |                   |
|------------|-------------------|
| v          | Vocabulary source |

### Spelled Like

Accepts wildcard patterns.

### Related Words

Related word constraints: require that the results, when paired with the word in this parameter, are in a predefined lexical relation indicated by [code]. Any number of these parameters may be specified any number of times. An assortment of semantic, phonetic, and corpus-statistics-based relations are available.

[code] is a three-letter identifier from the list below.

| [code] | Description                                                                   | Example           |
|--------|-------------------------------------------------------------------------------|-------------------|
| jja    | Popular nouns modified by the given word, per Google Books Ngrams             | raspy → voice     |
| jjb    | Popular adjectives used to modify the given noun, per Google Books Ngrams     | beach → sandy     |
| syn    | Synonyms (words contained within the same WordNet synset)                     | ocean → sea       |
| trg    | "Triggers", statistically associated words                                    | cow → milking     |
| ant    | Antonyms (per WordNet)                                                        | late → early      |
| spc    | "Kind of" (direct hypernyms, per WordNet)                                     | gondola → boat    |
| gen    | "More general than" (direct hyponyms, per WordNet)                            | boat → gondola    |
| com    | "Comprises" (direct holonyms, per WordNet)                                    | car → accelerator |
| par    | "Part of" (direct meronyms, per WordNet)                                      | trunk → tree      |
| bga    | Frequent followers (w′ such that P(w′ w) ≥ 0.001, per Google Books Ngrams)    | wreak → havoc     |
| bgb    | Frequent predecessors (w′ such that P(w w′) ≥ 0.001, per Google Books Ngrams) | havoc → wreak     |
| hom    | Homophones (sound-alike words)                                                | course → coarse   |
| cns    | Consonant match                                                               | sample → simple   |

#### cns: Consonant Match

Words that match when all vowel phenomes are removed from the words phonetic
Pronunciation transcription.

Here you can see several examples of shared ARPABET pronunciation after the
vowel phenomes have been removed.

┏━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Word   ┃ Pronunciation   ┃ Only Consonants ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ sample │ S AE1 M P AH0 L │ S - M P - L     │
│ simple │ S IH1 M P AH0 L │ S - M P - L     │
│ cow    │ K AW1           │ K -             │
│ key    │ K IY1           │ K -             │
│ coo    │ K UW1           │ K -             │
│ late   │ L EY1 T         │ L - T           │
│ lit    │ L IH1 T         │ L - T           │
│ loot   │ L UW1 T         │ L - T           │
└────────┴─────────────────┴─────────────────┘

For more information see [ARPABET Notation](doc/pronunciation.md#ARPABET Notation).

### Vocabulary sources

* default: a 550,000-term vocabulary of English words and multiword expressions is used.
* es: a 500,000-term vocabulary of words from Spanish-language books
* enwiki: ~6 million-term vocabulary of article titles from the English-language Wikipedia

### Context Hints

Context hints only impact the order in which results are returned.

|            |      |                                 |                                    |                          |
|------------|------|---------------------------------|------------------------------------|--------------------------|
| topics     | opt  | Topic words                     | theme of document                  | space/comma sep, up to 5 |
| lc         | opt  | Left context                    | word that appears to the left      |                          |
| rc         | opt  | Right context                   | word that appears to the right     |                          |

### Output

These parameters impact the nature of information to include in the results.

| Param | Meaning           | Expects      |                                                                          |
|-------|-------------------|--------------|--------------------------------------------------------------------------|
| max   | Max results       | `1` - `1000` |                                                                          |
| md    | Metadata flags    | Letter flag. | Additional lexical information to include.                               |
| qe    | Query echo        |              | ???                                                                      |
| ipa   | IPA Pronunciation | Any value.   | Provide pronunciation in International Phonetic Alphabet notation |

### Metadata

A list of single-letter codes (no delimiter) requesting that extra lexical knowledge be included with the results.

The API makes an effort to ensure that metadata values are consistent with the sense or senses of the word that best match the API query. For example, the word "refuse" is tagged as a verb ("v") in the results of a search for words related to "deny" but as a noun ("n") in the results of a search for words related to "trash". And "resume" is shown to have 2 syllables in a search of synonyms for "start" but 3 syllables in a search of synonyms for "dossier". There are occasional errors in this guesswork, particularly with pronunciations. Metadata is available for both English (default) and Spanish (v=es) vocabularies.

| Letter | Description     | Field(s)          | Prefix | Implementation notes                                                                                       |
|--------|-----------------|-------------------|--------|------------------------------------------------------------------------------------------------------------|
| d      | Definitions     | defs, defHeadword |        | From Wiktionary and WordNet.                                                                               |
| p      | Parts of speech | tags              |        | From Google Books Ngrams.                                                                                  |
| s      | Syllable count  | numSyllables      |        | When ambiguous the system's best guess is chosen.                                                          |
| r      | Pronunciation   | tags              | pron:  | May be based on spelling or the the system's best guess.                                                   |
| f      | Word frequency  | tags              | f:     | Number of times the word/phrase occurs per million words of English text according to Google Books Ngrams. |

Interpreting the results
------------------------

The result of an API call is always a JSON list of word objects, or an empty list (`[]`) if no words match the given constraints.

Results are ordered by popularity or strength of relationship.

Note that popular multiword expressions like "hot dog" are included in the default vocabulary, and these will appear as space-delimited strings.

### Fields

| Field       | Prefix | When   | Meaning                                                                    |
|-------------|--------|--------|----------------------------------------------------------------------------|
| word        |        |        | the matching vocabulary entry                                              |
| score       |        |        | raking of results                                                          |
| defs        |        | `md=d` | list of definitions                                                        |
| tags        |        |        | list of parts of speech, and possibly other prefixed metadata information. |
| tags        | pron:  | `md=r` | Pronunciation                                                              |
| tags        | f:     | `md=f` | Word frequency                                                             |
| defHeadword |        | `md=d` | Base of inflected words when applicable.                                   |
| numSyllables|        | `md=s` | Syllable count.                                                            |
|             |        |        |                                                                            |

#### Parts of speech

Multiple entries will be added when the word's part of speech is ambiguous.

Most popular listed first. 

| Acronym | Meaning                               |
|---------|---------------------------------------|
| n       | noun                                  |
| v       | verb                                  |
| adj     | adjective                             |
| adv     | adverb                                |
| u       | none of these or cannot be determined |

#### Pronunciation

Space-delimited list of Arpabet phoneme codes or a string formatted per International Phonetic Alphabet (if ipa=1 was passed).

Examples
--------

```bash
curl "https://api.datamuse.com/words?ml=ringing+in+the+ears&max=4" | python -mjson.tool
```

```json
[  
   {  
      "word":"tinnitus",
      "score":57312
   },
   {  
      "word":"ring",
      "score":50952
   },
   {  
      "word":"cinchonism",
      "score":50552
   },
   {  
      "word":"acouasm",
      "score":48952
   }
]
```

---

```json
{
    'word': 'accepts',
    'score': 10021555,
    'tags': ['v'],
    'defs': [
        'v\t(transitive) To receive, especially with a consent, with favour, or with approval. ',
        'v\t(transitive) To admit to a place or a group. ',
        'v\t(transitive) To regard as proper, usual, true, or to believe in. ',
        'v\t(transitive) To receive as adequate or satisfactory. ',
        'v\t(transitive) To receive or admit to; to agree to; to assent to; to submit to. ',
        'v\t(transitive) To endure patiently. ',
        'v\t(transitive) To acknowledge patiently without opposition or resistance. ',
        'v\t(transitive, law, business) To agree to pay. ',
        'v\t(transitive) To receive officially. ',
        'v\t(intransitive) To receive something willingly. '
    ],
    'defHeadword': 'accept'
}
```
