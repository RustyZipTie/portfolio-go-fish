from random import randint

from cards.deck import Deck
from players.UI import menu
from players.player import Player

def choose_random(options: list[str]) -> str:
    """choose a random string from a list"""
    idx = randint(0, len(options)-1)
    return options[idx]

# setup
game_deck = Deck()
user = Player("Player", game_deck, lambda a: menu(a, caption="Choose what value to request:"), True)
opp = Player("Opponent", game_deck, choose_random, False)
user.draw(7)
opp.draw(7)
user.check_books()
opp.check_books()

# main game loop
while True:
    # user's turn
    # check if empty
    if user.out_of_cards():
        print(">>>Player is out of cards")
        break

    # print info
    user.print_hand()
    user.print_books()
    opp.print_books()

    # make request
    user.receive(opp.respond(user.request()))

    # check for books
    user.check_books()

    # check if empty
    if user.out_of_cards():
        print(">>>Player is out of cards")
        break

    # opponent's turn
    # check if empty
    if opp.out_of_cards():
        print(">>>Opponent is out of cards")
        break

    # make request
    opp.receive(user.respond(opp.request()))

    # check for books
    opp.check_books()

    # check if empty
    if opp.out_of_cards():
        print(">>>Opponent is out of cards")
        break

# wrap-up
user.print_books()
print(f">>>Player has {len(user.books)} books")
opp.print_books()
print(f">>>Opponent has {len(opp.books)} books")

if len(user.books) > len(opp.books):
    print(">>>Player won")
elif len(opp.books) > len(user.books):
    print(">>>Opponent won")
else:
    print(">>>Game tied")
