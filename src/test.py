import cards
import random_qiskit

my_deck = cards.Deck(num_of_decks=2, security_bit_count=8)
my_deck.generate_deck()
my_deck.shuffle_deck()
my_deck.show_deck()

my_deck.show_commitment()
# import hashlib, secrets, time

# number = 123456789
# timestamp = int(time.time())  # current Unix time
# # nonce = secrets.token_hex(8)
# commitment = hashlib.sha3_512(f"{number}:{timestamp}".encode()).hexdigest()
# print("Commitment:", commitment)
# print("Timestamp:", timestamp)
# # print("Nonce:", nonce)