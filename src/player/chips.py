class Chips:
    def __init__(self):
        self.total = int(input('Purchase Chips Amount: '))
        self.bet = 0
    
    def make_bet(self, value: int):
        self.bet += value
    
    def win_bet(self, value: int):
        self.total += value
    
    def lose_bet(self, value: int):
        self.total -= value
