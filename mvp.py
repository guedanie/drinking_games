import pandas as pd
import numpy as np
from random import randint
from random import choice

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
    deck = deck.reset_index(drop=True)
    return deck

def draw_card(deck):
    random_number = choice(deck.index)
    card = deck.iloc[random_number]
    updated_deck = deck.drop(index=random_number)
    return card, updated_deck

def present_card(card):
    print(f"The card is: {card.values[0]}")

deck = build_deck(rules)
playing = True
while playing:
    draw = input("Do you want to draw a card? (Y / N) ")
    if draw == "Y": 
        print("--------------------")
        card, deck = draw_card(deck)
        present_card(card)
        print("Rule:")
        print("")
        print(rules[card.values[1]])
        print("--------------------")
    else:
        playing= False

print("Thank you for playing")