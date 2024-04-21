Datamuse API
============

Docs taken from the official [Datamuse API](https://www.datamuse.com/api/) website.

* API version:  1.1
* Queries per second:  29
* Latency (/words):  0.65 ms (median), 79.76 ms (99 %ile)
* Latency (/sug):  4.87 ms (median), 60.58 ms (99 %ile)

Examples
--------

In order to find...	...use https://api.datamuse.com…

* words with a meaning similar to ringing in the ears	/words?ml=ringing+in+the+ears
* words related to duck that start with the letter b	/words?ml=duck&sp=b*
* words related to spoon that end with the letter a	/words?ml=spoon&sp=*a
* words that sound like jirraf	/words?sl=jirraf
* words that start with t, end in k, and have two letters in between	/words?sp=t??k
* words that are spelled similarly to hipopatamus	/words?sp=hipopatamus
* adjectives that are often used to describe ocean	/words?rel_jjb=ocean
* adjectives describing ocean sorted by how related they are to temperature	/words?rel_jjb=ocean&topics=temperature
* nouns that are often described by the adjective yellow	/words?rel_jja=yellow
* words that often follow "drink" in a sentence, that start with the letter w	/words?lc=drink&sp=w*
* words that are triggered by (strongly associated with) the word "cow"	/words?rel_trg=cow
* suggestions for the user if they have typed in rawand so far	/sug?s=rawand

/words endpoint
---------------

This endpoint returns a list of words (and multiword expressions) from a given vocabulary that match a given set of constraints.

In the table below, the first four parameters (rd, sl, sp, rel_[code], and v) can be thought of as hard constraints on the result set, while the next three (topics, lc, and rc) can be thought of as context hints. The latter only impact the order in which results are returned. All parameters are optional.

|            |    |                   |                                    |                          |
|------------|----|-------------------|------------------------------------|--------------------------|
| ml         |main    | Means like        |                                    |                          |
| sl         |main    | Sounds like       |                                    |                          |
| sp         |main    | Spelled like      |                                    | wildcard patterns        |
| rel_[code] |main    | Related word      | words related in a particular way  |                          |
| v          |opt | Vocabulary source |                                    |                          |
| topics     |opt | Topic words       | theme of document                  | space/comma sep, up to 5 |
| lc         |opt | Left context      | word that appears to the left      |                          |
| rc         |opt | Right context     | word that appears to the right     |                          |
| max        |opt | Max results       |                                    | (default 100, max: 1000) |
| md         |opt | Metadata flags    | extra lexical knowledge to include |                          |
| qe         |    | Query echo        | ???                                |                          |

### vocabulary sources

* default: a 550,000-term vocabulary of English words and multiword expressions is used.
* es: a 500,000-term vocabulary of words from Spanish-language books
* enwiki: ~6 million-term vocabulary of article titles from the English-language Wikipedia

### related words

[code] is a three-letter identifier from the list below.

| [code] | Description                                                               | Example                               |
|--------|---------------------------------------------------------------------------|---------------------------------------|
| jja    | Popular nouns modified by the given adjective, per Google Books Ngrams    | gradual → increase                    |
| jjb    | Popular adjectives used to modify the given noun, per Google Books Ngrams | beach → sandy                         |
| syn    | Synonyms (words contained within the same WordNet synset)                 | ocean → sea                           |
| trg    | "Triggers", statistically associated words                                | cow → milking                         |
| ant    | Antonyms (per WordNet)                                                    | late → early                          |
| spc    | "Kind of" (direct hypernyms, per WordNet)                                 | gondola → boat                        |
| gen    | "More general than" (direct hyponyms, per WordNet)                        | boat → gondola                        |
| com    | "Comprises" (direct holonyms, per WordNet)                                | car → accelerator                     |
| par    | "Part of" (direct meronyms, per WordNet)                                  | trunk → tree                          |
| bga    | Frequent followers (w′ such that P(w′                                     | w) ≥ 0.001, per Google Books Ngrams)  | wreak → havoc |
| bgb    | Frequent predecessors (w′ such that P(w                                   | w′) ≥ 0.001, per Google Books Ngrams) | havoc → wreak |
| hom    | Homophones (sound-alike words)                                            | course → coarse                       |
| cns    | Consonant match                                                           | sample → simple                       |

### metadata flags

| Letter | Description     | Implementation notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| d      | Definitions     | Produced in the defs field of the result object. The definitions are from Wiktionary and WordNet. If the word is an inflected form (such as the plural of a noun or a conjugated form of a verb), then an additional defHeadword field will be added indicating the base form from which the definitions are drawn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| p      | Parts of speech | One or more part-of-speech codes will be added to the tags field of the result object. "n" means noun, "v" means verb, "adj" means adjective, "adv" means adverb, and "u" means that the part of speech is none of these or cannot be determined. Multiple entries will be added when the word's part of speech is ambiguous, with the most popular part of speech listed first. This field is derived from an analysis of Google Books Ngrams data.                                                                                                                                                                                                                                                                                                                                                                                                         |
| s      | Syllable count  | Produced in the numSyllables field of the result object. In certain cases the number of syllables may be ambiguous, in which case the system's best guess is chosen based on the entire query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| r      | Pronunciation   | Produced in the tags field of the result object, prefixed by "pron:". This is the system's best guess for the pronunciation of the word or phrase. The format of the pronunication is a space-delimited list of Arpabet phoneme codes. If you add "&ipa=1" to your API query, the pronunciation string will instead use the International Phonetic Alphabet. Note that for terms that are very rare or outside of the vocabulary, the pronunciation will be guessed based on the spelling. In certain cases the pronunciation may be ambiguous, in which case the system's best guess is chosen based on the entire query.                                                                                                                                                                                                                                   |
| f      | Word frequency  | Produced in the tags field of the result object, prefixed by "f:". The value is the number of times the word (or multi-word phrase) occurs per million words of English text according to Google Books Ngrams.The API makes an effort to ensure that metadata values are consistent with the sense or senses of the word that best match the API query. For example, the word "refuse" is tagged as a verb ("v") in the results of a search for words related to "deny" but as a noun ("n") in the results of a search for words related to "trash". And "resume" is shown to have 2 syllables in a search of synonyms for "start" but 3 syllables in a search of synonyms for "dossier". There are occasional errors in this guesswork, particularly with pronunciations. Metadata is available for both English (default) and Spanish (v=es) vocabularies. |

Interpreting the results
------------------------

For both /words and /sug, the result of an API call is always a JSON list of word objects, like so:

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

Each list item is an object that contains the matching vocabulary entry ("word") and some metadata, currently just an integer score. An empty list ([]) will be returned if no words or phrases are found that match your constraints. Note that popular multiword expressions like "hot dog" are included in the default vocabulary, and these will appear as space-delimited strings.

For queries that have a semantic constraint, results are ordered by an estimate of the strength of the relationship, most to least. Otherwise, queries are ranked by an estimate of the popularity of the word in written text, most to least. At this time, the "score" field has no interpretable meaning, other than as a way to rank the results.
