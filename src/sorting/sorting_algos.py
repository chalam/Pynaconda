import heapq
from copy import deepcopy


def bubble_sort(A):
    """
    less items “bubbles” up to the top, heavy items sink to the bottom
    k-th iteration has last k heavy items
    :param A:
    :return:
    """
    n = len(A)
    for i in range(0, n):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

def insertion_sort(A):
    """
    maintains a sorted sublist in the lower positions of the list.
    Each new item is then “inserted” back into the previous sublist keeping it sorted
    :param A:
    :return:
    """
    n = len(A)
    for i in range(1, n):

        current = A[i]
        position = i

        while position > 0 and A[position - 1] > current:
            A[position] = A[position - 1]
            position = position - 1

        # insert at the right spot
        A[position] = current

    return A

def selection_sort(A):
    """
    first the least item and move it to the top
    :param A:
    :return:
    """
    n = len(A)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            # print(i, j, min)
            if A[j] < A[min]:
                min = j
        # print(i, min)
        # swap to the top
        if i != min:
            A[i], A[min] = A[min], A[i]
    return A

def radix_sort(array, base=10):
    """
    O(N + b) * log b maxAA - b base of items
    LSD for Numbers, MSD for string (lexi)
    Sort each digit into bins in each iteration
    :param array:
    :param base:
    :return:
    """
    def list_to_buckets(array, base, iteration):
        """
        bin based on the digit in iteration
        :param array:
        :param base:
        :param iteration:
        :return:
        """
        buckets = [[] for x in range(base)]
        for number in array:
            # Isolate the base-digit from the number
            digit = (number // (base ** iteration)) % base
            # Drop the number into the correct bucket
            buckets[digit].append(number)
        return buckets

    def buckets_to_list(buckets):
        """
        flatten list
        :param buckets:
        :return:
        """
        numbers = []
        for bucket in buckets:
            # append the numbers in a bucket
            # sequentially to the returned array
            for number in bucket:
                numbers.append(number)
        return numbers

    maxval = max(array)

    it = 0
    # Iterate, sorting the array by each base-digit
    while base ** it <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1

    return array


def merge(left, right):
    """2-way merge list"""
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])  # first
            left = left[1:]         # rest
        else:
            result.append(right[0])
            right = right[1:]

    # Either left or right may have elements left; consume them.
    # (Only one of the following loops will actually be entered.)
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    return result

def merge_sort(A):
    """
    O(NlogN)
    Keep splitting until one element each top down and the merge bottom up
    :param A:
    :return:
    """
    n = len(A)
    # Base case for recursion. A list of zero or one elements is sorted, by definition.
    if n == 1:
        return A

    # create two sublist
    mid = n // 2
    left = A[:mid]
    right = A[mid:]

    # Recursively sort both sublist.
    left = merge_sort(left)
    right = merge_sort(right)

    # merge now sorted sublist
    return merge(left, right)

def partition(A, lo, hi):
    """
    Using Lomoto partition scheme choose pivot as the last item
    :param A:
    :param lo:
    :param hi:
    :return:
    """
    i = (lo - 1)  # index of smaller element
    pivot = A[hi]  # high as choice of pivot

    for j in range(lo, hi):
        # print(i, j, pivot, A)
        # If current element is smaller than or
        # equal to pivot
        if A[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[hi] = A[hi], A[i + 1]
    return i + 1

def quick_sort(A, lo, hi):
    """
    O(NlogN)
    partition to less that k, k, greater that k
    :param A:
    :param lo:
    :param hi:
    :return:
    """
    if lo < hi:
        p = partition(A, lo, hi)
        quick_sort(A, lo, p - 1)
        quick_sort(A, p + 1, hi)
        return A

def counting_sort(A):
    """
    O(N+K)  K is the max(N)
    bin it to K array
    :param A:
    :return:
    """
    aux = [0] * (max(A)+1)
    for i in range(len(A)):
        aux[A[i]] += 1

    sortedA = []
    for i in range(len(aux)):
        if aux[i] != 0:
            for j in range(aux[i]):
                sortedA.append(i)
    return sortedA

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

if __name__ == '__main__':
    # A = [54,26,93,17,77,31,44,55,20]
    # import random
    # random.shuffle(A)

    import numpy as np
    A = np.random.randint(0, 100, 10).tolist()
    # import timeit as tt
    # timer = tt.timeit("""AA = bubble_sort(deepcopy(A))""", ).repeat(3)
    AA = bubble_sort(deepcopy(A))
    print('bubble_sort\t\t%s => %s' % (A, AA))
    AA = insertion_sort(deepcopy(A))
    print('insertion_sort\t%s => %s' % (A, AA))
    AA = selection_sort(deepcopy(A))
    print('selection_sort\t%s => %s' % (A, AA))
    AA = radix_sort(deepcopy(A))
    print('radix_sort\t\t%s => %s' % (A, AA))
    AA = merge_sort(deepcopy(A))
    print('merge_sort\t\t%s => %s' % (A, AA))
    AA = quick_sort(deepcopy(A), 0, len(A)-1)
    print('quick_sort\t\t%s => %s' % (A, AA))
    AA = counting_sort(deepcopy(A))
    print('counting_sort\t%s => %s' % (A, AA))
    AA = heap_sort(deepcopy(A))
    print('heapsort\t\t%s => %s' % (A, AA))


