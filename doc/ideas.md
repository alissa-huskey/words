
| [code] | flag                                                              | Description                                                                   | Example           |
|--------|-------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------|
| jja    | nouns, describes, nouns-about, described-by, can-describe, can-be, nouns-that-are | Popular nouns modified by the given word, per Google Books Ngrams             | raspy → voice     |
| jjb    | describe, adj, adjectives-for, descriptions-for, adj-for          | Popular adjectives used to modify the given noun, per Google Books Ngrams     | beach → sandy     |
| syn    | syn, synonyms, word-for                                           | Synonyms (words contained within the same WordNet synset)                     | ocean → sea       |
| trg    | linked, connected, paired, paired-with                            | "Triggers", statistically associated words                                    | cow → milking     |
| ant    | ant, antonyms, opposite-of                                        | Antonyms (per WordNet)                                                        | late → early      |
| spc    | is-a, type, parent, category, kind-of, type-of                    | "Kind of" (direct hypernyms, per WordNet)                                     | gondola → boat    |
| gen    | hyponyms, subtypes, chidren, examples-of,                         | "More general than" (direct hyponyms, per WordNet)                            | boat → gondola    |
| com    | holonyms, parts, component, members, has                          | "Comprises" (direct holonyms, per WordNet)                                    | car → accelerator |
| par    | meronyms, member-of, belong-to                                    | "Part of" (direct meronyms, per WordNet)                                      | trunk → tree      |
| bga    | after                                                             | Frequent followers (w′ such that P(w′ w) ≥ 0.001, per Google Books Ngrams)    | wreak → havoc     |
| bgb    | before                                                            | Frequent predecessors (w′ such that P(w w′) ≥ 0.001, per Google Books Ngrams) | havoc → wreak     |
| hom    | homophones, same-sound                                            | Homophones (sound-alike words)                                                | course → coarse   |
| cns    |                                                                   | Consonant match                                                               | sample → simple   |

