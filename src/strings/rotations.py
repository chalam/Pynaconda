def rotate_left(s, n):
    return s[n:] + s[:n]

def rotate_right(s, n):
    return s[-n:] + s[:-n]

if __name__ == '__main__':
    assert rotate_left(['a', 'b', 'c', 'd'], 2) == ['c', 'd', 'a', 'b']
    assert rotate_left(['a', 'b', 'c', 'd'], 3) == ['d', 'a', 'b', 'c']