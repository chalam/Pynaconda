# knight
# 2
# 2 3 4 5 6 7 8 9
# 4
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #
# Ans: 16
#

SYMBOLS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
KNIGHT_DIRS = [[1, 2], [2, 1], [2, -1], [1, -2],
               [-1, -2], [-2, -1], [-2, 1], [-1, 2]]


# BISHOP_DIRS = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

class Board:

    def __init__(self, m, n):
        """
            build the board of size m * n
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
        if self.in_bounds(node) and self.is_symbol_valid(node):
            return True
        else:
            # TODO: Skip on invalid
            return False

    def get_dir_knights(self, node):
        possible_nodes = []
        for dir in KNIGHT_DIRS:
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

    def get_moves(self, node, piece):
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
        # return 0 <= node[0] and node[1] < self.size
        if node in self.nodes:
            return True
        else:
            return False

    # def find_phone_numbers(self, num_map, phone_len):
    #     """
    #
    #     :param num_map:
    #     :param phone_len:
    #     :return:
    #     """
    #     this_row = [1] * 10
    #     for row in range(1, phone_len):
    #         prev_row = this_row
    #         this_row = [0] * 10
    #         for prev, nexts in num_map.items():
    #             for next_ in nexts:
    #                 this_row[int(next_)] += prev_row[int(prev)]
    #     return sum(this_row)
    def find_phone_numbers(self, num_map, start, phone_len, path=[]):
        '''
        :param num_map:  The movement of knight
        :param start: You can start from anywhere except 0 and 1
        :param path:
        :return: list containing all the valid numbers
        '''
        path = path + [start]
        if len(path) == phone_len:  #if the total number of length of path is 7 return the path. It means we found a valid phone number
            return [path] #we found one valid phone number
        if not start in num_map:
            return []
        paths = []
        for node in num_map[start]:
            if node:
                newpaths = self.find_phone_numbers(num_map, node, phone_len, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


if __name__ == '__main__':
    # piece = str(input()).upper()
    # num_len = int(input())
    # start_digits = list(map(int, input().rstrip().split()))
    # m = int(input())
    # n = int(input())
    # board = []
    # for i in range(m):
    #     board.append(list(map(str, input().rstrip().split())))
    # print(piece)
    # print(num_len)
    # print(start_digits)
    # print(board)

    piece = 'BISHOP'  # 'BISHOP
    num_len = 4
    start_digits = ['2', '3', '4', '5', '6', '7', '8', '9']
    m = 4
    n = 3
    lines = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    board = Board(m, n)
    start_node = {}
    for row in range(m):
        for col in range(n):
            symbol = lines[row][col]
            if symbol.isdigit():
                start_node[symbol] = (row, col)
            board.nodes[(row, col)] = lines[row][col]
    # print(board)

    count = 0
    number_map = {}
    for digit in start_digits:
        nodes = board.get_moves(start_node[digit], piece)
        next_values = []
        for node in nodes:
            next_values.append(int(board.nodes[node]))
        count += len(nodes)
        number_map[int(digit)] = next_values
        # print(digit, nodes, next_values, count)
    print(number_map)

    paths=[]
    for digit in start_digits:
        path=[]
        paths.append(board.find_phone_numbers(number_map, int(digit), num_len, path))
    print('paths:', len(paths))
    print('paths:', paths)