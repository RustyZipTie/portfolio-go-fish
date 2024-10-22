from random import randint

from cards.deck import Deck
from players.UI import menu
from players.opponent import Opp
from players.player import Player

def choose_random(options: list[str]) -> str:
    """choose a random string from a list"""
    idx = randint(0, len(options)-1)
    return options[idx]

# setup
opponent_mind = Opp()
game_deck = Deck()
user = Player("Player", game_deck, lambda a: menu(a, caption="Choose what value to request:"), True)
opp = Player("Opponent", game_deck, opponent_mind.get_choice, False)
opponent_mind.register_books(user.books, opp.books)
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
    user_request = user.request()
    opponent_mind.register_player_request(user_request)
    opp_response = opp.respond(user_request)
    if len(opp_response) == 0:
        opponent_mind.register_player_draw()
    user.receive(opp_response)

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
    opp_request = opp.request()
    opponent_mind.register_opp_request(opp_request)
    user_response = user.respond(opp_request)
    opp.receive(user_response)

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
