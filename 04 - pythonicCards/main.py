# File        :   pythonicCards.py
# Version     :   1.0.1
# Description :   Checking out a pythonic card deck
#
# Date:       :   Jan 14, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0


import collections
import random

# namedtuple creates a basic class that it is just a "bundle" of
# attributes (rank and suit)
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    # Creates the "ranks" list with numbers 2 - 10 and the letters J, Q, K and A:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # Creates a list of suits strings: spades, diamonds, clubs, hears
    suits = "spades diamonds clubs hears".split()

    def __init__(self):
        # Create combinations with each string in the rank list and
        # each string in the suits list -> i.e., ("2", "spades"),
        # ("2", "diamonds"), ("2", "clubs"), etc...
        # Should be 52 tuples
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        print(self._cards)

    def __len__(self):
        # Get total of cards created (should be 52)
        return len(self._cards)

    def __getitem__(self, item):
        # Returns a specific card from the deck
        return self._cards[item]


# Test the card class:
beer_card = Card("7", "diamonds")
print(beer_card)

# Create a deck object:
deck = FrenchDeck()
print(deck)

# How many cards are in the deck?
print(len(deck))

# What's the first card?
print(deck[0])

# What's the last card?
print(deck[-1])

# Leverage the fact that random accepts a sequence and use it to
# choose a random card!
random.seed(69)
randomCard = random.choice(deck)
print(randomCard)

# __getitem__ makes the sequence slice-able:
# Get a "hand" of 5 cards:
hand = deck[0:4]
print(hand)

# Get a random card object:
oneCard = hand[random.randint(0, len(hand))]
# Print attributes:
print(oneCard.rank, oneCard.suit)

# __getitem__ makes the sequence iterable,
# iterate through the 5 cards and print em:
for i, currentCard in enumerate(hand):
    print("card:" + str(i), "->", currentCard)
