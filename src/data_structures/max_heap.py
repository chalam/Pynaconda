class MaxHeap:
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
            if self.heap[index//2] < self.heap[index]:
                temp = self.heap[index//2]
                self.heap[index//2] = self.heap[index]
                self.heap[index] = temp
            index //= 2

    def sink(self, index):
        while index * 2 <= self.size:
            max_child = self.get_max_child_index(index)
            if self.heap[index] < self.heap[max_child]:
                temp = self.heap[index]
                self.heap[index] = self.heap[max_child]
                self.heap[max_child] = temp
            index =  max_child

    def get_max(self):
        max_n = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.sink(1)
        return max_n

    def peek_max(self):
        return self.heap[1]

    def get_last(self):
        self.size -= 1
        return self.heap.pop()

    def get_max_child_index(self, i):
        left = i * 2
        right = i * 2 + 1
        if right > self.size:
            return left
        else:
            if self.heap[left] > self.heap[right]:
                return left
            else:
                return right