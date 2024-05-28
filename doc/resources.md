Resources
=========

Data Generating APIs
--------------------

### ASDFast

* [ASDFast](https://asdfast.beobit.net/docs/): Lorem Ipsum API

Fast Lorem Ipsum generator.

```bash
curl "http://asdfast.beobit.net/api/"
```

### lorem-json

* [lorem-json](https://lorem-json.com/)

An API that takes complex specifications in JSON.

```bash
curl "https://lorem-json.com/api/json" --json '{"animals": { "type": "array", "count": 5, "items":  "{{animal()}}"} }'
```

### litipsum.com

* [litipsum.com](https://litipsum.com/)

Random selection of text from the following literary works:

* adventures-sherlock-holmes
* dr-jekyll-and-mr-hyde
* dracula
* evelina
* life-of-samuel-johnson
* picture-of-dorian-gray
* pride-and-prejudice

```bash
curl "https://litipsum.com/api/evelina/10/json"
```

### dinoipsum.com

* [dinoipsum.com](https://dinoipsum.com/)

Random list of dinosaurs.

```bash
curl "https://dinoipsum.com/api/?format=json&words=10&paragraphs=1"
```

Data Sources
------------

### Books

* [Project Gutenberg](https://www.gutenberg.org/ebooks/)

### Word Lists

* [SCOWL (Spell Checker Oriented Word Lists)](http://wordlist.aspell.net/) 
* [12Dicts](http://wordlist.aspell.net/12dicts/): a collection of dictionaries focused on common words
* [Automatically Generated Inflection Database (AGID)](http://wordlist.aspell.net/agid-readme/)
* [dariusk/corpora](https://github.com/dariusk/corpora): json files containing lists of data like animals, colors, foods, mythology, sports, etc

Datamuse Sources
----------------

### WordNet

* [WordNet](https://wordnet.princeton.edu/) -- A Lexical Database for English
* [Wikipedia > Wordnet](https://en.wikipedia.org/wiki/WordNet)

Used for datamuse `rel-syn`.

General
-------

Here are some other word-related tools that I like.

* [Onelook](https://onelook.com/)
* [Wordhippo.com](https://wordhippo.com)
* [Power Thesaurus](https://www.powerthesaurus.org/)
* [Wiktionary](https://en.wiktionary.org/)
* [Rhyme Zone](https://www.rhymezone.com/)
* [Civic Search](https://civicsearch.org/): Search millions of comments made at recent local government meetings


Python Packages
---------------

* [nltk](https://www.nltk.org/): Natural Language Toolkit [How to Create a Text Generator with Python](https://reintech.io/blog/how-to-create-a-text-generator-with-python)
* [Faker](https://faker.readthedocs.io/en/master/): [Using Faker to Generate Random Text](https://www.slingacademy.com/article/python-using-faker-to-generate-random-text/)
* [python-lorem](https://github.com/sfischer13/python-lorem)
