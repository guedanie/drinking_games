import pandas as pd
import numpy as np
from numpy.random import randint
from random import choice
from time import sleep

# objective: To be able to play kings the drinking game
# in order to accomplish this - I will first build a terminal version as an MVP

# Steps:

# Build a random deck of cards
# 1. Allow users to pull a card at random from the deck -
    # have to be able to keep track of all the cards that are still in the deck and which ones are out
# 2. Once a card is pull - there should be a quick summary of what the card does
# 3. Have a random number, which will symbolize the can being cracked after the cards pile up 

# creating the deck - 52 cards, 4 suits

# Game Rules

rules = {"2": "You - Whoever drew the card assigns a drink",
    "3": "Me - Whoever drew the card drinks",
    "4": "Floor - Everyone races to touch the floor, last person to do so drinks",
    "5": "Guys - All guys drink", 
    "6": "Chicks - All girls drink",
    "7": "Heaven - All players point towards the sky, last player to do so drinks",
    "8": "Mate - Pick a person to drink with",
    "9": "Rhyme - Say a phrase, and everyone else must say phrases that rhyme",
    "10": 'Categories - Pick a category, and say something from that category (i.e. if "drinking games" was the category, "kings" would be a viable answer.',
    "Jack": 'Never have I ever - Each player puts up 3 fingers, then starting with the person who drew the card, each player says "never have I ever «something»". If you\'ve done it, you put a finger down, until someone loses',
    "Queen": "Questions - The person who drew the card asks a random person a question, and they then turn and ask a random person a question, until someone loses by either failing to ask a question or by responding to the person who just asked them a question",
    "King":" Ruler - Make a rule that everyone must follow until the next King is drawn (i.e. force everyone to drink after each turn)",
    "Ace": "Waterfall - Every player begins drinking, and no one can stop until the player before them does"
}

def build_deck(rules):
    numbers = list(range(2,11))
    letters = ["J", "Q", "K", "A"]
    suites = ["♥️", "♦️", "♠️", "♣️"]
    one_set = numbers + letters
    rule_value = list(rules.keys())
    deck = pd.DataFrame()
    for suit in suites:
        new_set = []
        for i in one_set:
            new_set.append(str(i) + suit)
        test = pd.DataFrame({"value": new_set, "key": rule_value})
        deck = pd.concat([deck, test])
    deck = deck.reset_index(drop=True).sample(frac=1)
    return deck

def draw_card(deck):
    # In order to increase randomness - I have added two "shuffles". We randomly select a number from the index using the random library
    random_number = choice(deck.index)
    card = deck.loc[random_number]
    updated_deck = deck.drop(index=random_number).sample(frac=1) # and the deck is shuffle every time it is updated but shuffing the index. This reduces the chances of similar cards coming back to back
    return card, updated_deck

def present_card(card):
    print(f"The card is: {card.values[0]}")

# ------------------------- #
#      Main Game Loop       #
# ------------------------- #

deck = build_deck(rules)
values = randint(3, 31, 100)
beer_crack = choice(values)
print("")
print("~~~~ Welcome to Kings ~~~~~")
print("")
print("Be prepare to questions your friendships for coming up with the stupidest rules and not being able to form a single rhyme")
print("")
print("At any point in the game, after drawing a card, a player might crack the seal. At that point, that player that drew the card has to finish their drink")
print("")
playing = True
while playing:
    draw = input("Do you want to draw a card? (Y / N) ")
    if draw == "y" or draw == "Y": 
        print("")
        print("--------------------")
        card, deck = draw_card(deck)
        if deck.shape[0] ==  beer_crack:
            print("")
            print("STOP")
            print("")
            print("*******************")
            print("")
            print("Someone has cracked the beer can!! Who's ever turn it was has to finish their drink now!")
            print("")
            print("*******************")
            print("")
            sleep(10)
        print(f"There are {deck.shape[0]} cards left in the deck")
        present_card(card)
        print("Rule:")
        print("")
        print(rules[card.values[1]])
        print("--------------------")
        print("")
        if deck.shape[0] == 1:
            print("")
            print("~~~~ One more card left! ~~~~")
            print("")
        elif deck.shape[0] == 0:
            print("************************************")
            print("That's all the cards! EVERYBODY DRINK!!!")
            print("************************************")
            playing=False
    else:
        playing= False
        print("")
        print("Thank you for playing")
        print("")
        print("Please don't drink and drive!")
        print("")
