# https://app.codility.com/c/run/trainingYWY9WQ-2KW
# https://codesays.com/2014/solution-to-sigma-2012-stone-wall-by-codility/
# rectilinear skyline problem or Manhattan skyline problem,
# https://codility.com/media/train/solution-stone-wall.pdf

def stone_wall(H):
    stack = []
    block_count = 0    # The number of needing blocks
    for height in H:
        while len(stack) != 0 and height < stack[-1]:
            # If the height of current block is less than
            #    the previous ones, the previous ones have
            #    to end before current point. They have no
            #    chance to exist in the remaining part.
            # So the previous blocks are completely finished.
            stack.pop()
            block_count += 1
        if len(stack) == 0 or height > stack[-1]:
            # If the height of current block is greater than
            #    the previous one, a new block is needed for
            #    current position.
            stack.append(height)
        # Else (the height of current block is same as that
        #    of previous one), they should be combined to
        #    one block.
    # Some blocks with different heights are still in the stack.
    block_count += len(stack)
    return block_count

def stone_wall2(H):
    N = len(H)
    stones = 0
    stack = [0] * N
    stack_num = 0

    for i in range(N):
        while stack_num > 0 and stack[stack_num - 1] > H[i]:
            stack_num -= 1
        if stack_num > 0 and stack[stack_num - 1] == H[i]:
            pass
        else:
            stones += 1
            stack[stack_num] = H[i]
            stack_num += 1
    return stones



assert stone_wall([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7
assert stone_wall2([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7