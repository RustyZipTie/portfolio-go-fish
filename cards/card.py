from cards.card_data import suits, values

class Card:
    def __init__(self, value: int, suit: str):
        if suit.lower() in suits:
            self.__suit = suit
        else:
            raise ValueError(f"Improper suit: {suit}")

        if value in values:
            self.__value = value
        else:
            raise ValueError(f"Improper value: {value}")

    def get_value(self):
        return self.__value

    def get_suit(self):
        return self.__suit

    def __eq__(self, other):
        return self.__value == other.get_value()

    def __str__(self):
        return f"{values[self.__value]} of {self.__suit}"