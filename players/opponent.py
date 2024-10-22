from cards.card_data import values
from players.UI import show_list


class Opp:
    """
    This class manages the algorithm that chooses the opponent's moves
    """
    def __init__(self):
        """
        Constructor for the Opp class.

        Notes:
            you must call register_books() once before the Opp object is usable
        """
        self.__probabilities = {
            values[i]: 7 for i in range(0, 13)
        }
        self.__available_probabilities = lambda: {}

    def register_books(self, books1: list[str], books2: list[str]):
        """
        Registers player and opponent's lists of books so Opp object knows that values in them are not available

        Args:
            books1 (list[str]): first list of books
            books2 (list[str]): second list of books
        """
        self.__available_probabilities = lambda: {
            v: p for v, p in self.__probabilities.items() if v not in books1 and v not in books2
        }

    def print_probabilities(self):
        """
        prints the probability for each value
        """
        show_list([f"{v}: {p}" for v, p in self.__available_probabilities().items()], caption="probabilities:")

    def register_player_draw(self):
        """
        Increments the probability for all values by one

        To be called whenever the player draws during the game
        """
        for option in self.__probabilities.keys():
            self.__probabilities[option] += 1

    def register_player_request(self, value: str):
        """
        Sets the probability of the given value to 52

        To be called when the player makes a request
        Args:
            value (str): the value the player is requesting
        """
        self.__probabilities[value] = 52

    def register_opp_request(self, value: str):
        """
        Sets the probability of the given value to 0

        To be called whenever the opp makes a request, whether or not the player responds with cards
        In either case, it is certain that the player now has no cards of this value
        Args:
            value (str): the value the opp is requesting
        """
        self.__probabilities[value] = 0

    def get_choice(self, options: list[str]) -> str:
        """
        Takes the available values, and returns the one with the highest probability

        Args:
            options (list[str]): list of values that are in opp's hand
        Returns:
            (str) the most probable value
        """
        available = {v: p for v, p in self.__available_probabilities().items() if v in options}
        t_max = max(available, key=lambda a: available[a])
        return t_max
