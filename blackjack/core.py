#!/usr/bin/env python3

import itertools
import random
from enum import Enum

class Suit(Enum):
    hearts   = 1
    clubs    = 2
    spades   = 3
    diamonds = 4

class Rank(Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    

class Card:

    def __init__(self, rank, suit):
        self.set_rank(rank)
        self.set_suit(suit)

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_suit(self, suit):
        self.suit = Suit(suit)

    def set_rank(self, rank):
        self.rank = Rank(rank)

class Deck:

    def __init__(self, shuffled=True):
        self.set_cards()
        if shuffled:
            self.shuffle()

    def set_cards(self):
        cards = []
        for rank, suit in itertools.product(Rank, Suit):
            cards.append(Card(rank, suit))
        self.cards = cards

    def get_cards(self):
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
    
