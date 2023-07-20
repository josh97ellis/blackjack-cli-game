"""
Functions for handling different ending scenarios of a
game of Blackjack
"""
from player import Chips
import os
from playsound import playsound
from config import Configuration

# Table rules for blackjack payout value
game_config = Configuration(f'{os.getcwd()}\game_config.yaml')


def player_busts(chips: Chips) -> None:
    print("Player busts!")
    chips.lose_bet(chips.bet)


def player_wins(chips: Chips, blackjack=False):
    if blackjack:
        print("Blackjack!")
        chips.win_bet(chips.bet * (float(eval(game_config.get_value('blackjack_payout')))))
    else:
        print("Player wins!")
        chips.win_bet(chips.bet)
    
    playsound('casino_sounds/mixkit-coin-win-notification-1992.wav')


def dealer_busts(chips: Chips):
    print("Dealer busts!")
    chips.win_bet(chips.bet)
    playsound('casino_sounds/mixkit-coin-win-notification-1992.wav')


def dealer_wins(chips: Chips):
    print("Dealer wins!")
    chips.lose_bet(chips.bet)


def push():
    print("Dealer and Player tie! It's a push.")
