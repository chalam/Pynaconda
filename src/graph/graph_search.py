# import heapq
from queue import Queue
from src.graph.implementation import *
from src.data_structures.stackk import Stack
class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

    def cost(self, from_node, to_node):
        return 1

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def dfs(graph, start, goal):
    frontier = Stack()
    frontier.push(start)
    came_from = {start: None}
    while not frontier.empty():
        current = frontier.pop()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.push(next)
                came_from[next] = current
    return came_from

def bfs(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
                visited[next] = True
    return came_from

def path_from(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    return list(reversed(path))

def dijkstra(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in came_from or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = current
    return came_from

def heuristic(a, b):
    # Manhattan distance on a square grid
    # return abs(a.x - b.y) + abs(a.y - b.y)
    return 1

def greedy_bfs(graph, start, goal):
    """only heuristics"""
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                priority = heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from

def a_star(graph, start, goal):
    """dijkstra's + heuristics"""
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in came_from or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from

if __name__ == '__main__':
    g = SimpleGraph()
    g.edges = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}

    paths = dfs(g, 'A', None)
    print('dfs', path_from(paths, 'A', 'E'))
    paths = bfs(g, 'A', None)
    print('bfs', path_from(paths, 'A', 'E'))
    paths = a_star(g, 'A', 'E')
    print('a_star', path_from(paths, 'A', 'E'))
    paths = dijkstra(g, 'A', 'E')
    print('dijkstra', path_from(paths, 'A', 'E'))