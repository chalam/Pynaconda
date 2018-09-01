import math


class ChessBoard:
    def __init__(self, size):
        self.size = size
        self.nodes = []
        for row in range(self.size):
            for col in range(self.size):
                self.nodes.append((row, col))

    def __repr__(self):
        return '%s' % self.nodes

    def get_moves(self, node):
        knight_directions =[[1,2], [2,1], [2,-1], [1,-2],
                    [-1,-2],[-2,-1],[-2,1],[-1,2]]
        valid_nodes = []
        for dir in knight_directions:
            possible_node = (node[0] + dir[0], node[1] + dir[1])
            if self.in_bounds(possible_node):
                valid_nodes.append(possible_node)

        return valid_nodes

    def in_bounds(self, node):
        # return 0 <= node[0] and node[1] < self.size
        return node in self.nodes

    def make_tour(self):
        pass

    def get_rings(self):
        levels = self.size // 2
        rings = {}
        for level in range(levels):
            rings[level] = []
            for top_row_col in range(level, self.size - level - 1):
                rings[level].append((level, top_row_col))
            for right_col in range(level, self.size - level - 1):
                rings[level].append((right_col, self.size - level - 1))
            for bottom_row_col in range(self.size - level - 1, level, -1):
                rings[level].append((self.size - level - 1, bottom_row_col))
                # print((self.size - level - 1, bottom_row_col))
            for left_col in range(self.size - level - 1, level, -1):
                rings[level].append((left_col, level))
                # print((left_col + 1, level))
        return rings

    def rotate_left(self, ring, k):
        k = k % len(ring)
        return ring[k:] + ring[0:k]

    def print_matrix(self, ring, level):
        for part in self.chunks(ring, self.size - 2 * level):
            print(part)

    # Create a function called "chunks" with two arguments, l and n:
    def chunks(self, l, n):
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i + n]

    def sort_lonely_neighbors(self, to_visit):
        """
        It is more efficient to visit the lonely neighbors first,
        since these are at the edges of the chessboard and cannot
        be reached easily if done later in the traversal
        """
        neighbor_list = self.get_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.get_moves(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key=lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours

    def tour(self, n, path, to_visit):
        """
        Recursive definition of knights tour. Inputs are as follows:
        n = current depth of search tree
        path = current path taken
        to_visit = node to visit
        """
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit)  # append the newest vertex to the current point
        print("Visiting: ", to_visit)

        if n == self.w * self.h:  # if every grid is filled
            self.print_board()
            print
            path
            print
            "Done!"
            sys.exit(1)

        else:
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.tour(n + 1, path, neighbor)

            # If we exit this loop, all neighbours failed so we reset
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                print
                "Going back to: ", path[-1]
            except IndexError:
                print
                "No path found"

                sys.exit(1)

if __name__ == '__main__':
    cb = ChessBoard(5)
    print(cb)
    print(cb.get_moves((2, 2)))
    print(cb.get_moves((0, 2)))
    rings = cb.get_rings()
    for level, ring in rings.items():
        rotated = cb.rotate_left(ring, 4)
        cb.print_matrix(rotated, level)