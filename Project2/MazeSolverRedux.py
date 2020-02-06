import json
import requests

class MazeSolver:
    START = 'A'
    END = 'B'
    WALL = 'X'
    OPEN = ' '
    VISITED = 'v'

    def __init__(self, maze):
        self.current_number_of_moves = 0
        self.shortest_number_of_moves = 1000000000
        self.shorted_possible_maze_output = ''
        self.maze = maze
        for row_index, row in enumerate(maze):
            for column_index, value in enumerate(row):
                if value == self.START:
                    self.start = { 'X': row_index, 'Y': column_index}

    def __str__(self):
       return "Solved the maze in {} moves\n".format(self.current_number_of_moves) \
            + "\n".join(str(row) for row in self.maze)

    def _is_position_within_maze_and_open(self, row_index, column_index):
        return 0 <= row_index < len(self.maze) \
            and 0 <= column_index < len(self.maze[row_index]) \
            and ( self.maze[row_index][column_index] == self.OPEN
                or self.maze[row_index][column_index] == self.END )

    def _solve(self, row_index, column_index):
        #print()
        #self.print()
        self.current_number_of_moves += 1

        if self.maze[row_index][column_index] == self.END:
            if self.current_number_of_moves < self.shortest_number_of_moves:
                self.shortest_number_of_moves = self.current_number_of_moves
                self.shorted_possible_maze_output = str(self)

            self.current_number_of_moves -= 1
            return

        if self.maze[row_index][column_index] != self.START:
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

        self.maze[row_index][column_index] = self.OPEN
        self.current_number_of_moves -= 1

    def solve(self):
        self._solve(self.start['X'], self.start['Y'] )

    def print_shortest_solution(self):
        print(self.shorted_possible_maze_output)



maze = [
    ['S', 'W', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', ' '],
    [' ', 'W', ' ', ' ', 'E'],
]

#maze_solver = MazeSolver(maze)

response = requests.get("https://api.noopschallenge.com/mazebot/random?minSize=10&maxSize=15")

if response.ok:
    response_body = json.loads(response.content)
    maze_solver = MazeSolver(response_body["map"])
    maze_solver.solve()
    maze_solver.print_shortest_solution()