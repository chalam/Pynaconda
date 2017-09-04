import collections


# name of the class to create and a sequence of attribute names.
Card = collections.namedtuple('Card', ['rank', 'suit'])


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    my_card = eval(repr(beer_card))
    print(my_card == beer_card)