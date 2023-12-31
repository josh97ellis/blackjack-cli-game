"""
Obejcts relating to physical things that a player requires
to play a game of blackjack, such as a a hand of cards and chips
"""
from cards import Card
from playsound import playsound


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.is_bust = False
    
    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1
        
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
    def display_cards(self, show_all=True):
        if show_all:
            print(f'Cards: {[card.__str__() for card in self.cards]} -> Value: {self.value}')
        else:
            print(f'Cards: {[self.cards[1].__str__(), "?"]}')


class Chips:
    def __init__(self):
        self.total = 0
        self.bet = 0
    
    def purchase_chips(self):
        amt = input('How many chips would you like to purhcase?: $')
        self.total += int(amt)
        playsound('src/static/mixkit-coins-sound-2003.wav')
    
    def make_bet(self):
        amt = input('How much would you like to bet?: $')
        self.bet += int(amt)
        playsound('src/static/mixkit-coins-sound-2003.wav')
    
    def win_bet(self, value: int):
        self.total += value
    
    def lose_bet(self, value: int):
        self.total -= value
