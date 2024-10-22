from cards.card_data import suits, values


class Card:
    """
    This class represents a single playing card
    """
    def __init__(self, value: str, suit: str):
        """
        Constructor for Card class

        Args:
            value (str): the face value of the card. must be between 1 and 13, inclusive
            suit (str): the suit of the card. must be "none", "hearts", "diamonds", "spades", or "clubs"
        """
        if suit.lower() in suits:
            self.__suit = suit
        else:
            raise ValueError(f"Improper suit: {suit}")

        if value in values:
            self.__value = value
        else:
            raise ValueError(f"Improper value: {value}")

    def get_value(self) -> str:
        """
        Returns the value of the card

        Returns:
            (str): the value of the card
        """
        return self.__value

    def get_suit(self):
        """
        Returns the suit of the card

        Returns:
            suit (str): the suit of the card
        """
        return self.__suit

    def __eq__(self, other):
        if type(other) == Card:
            return self.__value == other.get_value()
        else:
            return self.__value == other

    def __str__(self):
        return f"{self.__value} of {self.__suit}"
