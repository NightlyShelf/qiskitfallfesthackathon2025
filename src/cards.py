import numpy as np
import random_qiskit
import time
import hashlib

colors = ["spades", "hearts", "clubs", "diamonds"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]


class Card:
    def __init__(self, number = None, color = None):
        self.number = number
        self.color = color


class Deck:

    current_card = 0

    def __init__(self, num_of_decks, security_bit_count):
        self.num_of_decks = num_of_decks
        self.security_bit_count = security_bit_count
        self.deck = None

    def generate_deck(self):
        self.deck = np.empty(shape=((len(colors) * len(numbers)) * self.num_of_decks), dtype=Card)

        for i in range(self.num_of_decks):
            for j, color in enumerate(colors):
                for k, number in enumerate(numbers):                    
                    self.deck[i * (len(colors) * len(numbers)) + j * len(numbers) + k] = Card(number, color)

    def shuffle_deck(self):
        self.qseed = int(random_qiskit.quantum_generate_random(bit_count=self.security_bit_count), 2)
        np.random.seed(self.qseed)
        np.random.shuffle(self.deck)

    def show_deck(self):
        for i, card in enumerate(self.deck):
            print(f"{i}: {card.color} {card.number}")

    def next_card(self):
        self.current_card += 1
        if self.current_card >= (len(colors) * len(numbers)) * self.num_of_decks:
            return None

        return self.deck[self.current_card - 1]
    
    def show_commitment(self):
        timestamp = time.time_ns()
        commitment = hashlib.sha3_512(f"{self.qseed}:{timestamp}".encode()).hexdigest()
        print(self.qseed)
        print(commitment)
        return commitment