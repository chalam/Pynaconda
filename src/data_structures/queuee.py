import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        return self.elements.popleft()

    def empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)
