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

    def __str__(self):
        return f"{self.color} {self.number}"


class Deck:
    def __init__(self, num_of_decks, security_bit_count):
        '''
        Args
            - num_of_decks: number of 52 card deckcs in whole deck
            - security_bit_count: number of bits in quantum random number generator for shuffle seed
        Returns
            Deck object
        '''
        self.num_of_decks = num_of_decks
        self.security_bit_count = security_bit_count
        self.deck = None
        self.current_card = 0

    def generate_deck(self):
        '''
        generating table of cards, null for now
        '''
        self.deck = np.empty(shape=((len(colors) * len(numbers)) * self.num_of_decks), dtype=Card)

        for i in range(self.num_of_decks):
            for j, color in enumerate(colors):
                for k, number in enumerate(numbers):                    
                    self.deck[i * (len(colors) * len(numbers)) + j * len(numbers) + k] = Card(number, color)

    def shuffle_deck(self):
        '''
        shuffling deck with seed from quantum random number generator
        '''
        self.current_card = 0

        self.qseed = int(random_qiskit.quantum_generate_random_device_independent(bit_count=self.security_bit_count), 2)
        np.random.seed(self.qseed)
        np.random.shuffle(self.deck)

    def show_deck(self):
        '''
        prints whole deck to the console "{position in deck}: {color} {number}"
        '''
        for i, card in enumerate(self.deck):
            print(f"{i}: {card.color} {card.number}")

    def next_card(self):
        '''
        Returns
            Card object of a next card in deck
        '''
        self.current_card += 1
        if self.current_card >= (len(colors) * len(numbers)) * self.num_of_decks:
            return None

        return self.deck[self.current_card - 1]
    
    def show_commitment(self):
        '''
        calculates hash to proooove that data wasnt tempered
        Returns:
            - hash string
            - timestamp of generation
        '''
        self.timestamp = time.time_ns()
        commitment = hashlib.sha3_512(f"{self.qseed}:{self.timestamp}".encode()).hexdigest()
        return commitment, self.timestamp