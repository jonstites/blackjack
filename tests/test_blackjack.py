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


class TestDeck:


    def test_create_deck(self):
        deck = blackjack.core.Deck()
        len(deck.cards) == 52

    def test_first_card(self):
        deck = blackjack.core.Deck()
        deck.cards[0] == blackjack.core.Card(1, 1)

    def test_first_card(self):
        deck = blackjack.core.Deck()
        deck.cards[-1] == blackjack.core.Card(13, 4)
        
