import numpy as np
from .card import Card

class Deck:
    def __init__(self):
        self.ranks = [str(rank) for rank in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()
    
    
    def shuffle(self):
        np.random.shuffle(self.cards)
    
    def deal_card(self):
        extracted_card = self.cards.pop()
        if len(self.cards) < 15:
            self.reshuffle() # Reshuffle when remaining cards are less than 15
        return extracted_card
    
    def reshuffle(self):
        self.__init__()
