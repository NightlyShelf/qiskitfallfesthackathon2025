import cards
import random_qiskit

my_deck = cards.Deck(2)
my_deck.generate_deck()
my_deck.shuffle_deck()
my_deck.show_deck()