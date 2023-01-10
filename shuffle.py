class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    
    >>> odd_cards = [1, 2, 3, 4, 5]
    >>> mod_oh_even = Shuffle.modified_overhand(odd_cards, 2)
    >>> mod_oh_even
    [1, 2, 3, 4, 5]
    """     
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        assert type(num) == int and num >=0
        assert type(cards) == list
        assert num < len(cards)
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        if num == 0 :
            return cards
        else:
            if len(cards) % 2 == 0 and num % 2 == 1:
                top_half_take = num // 2 + 1
                bottom_half_take = num - top_half_take
                top_half_remain = len(cards) // 2 - top_half_take
                top_half = cards[0:int(len(cards) / 2)][::-1]
                bottom_half = cards[int(len(cards) / 2):]
                cards = top_half[0:top_half_take][::-1] + \
                    bottom_half[0:bottom_half_take] + \
                    top_half[::-1][0:top_half_remain] + \
                    bottom_half[bottom_half_take:]
            elif len(cards) % 2 == 1 and num % 2 == 0:
                top_half_take = num // 2 + 1
                bottom_half_take = num - top_half_take
                top_half = cards[0:int(len(cards) / 2) + 1][::-1]
                top_half_remain = len(top_half) - top_half_take
                bottom_half = cards[int(len(cards) / 2) + 1:]
                cards = top_half[0:top_half_take][::-1] + \
                    bottom_half[0:bottom_half_take] + \
                    top_half[::-1][0:top_half_remain] + \
                    bottom_half[bottom_half_take:]
            else:
                top_half = cards[0:int(len(cards) / 2 + 0.5)][::-1]
                bottom_half = cards[int(len(cards) / 2 + 0.5):]
                top_half_take = int(num / 2 + 0.5)
                top_half_remain = len(top_half) - top_half_take
                bottom_half_take = num - top_half_take
                cards = top_half[0:top_half_take][::-1] + \
                    bottom_half[0:bottom_half_take] + \
                    top_half[::-1][0:top_half_remain] + \
                    bottom_half[bottom_half_take:]
            return Shuffle.modified_overhand(cards, num - 1)

    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores
        the deck.
        """
        assert type(cards) == list
        if len(cards) == 0:
            return []
        else:
            return_list = Shuffle.mongean(cards[:-1])
            if len(return_list) % 2 == 0:
                return return_list + [cards[-1]]
            else:
                return [cards[-1]] + return_list
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
            