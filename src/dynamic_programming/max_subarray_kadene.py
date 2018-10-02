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
        # print('A', x, 'max_ending_here', max_ending_here, 'max_so_far', max_so_far)
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
        # print(i, A[i], start, end, max_ending_here, max_so_far)

    # print(A[start:end+1], max_so_far)
    return A[start:end+1], max_so_far


def circular_max_sum_array(a):
    """
    O(N^2)
    :param a:
    :return:
    """
    n = len(a)
    max_single = max_subarray(a)  # single pass

    # wrapped
    aa = []
    wrapped_sum = 0
    # aa = a[n] + a[:n-1]
    for i in range(n - 1, -1, -1):
        aa = a[i:] + a[:i]
        # print(aa)
        wrapped_sum = max(max_subarray(aa), wrapped_sum)
    # print(wrapped_sum)

    if wrapped_sum > max_single:
        return wrapped_sum
    else:
        return max_single


def maxCircularSum(a):
    """
    https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/
    :param a:
    :return:
    """
    n = len(a)

    # Case 1: get the maximum sum using standard kadane's
    # algorithm
    max_kadane = max_subarray(a)

    # Case 2: Now find the maximum sum that includes corner
    # elements.
    # change wrapping to non-wrapping.
    # Wrapping of contributing elements implies non wrapping of
    # non contributing elements, so find out the sum of non
    # contributing elements and subtract this sum from the total sum.
    #
    # To find out the sum of non contributing, invert sign of each element and then run Kadane’s algorithm.
    # Our array is like a ring and we have to eliminate the maximum continuous
    # negative that implies maximum continuous positive in the inverted arrays.
    #
    # Finally we compare the sum obtained by both cases, and return the maximum of the two sums.
    max_wrap = 0
    for i in range(0, n):
        max_wrap += a[i]    # sum array
        a[i] = -a[i]        # invert array element

    # Max sum with corner elements will be:
    # array_sum - (- max subarray sum of inverted array)
    max_wrap = max_wrap + max_subarray(a)

    # The maximum circular sum will be maximum of two sums
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane


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

    a = [3, 4, -6, 5, 6, 7]
    assert max_subarray(a) == 19
    assert circular_max_sum_array(a) == 25
    assert maxCircularSum(a) == 25
    a = [-2, 1, -3, 4, 5]
    assert max_subarray(a) == 9
    assert circular_max_sum_array(a) == 9
    assert maxCircularSum(a) == 9
