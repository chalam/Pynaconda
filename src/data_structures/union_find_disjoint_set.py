"""
MakeSet(x) initializes disjoint set for object x
Find(x) returns representative object of the set containing x
Union(x,y) makes two sets containing x and y respectively into one set

Some Applications:
- Kruskal's algorithm for finding minimal spanning trees
- Finding connected components in graphs
- Finding connected components in images (binary)

O(log*N)
"""
import itertools


class UnionFind:

    class Node:
        def __init__(self, label):
            self.label = label

        def __repr__(self):
            return self.label

        def __str__(self):
            return self.label

    def __init__(self, seq):
        self.items = []
        for ch in seq:
            # create a Node
            node = self.Node(ch)
            node.parent = node
            node.rank = 0
            # self.make_set(node)
            self.items.append(node)


    def make_set(self, x):
        """
            make the Node List with self referencial parent
        :param x:
        :return:
        """
        x.parent = x
        x.rank   = 0

    def union(self, x: Node, y: Node):
         xRoot = self.find(x)
         yRoot = self.find(y)
         if xRoot.rank > yRoot.rank:
             yRoot.parent = xRoot
         elif xRoot.rank < yRoot.rank:
             xRoot.parent = yRoot
         elif xRoot != yRoot: # Unless x and y are already in same set, merge them
             yRoot.parent = xRoot
             xRoot.rank = xRoot.rank + 1

    def find(self, x: Node):
        if x.parent == x:
            return x
        else:
            x.parent = self.find(x.parent)
        return x.parent

    def disjoint_set(self):
        sets = [self.find(x) for x in self.items]
        return sets

    def __repr__(self):
        return "%s" % self.items

    def __str__(self):
        return "%s" % self.items

    def __getitem__(self, item):
        return self.items[item]


if __name__ == '__main__':
    # l = [Node(ch) for ch in "abcdefg"]      #list of seven objects with distinct labels
    # print ("objects labels:\t\t\t", [str(i) for i in l])

    uf = UnionFind("abcdefg")
    sets = uf.disjoint_set()
    print ("set representatives:\t\t", sets)
    print ("number of disjoint sets:\t", len(set([i for i in itertools.groupby(sets)])))

    # make connections
    assert uf.find(uf[0]) != uf.find(uf[2])
    uf.union(uf[0], uf[2])  # joining first and third
    assert uf.find(uf[0]) == uf.find(uf[2])

    assert(uf.find(uf[0]) != uf.find(uf[1]))
    assert(uf.find(uf[2]) != uf.find(uf[1]))
    uf.union(uf[0], uf[1])        #joining first and second
    assert(uf.find(uf[0]) == uf.find(uf[1]))
    assert(uf.find(uf[2]) == uf.find(uf[1]))

    uf.union(uf[-2], uf[-1])        #joining last two sets
    uf.union(uf[-3], uf[-1])        #joining last two sets

    # display
    sets = uf.disjoint_set()
    print ("set representatives:\t\t", sets)
    print ("number of disjoint sets:\t", len(set([i for i in itertools.groupby(sets)])))

    # # uniqKeys = []
    # # kv = {}
    # # for k, grp in itertools.groupby(sets):
    # #     uniqKeys.append(k)
    # #     kv[k] = list(grp)
    # #     # for g in grp:
    # #     #     print(g)
    # # print(kv)
    # # print(len(set(uniqKeys)))
