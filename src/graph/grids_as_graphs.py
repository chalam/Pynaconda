# http://www.redblobgames.com/pathfinding/grids/graphs.html
import pprint as pp
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)

class Grid:
    def __init__(self, m, n):
        self.all_nodes = []
        self.m = m
        self.n = n
        for x in range(m):
            for y in range(n):
                self.all_nodes.append([x, y])

    def __repr__(self):
        return '%s' % self.all_nodes

    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]] # S, E, N, W relative to [0,0]
        nodes = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            if neighbor in self.all_nodes:
            # if 0 <= neighbor[0] < self.m and 0 <= neighbor[1] < self.n:
                nodes.append(neighbor)
        return nodes

if __name__ == '__main__':
    grid = Grid(3,4)
    print(grid)

    print(grid.neighbors([0,2]))
    print(grid.neighbors([1,1]))
    print(grid.neighbors([2,3]))

