# Kings

### Objective: 

Given that the pandemic is still going on - it gave me the idea of trying to build drinking games that me and my friends can use to still enjoy happy hour - while still being socially distant. 

Also - I can't find my deck of cards and this seemed more feasable than going shopping

>If you are a recruiter reading this - please don't focus too much on this particular repo.

### Rules: 

The objective of the game is to drink - every player will take turns drawing a card from the digital deck. The terminal will show you what card you drew, along with the particular rule that that card has. Rules change by card value, but ignore suites. 

At any point in the game, there is a probability that a player *cracks* the seal of a beer can when they draw a card. At this point - that player has to finish their drink and then read the rule for that card that they drew.

### Fun Technical bits:

The game is build with a heavy emphasis on randomness so as to replicate the feeling of playing with an actual *shuffled* deck. In order to accomplish this - I introduced random functions into three different points of the game. When ever the deck is first build, it is also shuffled with `pandas.sample`. I then use `random` to select a random number which will be used to select a card in the deck using the `index`. Once the card is *removed*, the deck is then suffled again using `pandas.sample`. This happens after every player draws a card. Lastly, in order to randomize the seal - I used `numpy.randint` to generate a over 100 numbers within different ranges
The game is build with a heavy emphasis on randomness so as to replicate the feeling of playing with an actual *shuffled* deck. In order to accomplish this - I introduced random functions into three different points of the game. When ever the deck is first build, it is also shuffled with `pandas.sample`. I then use `random` to select a random number which will be used to select a card in the deck using the `index`. Once the card is *removed*, the deck is then suffled again using `pandas.sample`. This happens after every player draws a card. Lastly, in order to randomize the seal - I used `numpy.randint` to generate a over 100 numbers within ranges 0 and 52 (to represent the deck of cards). The random number is selected after the deck is first created, and then when ever the deck count matches that number, the crack is sealed. 

#### I hope you enjoy the game - please drink responsably and don't drink and drive! 