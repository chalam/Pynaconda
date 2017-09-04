import random

from src.objects.Card import Card


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        """impl len()"""
        return len(self._cards)

    def __getitem__(self, position):
        """impl use of []"""
        return self._cards[position]

    # def __setitem__(self, key, value):
    #     """ use of deck[i] = card"""
        # pass

    def __contains__(self, item):
        """imple for in"""
        return item in self._cards

if __name__ == '__main__':
    deck = FrenchDeck()
    print('len: %d' % len(deck))

    print(deck[5])
    print(deck[-5])
    print(deck[1:5])
    print(deck[12::13])

    print(Card('Q', 'hearts') in deck)
    print(Card('Z', 'hearts') in deck)

    for card in deck[-5]:
        print(card)

    print(list(enumerate(reversed(deck), 1)))

    try:
        random.shuffle(deck)
    except TypeError as e:  # this error is expected!
        print(repr(e))
    else:
        print('The deck was shuffled!')


    # monkey patch
    def put(deck, index, card):
        deck._cards[index] = card


    FrenchDeck.__setitem__ = put
    print(deck[:5])
    try:
        random.shuffle(deck)
    except TypeError as e:  # this error is expected!
        print(repr(e))
    else:
        print('The deck was shuffled!')
    print(deck[:5])