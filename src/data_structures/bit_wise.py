def count_bits(n):
    nbits = 0
    while n > 0:
        nbits += (n & 1)
        n >>= 1
    return nbits

def parity(n):
    """
        parity of n is 1 if odd number of 1's, else 0
    :param n:
    :return:
    """
    nbits = count_bits(n)
    return 0 if nbits % 2 == 0 else 1

def parity1(n):
    """
        parity of n is 1 if odd number of 1's, else 0
    :param n:
    :return:
    """
    par = 0
    while n > 0:
        par ^= (n & 1)  # isolate the last bit
        n >>= 1         # shift
    return par

def parity2(n):
    """
        parity of n is 1 if odd number of 1's, else 0
        * The C Programming Language 2nd Ed., Kernighan & Ritchie, 1988.
    :param n:
    :return:
    """
    par = 0
    while n > 0:
        n &= (n - 1)  # isolate the last bit and shift in one op
        par ^= 1
    return par

def get_lsb(n):
    """
        Extract LSB
    :param n:
    :return:
    """
    par = 0
    while n > 0:
        n &= (n - 1)  # isolate the last bit and shift in one op
        par ^= 1
    return par

if __name__ == '__main__':
    assert count_bits(11) == 3
    assert count_bits(0) == 0
    assert count_bits(15) == 4

    assert parity(11) == 1
    assert parity(0) == 0
    assert parity(15) == 0
    assert parity(1257) == 0
    assert parity(1256) == 1

    assert parity1(11) == 1
    assert parity1(0) == 0
    assert parity1(15) == 0
    assert parity1(1257) == 0
    assert parity1(1256) == 1

    assert parity2(11) == 1
    assert parity2(0) == 0
    assert parity2(15) == 0
    assert parity2(1257) == 0
    assert parity2(1256) == 1