#!/usr/bin/env python3


import blackjack.core



def play_game():
    game = blackjack.core.Game()
    game.start_game()

if __name__ == "__main__":
    play_game()
