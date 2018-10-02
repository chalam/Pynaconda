class MinHeap:
    """
        Min-heap has the min element at the root
    """
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, element):
        # add element to the end
        self.heap.append(element)
        self.size += 1
        self.swim(self.size)

    def swim(self, index):
        while index // 2 > 0:
            if self.heap[index//2] > self.heap[index]:
                temp = self.heap[index//2]
                self.heap[index//2] = self.heap[index]
                self.heap[index] = temp
            index //= 2

    def sink(self, index):
        while index * 2 <= self.size:
            min_child = self.get_min_child_index(index)
            if self.heap[index] > self.heap[min_child]:
                temp = self.heap[index]
                self.heap[index] = self.heap[min_child]
                self.heap[min_child] = temp
            index = min_child

    def get_min(self):
        min_n = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.sink(1)
        return min_n

    def peek_min(self):
        return self.heap[1]

    def get_last(self):
        last = self.heap[self.size]
        self.size -= 1
        return last

    def get_min_child_index(self, i):
        left = i * 2
        right = i * 2 + 1
        if right > self.size:
            return left
        else:
            if self.heap[left] < self.heap[right]:
                return left
            else:
                return right