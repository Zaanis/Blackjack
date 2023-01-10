from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, spades), (2, hearts), (2, diamonds), (2, clubs), (3, spades)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, spades), (Q, spades), (10, spades), (7, hearts), (5, hearts)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, spades)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        self.cards = [Card(x,y) for x in [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] \
            for y in ['spades', 'hearts', 'diamonds', 'clubs']]
    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all(isinstance(x, int) for x in shuffle_and_count.values())
        assert all([True if x == 'mongean' or x == 'modified_overhand' \
            else False for x in shuffle_and_count.keys()])
        if 'modified_overhand' in shuffle_and_count:
            self.cards = Shuffle.modified_overhand(self.cards, \
                shuffle_and_count['modified_overhand'])
        if 'mongean' in shuffle_and_count:
            for i in range(shuffle_and_count['mongean']):
                self.cards = Shuffle.mongean(self.cards)
    
    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert type(hand) == PlayerHand or type(hand) == DealerHand
        hand.add_card(self.cards[0])
        self.cards.pop(0)

    def get_cards(self):
        return self.cards