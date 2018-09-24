import heapq


# class MinHeap(object):
#     def __init__(self): self.h = []
#
#     def heappush(self, x): heapq.heappush(self.h, x)
#
#     def heappop(self): return heapq.heappop(self.h)
#
#     def __getitem__(self, i): return self.h[i]
#
#     def __len__(self): return len(self.h)
#
#
# class MaxHeap(MinHeap):
#     def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
#
#     def heappop(self): return heapq.heappop(self.h).val
#
#     def __getitem__(self, i): return self.h[i].val


if __name__ == '__main__':
    a = [5, 1, 3, 4, 6, 2]
    print(a)
    heapq.heapify(a)
    print(a)
    print('min', a[0])
    print('k-min', heapq.nsmallest(3, a))
    print(heapq.heappop(a))
    print(heapq.heappop(a))
    print('k-min', heapq.nsmallest(3, a))
    heapq.heappush(a, 1)
    print('k-min', heapq.nsmallest(3, a))
    print('k-max', heapq.nlargest(3, a))
    heapq.heappush(a, 7)
    print('k-max', heapq.nlargest(3, a))
    print('max', a[-1])
    print(a)

    # Undocumented max-heap features !!!
    print(heapq._heapify_max(a))  # for a maxheap
    print(a)
    print(heapq.heappop(a))  # pop from minheap
    print(heapq._heappop_max(a))  # pop from maxheap

