

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)


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

    def __str__(self):
        str_cards = [str(card) for card in self.cards]
        return "Deck with {} cards:\n{}".format(len(self.cards), ",\n".join(str_cards))


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Game:
    def __init__(self):
        deck = Deck()
        player = Player()

    def run(self):
        pass


if __name__ == "__main__":
    deck = Deck()
    print(deck)
