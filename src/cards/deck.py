import random
from card import Card


class Deck:
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    
    def __init__(self):
        # Add a card to the deck for each suit and rank
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __str__(self):
        deck_str = ""
        for card in self.cards:
            deck_str += str(card) + "\n"
        return deck_str

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
