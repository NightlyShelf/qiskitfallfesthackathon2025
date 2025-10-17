import cards

my_deck = cards.Deck(num_of_decks=2, security_bit_count=8)
my_deck.generate_deck()
my_deck.shuffle_deck()
my_deck.show_deck()


print("my cards is")
print(my_deck.next_card())
print(my_deck.next_card())
print(my_deck.next_card())
print(my_deck.next_card())
print(my_deck.next_card())
