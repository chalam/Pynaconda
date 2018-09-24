from collections import deque

class Stack:
    def __init__(self):
        self.elements = deque()

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def peek(self):
        return self.elements[-1] #if not self.empty() else None

    def __str__(self):
        return '%s' % self.elements

    # https://www.forth.com/starting-forth/2-stack-manipulation-operators-arithmetic/
    def dup(self):
        """ duplicate the top stack items """
        return self.elements.append(self.elements[-1])

    def swap(self):
        """ reverses the top two stack items """
        pass

    def over(self):
        """ makes a copy of second item and pushes it to the top """
        pass

    def rot(self):
        """ rotates the third item to the top """
        pass


if __name__ == '__main__':
    s = Stack()
    print(s.empty())
    s.push(10)
    s.push(30)
    s.push(20)
    print(s)
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    # print(s.peek())
    # print(s.pop())
    print(s.empty())

