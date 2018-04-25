

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
    card_values = {
        1: 11,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10
    }

    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.table_cards = []

    def draft_card(self):
        card = self.deck.give_random_card()
        self.table_cards.append(card)
        print(card)

    def count_table_cards(self):
        total = 0
        for card in self.table_cards:
            if card.number == 1 and total + self.card_values[card.number] > 21:
                total += 1
            else:
                total += self.card_values[card.number]
        return total

    def player_wants_to_continue(self):
        response = input("¿Quieres otra carta? (Y/N)")
        return response == "Y"

    def run(self):
        user_continue = True

        while user_continue and self.count_table_cards() < 21:
            self.draft_card()
            user_continue = self.player_wants_to_continue()

        score = self.count_table_cards()
        print("Tu puntuación es de {}".format(score))

        if score > 21:
            print("Has perdido")


if __name__ == "__main__":
    blackjack = Game()
    blackjack.run()
