import random
from random import shuffle

class Cards:
    def __init__(self):
        tabColors = ["Trèfle", "Pique", "Coeur", "Carreau"];
        tabValues = ["As", "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi"];
        self.deck = [value + " de " + color for value in tabValues for color in tabColors];
        shuffle(self.deck)
    def draw( self):
        res = self.deck[0]
        self.deck.pop(0)
        return res

    def counter(self):
        self.count = len(self.deck)
        return self.count