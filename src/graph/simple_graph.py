class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


if __name__ == '__main__':
    g = SimpleGraph()
    g.edges = {'A': ['B'],
               'B': ['A', 'C', 'D'],
               'C': ['A'],
               'D': ['E', 'A'],
               'E': ['B']}
