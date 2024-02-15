import numpy as np

# Objective function
def objective_function(x):
    return 4 + 2 * x + 2 * np.sin(20 * x) - 4 * x**2

# Mutation operation
def mutate(x, epsilon=0.01):
    mutation_prob = np.random.rand()
    if mutation_prob < 0.3:
        x = x - epsilon
    elif mutation_prob < 0.7:
        pass  # No mutation
    else:
        x = x + epsilon
    return np.clip(x, 0, 1)  # Clip to stay within [0, 1] range

# Crossover operation
def crossover(parent1, parent2):
    a = np.random.rand()
    child = a * parent1 + (1 - a) * parent2
    return np.clip(child, 0, 1)  # Clip to stay within [0, 1] range

# Parameters
N = 10  # Population size
epsilon = 0.01  # Mutation step size
num_generations = 100  # Number of generations

# Initialize population
population = np.arange(0, 1.01, 0.01)[:N]

# Main optimization loop
for generation in range(num_generations):
    # Evaluate fitness of each individual in the population
    fitness_values = np.array([objective_function(x) for x in population])

    # Roulette wheel selection for crossover
    total_fitness = np.sum(fitness_values)
    probabilities = fitness_values / total_fitness

    new_population = []
    for _ in range(N // 2):
        # Select two parents using roulette wheel selection
        parents_indices = np.random.choice(N, size=2, p=probabilities)
        parent1, parent2 = population[parents_indices]

        # Crossover
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent1, parent2)

        # Mutation
        child1 = mutate(child1, epsilon)
        child2 = mutate(child2, epsilon)

        new_population.extend([child1, child2])

    # Replace the old population with the new one
    population = np.array(new_population)

# Find the best individual in the final population
best_solution = population[np.argmax([objective_function(x) for x in population])]

print(f"Population size (N): {N}")
print(f"Best solution found: x = {best_solution}, F(x) = {objective_function(best_solution)}")
