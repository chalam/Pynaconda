# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# subarray = contiguous elements of array
# for the array of values −2, 1, −3, 4, −1, 2, 1, −5, 4;
# the contiguous subarray with the largest sum is 4, −1, 2, 1, with sum 6
# Largest Sum Contiguous Subarray
# key if max_ending_here Bi is know, what is  Bi+1
# is part of subset with i+1 or ignores the subset upto i
import itertools


def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        print('A', x, 'max_ending_here', max_ending_here, 'max_so_far', max_so_far)
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_subarray_subset(A):
    max_ending_here = max_so_far = A[0]
    start = end = 0
    for i in range(1, len(A)):
        max_ending_here = max_ending_here + A[i]

        # update the global max
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = i

        # reset the sequence if max subset is broken
        if max_ending_here < 0:
            start = i + 1
            end = i + 1
            max_ending_here = 0
        print(i, A[i], start, end, max_ending_here, max_so_far)

    print(A[start:end+1], max_so_far)
    return A[start:end+1], max_so_far


if __name__ == '__main__':
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([-2, 1, -3, -4, 5]) == 5
    assert max_subarray([1, -1, 1, -1, 2, 0, -1, 2 ]) == 3
    assert max_subarray([3, 4, -8, 5, 6, 7]) == 18
    assert max_subarray([3, 4, -6, 5, 6, 7]) == 19
    assert max_subarray_subset([3, 4, -8, 5, 6, 7]) == ([5, 6, 7], 18)
    assert max_subarray_subset([3, 4, -6, 5, 6, 7]) == ([3, 4, -6, 5, 6, 7], 19)
    assert max_subarray_subset([-2, -3, 4, -1, -2, 1, 5, -3]) == ([4, -1, -2, 1, 5], 7)
    assert max_subarray_subset([-2, 1, -3, -4, 5]) == ([5], 5)
