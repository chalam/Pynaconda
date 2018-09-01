class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)
