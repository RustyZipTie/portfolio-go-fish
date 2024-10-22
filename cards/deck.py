from cards.card import Card
from random import randint
from cards.card_data import values


class Deck:
    """
    This class represents a collection of cards

    Attributes:
        cards (list[Card]): list of cards in the deck
    """

    def __init__(self, empty: bool = False):
        """
        Constructor for Deck class

        Args:
            empty (bool): if false, the deck will be filled with a full, shuffled deck of cards
        """
        if empty:
            self.cards = []
        else:
            self.cards = (
                    [Card(values[i], "hearts") for i in range(0, 13)] +
                    [Card(values[i], "diamonds") for i in range(0, 13)] +
                    [Card(values[i], "spades") for i in range(0, 13)] +
                    [Card(values[i], "clubs") for i in range(0, 13)]
            )

            self.shuffle()

    def shuffle(self):
        """Rearranges deck in random order"""
        new_deck = [self.cards.pop(randint(1, len(self.cards) - 1)) for _ in range(len(self.cards) - 1)]
        new_deck.append(self.cards[0])
        self.cards = new_deck

    def push(self, a_card: Card):
        """Equivalent to .cards.append()"""
        self.cards.append(a_card)

    def pop(self, idx: int) -> Card:
        """Equivalent to .cards.pop()"""
        return self.cards.pop(idx)

    def pop_matches(self, value: str) -> list[Card]:
        """
        Returns all cards found that match value, and removes them from deck

        Args:
            value (str): the value to search for
        Return:
            card (list[Card]): the cards that were found
        """
        matches = []
        while value in self.cards:
            matches.append(self.pop(self.cards.index(value)))

        return matches
