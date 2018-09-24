# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


def partition(A, lo, hi):
    """
    Standard QuickSort partitio using Lomoto partition scheme choose pivot as the last item
    :param A:
    :param lo:
    :param hi:
    :return:
    """
    i = (lo - 1)  # index of smaller element seen so far is before the first element
    pivot = A[hi]  # high as choice of pivot

    for j in range(lo, hi):
        # print(i, j, pivot, A)
        # If current element is smaller than or
        # equal to pivot
        if A[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            A[i], A[j] = A[j], A[i]

    # swap to place pivot at correct position
    # i is the lowest element seen so far
    A[i + 1], A[hi] = A[hi], A[i + 1]
    return i + 1

def kth_smallest(a, l, r, k):
    """
        O(N) average or O(N^2) for worst case
    :param a:
    :param l:
    :param r:
    :param k:
    :return:
    """
    # If k is smaller than number of elements
    for k in range(0, r - l + 1):
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(a, l, r)
        print('pivot', pos)

        # position is same as k
        if pos - 1 == k - 1:
            return a[pos]

        # position is greater, recur for left subarray
        if pos - 1 > k - 1:
            return kth_smallest(a, l, pos - 1, k)

        # position is lesser, recur for right subarray
        return kth_smallest(a, pos + 1, r, k - pos + l - 1)



a = [12, 3, 5, 7, 4, 19, 26]
k = 3
print(a)
print(kth_smallest(a, 0, len(a) - 1, k))
# assert kth_smallest(a, 0, len(a) - 1, k) == 5
