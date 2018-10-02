class ChessBoard:

    def __init__(self, m, n):
        """
            build the board of size m * n
        :param m: rows
        :param n: cols
        """
        self.m = m
        self.n = n
        self.size = m * n
        self.nodes = {}
        i = 0
        for row in range(self.m):
            for col in range(self.n):
                self.nodes[(row, col)] = i
                i += 1

    def __repr__(self):
        return '%s' % self.nodes

    def is_valid(self, node):
        if self.in_bounds(node):
            return True
        else:
            # TODO: Skip on invalid
            return False

    KNIGHT_DIRS = [[1, 2], [2, 1], [2, -1], [1, -2],
                   [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

    def get_dir_knights(self, node):
        possible_nodes = []
        for dir in self.KNIGHT_DIRS:
            possible_nodes.append((node[0] + dir[0], node[1] + dir[1]))
        return possible_nodes

    def get_dir_bishop(self, node):
        # Move NE
        possible_moves = []

        # Move NE
        i = node[0] - 1
        j = node[1] + 1
        while i >= 0 and j < self.n:
            # print(i, j)
            possible_moves.append((i, j))
            i -= 1
            j += 1

        # Move SE
        i = node[0] + 1
        j = node[1] + 1
        while i < self.m and j < self.n:
            # print(i, j)
            possible_moves.append((i, j))
            i += 1
            j += 1

        # Move SW
        i = node[0] + 1
        j = node[1] - 1
        while i < self.m and j >= 0:
            # print(i, j)
            possible_moves.append((i, j))
            i += 1
            j -= 1

        # Move NE
        i = node[0] - 1
        j = node[1] - 1
        while i >= 0 and j >= 0:
            # print(i, j)
            possible_moves.append((i, j))
            i -= 1
            j -= 1

        return possible_moves

    def get_dir_rook(self, node):
        possible_moves = []

        # Move E
        i = node[0]
        j = node[1] + 1
        while j < self.n:
            # print(i, j)
            possible_moves.append((i, j))
            j += 1

        # Move W
        i = node[0]
        j = node[1] - 1
        while j >= 0:
            # print(i, j)
            possible_moves.append((i, j))
            j -= 1

        # Move N
        i = node[0] - 1
        j = node[1]
        while i >= 0:
            # print(i, j)
            possible_moves.append((i, j))
            i -= 1

        # Move S
        i = node[0] + 1
        j = node[1]
        while i < self.m:
            # print(i, j)
            possible_moves.append((i, j))
            i += 1

        return possible_moves

    def get_dir_queen(self, node):
        possible_moves = []
        possible_moves.extend(self.get_dir_rook(node))
        possible_moves.extend(self.get_dir_bishop(node))
        return possible_moves

    MOVES_MAP = {
        'KNIGHT': get_dir_knights,
        'BISHOP': get_dir_bishop,
        'ROOK': get_dir_rook,
        'QUEEN': get_dir_queen,
    }

    def get_moves(self, node, piece):
        valid_nodes = []
        possible_nodes = self.MOVES_MAP[piece](self, node)
        for possible_node in possible_nodes:
            if self.is_valid(possible_node):
                valid_nodes.append(self.nodes[possible_node])

        return valid_nodes

    def in_bounds(self, node):
        # return 0 <= node[0] and node[1] < self.size
        if node in self.nodes:
            return True
        else:
            return False

    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                # print('%s-%s' % ((i, j), self.nodes[(i, j)]), end=' ')
                print('%s' % (self.nodes[(i, j)]), end=' ')
            print()


if __name__ == '__main__':
    board = ChessBoard(5, 5)
    board.display()
    print('KNIGHT', board.get_moves((2, 2), 'KNIGHT'))
    print('BISHOP', board.get_moves((2, 2), 'BISHOP'))
    print('ROOK', board.get_moves((2, 2), 'ROOK'))
    print('QUEEN', board.get_moves((2, 2), 'QUEEN'))