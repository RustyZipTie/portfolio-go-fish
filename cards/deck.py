from cards.card import Card
from random import randint
from cards.card_data import values


class Deck:
    def __init__(self, shuffled: bool = True, empty: bool = False):
        if empty:
            self.cards = []
        else:
            self.cards = (
                    [Card(i, "hearts") for i in range(1, 14)] +
                    [Card(i, "diamonds") for i in range(1, 14)] +
                    [Card(i, "spades") for i in range(1, 14)] +
                    [Card(i, "clubs") for i in range(1, 14)]
            )

            if shuffled:
                self.shuffle()

    def shuffle(self):
        new_deck = [self.cards.pop(randint(1, len(self.cards) - 1)) for _ in range(len(self.cards) - 1)]
        new_deck.append(self.cards[0])
        self.cards = new_deck

    def match(self, value: int) -> list[Card]:
        if not value in values:
            raise ValueError(f"Improper value: {value}")
        return [a_card for a_card in self.cards if a_card.get_value() == value]

    def __getitem__(self, idx: int) -> Card:
        return self.cards[idx]

    def __iadd__(self, a_card: Card):
        self.cards.append(a_card)

    def pop(self, idx: int) -> Card:
        return self.cards.pop(idx)

    def __str__(self):
        return "\n".join(str(a_card) for a_card in self.cards)



