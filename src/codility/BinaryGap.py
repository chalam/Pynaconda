# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def binary_gap(n):
    max_len  =0
    start_idx, end_idx = 0, 0
    b = list(bin(n))[2:]
    zero_seen = False
    print('n: %d, b: %s' % (n, b))
    for i in range(len(b)):
        print(b[i])
        if b[i] == '0' and not zero_seen:
            zero_seen = True
            start_idx = i
        if b[i] == '1' and zero_seen:
            end_idx = i - 1
            zero_seen = False
            curr_len = end_idx - start_idx + 1
            print('curr_len %d' % curr_len)
            if curr_len > max_len:
                max_len = curr_len
                print('updating max_len %d' % max_len)
    print('max_len %d' % max_len)
    return max_len


if __name__ == '__main__':
    # assert binary_gap(529) == 4
    # assert binary_gap(20) == 1
    # assert binary_gap(15) == 0
    # assert binary_gap(32) == 0
    # assert binary_gap(1041) == 5
    assert binary_gap(2147423626) == 3
    assert binary_gap(1610612737) == 3
    # assert binary_gap(2147483646) == 0
    # assert binary_gap(2147483647) == 0
