CLI API
=======

Brainstorm about the best CLI api.

Examples
--------

* words with a meaning similar to ringing in the ears: /words?ml=ringing+in+the+ears

```
words --ml "ringing in the ears"
```

* words related to duck that start with the letter b: /words?ml=duck&sp=b

```
words --ml duck -sp 'b*'
```

* words related to spoon that end with the letter a: /words?ml=spoon&sp=*a

```
words --ml spoon -sp '*a'
```

* words that sound like jirraf: words?sl=jirraf

```
words --sl 'jirraf
```

* words that start with t, end in k, and have two letters in between: /words?sp=t??k

```
words --sp 't??k'
```

* words that are spelled similarly to hipopatamus: /words?sp=hipopatamus

```
words --sp 
```

* adjectives that are often used to describe ocean: /words?rel_jjb=ocean

```
words --rel jjb ocean
```

* adjectives describing ocean sorted by how related they are to temperature: /words?rel_jjb=ocean&topics=temperature

```
words --rel jjb ocean --top temperature
```

* nouns that are often described by the adjective yellow: /words?rel_jja=yellow

```
words --rel jja yellow
```

* words that often follow "drink" in a sentence, that start with the letter w: /words?lc=drink&sp=w*

```
words --lc drink --sp 'w*'
```

* words that are triggered by (strongly associated with) the word "cow": /words?rel_trg=cow

```
words --rel trg cow
```
