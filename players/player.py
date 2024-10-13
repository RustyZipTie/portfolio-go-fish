from cards.deck import Deck

class Player:
    def __init__(self, game_deck: Deck, request):
        self.__game_deck = game_deck
        self.__hand = Deck(empty=True)
        self.request = lambda a: request()
