def fib(nth):
    if nth == 1 or nth == 2:
        return 1
    return fib(nth-1) + fib(nth-2)

def interative_fib(nth):
    if nth == 1 or nth == 2:
        return 1
    current = 2
    previous = 1
    current_nth = 3
    while current_nth != nth:
        current_nth += 1
        next = current + previous
        previous = current
        current = next
    return current

def _good_recursive_fib(nth, previous, current, current_nth):
    if nth == current_nth:
        return current
    return _good_recursive_fib(nth, current, previous + current, current_nth+1)

def good_recursive_fib(nth):
    if nth == 1 or nth == 2:
        return 1
    return _good_recursive_fib(nth, 1, 2, 3)

for nth in range(1, 40):
    print(nth, ":", good_recursive_fib(nth))


class MazeSolver:
    START = 'S'
    END = 'E'
    WALL = 'W'
    OPEN = ' '
    DEAD_END = 'X'
    VISITED = 'v'

    def __init__(self, maze):
        self.maze = maze
        for row_index, row in enumerate(maze):
            for column_index, value in enumerate(row):
                if value == self.START:
                    self.start = { 'X': row_index, 'Y': column_index}
        self.solved = False

    def print(self):
        for row in self.maze:
            print(row)

    def _is_position_within_maze_and_open(self, row_index, column_index):
        return 0 <= row_index < len(self.maze) \
            and 0 <= column_index < len(self.maze[row_index]) \
            and ( self.maze[row_index][column_index] == self.OPEN
                or self.maze[row_index][column_index] == self.END )

    def _solve(self, row_index, column_index):
        #print()
        #self.print()
        if self.maze[row_index][column_index] == self.END:
            self.print()
            self.solved = True
            return

        self.maze[row_index][column_index] = self.VISITED

        # east
        if self._is_position_within_maze_and_open(row_index, column_index + 1):
            self._solve(row_index, column_index+1)

        # north
        if self._is_position_within_maze_and_open(row_index - 1, column_index):
            self._solve(row_index - 1, column_index)

        # west
        if self._is_position_within_maze_and_open(row_index, column_index - 1):
            self._solve(row_index, column_index - 1)

        # south
        if self._is_position_within_maze_and_open(row_index + 1, column_index):
            self._solve(row_index + 1, column_index)

        if not self.solved:
            self.maze[row_index][column_index] = self.DEAD_END

    def solve(self):
        self._solve(self.start['X'], self.start['Y'] )





maze = [
    ['S', 'W', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', ' '],
    [' ', 'W', ' ', 'W', 'E'],
]

maze_solver = MazeSolver(maze)
maze_solver.print()
maze_solver.solve()



class EightQueens:

    QUEEN = 'Q'

    def __init__(self):
        self.board = []
        self.number_of_queens_on_the_board = 0
        for row in range(8):
            self.board.append([' ']*8)
        self.solved = False
        self.solve()

    def _is_diagonal_up_safe(self, row):
        current_column = self.number_of_queens_on_the_board-1
        row -= 1

        while current_column >= 0 and row >= 0:
            if self.board[row][current_column] == self.QUEEN:
                return False
            current_column -= 1
            row -= 1

        return True

    def _is_diagonal_down_safe(self, row):
        current_column = self.number_of_queens_on_the_board - 1
        row += 1

        while current_column >= 0 and row < 8:
            if self.board[row][current_column] == self.QUEEN:
                return False
            current_column -= 1
            row += 1

        return True

    def _is_row_safe(self, row):
        return self.QUEEN not in self.board[row]

    def _can_place_queen(self, row):
        return self._is_row_safe(row) \
            and self._is_diagonal_up_safe(row) \
            and self._is_diagonal_down_safe(row)

    def solve(self):
        if self.number_of_queens_on_the_board == 8:
            self.print()
            self.solved = True
            return

        for row in range(8):
            if self._can_place_queen(row):
                self.board[row][self.number_of_queens_on_the_board] = self.QUEEN
                self.number_of_queens_on_the_board += 1
                self.solve()
                if not self.solved:
                    self.number_of_queens_on_the_board -= 1
                    self.board[row][self.number_of_queens_on_the_board] = ' '

    def print(self):
        for row in self.board:
            print(row)

eight_queens = EightQueens()










