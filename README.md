# fact-join

##General

Script that takes two Wikipedia pages from user input or at random, and then merges them to create new facts.

Atlantis + San Francisco

`Despite its minor importance in Plato's work, the Atlantis story is the most densely settled large city (population greater than 200,000) in the state of California and the second-most densely populated major city in the United States after New York City.`

Peacock spiders + the sun

`In at least one species, Maratus vespertilio, the expansion of the flaps also is about 109 times that of Earth, and it has a mass about 330,000 times that of Earth, accounting for about 99.86 % of the total mass of the Solar System. `

Computer programming + witchcraft

`In general, good programming derives from Old Testament laws against witchcraft, and entered the mainstream when belief in witchcraft gained Church approval in the Early Modern Period.`

##Changes

Updated from original project to deploy as a flask server.

Also upgraded to python3


##Usage

To install deps, create env and run:

```
pip install -r requirements.txt

```

To run:

```
./manage.py runserver

```

To Use:

```
http://localhost:5000/word1/word2

```

Where if word2 or word1 are ommited they are replaced with random articles.

###Notes:

Simple cacheing is implemented at a default of 1 hour, this can be changed in the config


