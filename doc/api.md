CLI API
=======

Brainstorm about the best CLI api.

Commands
--------

The ideal commands might be:

| Command/Aliases    | Source   |             | Meaning                                     |
|--------------------|----------|-------------|---------------------------------------------|
| `def`, `dict`, `d` | Dict.org |             | define a word                               |
| `syn`, `thes`      | datamuse | `--rel-syn` | look for similar words                      |
| `ant`              | datamuse | `--rel-ant` | antonyms                                    |
| `rand`, `random`   | local    |             | provide one or more random words or phrases |

| Param | Name         | Description                                | Example          |
|-------|--------------|--------------------------------------------|------------------|
| ml    | Means like   | Words with similar dictionary definitions. | provoke → raise  |
| sl    | Sounds like  | Words that are pronounced similarly.       | slack → slick    |
| sp    | Spelled like | Common misspellings                        | dessert → desert |

| [code] | flag                                | Description                                                                   | Example            |
|--------|-------------------------------------|-------------------------------------------------------------------------------|--------------------|
| jja    |                                     | Popular nouns modified by the given adjective, per Google Books Ngrams        | gradual → increase |
| jjb    | describe, adj, adjectives-for       | Popular adjectives used to modify the given noun, per Google Books Ngrams     | beach → sandy      |
| syn    | syn                                 | Synonyms (words contained within the same WordNet synset)                     | ocean → sea        |
| trg    |                                     | "Triggers", statistically associated words                                    | cow → milking      |
| ant    | ant                                 | Antonyms (per WordNet)                                                        | late → early       |
| spc    | is-a, type, parent, category        | "Kind of" (direct hypernyms, per WordNet)                                     | gondola → boat     |
| gen    | hyponyms, subtypes, chidren         | "More general than" (direct hyponyms, per WordNet)                            | boat → gondola     |
| com    | holonyms, parts, component, members | "Comprises" (direct holonyms, per WordNet)                                    | car → accelerator  |
| par    | meronyms, member-of, belong-to      | "Part of" (direct meronyms, per WordNet)                                      | trunk → tree       |
| bga    | after                               | Frequent followers (w′ such that P(w′ w) ≥ 0.001, per Google Books Ngrams)    | wreak → havoc      |
| bgb    | before                              | Frequent predecessors (w′ such that P(w w′) ≥ 0.001, per Google Books Ngrams) | havoc → wreak      |
| hom    | homophones, same-sound              | Homophones (sound-alike words)                                                | course → coarse    |
| cns    |                                     | Consonant match                                                               | sample → simple    |


Current API
-----------

The CLI thus far was written just for datamuse, so the options are limited 
