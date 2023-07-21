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
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        # Add a card to the deck for each suit and rank
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def __str__(self):
        deck_str = ""
        for card in self.cards:
            deck_str += str(card) + "\n"
        return deck_str
    
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


class Shoe:
    def __init__(self, num_decks=6):
        self.num_decks = num_decks
        self.decks = []
        
        for _ in range(num_decks):
            deck = Deck()
            deck.shuffle()
            self.decks.append(deck)
    
    def __str__(self):
        shoe_str = ""
        for deck in self.decks:
            shoe_str += str(deck)
        return shoe_str
    
    def shuffle(self):
        for deck in self.decks:
            deck.shuffle()
    
    def deal_card(self, sound=True, show=True, side='front'):
        if side not in ['front', 'back']:
            raise ValueError(f'{side} is not a valid value for side')
        
        if len(self.decks) > 0:
            card = self.decks[-1].deal_card()
            if show:
                if side == 'front':
                    print(f'{card.__str__()} \n')
                else:
                    print(f'????? \n')
            
            if sound:
                playsound(_config.get_value('sounds')[0]['place_card'])
            
            return card
        else:
            return None
