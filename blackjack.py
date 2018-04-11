

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


class Deck:
    suits = ["diamonds", "heart", "spades", "clubs"]
    max_number = 13

    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        pos = 0
        return self.cards.pop(pos)
