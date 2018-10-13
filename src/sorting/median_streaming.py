
import heapq
# https://leetcode.com/problems/find-median-from-data-stream/solution/
# https://leetcode.com/articles/recursive-approach-segment-trees-range-sum-queries-lazy-propagation/
# 1. use list, sort O(nlogn) and get the median
# 2. Insertion with binary search O(logn) and shift-insert O(n) the number in the right index
# 3. use Heap O(logn) insert and O(1) min or max
# 4. use self-balancing Binary Search Tree BST
# 5. Order statistics distributed selection algorithm - O(n) Median_of_medians
# 6. Counting sort O(n+p) the distribution and find median
# 7. multiset and two pointer
import random
from collections import Counter


def median(a):
    n = len(a)
    if n & 1:
        med = a[n // 2]
    else:
        med = (a[n // 2 - 1] + a[n // 2]) * 0.5
    print(a, med)

def find_median_sort(seq):
    """
        O(nlogn) sort + O(1) median
    :param a:
    :return:
    """
    a = []
    for s in seq:
        a.append(s)
        a = sorted(a)
        median(a)

def find_median_binary_search(seq):
    """
        O(logn) find index + 0(n) for shift-insert
    :param a:
    :return:
    """
    a = []
    n = 0
    for s in seq:
        if n == 0:
            a.append(s)
        else:
            # binary search the insert index i
            i = find_index_binary_search(a, s)
            # print(i)
            # copy 0..i, [s], i..n to new a
            if i < 0:
                aa = [s] + a
                a = aa
            elif i == len(a):
                aa = a + [s]
                a = aa
            else:
                aa = a[:i] + [s] + a[i:]
                a = aa
        n += 1
        median(a)


def find_index_binary_search(a, target):
    # a = sorted(a) # redundant since we insert in sorted order
    lo = 0
    hi = len(a)-1
    if target > a[hi]:
        return hi+1
    while lo <= hi:
        # mid = (lo + hi) // 2
        mid = lo + (hi - lo) // 2   # int overflow
        if target < a[mid]:
            hi = mid - 1
        elif target > a[mid]:
            lo = mid + 1
    return lo


def find_median_heaps(seq):
    """
        2 heap to find median
        3*O(logn) push + 2*O(logn) pop = 5*O(logn) + O(1) median
    :param seq:
    :return:
    """
    a = []
    lo = [] # left_max_heap store smaller half of number,
            # py: no max-heap, so negate on push and pop
    hi = [] # right_min_heap store the larger half;
            # py: default min-heap

    for s in seq:
        a.append(s)

        # always add to left
        heapq.heappush(lo, -s)

        # balance step to move left high to right
        heapq.heappush(hi, -heapq.heappop(lo))

        # maintain the heap size property
        # 2n or 2n+1 in left and 2n in right
        # move right to left if so.
        if len(lo) < len(hi):
            heapq.heappush(lo, -heapq.heappop(hi))

        if len(lo) > len(hi):
            med = -lo[0]    # n+1 in lo (default odd n)
        else:
            med = (-lo[0] + hi[0]) * 0.5    # n in lo|hi
        print(a, med)


def find_median_multiset(seq):
    """
        No multiset in py, use Counter dict but it doesnt have indexed access
        O(logn)
        3*O(logn) push + 2*O(logn) pop = 5*O(logn) + O(1) median
        INCOMPLETE
    :param seq:
    :return:
    """
    a = Counter()
    lo = None
    hi = None
    for s in seq:
        n = len(a)          # store prev size

        a[s] += 1           # add new item
        keys = list(a.keys())

        if n == 0:
            lo = hi = n
        elif n & 1:    # odd size before
            if s < keys[lo]:
                lo -= 1
            else:
                hi += 1     # insert at end
        else:               # even size before
            if keys[lo] < s < keys[hi]:
                lo += 1
                hi -= 1
            elif s > keys[hi]:
                lo += 1
            else:
                hi -= 1
                lo = hi

        med = (keys[lo] + keys[hi]) * 0.5    # n in lo|hi
        print(a, med, lo, hi)


def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) // 2 - 1, pivot_fn) +
                      quickselect(l, len(l) // 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

def pick_pivot(l):
    """
    INCOMPLETE: Pick a good pivot within l, a list of numbers
    This algorithm runs in O(n) time.
    https://rcoh.me/posts/linear-time-median-finding/
    """
    assert len(l) > 0

    # If there are < 5 items, just return the median
    if len(l) < 5:
        # In this case, we fall back on the first median function we wrote.
        # Since we only run this on a list of 5 or fewer items, it doesn't
        # depend on the length of the input and can be considered constant
        # time.
        return find_median_sort(l)

    # First, we'll split `l` into groups of 5 items. O(n)
    chunks = chunked(l, 5)

    # For simplicity, we can drop any chunks that aren't full. O(n)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]


    # Next, we sort each chunk. Each group is a fixed length, so each sort
    # takes constant time. Since we have n/5 chunks, this operation
    # is also O(n)
    sorted_groups = [sorted(chunk) for chunk in full_chunks]

    # The median of each chunk is at index 2
    medians = [chunk[2] for chunk in sorted_groups]

    # It's a bit circular, but I'm about to prove that finding
    # the median of a list can be done in provably O(n).
    # Finding the median of a list of length n/5 is a subproblem of size n/5
    # and this recursive call will be accounted for in our analysis.
    # We pass pick_pivot, our current function, as the pivot builder to
    # quickselect. O(n)
    median_of_medians = quickselect_median(medians, pick_pivot)
    return median_of_medians

def chunked(l, chunk_size):
    """Split list `l` it to chunks of `chunk_size` elements."""
    return [l[i:i + chunk_size] for i in range(0, len(l), chunk_size)]

def stream_next(a):
    for i in a:
        yield i

a = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
find_median_sort(stream_next(a))
find_median_binary_search(stream_next(a))
find_median_heaps(stream_next(a))
# print(pick_pivot(a))

a = [41,35,62,4,97,108]
find_median_sort(stream_next(a))
find_median_binary_search(stream_next(a))
find_median_heaps(stream_next(a))
# find_median_multiset(stream_next(a))
# print(pick_pivot(a))