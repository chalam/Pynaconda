def ternary_search(ar, l, r, x):
    """
    O(log3N) - since three branching
    :param ar:
    :param l:
    :param r:
    :param x:
    :return:
    """
    if r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if ar[mid1] == x:
            return mid1
        if ar[mid2] == x:
            return mid2
        if x < ar[mid1]:
            return ternary_search(ar, l, mid1 - 1, x)
        elif x > ar[mid2]:
            return ternary_search(ar, mid2 + 1, r, x)
        else:
            return ternary_search(ar, mid1 + 1, mid2 - 1, x)
    return -1


if __name__ == '__main__':
    ar = [2, 3, 5, 6, 8, 9, 12, 13, 14]
    assert ternary_search(ar, 0, len(ar), 13) == 7
