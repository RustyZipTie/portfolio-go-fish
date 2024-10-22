from cards.card import Card
from cards.card_data import values
from players.UI import show_list
from cards.deck import Deck
from typing import Callable


class Player:
    """
    This class represents a player in the go fish game
    """

    def __init__(self, name: str, game_deck: Deck, request: Callable[[list[str]], str], visible: bool):
        """
        constructor for the Player class

        Args:
            name (str): name of the player, used to clarify outputs
            game_deck (Deck): the central Deck of the game that the player is playing
            request (function(list[int]) -> int): function that takes a list of possible values and returns the one that the player is choosing to request
            visible (bool): indicates whether to show the user certain information about player
        """
        self.__game_deck = game_deck
        self.hand = Deck(empty=True)
        self.books = []  #: list of player's books
        self.__name = name
        self.__visible = visible
        self.__request = lambda: request(list({c.get_value() for c in self.hand.cards}))

    def draw(self, num: int = 1, print_card: bool = False):
        """
        draws a given number of cards from game deck to player's hand

        Args:
            num (int): the number of cards to draw. default is 1
            print_card (bool): indicates whether to print a message with the name of the drawn card
        """
        if len(self.__game_deck.cards) == 0:
            print(f">>>Deck is empty, {self.__name} could not draw")
        else:
            for i in range(num):
                card = self.__game_deck.pop(0)
                if print_card:
                    print(f">>>{self.__name} drew the {card}")
                self.hand.push(card)

    def print_hand(self):
        """prints player's hand"""
        show_list(self.hand.cards, caption=f"{self.__name}'s hand:")

    def print_books(self):
        """print player's books"""
        if len(self.books) == 0:
            print(f">>>{self.__name} has no books")
        else:
            show_list([f"Book of {val}s" for val in self.books], caption=f"{self.__name}'s books:")

    def __add_book(self, value: int):
        print(f">>>{self.__name} has a new pair of {value}s")
        self.hand.pop(self.hand.cards.index(value))
        self.hand.pop(self.hand.cards.index(value))
        self.books.append(value)

    def check_books(self):
        """
        checks for books in player's hand

        Prints appropriate messages.
        If books found, they are removed from hand and put in player's books
        """
        print(f">>>Checking for books in {self.__name}'s hand...")
        books_found = False
        for value in values:
            matches = self.hand.pop_matches(value)
            if len(matches) == 4:
                self.books.append(value)
                books_found = True
            else:
                self.hand.cards.extend(matches)

        if books_found:
            self.print_books()
            if self.__visible and len(self.hand.cards) > 0:
                self.print_hand()
        else:
            print(">>>No books found")

    def respond(self, value: str) -> list[Card]:
        """
        used to respond to a request from another player

        to be used in conjunction with receive() and request() in the following manner:
        Examples:
            playerA.receive(playerB.respond(playerA.request()))
        Args:
            value (str): the value being requested
        Returns:
            (list[Card]) list of matching cards
        """
        cards = self.hand.pop_matches(value)
        for card in cards:
            print(f">>>{self.__name} is giving up the {card}")

        if len(cards) == 0:
            print(">>>Go Fish!")

        return cards

    def receive(self, cards: list[Card]):
        """
        used to receive requested cards from another player

        to be used in conjunction with respond() and request() in the following manner:
        Examples:
            playerA.receive(playerB.respond(playerA.request()))
        Args:
            cards (list[Card]): cards given by opponent
        """
        if len(cards) == 0:
            self.draw(print_card=self.__visible)
        else:
            self.hand.cards.extend(cards)

    def request(self) -> str:
        """
        used to request a value from another player

        to be used in conjunction with respond() and receive() in the following manner:
        Examples:
            playerA.receive(playerB.respond(playerA.request()))

        Returns:
            (str) the value being requested
        """
        the_request = self.__request()
        print(f">>>{self.__name} is looking for {the_request}s")
        return the_request

    def out_of_cards(self) -> bool:
        """
        Check if player's hand is empty

        Returns:
            (bool) indicates if player's hand is empty
        """
        return len(self.hand.cards) == 0
