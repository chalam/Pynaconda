KNIGHT_DIRS = [[1, 2], [2, 1], [2, -1], [1, -2],
               [-1, -2], [-2, -1], [-2, 1], [-1, 2]]


# BISHOP_DIRS = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

class Board:

    def __init__(self, m, n):
        """
            Build the board of size m * n
        :param m: rows
        :param n: cols
        """
        self.m = m
        self.n = n
        self.nodes = {}

    def __repr__(self):
        return '%s' % self.nodes

    def is_symbol_valid(self, node):
        """
            valid number
        :param node:
        :return:
        """
        return self.nodes[node].isdigit()

    def is_valid(self, node, dir, piece):
        """
            valid node is bound and data is number
        :param node:
        :param dir:
        :param piece:
        :return:
        """
        if self.in_bounds(node) and self.is_symbol_valid(node):
            return True
        else:
            # TODO: Skip on invalid
            return False

    def get_dir_knights(self, node):
        """
            get all possible knight moves from node
        :param node: node
        """
        possible_nodes = []
        for dir in KNIGHT_DIRS:
            possible_nodes.append((node[0] + dir[0], node[1] + dir[1]))
        return possible_nodes

    def get_dir_bishop(self, node):
        """
            get all possible bishop moves from node diagonally NorthEast, SouthEast, SouthWest, NorthWest
        :param node: node
        """

        # Move NE
        # node = (1, 1) # 5
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

    def get_moves(self, node, piece):
        """
            get all valid modes
        :param node: node
        :param node: piece
        """
        valid_nodes = []
        if piece == 'KNIGHT':
            possible_nodes = self.get_dir_knights(node)
        elif piece == 'BISHOP':
            possible_nodes = self.get_dir_bishop(node)
        else:
            raise ValueError('Unknown piece %s' % piece)

        for possible_node in possible_nodes:
            if self.is_valid(possible_node, dir, piece):
                valid_nodes.append(possible_node)

        return valid_nodes

    def in_bounds(self, node):
        """
        Is the node in boundary
        :param node: node
        """
        # return 0 <= node[0] and node[1] < self.size
        if node in self.nodes:
            return True
        else:
            return False

    def find_phone_numbers(self, num_map, phone_len):
        """
            Find the count from each starting number
        :param num_map:
        :param phone_len:
        :return:
        """
        this_row = [1] * 10  # digits
        for row in range(1, phone_len):
            prev_row = this_row
            this_row = [0] * 10
            for prev, nexts in num_map.items():
                for next_ in nexts:
                    this_row[int(next_)] += prev_row[int(prev)]
        return sum(this_row)


if __name__ == '__main__':
    piece = str(input()).upper()
    phone_len = int(input())
    start_digits = list(map(str, input().rstrip().split()))
    m = int(input())
    n = int(input())
    board = Board(m, n)
    start_node = {}
    for i in range(m):
        lines = list(map(str, input().rstrip().split()))
        for j in range(n):
            symbol = lines[j]
            if symbol.isdigit():
                start_node[symbol] = (i, j)
            board.nodes[(i, j)] = lines[j]

    # print(piece)
    # print(num_len)
    # print(start_digits)
    # print(board)

    count = 0
    number_map = {}
    for digit in start_digits:
        nodes = board.get_moves(start_node[digit], piece)
        next_values = []
        for node in nodes:
            next_values.append(board.nodes[node])
        count += len(nodes)
        number_map[digit] = next_values
        # print(digit, nodes, next_values, count)
    # print(number_map)

    print(board.find_phone_numbers(number_map, phone_len))

