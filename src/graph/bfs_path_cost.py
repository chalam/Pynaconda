from queue import Queue
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.nodes = [i + 1 for i in range(n)]
        self.edges = defaultdict(lambda: [])

    def __repr__(self):
        return '%s:%s:%s' % (self.n, self.nodes, self.edges)

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def bfs(self, start):
        frontier = Queue()
        frontier.put(start)
        came_from = {start: None}
        while not frontier.empty():
            current = frontier.get()
            if current in self.edges:
                for next in self.edges[current]:
                    if next not in came_from:
                        frontier.put(next)
                        came_from[next] = current
        return came_from

    def path_len(self, came_from, start, goal):
        path = []
        current = goal
        if goal not in came_from:
            return -1
        while current != start:
            path.append(current)
            current = came_from[current]
        # path.append(start)
            print('path from %s -> %s: %s' % (start, goal, path))
        return len(path) * 6

    def find_all_distances(self, start):
        paths = self.bfs(start)
        costs = []
        for node in self.nodes:
            if node != start:
                costs.append(self.path_len(paths, start, node))
        return ' '.join(str(x) for x in costs)


# t = int(input())
# for i in range(t):
#     n, m = [int(value) for value in input().split()]
#     graph = Graph(n)
#     for i in range(m):
#         x, y = [int(x) for x in input().split()]
#         graph.connect(x, y)
#     print(graph)
#     s = int(input())
#     graph.find_all_distances(s - 1)

if __name__ == '__main__':
    graph = Graph(6)
    lines = """1 2
2 3
3 4
1 5"""
    for line in lines.split('\n'):
        x, y = [int(x) for x in line.split()]
        graph.connect(x, y)
    print(graph)
    assert graph.find_all_distances(1) == "6 12 18 6 -1"

    graph = Graph(7)
    lines = """1 2
1 3
3 4
2 5"""
    for line in lines.split('\n'):
        x, y = [int(x) for x in line.split()]
        graph.connect(x,y)
    print(graph)
    assert graph.find_all_distances(2) == "6 12 18 6 -1 -1"