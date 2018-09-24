class Node:
    def __init__(self):
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def insert(self):
        pass

    def delete(self):
        pass


def isBinarySearchTree(root):
    numbers = []
    f = lambda node: numbers.append(node.value)

    inorder(root, f)

    for i in range(1, len(numbers)):
        if numbers[i - 1] > numbers[i]:
            return False

    return True


def inorder(root, f):
    if root.leftChild is not None:
        inorder(root.leftChild, f)
    print(f(root))
    if root.rightChild is not None:
        inorder(root.rightChild, f)


def preorder(root, f):
    print(f(root))
    if root.leftChild != None:
        preorder(root.leftChild, f)

    if root.rightChild != None:
        preorder(root.rightChild, f)


def postorder(root, f):
    if root.leftChild != None:
        postorder(root.leftChild, f)

    if root.rightChild != None:
        postorder(root.rightChild, f)
    print(f(root))


if __name__ == '__main__':
    # Tree for Expression (1 + 3) * (3 - 4)
    root = Node()
    root.value = '*'

    n1 = Node()
    n1.value = '1'
    n2 = Node()
    n2.value = '3'
    n3 = Node()
    n3.value = '+'
    n4 = Node()
    n4.value = '3'
    n5 = Node()
    n5.value = '4'
    n6 = Node()
    n6.value = '-'

    root.leftChild = n3
    root.rightChild = n6
    n3.leftChild = n1
    n3.rightChild = n2
    n6.leftChild = n4
    n6.rightChild = n5

    print(isBinarySearchTree(root))

    f = lambda node: node.value
    print(inorder(root, f))
    print(preorder(root, f))
    print(postorder(root, f))
