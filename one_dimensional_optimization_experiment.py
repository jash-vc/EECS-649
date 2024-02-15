import numpy as np

# Objective function
def objective_function(x):
    return 4 + 2 * x + 2 * np.sin(20 * x) - 4 * x**2

# Mutation operation
def mutate(x, epsilon=0.01):
    mutation_prob = np.random.rand()
    if mutation_prob < 0.3:
        return x - epsilon
    elif mutation_prob < 0.7:
        return x
    else:
        return x + epsilon

# Parameters
N = 10  # Population size
epsilon = 0.01  # Mutation step size
num_generations = 100  # Number of generations

# Initialize population
population = np.arange(0, 1.01, 0.01)[:N]

# Main optimization loop
for generation in range(num_generations):
    # Evaluate fitness of each individual in the population
    fitness_values = [objective_function(x) for x in population]

    # Select N/2 pairs of parents and create N/2 offspring
    new_population = []
    for _ in range(N // 2):
        # Fitness-proportional selection (Roulette wheel selection)
        total_fitness = np.sum(fitness_values)
        probabilities = fitness_values / total_fitness
        selected_index = np.random.choice(len(population), p=probabilities)
        parent = population[selected_index]

        # Mutation
        child = mutate(parent, epsilon)

        new_population.append(child)

    # Replace the old population with the new one
    population = np.array(new_population)

# Find the best individual in the final population
best_solution = population[np.argmax([objective_function(x) for x in population])]

print(f"Population size (N): {N}")
print(f"Best solution found: x = {best_solution}, F(x) = {objective_function(best_solution)}")
