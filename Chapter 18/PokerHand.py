"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
from tabulate import tabulate
from operator import itemgetter


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """ Checks if the PokerHand contains a pair
            Returns True or False
        """
        self.rank_hist()
        return 2 in self.ranks.values()

    def has_three_of_a_kind(self):
        """ Checks if the PokerHand contains a three of a kind
            Returns True or False
        """
        self.rank_hist()
        return 3 in self.ranks.values()

    def has_four_of_a_kind(self):
        """ Checks if the PokerHand contains a four of a kind
            Returns True or False
        """
        self.rank_hist()
        return 4 in self.ranks.values()

    def has_full_house(self):
        return self.has_three_of_a_kind() and self.has_pair()

    def has_two_pair(self):
        self.rank_hist()
        c = 0
        for val in self.ranks.values():
            if val == 2:
                c += 1
        return c >= 2

    def has_straight(self):
        self.rank_hist()
        # sorted list of ranks from Ace, 2, 3 ... to King
        sr = sorted(self.ranks.keys())
        # need to declare as empty list in case there is no Ace and therefore we don't implement Ace-high logic below
        sr_ace = []
        # Ace-high straight logic: remove the Ace (as 1) and replace with Ace (as 14)
        if 1 in sr:
            sr_ace = sr[:]
            sr_ace.pop(0)
            sr_ace.append(14)
        # Note: the string slice here is to make sure we only send the last 5 numbers as we only care about Ace-high straights in this case
        return has_5_consecutive(sr) or has_5_consecutive(sr_ace[-5:])

    def build_rank_suit_map(self):
        """ Builds a mapping from ranks to suits within the hands
        """
        self.rank_suit_map = {}
        for card in self.cards:
            self.rank_suit_map[card.rank] = self.rank_suit_map.get(card.rank, []) + [card.suit]

    def has_straight_flush(self):
        # First check that there is any straight, then check if there is a flush
        # These two won't guarantee a straight flush but the absence of them will guarantee there isn't one       
        if self.has_straight() and self.has_flush():
            # Build out the mapping from rank to suit
            self.build_rank_suit_map()
            self.straights = []
            # Sorted ranks for entire Poker Hand
            sr = sorted(self.rank_suit_map.keys())
            # Logic for Ace-high
            sr_ace = []
            if 1 in sr:
                sr_ace = sr[:]
                sr_ace.pop(0)
                sr_ace.append(14)
            # Finds all the straights in the hand and adds them to self.straights (including Ace-high logic)
            for i, n in enumerate(sr):
                if i == len(sr) - 4:
                    break
                # string slice of 5 adjacent rank numbers
                five_cards = sr[i:i+5]
                # Note: has_5_consecutive does have a similar for loop but it is not sufficient for our purposes...
                #       ...therefore we call it in this for loop instead with a restriction of 5 card sequences
                if has_5_consecutive(five_cards):
                    self.straights.append(five_cards)
            last_five = sr_ace[-5:]
            if has_5_consecutive(last_five):
                self.straights.append(last_five)
            # Check each possible straight to see if it is a straight flush
            for straight in self.straights:
                # maps from suits (within the straight) to counters so we know how many of each suit is represented by the straight
                # once this hits 5 we know we have a straight flush
                straight_suit_hist = {}
                for rank in straight:
                    # rank of 14 is relevant for straight calculations, but should be a 1 for looking up the Ace rank or else will get KeyError
                    if rank == 14:
                        rank_lookup = 1
                    else:
                        rank_lookup = rank
                    straight_suits = self.rank_suit_map[rank_lookup]
                    for suit in straight_suits:
                        straight_suit_hist[suit] = straight_suit_hist.get(suit, 0) + 1
                # 5 of the same suit represented within the straight rank cards = straight flush found
                if 5 in straight_suit_hist.values():
                    return True
            # end of search - if we haven't found a straight flush at this point then return False
            return False
        # else not a straight or a flush, so can't be a straight flush - hopefully saves wasted computation
        else:
            return False

    def classify(self):
        """ Checks for the highest-value hand within the Poker Hand
            Starts at the highest possible and ends once it's found one (other lower classifications are then irrelevant)
        """
        if self.has_straight_flush():
            self.label = 'Straight Flush'
        elif self.has_four_of_a_kind():
            self.label = 'Four of a Kind'
        elif self.has_full_house():
            self.label = 'Full House'
        elif self.has_flush():
            self.label = 'Flush'
        elif self.has_straight():
            self.label = 'Straight'
        elif self.has_three_of_a_kind():
            self.label = 'Three of a Kind'
        elif self.has_two_pair():
            self.label = 'Two Pair'
        elif self.has_pair():
            self.label = 'Pair'
        else:
            self.label = 'High Card'

    def _test_print(self):
        print(self)
        print('')
        if self.has_pair(): print('Poker Hand: Pair')
        if self.has_three_of_a_kind(): print('Poker Hand: Three of a Kind')
        if self.has_four_of_a_kind(): print('Poker Hand: Four of a Kind')
        if self.has_full_house(): print('Poker Hand: Full House')
        if self.has_two_pair(): print('Poker Hand: Two Pair')
        if self.has_flush(): print('Poker Hand: Flush')
        if self.has_straight(): print('Poker Hand: Straight')
        if self.has_straight_flush(): print('Poker Hand: Straight Flush')
        print('')

        
def has_5_consecutive(t):
    """ Checks if a given list of integers has 5 consecutive numbers anywhere inside
        Expects a sorted list
        Returns True or False
    """
    # Avoids unnessecsary execution and also some rare index out of range errors for smaller lists of ranks
    if len(t) < 5:
        return False
    for i, n in enumerate(t):
        # Logic to stop more index out of range errors from the string slices
        if i == len(t) - 4:
            break
        if t[i] == t[i+1]-1 and t[i] == t[i+2]-2 and t[i] == t[i+3]-3 and t[i] == t[i+4]-4:
            return True
    return False

def classification_probabilities():
    """ Creates a number of Poker Hands and counts the occurrence of various classifications
        Prints a table with each classification and its probability
    """
    class_hist = {}
    hand_counter = 0
    for i in range(1000000):
        deck = Deck()
        deck.shuffle()

        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.sort()
            hand.classify()
            class_hist[hand.label] = class_hist.get(hand.label, 0) + 1
            hand_counter += 1

    table = [] 
    print('')
    # Sort by the 2nd tuple item (count)
    sorted_class_hist = sorted(class_hist.items(), key=itemgetter(1))
    for classification, count in sorted_class_hist:
        table.append([classification, count,  f'{count / hand_counter:.2%}'])
    print(tabulate(table, headers=['Classification', 'Count', 'Probability']))
    print('\nTotal Poker Hands processed:', hand_counter)
    print('')


if __name__ == '__main__':
    classification_probabilities()
            
