# https://en.wikipedia.org/wiki/Trie


class Node():
    def __init__(self):
        # Note that using dictionary for children (as in this implementation) would not
        # allow lexicographic sorting mentioned in the next section (Sorting),
        # because ordinary dictionary would not preserve the order of the keys
        self.children = {}  # mapping from character ==> Node
        self.value = None

    def find(root, key):
        node = root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value

    def insert(root, string, value):
        node = root
        index_last_char = None
        for index_char, char in enumerate(string):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break

        # append new nodes for the remaining characters, if any
        if index_last_char is not None:
            for char in string[index_last_char:]:
                node.children[char] = Node()
                node = node.children[char]

        # store value in the terminal node
        node.value = value

    def __repr__(self) -> str:
        return '[%s: %s]' % (self.value, self.children)

    def __str__(self) -> str:
        return '[%s: %s]' % (self.value, self.children)


if __name__ == '__main__':
    trie = Node()
    trie.insert('a', 0)
    trie.insert('tea', 1)
    trie.insert('ted', 2)
    trie.insert('ten', 3)
    trie.insert('i', 4)
    trie.insert('in', 5)
    trie.insert('inn', 6)
    print(trie)
    print('ted=%s' % trie.find('ted'))
    print('in=%s' % trie.find('in'))
    print('int=%s' % trie.find('int'))