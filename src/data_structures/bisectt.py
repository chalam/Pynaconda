from bisect import bisect_left, bisect_right, bisect


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 7, 8, 9, 10]

    print(index(a, 5))

    try:
        print(index(a, 6))
    except:
        pass

    print(find_le(a, 5))
    print(find_le(a, 6))
    print(find_lt(a, 6))
    print(find_ge(a, 6))
    print(find_gt(a, 6))
    print(bisect(a, 6))
