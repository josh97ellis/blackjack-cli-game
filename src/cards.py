"""
Objects relating to a playing card: a card, a deck, and a shoe
"""
import random
from playsound import playsound
from config import Configuration

_config = Configuration('game_config.yaml')

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
        if rank in ['Jack', 'Queen', 'King']:
            self.value = 10
        elif rank == 'Ace':
            self.value = 11
        else:
            self.value = int(rank)
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        # Add a card to the deck for each suit and rank
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
    
    def __repr__(self):
        return '\n'.join(str(card) for card in self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self, sound=True, show=True, side='front'):
        if side not in ['front', 'back']:
            raise ValueError(f'{side} is not a valid value for side')
        
        # Checks to ensure that cards still exist in the deck
        if len(self.cards) == 0:
            return None
        
        # Remove top card
        card = self.cards.pop(0)
        
        # Determine what side of the card should be shown
        if show and side=='front':
            print(f'{card.__str__()} \n')
        elif show and side=='back':
            print(f'????? \n')
        
        # Determine if a sound effect should be played when delt
        if sound:
            playsound(_config.get_value('sounds')[0]['place_card'])
        
        return card


class Shoe(Deck):
    def __init__(self, num_decks=6):
        super().__init__()
        if num_decks < 1:
            raise ValueError("Number of decks must be at least 1.")
        self.num_decks = num_decks
        self.cards *= num_decks
    
    def __repr__(self):
        return super().__repr__()
