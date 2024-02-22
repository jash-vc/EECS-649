import random

def random_board():
    return [random.randint(0, 7) for _ in range(8)]

def fitness(board):
    fitness = 28
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                fitness -= 1
    return fitness

def min_conflicts(board, max_iterations=1000, random_var=True):
    total_evaluations = 0

    for _ in range(100):
        current_board = board[:]
        current_fitness = fitness(current_board)
        evaluations = 1

        while current_fitness < 28 and evaluations < max_iterations:
            # For Random Variable
            if random_var:
                conflicted_vars = [i for i in range(8) if any([current_board[i] == current_board[j] or abs(i - j) == abs(current_board[i] - current_board[j]) for j in range(8)])]
                var_to_change = random.choice(conflicted_vars)
            # For Cyclic Variable 
            else:
                var_to_change = evaluations % 8  # Cyclic order: 1, 2, ..., 8, 1, 2, ..., 8, ...

            min_conflict_val = min(range(8), key=lambda val: sum([1 for j in range(8) if j != var_to_change and (current_board[j] == val or abs(j - var_to_change) == abs(current_board[j] - val))]))

            current_board[var_to_change] = min_conflict_val
            current_fitness = fitness(current_board)

            evaluations += 1

        total_evaluations += evaluations

        if current_fitness == 28:
            print("Solution found")
            print(" ".join(map(str, current_board)))
            print("Total evaluations:", evaluations)
            break

    return total_evaluations

# Example Usage:
max_iterations = 1000

min_conflicts_evaluations_random = min_conflicts(random_board(), max_iterations, random_var=True)
print("Min-Conflicts (Random Variable) Total Evaluations:", min_conflicts_evaluations_random)

min_conflicts_evaluations_cyclic = min_conflicts(random_board(), max_iterations, random_var=False)
print("Min-Conflicts (Cyclic Variable) Total Evaluations:", min_conflicts_evaluations_cyclic)
