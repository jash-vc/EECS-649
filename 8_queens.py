import random

#initial random board
def random_board():
    return [random.randint(0, 7) for _ in range(8)]

#Define fitness function
def fitness(board):
    fitness = 28
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                fitness -= 1
    return fitness

#Drawing board after solution
def print_board(board):
    for row in range(8):
        line = ['Q' if col == board[row] else '.' for col in range(8)]
        print(' '.join(line))
    print()

def random_restart_hill_climbing(max_iterations=1000):
    total_evaluations = 0

    for _ in range(100):
        current_board = random_board()
        current_fitness = fitness(current_board)
        evaluations = 1

        while current_fitness < 28 and evaluations < max_iterations:
            neighbors = [current_board[:] for _ in range(7)]
            for i in range(7):
                neighbors[i][random.randint(0, 7)] = random.randint(0, 7)

            neighbor = max(neighbors, key=fitness)
            neighbor_fitness = fitness(neighbor)

            if neighbor_fitness > current_fitness:
                current_board = neighbor
                current_fitness = neighbor_fitness

            evaluations += 1

        total_evaluations += evaluations

        if current_fitness == 28:
            print("Solution found")
            print_board(current_board)
            print("Total evaluations:", evaluations)
            break
        
random_restart_hill_climbing()
