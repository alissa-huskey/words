CLI API
=======

Brainstorm about the best CLI api.

Datamuse
--------

More intuitive commands/flags/parameters for the current Datamuse API.

For each parameter below there is a description of the command, a description
of its behavior, and examples of the results for various words from the top 20
results.

The examples are not exhaustive. I chose them based on my own subjective and
inscrutable criteria.

I omit most prepositions, but they almost always show up in `rel-bga`,
`rel-bgb` and others. (Like: to, and, the, or, in, the, as, a, his, was, so,
be, from, this, not, for...).

A set of square brackets (`[]`) indicates no matches, or very occasionally that
there are no matches except for propositions, derived forms of the word, or
words that seem made up.

| orig (s) | orig (l)           | datamuse desciption                     | Technical             | natural language                                            | action        | returns                           |
|----------|--------------------|-----------------------------------------|-----------------------|-------------------------------------------------------------|---------------|-----------------------------------|
| ml       | means-like         | reverse dictionary                      |                       | defined-as                                                  | means         |                                   |
| sl       | sounds-like        | pronounced similarly                    | minimal-pair          | sounds-close, phonetically-close, pronounced-like           |               |                                   |
| sp       | spelled-like       | similar spelling/match wildcard pattern |                       | text-search search, spell-search                            | search        | match                             |
| rel-jja  |                    | popular per Google Books Ngrams         |                       | modified-by, described-as                                   | describes     | nouns                             |
| rel-jjb  |                    | per Google Books Ngrams                 | attributive adjective | descriptions-for, can-be                                    | seems         | adjectives                        |
| rel-syn  | related-synonyms   | same WordNet synset                     | synonym               | words-for                                                   | like          | synonyms                          |
| rel-ant  | related-antonyms   | per WordNet                             | antonym               | opposite-of                                                 | unlike        | antonyms                          |
| rel-trg  | related-triggers   | statistically associated                |                       | said-with, concurent, associated                            | with          | neighbor, sibling                 |
| rel-spc  | related-specific   | direct hypernym, per WordNet            | hypernym              | class-of, superset-of, models-for                           | superclasses  | superset                          |
| rel-gen  | related-general    | more general than, per WordNet          | hyponym               | [subtype/sebset/example/child/model]-of                     | subclasses    | subset                            |
| rel-com  | related-comprises  | "Comprises"                             | holonyms              | made-of, members-of, comprises                              | has           | meronym, part, member             |
| rel-par  | related-part-of    | "Part-of",  per WordNet                 | meronyms              | part-of, belongs-to                                         | is-a          | holonym, whole, sum               |
| rel-bga  | related-bg-after   | Frequently after, Google Books Ngrams   |                       | follows, comes-after, is-after                              | follows       | follower                          |
| rel-bgb  | related-bg-before  | Frequently before, Google Books Ngrams  |                       | comes-before, preceeds that-precede                         | preceeds      | antecedent, forerunner, preceeder |
| rel-hom  | related-homophones | sound-alike words                       | homophones            | same-sound, sound/s(same/identical/matches), prounounced-as |               | pronunciation                     |
| rel-cns  | related-consonant  | consonant match                         |                       | same-consonants                                             |               |                                   |

### ml

> Means like
> Words with similar dictionary definitions.
>
> API: defined-as, means, means-like, ml
>

provoke → molest, hassle, arouse, harry, elicit, kindle, plague
awake → alert, alive, up, sleepless
beach → shore, shoreline, waterfront, seaside, coast
cow → bovine, bull, oxen, beef, cowboy, pig
slack → slow, slow up, abate, let up, weak, limp, slump
dessert → sweet, confection, candy, cake, eat, tart, hindsight
sandy → sandlike, gritty, granular, grainy, flaxen
late → tardy, lateish, belatedly, dead, latter, recent
gondola → car, cabana, cockpit, basket, compartment
car → automobile, machine, elevator car, bus, passenger
trunk → tree trunk, torso, boot, body, elephant
wreak → havoc, inflict, provoke, spread, create, unleash

* defined-as
* means
* same meaning
* shared meaning
* definition

### sl

> * [Wikipedia > Minimal Pair](https://en.wikipedia.org/wiki/Minimal_pair)

A set of two words or phrases that, when spoken, differ in only one
phonological element.

> Words that are pronounced similarly.
> Usually the same number of syllables
>
> sl, sounds-like, sounds-close, phonetically-like, minimal-pairs
>
>
> phonetic, phoneme, sound patterns, substitution of one phoneme, speech sounds, distinct speech sound
> one phoneme difference, minimal pair
>

slack → slick
awake → awoke, a walk, quake, away
provoke → provoked, provokes, provoker, privy, presoak, brevik
beach → beech, batch, butch, botch, peach
cow → kow, cao, caw
slack → sleek, slag, slake, slyke, sack
dessert → desert, dissert, tizard, does it, deciet
sandy → sandi, sandee, cindi, santi
late → let, laid, leight
gondola → candella, candela, gaudily, giddily, candel
car → core, carr, corps, cower
trunk → trank, drunk, drink, shrunk
wreak → reek, reak, rack, wreak

* minimal-pairs
* phoneticly-like
* sound-like, sl
* sounds-close-to
* near-sound
* like-sound
* alike-sound
* similar-sound
* close-sound
* near-to-sound
* alike-sound
* like-sound
* approx-sound
* similar
* alike
* near-same
* almost-same
* like
* close
* audibly
* to the ear
* verbally/vocally
* when spoken
* orally
* heard
* pronounced
* said
* dictated
* voiced

### sp

> Spelled like
> Words that are spelled similarly.
> Also find words using patterns with wildcards.
> Find words by spelling
>
> sp, spelled-like, text-search, search
>

dessert → desert
awake → wake, aware, awoke
provoke → []
beach → breach, reach, teach, bench, leach
cow → []
slack → black, stack, lack, smack, flack
dessert → desert, dissert
sandy → candy, sand, dandy, randy, andy
late → []
gondola → []
car → []
trunk → truck, drunk, thunk, trank, crunk

* text-search
* spelled-like, sp
* spell-search
* find-by-spelling, letters, characters
* letter-search
* expression
* char-pattern
* text/spell/spelling search/lookup
* modified by

### rel-jja

> Popular nouns modified by the given word, per Google Books Ngrams
>
> rel-jja, modified-by, described-as, seem, nouns
>

raspy → voice
awake → nights, state, thinking, monkeys, man
provoke → shame, anger
beach → []
cow → dung, boy, milk, tail, wheat, pens
slack → water, season, time, demand, rope, hand, mouth
dessert → spoon
sandy → soil, beach, hair, bottom, clay, areas
car → family, train, smell, garage, fleet, races
late → century, afternoon, years, war, hour
gondola → days
trunk → maker, line, fish, armour, legs, rotation

sandy describes beach

* described-as
* seems
* that-are
* can-be
* nouns-that-are
* nouns-described-as
* described-by
* nouns-called
* nouns
* nouns-labeled
* represented-as
* characterized-as
* said-to-be
* seen-as
* said-to-be
* styled
* can-describe
* considered
* nouns-seen-as
* deemed
* seem
* look-as-if
* evoke
* exhibit being
* regarded-as

### rel-jjb

> Popular adjectives used to modify the given noun, per Google Books Ngrams
>
> rel-jjb, descriptions-for, adjectives
>

beach → sandy
awake → wide, stay, lay, lie
provoke → good, bad, bold, first, less
beach → sandy, white, long, private, small, public
cow → old, holy, white, fat, young, big, brown
slack → little, much, enough, economic, considerable, extra
dessert → favorite, rich, delicious, frozen, traditional, extra
sandy → old, poor, young, right, bold
late → little, open, hour, better, bloody, icy, till
gondola → venetian, black, large, open, private, single, overturned
car → new, old, private, motor, used, street, black, armored
trunk → main, old, common, large, hollow, arterial, fallen

car seems new

* descriptions-for
* adjectives-for
* adj
* adj-for

### rel-syn

> Synonyms (words contained within the same WordNet synset)
>
> rel-syn, words-for, synonyms, like
>

ocean → sea
awake → alive, arouse, wake, alert, come alive
provoke → fire, elicit, raise, evoke, beset
beach → []
cow → overawe, moo-cow
slack → loose, abate, slump, limp, slake, let up
dessert → sweet
sandy → light, gritty, beachy, granulose
late → new, modern, former, advanced, tardy, recent, lately
gondola → car
car → machine, automobile, gondola, motorcar, elevator car
trunk → body, boot torso, bole, luggage compartment

* word-for
* like
* synonyms

### rel-ant

> Antonyms (per WordNet)
>
> rel-ant, opposite-of, unlike, antonyms
>

late → early
awake → doze off, drift off, fall asleep, nod off
provoke → []
beach → []
cow → []
slack → []
dessert → []
sandy → clayey, argillaceous
late → early, middle, ahead of time, too soon
gondola → []
car → []
trunk → []

* opposite-of
* antonyms, ant
* unlike

### rel-trg

> "Triggers", statistically associated words
>
> rel-trg, said-with, goes-with,
>

cow → milking
awake → everlasting, rem, dreaming, breathe
provoke → laughter, allergic, jealousy, outrage, wrath
beach → surf, volleyball, dunes, palm, erosion, resort
cow → dung, milking, calf, manure, pasture
slack → beamer, maul, rope, constraints, tide
dessert → balkava, meringue, flan, custard, pudding, pastry
sandy → loam, silty, bottoms, hook, muddy, flats
late → lettermen, century, afternoon, early, gothic, night
gondola → chairlift, lift, envelope, resort, aerial
car → dealership, porsche, driver, crash, rental
trunk → buttressed, scaly, lid, circumference, branches, tree

* said-together
* with
* coincides-with
* co-exists
* happens-with
* goes-with
* affinity
* sibling
* tied-to
* accompanies
* co-occurrent
* said-together-with
* attends
* fellow / fellowship
* frequents
* mingles
* company
* pal
* complement
* mate
* partner
* complementary, complement
* associate
* companion
* peer
* counterpart
* neighbor
* affiliate
* consort
* sidekick
* accomplice
* often-said-with
* colleague
* complement
* affiliated
* acquaintance
* associate
* concurent
* linked-to
* triggered-by
* often-with
* along-with
* accompanied-by
* together-with
* spoken-with
* said-with
* coupled-with
* paired-with
* found-with
* seen-together
* connected-to
* found-together
* often-together
* together-with
* linked
* associated-with
* paired
* paired-with

### rel-spc (specific)

> "Kind of" (direct hypernyms, per WordNet)
>
> rel-spc, kind-of, class-of, parents
>

beach → land, formation, geology
elephant → animal
gondola → boat
awake → sleep, slumber, kip
provoke → do, make, challenge, cause, bother, annoy
cow → awe, oxen, cattle, kine, bos taurus
slack → play, stretch, loose, neglect, shrink, hydrate
dessert → course
sandy → []
late → []
gondola → boat
car → compartment, motor vehicle, wheeled vehicle
trunk → stem, stalk, luggage, baggage, snout, body part

more specific → more general

* is-a
* archetype-of
* superset-of
* class-of
* model-of
* broad/general/overarching
* type/category/kind
* is-a
* words that are a subtype of
* type
* parent
* category
* kind-of

### rel-gen

> "More general than" (direct hyponyms, per WordNet)

boat → gondola
awake → []
provoke → draw, interest, upset, lure, wound, shame
beach → plage
cow → buffalo, heifer, springer
slack → air-slake
dessert → pudding, trifle, mouse, dumpling, ambrosia
sandy → []
late → []
gondola → []
car → gun, door, boot, gas, window, hood
trunk → locker

more general → more specific

* subtype-of
* subset-of
* instance-of
* example-of
* specific-type-of
* models-for
* model-of
* examples-of
* subtypes
* hyponyms
* chidren

### rel-com

> "Comprises" (direct holonyms, per WordNet)
> container
> whole → part

cow → bag, poll, udder
car → accelerator
awake → []
provoke → []
beach → []
slack → []
dessert → []
sandy → []
late → []
gondola → []
car → lift, funicular, airship, elevator
trunk → back, side, chest, belly, bark
face → eye


* member-of
* has
* belongs-to
* part-of
* components-of
* includes
* contains
* holonyms
* parts
* component

### rel-par

> "Part of" (direct meronyms, per WordNet)
> member
> meronym
> part -> whole

trunk → tree
awake → []
provoke → []
beach → shore
cow → []
slack → []
dessert → []
sandy → []
late → []
gondola → dirigible
car → door, accident
trunk → tree, car, body, machine, automobile
engine →  car

part →  whole

* composed-of
* comprised-of
* made-up-of
* made-of
* assembled-from
* composite-of
* whole-of
* entirety-of
* encompassed
* container-for
* assembly-of
* sum-of-parts
* body-of
* aggregate-of
* summation-of
* ensemble-of
* whole-of
* parent-of
* meronym

### rel-bga

> Frequent followers (w′ such that P(w′ w) ≥ 0.001, per Google Books Ngrams)
>
>
>

wreak → havoc
awake → and, for, when, until, again
provoke → a, the, an, him, them, me
beach → and, in, is, with, where, hotel, resort, boys
cow → and, is, that, dung, manure, disease, milk
slack → in, and, water, season, variables, off, times
dessert → and, was, is, wines, plates, dishes, menu
sandy → soil, loam, beach, hair, plain, river
late → in, ninteenth, for, years, summar
gondola → cars, ride
car → park, accident
trunk → roats, railway, lines

* comes-after
* follows
* are-after
* that-follow

### rel-bgb

> Frequent predecessors (w′ such that P(w w′) ≥ 0.001, per Google Books Ngrams)

havoc → wreak
awake → wide, lay, stay, fully, lying, kept
provoke → would, may, might, will
beach → long, palm, sandy, north
cow → per, dairy, mad, sacred
slack → some, during, went, little
dessert → favorite, after, frozen
sandy → big, fine, light, very
late → until, very
gondola → venetian, black, passenger, another
car → new, motor, police, sports, used, own
trunk → tree, grand, nerve, pulmonary, great

* comes-before
* preceeds
* are-before
* that-precede

### rel-hom

> Homophones (sound-alike words)
> phonetic variants
> same-sound

course → coarse
awake → []
provoke → []
beach → beech
cow → cao, kau, cau, kao
slack → []
dessert → desert
sandy → sandi, sandie, san d, sand he
late → leight
gondola → []
car → carr, carre
trunk → []

* sound-matches
* same-sound-as
* same-sound
* sounds-twin-to
* sounds-exactly-like
* sounds-the-same-as
* sounds-the-same
* sounds-same-as
* sounds-identical-to
* sounds-identical
* audibly-same
* homophones

### rel-cns

> Consonant match
>
> I l
>

sample → simple
awake → awoke, awork, a work, ai work, eye work, high work
provoke → []
beach → batch, birch, beech, botch, bouche
cow → key, coy, coo, qi, chi, caw
slack → sleek, slick, slake, slock
dessert → desert does it, dies at, dies out, does hurt
sandy → sunday, cindy, sunder, sander
late → lot, let, lit, loot
gondola → []
car → care, core, coar, khor
trunk → trank, trink

* matches-consonants-of
* cns

Notes About Words
-----------------

* [Wikipedia > Homonym](https://en.wikipedia.org/wiki/Homonym) -- This page has a list of linguistic concepts about word relationships.

Commands
--------

The ideal commands might be:

| Command/Aliases       | Source   |             | Meaning                                     |
|-----------------------|----------|-------------|---------------------------------------------|
| `define`, `dict`, `d` | Dict.org |             | define a word                               |
| `syn`, `thes`         | datamuse | `--rel-syn` | look for similar words                      |
| `ant`                 | datamuse | `--rel-ant` | antonyms                                    |
| `rand`, `random`      | local    |             | provide one or more random words or phrases |
