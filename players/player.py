from cards.card import Card
from cards.card_data import values, reverse_values
from cards.deck import Deck
from typing import Callable

class Player:
    def __init__(self, game_deck: Deck, request: Callable[[list[str]], int]):
        self.__game_deck = game_deck
        self.__hand = Deck(empty=True)
        self.request = lambda a: request(list({values[c.getValue()] for c in self.__hand.cards}))

    def draw(self, num: int = 1):
        for i in range(num):
            self.__hand += self.__game_deck.pop(0)

