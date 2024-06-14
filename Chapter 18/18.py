import copy
import random

class Card:
    """ Represents a standard playing card """

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return Card.rank_names[self.rank] + ' of ' + Card.suit_names[self.suit]

    def __lt__(self, other):
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # otherwise the suits are the same so check the rank
        return self.rank < other.rank


class Deck:
    """ Represents a standard playing card deck containing 52 cards """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def deal_hands(self, hands, cards):
        """ Deals a set number of hands from the deck
            hands = number of hands to deal
            cards = number of cards in each hand
            Returns the Hand objects created in a list
        """
        res = []
        for i in range(hands):
            new_hand = Hand('Hand ' + str(i+1))
            self.move_cards(new_hand, cards)
            res.append(new_hand)
        return res



class Hand(Deck):
    """ Represents a hand of playing cards
        Inherited from Deck() class
    """

    def __init__(self, label=''):
        self.cards = []
        self.label = label

def testing_deal_hands():
    my_deck = Deck()
    my_deck.shuffle()
    test_hands = my_deck.deal_hands(5, 2)

    for hand in test_hands:
        print(hand.label)
        print(hand)
        print('')

testing_deal_hands()