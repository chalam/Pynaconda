import math

def long_cons_char(seq):
    count = max_count = -math.inf
    max_char = None
    for i in range(1, len(seq)):
        prev, curr = seq[i - 1], seq[i]
        if curr == prev:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_char = curr
    return {max_char: max_count}


assert long_cons_char('AABCDDBBBEA') == {'B': 3}
assert long_cons_char('AABCDDDBBBEA') == {'D': 3}

