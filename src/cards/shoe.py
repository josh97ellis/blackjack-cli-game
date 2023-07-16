from deck import Deck

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
