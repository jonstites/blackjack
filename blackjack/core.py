#!/usr/bin/env python3

import itertools
import random
import time
from enum import Enum

from . import helpers

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
        self.blind = False

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_suit(self, suit):
        self.suit = Suit(suit)

    def set_rank(self, rank):
        self.rank = Rank(rank)

    def set_blind(self):
        self.blind = True

    def unset_blind(self):
        self.blind = False

    def __str__(self):
        if not self.blind:
            return "".join([helpers.rank_to_str(self.rank.name), 
                            helpers.suit_to_str(self.suit.name)])
        return "XX"

    def __repr__(self):
        if not self.blind:
            return "".join([helpers.rank_to_str(self.rank.name), 
                            helpers.suit_to_str(self.suit.name)])
        return "XX"

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

    def get_top_card(self):
        return self.cards.pop()

class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card, blind=False):
        if blind:
            card.set_blind()
        self.cards.append(card)

    def add_cards(self, cards, blind=False):
        for card in cards:
            self.add_card(card, blind)

    def score_cards(self):
        score    = 0
        num_aces = 0
        for card in self.cards:
            score += helpers.rank_to_score(card.rank.name)
            if card.rank == Rank.ace:
                num_aces += 1

        for i in range(num_aces):
            if score + 10 <= 21:
                score += 10
        return score

    def get_score(self):
        return self.score_cards()

    def __str__(self):
        return " ".join(str(card) for card in self.cards)

    def __repr__(self):
        return " ".join(str(card) for card in self.cards)


class Player:

    def __init__(self):
        self.hand = Hand()
        self.done = False

    def add_card_from_deck(self, deck, blind=False):
        self.hand.add_card(deck.get_top_card(), blind=blind)

    def __str__(self):
        return str(self.hand)

    def __repr__(self):
        return str(self.hand)

    def is_done(self):
        return self.done

    def set_done(self):
        self.done = True

    def dealer_hit(self):
        if self.get_score() < 17:
            print("dealer hits.")
            return True
        print("dealer stays.")

    def busted(self):
        if self.get_score() > 21:
            return True

    def get_score(self):
        return self.hand.get_score()

    def reveal(self):
        for card in self.hand.cards:
            card.unset_blind()

class Game:
    
    def __init__(self):
        self.set_welcome()
        self.dealer = Player()
        self.player = Player()
        self.deck   = Deck()

    def set_welcome(self):
        welcome = """Welcome to Jon's Blackjack!"""
        self.welcome = welcome

    def deal_cards(self, player, number=1, blind=False):
        for i in range(number):
            player.add_card_from_deck(self.deck, blind=blind)

    def deal_card(self, player, blind=False):
        player.add_card_from_deck(self.deck, blind=blind)

    def start_game(self):
        # welcome message
        self.print_welcome()

        # make deck
        # shuffle deck
        # start empty hands 
        self.reset()

        # pass cards dealer
        self.deal_cards(self.dealer, number=1, blind=True)
        self.deal_cards(self.dealer, number=1)

        # pass cards player
        self.deal_cards(self.player, number=2)

        self.show_game()

        while not self.player.is_done():
            hit = self.prompt()
            if hit:
                self.deal_card(self.player)
                self.show_game()
                if self.player.busted():
                    self.player.set_done()
            else:
                self.player.set_done()

        if self.player.busted():
            print("you busted.")
            return 

        if not self.player.busted():
            self.dealer.reveal()
            self.show_game()

            while not self.dealer.is_done():
                if self.dealer.dealer_hit():
                    self.deal_card(self.dealer)
                    self.show_game()
                    if self.dealer.busted():
                        self.dealer.set_done()
                else:
                    self.dealer.set_done()
        
        if self.dealer.busted():
            print("dealer busted. you win!")
  
        elif self.player.get_score() > self.dealer.get_score():
            print("score higher. you win!")
        
        elif self.player.get_score() == self.dealer.get_score():
            print("you tie.")

        elif self.player.get_score() < self.dealer.get_score():
            print("you lost.")
        # bet fake money?
        # record high score?
        pass

    def print_welcome(self):
        print(self.welcome)

    def reset(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()

    def show_game(self):
        print("Dealer: ", self.dealer)
        print("Player: ", self.player)
        print()
        time.sleep(1)

    def prompt(self):
        player_score = self.player.get_score()
        question = "Your score is {}. Do you hit (h) or stay (s)?   "
        formatted = question.format(player_score)
        hit = input(formatted)
        if hit == "h":
            return True
        elif hit == "s":
            return False
        else:
            return self.prompt()
