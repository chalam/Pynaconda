# can you hop from towers of height 4, 2, 0, 0, 2, 0
# you can jump distance = height of the tower
# https://www.youtube.com/watch?v=kHWy5nEfRIQ
a = [4, 2, 0, 0, 2, 0]


# int jumpTo = size;
# for(int i = size-1; i >= 0; i--)
# if(towers[i] >= jumpTo-i) jumpTo = i; return (jumpTo == 0);
def is_hoppable(towers):
    # Time: O(N), space = O(N)
    # By going backwards we are able to check each tower always only one time.
    jump_to = len(towers)
    i = jump_to - 1
    while i >= 0:
        if towers[i] >= jump_to - i:
            jump_to = i
        i -= 1
    return jump_to == 0


def is_hoppable_2(towers):
    # Time: O(N^2) Space: O(N)
    def hopper(idx, towers, length, jumper):
        # can you clear from starting idx
        if idx + towers[idx] >= length:
            jumper[idx] = True
        else:
            # can you jump to possible index where jumpable is T
            for i in range(idx + 1, towers[idx] + 1):
                if jumper[i]:
                    jumper[idx] = True
                    return
            jumper[idx] = False

    n = len(towers)
    jumper = [False] * n
    for i in range(n - 1, -1, -1):
        hopper(i, towers, n, jumper)
    return jumper[0]


a = [4, 2, 0, 0, 2, 0]
assert is_hoppable(a)
assert is_hoppable_2(a)

a = [1, 0]
assert not is_hoppable(a)
assert not is_hoppable_2(a)

a = [4, 3, 0, 3, 1, 0]
assert is_hoppable(a)
assert is_hoppable_2(a)
