from cards2 import Chips


def player_busts(chips: Chips) -> None:
    print("Player busts!")
    chips.lose_bet(chips.bet)


def player_wins(chips: Chips, blackjack=False):
    if blackjack:
        print("Blackjack!")
        chips.win_bet(chips.bet * (3/2))
    else:
        print("Player wins!")
        chips.win_bet(chips.bet)


def dealer_busts(chips: Chips):
    print("Dealer busts!")
    chips.win_bet(chips.bet)


def dealer_wins(chips: Chips):
    print("Dealer wins!")
    chips.lose_bet(chips.bet)


def push():
    print("Dealer and Player tie! It's a push.")
