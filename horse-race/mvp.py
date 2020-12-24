import pandas as pd
import numpy as np
from numpy.random import randint
from random import choices
from random import choice
from time import sleep
import time, sys
from IPython.display import clear_output
import os


heart = ["♥️", '0', '0', '0', '0', '0', '0', '0', '0']
diamond = ["♦️", '0', '0', '0', '0', '0', '0', '0', '0']
spade = ["♠️", '0', '0', '0', '0', '0', '0', '0', '0']
club = ["♣️", '0', '0', '0', '0', '0', '0', '0', '0']


def build_deck():
    numbers = list(range(2,11))
    letters = ["J", "Q", "K", "A"]
    suites = ["♥️", "♦️", "♠️", "♣️"]
    one_set = numbers + letters
    deck = pd.DataFrame()
    for suit in suites:
        new_set = []
        for i in one_set:
            new_set.append(str(i) + suit)
        test = pd.DataFrame({"value": new_set, "suit": suit})
        deck = pd.concat([deck, test])
    deck = deck.reset_index(drop=True).sample(frac=1)
    return deck


def remove_aces(deck):
    deck = deck[~deck.value.str.contains("A")]
    return deck

def select_8_cards(deck):
    card_index = choices(deck.index, k=8)
    cards = deck[deck.index.isin(card_index)].sample(frac=1) 
    updated_deck = deck.drop(index=card_index).sample(frac=1) # and the deck is shuffle every time it is updated but shuffing the index. This reduces the chances of similar cards coming back to back
    return cards, updated_deck

def draw_card(deck):
    # In order to increase randomness - I have added two "shuffles". We randomly select a number from the index using the random library
    random_number = choice(deck.index)
    card = deck.loc[random_number]
    updated_deck = deck.drop(index=random_number).sample(frac=1) # and the deck is shuffle every time it is updated but shuffing the index. This reduces the chances of similar cards coming back to back
    return card, updated_deck

def create_board(heart, diamond, spade, club):
    board = (
        pd.DataFrame(
            {"Heart": heart,
            "Diamond": diamond,
            "Spade": spade,
            "Clubs": club}
            )
    ).T

    return board

def update_board(heart, diamond, spade, club):
    os.system('clear')
    deck = build_deck()
    deck = remove_aces(deck)
    cards, deck = select_8_cards(deck)

    card, deck = draw_card(deck)
    print(f"The card is: {card.values[0]}")
    
    if card.suit == '♥️':
        h_index = heart.index('♥️')
        heart.insert(h_index + 1, heart.pop(h_index))
        h_index += 1
        board = create_board(heart, diamond, spade, club)
        
        return board
    if card.suit == "♦️":
        d_index = diamond.index("♦️")
        diamond.insert(d_index + 1, diamond.pop(d_index))
        d_index += 1
        board = create_board(heart, diamond, spade, club)
        return board
        
    if card.suit == "♠️":
        s_index = spade.index("♠️")
        spade.insert(s_index + 1, spade.pop(s_index))
        s_index += 1
        board = create_board(heart, diamond, spade, club)
        return board
        
    if card.suit == "♣️":
        c_index = club.index("♣️")
        club.insert(c_index + 1, club.pop(c_index))
        c_index += 1
        board = create_board(heart, diamond, spade, club)
        return board
    
    

   

playing= True
board = create_board(heart, diamond, spade, club)
print(board)

while playing:
    answer = input("Ready to draw a card? (Y/N): ")
    if answer == "Y":
        board = update_board(heart, diamond, spade, club)
        print(board)
        
    else:
        print("Thank you for playing")
        playing=False
    


        
