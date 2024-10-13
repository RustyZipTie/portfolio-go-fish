from cards.deck import Deck
from UI import menu, msg
from players.player import Player

# setup
game_deck = Deck()
user = Player(game_deck, request=lambda a: menu(a, num=True, obj=False))

user.request()
