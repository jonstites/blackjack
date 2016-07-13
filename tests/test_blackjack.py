#!/usr/bin/env python3

import pytest
import blackjack.core


class TestCard:

    def test_suit_hearts(self):
        card = blackjack.core.Card(1, 1)
        card.get_suit() == "hearts"

    def test_suit_diamonds(self):
        card = blackjack.core.Card(1, 1)
        card.get_suit() == "diamonds"

    def test_suit_fail(self):
        with pytest.raises(ValueError):
            blackjack.core.Card(1, 5)
        
    def test_rank_ace(self):
        card = blackjack.core.Card(1, 1)
        card.get_rank() == "ace"

    def test_rank_king(self):
        card = blackjack.core.Card(13, 1)
        card.get_rank() == "king"

    def test_rank_fail(self):
        with pytest.raises(ValueError):
            blackjack.core.Card(14, 1)

    def test_print(self):
        card = blackjack.core.Card(13, 1)
        str(card) == "K" + u"\u2665"
        
class TestDeck:

    def test_create_deck(self):
        deck = blackjack.core.Deck()
        len(deck.cards) == 52

    def test_first_card(self):
        deck = blackjack.core.Deck(shuffled=False)
        deck.cards[0] == blackjack.core.Card(1, 1)

    def test_last_card(self):
        deck = blackjack.core.Deck(shuffled=False)
        deck.cards[-1] == blackjack.core.Card(13, 4)

    def test_shuffle(self):
        deck  = blackjack.core.Deck(shuffled=False)
        deck2 = blackjack.core.Deck()
        deck != deck2

    def test_print_deck(self):
        deck = blackjack.core.Deck()
        for card in deck.cards:
            str(card)
        
    def test_pop_card(self):
        deck = blackjack.core.Deck(shuffled=False)
        card = deck.get_top_card()
        card == blackjack.core.Card(13, 4)
        len(deck.cards) == 51

class TestHand:

    def test_create_hand(self):
        hand = blackjack.core.Hand()
        len(hand.cards) == 0

    def test_add_card(self):
        card = blackjack.core.Card(1, 1)
        hand = blackjack.core.Hand()
        hand.add_card(card)
        len(hand.cards) == 1

    def test_score_card(self):
        card = blackjack.core.Card(5, 1)
        hand = blackjack.core.Hand()
        hand.add_card(card)
        hand.score_cards() == 5

    def test_score_cards(self):
        card1 = blackjack.core.Card(5, 1)
        card2 = blackjack.core.Card(6, 1)
        hand  = blackjack.core.Hand()
        hand.add_cards([card1, card2])
        hand.score_cards() == 11

    def test_score_aces_low(self):
        card1 = blackjack.core.Card(9, 1)
        card2 = blackjack.core.Card(11, 1)
        card3 = blackjack.core.Card(1, 1)
        hand  = blackjack.core.Hand()
        hand.add_cards([card1, card2, card3])
        hand.score_cards() == 20

    def test_score_aces_high(self):
        card1 = blackjack.core.Card(9, 1)
        card2 = blackjack.core.Card(1, 1)
        card3 = blackjack.core.Card(1, 1)
        hand  = blackjack.core.Hand()
        hand.add_cards([card1, card2, card3])
        hand.score_cards() == 21

    def test_print_hand(self):
        card1 = blackjack.core.Card(9, 1)
        card2 = blackjack.core.Card(1, 2)
        card3 = blackjack.core.Card(3, 3)
        card4 = blackjack.core.Card(13, 4)
        hand  = blackjack.core.Hand()
        hand.add_cards([card1, card2, card3, card4])
        correct_str = " ".join([
            "9" + u"\u2665",
            "A" + u"\u2666",
            "3" + u"\u2660",
            "K" + u"\u2663"
            ])
        str(hand) == correct_str

