import numpy as np


colors = ["spades", "hearts", "clubs", "diamonds"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]


class Card:
    def __init__(self, number = None, color = None):
        self.number = number
        self.color = color


class Deck:
    def __init__(self, num_of_decks):
        self.num_of_decks = num_of_decks

    def generate_deck(self):
        self.deck = np.empty(shape=(52 * self.num_of_decks), dtype=Card)
        pass

    def shuffle_deck(self):
        pass