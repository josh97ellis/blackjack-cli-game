import random

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
    
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    
    def __str__(self):
        deck_str = ""
        for card in self.cards:
            deck_str += str(card) + "\n"
        return deck_str


class Shoe:
    def __init__(self, num_decks=6):
        self.num_decks = num_decks
        self.decks = []
        
        for _ in range(num_decks):
            deck = Deck()
            deck.shuffle()
            self.decks.append(deck)
    
    def shuffle(self):
        for deck in self.decks:
            deck.shuffle()
    
    def deal_card(self):
        if len(self.decks) > 0:
            return self.decks[-1].deal_card()
        else:
            return None
    
    def __str__(self):
        shoe_str = ""
        for deck in self.decks:
            shoe_str += str(deck)
        return shoe_str


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
            print(f'Cards: {["?", self.cards[1].__str__()]}')


class Chips:
    def __init__(self):
        self.total = 0
        self.bet = 0
    
    def purchase_chips(self, value: int):
        self.total += value
    
    def make_bet(self, value: int):
        self.bet += value
    
    def win_bet(self, value: int):
        self.total += value
    
    def lose_bet(self, value: int):
        self.total -= value
