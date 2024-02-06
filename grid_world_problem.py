# Author - Jash Miteshkumar Patel
# Date - 4th February 2024
# Problem - Planning in a grid world

from queue import PriorityQueue

def is_valid_move(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

class State:
    def __init__(self, position, cost, heuristic, path):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic
        self.path = path

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def forward_search(grid, start, goal, heuristic_func, algorithm):
    visited = set()

    if algorithm == "BFS":
        queue = PriorityQueue()
    elif algorithm == "Greedy":
        queue = PriorityQueue()
    elif algorithm == "A*":
        queue = PriorityQueue()

    start_state = State(start, 0, heuristic_func(start, goal), [start])
    queue.put(start_state)

    while not queue.empty():
        current_state = queue.get()

        if current_state.position == goal:
            return current_state.path

        if current_state.position not in visited:
            visited.add(current_state.position)
            i, j = current_state.position

            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if is_valid_move(grid, x, y):
                    new_state = State((x, y), current_state.cost + 1, heuristic_func((x, y), goal), current_state.path + [(x, y)])

                    if algorithm == "BFS":
                        queue.put(new_state)
                    elif algorithm == "Greedy":
                        queue.put(new_state)
                    elif algorithm == "A*":
                        queue.put(new_state)

def bfs(position, goal):
    return 0

def greedy_heuristic(position, goal):
    return manhattan_distance(position[0], position[1], goal[0], goal[1])

def astar_heuristic(position, goal):
    return manhattan_distance(position[0], position[1], goal[0], goal[1])

# Define the grid (0 denotes obstacle-free, 1 denotes obstacle)
grid = [
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
]

# Define initial and goal positions
start = (0, 0)
goal = (3, 3)

# For Run Results
print(f"BFS Path: {forward_search(grid, start, goal, bfs, 'BFS')}")
print(f"Greedy Best-First Search Path: {forward_search(grid, start, goal, greedy_heuristic, 'Greedy')}")
print(f"A* Path: {forward_search(grid, start, goal, astar_heuristic, 'A*')}")
