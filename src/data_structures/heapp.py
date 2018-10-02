import heapq


class Heap(object):

    def __init__(self, l=[]):
        self._heap = l
        heapq.heapify(self._heap)

    def isempty(self):
        if len(self._heap) == 0:
            return True
        return False

    def getroot(self):
        return self._heap[0] if len(self._heap) != 0 else 0

    def __len__(self):
        return len(self._heap)

    def push(self, item):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def pushpop(self, item):
        raise NotImplementedError

    def replace(self, item):
        raise NotImplementedError


class HeapMax(Heap):
    def push(self, item):
        heapq.heappush(self._heap, -item)

    def pop(self):
        return -heapq.heappop(self._heap)

    def view_max(self):
        return self.getroot()

    def pushpop(self, item):
        return -heapq.heappushpop(self._heap, -item)

    def replace(self, item):
        return -heapq.heapreplace(self._heap, -item)


class HeapMin(Heap):
    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        return heapq.heappop(self._heap)

    def view_min(self):
        return self.getroot()

    def pushpop(self, item):
        return heapq.heappushpop(self._heap, item)

    def replace(self, item):
        return heapq.heapreplace(self._heap, item)


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

    min_heap = HeapMin()
    max_heap = HeapMax([])  # default args are init once and not reused
    for i in a:
        min_heap.push(i)
        max_heap.push(i)
    assert min_heap.pop() == min(a)
    assert max_heap.pop() == max(a)
