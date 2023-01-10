class Card:
    """
    Card class.

    Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    True

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'K', 'Q']
        assert suit in ['hearts', 'spades', 'clubs', 'diamonds']
        assert type(visible) == bool
        self.rank = rank
        self.suit = suit
        self.visible = visible
        
    def suit_rankings(self):
        if self.suit == 'clubs':
            return 4
        elif self.suit == 'diamonds':
            return 3
        elif self.suit == 'hearts':
            return 2
        elif self.suit == 'spades':
            return 1
    def rank_rankings(self):
        if type(self.rank) == int:
            return self.rank
        else:
            if self.rank == 'A':
                return 14
            elif self.rank == 'K':
                return 13
            elif self.rank == 'Q':
                return 12
            elif self.rank == 'J':
                return 11
    
    def __lt__(self, other_card):
        if self.rank_rankings() < other_card.rank_rankings():
            return True
        elif self.rank_rankings() > other_card.rank_rankings():
            return False
        else:
            if self.suit_rankings() < other_card.suit_rankings():
                return True
            else:
                return False

    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.suit == 'hearts':
            suit = '♥'
        elif self.suit == 'diamonds':
            suit = '♦'
        elif self.suit == 'spades':
            suit=  '♠'
        elif self.suit == 'clubs':
            suit = '♣'
        if not self.visible:
            return '____\n|?  |\n| ? |\n|__?|'
        else:
            return '____\n|{}  |\n| {} |\n|__{}|'.format(str(self.rank), \
                suit, str(self.rank))

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        
        if not self.visible:
            return '(?, ?)'
        else:
            return '({}, {})'.format(str(self.rank), self.suit)

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert type(visible) == bool
        self.visible = visible
def doctests():
    """
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """
    