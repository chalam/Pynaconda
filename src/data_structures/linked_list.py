class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def __str__(self):
            return '[%s]' % self.data

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, item):
        if self.tail is None:
            node = self.Node(item)
            self.head = node
            self.tail = node
        else:
            node = self.Node(item)
            node.prev = self.tail
            self.tail.next = node
        self.size += 1

    def prepend(self, item):
        if self.head is None:
            node = self.Node(item)
            self.head = node
            self.tail = node
        else:
            node = self.Node(item)
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __reversed__(self):
        currNode = self.head
        prevNode = nextNode = None
        self.tail = self.head

        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        self.head = prevNode

    def search(self, item):
        for node in self:
            if node is None or node.data == item:
                return node


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(3)
    ll.prepend(4)
    for i in ll:
        print(i)
    print('reversed')
    reversed(ll)
    for i in ll:
        print(i)

    print('search 3', ll.search(3))
    print('search 6', ll.search(6))
