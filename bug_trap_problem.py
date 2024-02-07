# Author - Jash Miteshkumar Patel 
# Date - 4th February 2024 
# Problem - Bug Trap Problem

from queue import Queue

def is_valid_move(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and not grid[i][j]

def bfs(grid, start, goal):
    closed_set = set()
    fringe = Queue()
    fringe.put(start)
    path_length = 0

    while not fringe.empty():
        current = fringe.get()
        i, j = current

        if current == goal:
            return len(closed_set), fringe.qsize(), path_length

        if current not in closed_set:
            closed_set.add(current)
            path_length += 1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if is_valid_move(grid, x, y) and (x, y) not in closed_set:
                    fringe.put((x, y))

    return len(closed_set), fringe.qsize(), -1  # Goal not reachable

def dfs(grid, start, goal):
    closed_set = set()
    stack = [start]
    path_length = 0

    while stack:
        current = stack.pop()
        i, j = current

        if current == goal:
            return len(closed_set), len(stack), path_length

        if current not in closed_set:
            closed_set.add(current)
            path_length += 1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if is_valid_move(grid, x, y) and (x, y) not in closed_set:
                    stack.append((x, y))

    return len(closed_set), len(stack), -1  # Goal not reachable

def bidirectional(grid, start, goal):
    forward_closed_set = set()
    backward_closed_set = set()
    forward_fringe = Queue()
    backward_fringe = Queue()
    forward_fringe.put(start)
    backward_fringe.put(goal)
    forward_path_length = 0
    backward_path_length = 0

    while not forward_fringe.empty() and not backward_fringe.empty():
        forward_current = forward_fringe.get()
        backward_current = backward_fringe.get()
        forward_i, forward_j = forward_current
        backward_i, backward_j = backward_current

        if forward_current == goal or backward_current == start:
            return len(forward_closed_set) + len(backward_closed_set), forward_fringe.qsize() + backward_fringe.qsize(), forward_path_length + backward_path_length

        if forward_current not in forward_closed_set:
            forward_closed_set.add(forward_current)
            forward_path_length += 1
            for x, y in [(forward_i-1, forward_j), (forward_i+1, forward_j), (forward_i, forward_j-1), (forward_i, forward_j+1)]:
                if is_valid_move(grid, x, y) and (x, y) not in forward_closed_set:
                    forward_fringe.put((x, y))

        if backward_current not in backward_closed_set:
            backward_closed_set.add(backward_current)
            backward_path_length += 1
            for x, y in [(backward_i-1, backward_j), (backward_i+1, backward_j), (backward_i, backward_j-1), (backward_i, backward_j+1)]:
                if is_valid_move(grid, x, y) and (x, y) not in backward_closed_set:
                    backward_fringe.put((x, y))

    return len(forward_closed_set) + len(backward_closed_set), forward_fringe.qsize() + backward_fringe.qsize(), -1  # Goal not reachable

# Given Bug Trap Grid
bug_trap_grid = [[0]*100 for _ in range(100)]
for i in range(100):
    for j in range(100):
        if i < 50:
            d = abs(i - 51) + abs(j - 50)
            if d == 50:
                bug_trap_grid[i][j] = 1
        else:
            if j > 50:
                d = abs(i - 50) + abs(j - 75)
                if d == 24:
                    bug_trap_grid[i][j] = 1
            elif j < 50:
                d = abs(i - 50) + abs(j - 25)
                if d == 24:
                    bug_trap_grid[i][j] = 1

# Start and Goal Positions
start_position = (50, 55)
goal_position = (75, 70)

# Reversed Start and Goal State
# start_position = (75, 70)
# goal_position = (50, 55)

# Run BFS
bfs_closed, bfs_fringe, bfs_path_length = bfs(bug_trap_grid, start_position, goal_position)
print(f"BFS: Closed Set Size - {bfs_closed}, Fringe Size - {bfs_fringe}, Path Length - {bfs_path_length}")

# Run DFS
dfs_closed, dfs_stack, dfs_path_length = dfs(bug_trap_grid, start_position, goal_position)
print(f"DFS: Closed Set Size - {dfs_closed}, Stack Size - {dfs_stack}, Path Length - {dfs_path_length}")

# Run Bidirectional Search
bidirectional_closed, bidirectional_fringe, bidirectional_path_length = bidirectional(bug_trap_grid, start_position, goal_position)
print(f"Bidirectional Search: Closed Set Size - {bidirectional_closed}, Fringe Size - {bidirectional_fringe}, Path Length - {bidirectional_path_length}")

# Reverse the start and goal for Bidirectional Search
bidirectional_closed_reverse, bidirectional_fringe_reverse, bidirectional_path_length_reverse = bidirectional(bug_trap_grid, goal_position, start_position)
print(f"Bidirectional Search (Reversed): Closed Set Size - {bidirectional_closed_reverse}, Fringe Size - {bidirectional_fringe_reverse}, Path Length - {bidirectional_path_length_reverse}")
