
import random
import math
print("Shrinanda Dinde")
print("1BM23CS324")

def calculate_cost(state):
    """Calculate number of attacking pairs diagonally."""
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def random_neighbor(state):
    """Generate a random neighbor by swapping two columns' queen positions."""
    neighbor = state.copy()
    i, j = random.sample(range(len(state)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def simulated_annealing(initial_state, initial_temp=10000, cooling_rate=0.99, min_temp=0.1):
    current = initial_state
    current_cost = calculate_cost(current)
    T = initial_temp
    step = 0

    print(f"Step {step}: State = {current}, Cost = {current_cost}")
    print_board(current)

    while T > min_temp:
        next_state = random_neighbor(current)
        next_cost = calculate_cost(next_state)
        delta_E = current_cost - next_cost

        if delta_E > 0:
            current = next_state
            current_cost = next_cost
        else:
            p = math.exp(delta_E / T)
            if random.random() < p:
                current = next_state
                current_cost = next_cost

        step += 1
        print(f"Step {step}: State = {current}, Cost = {current_cost}")
        print_board(current)

        T *= cooling_rate

        if current_cost == 0:
            print(f"Solution found at step {step}")
            break

    return current, current_cost

if __name__ == "__main__":
    initial_state = random.sample(range(4), 4)
    print("Initial state:", initial_state)
    print_board(initial_state)

    solution, cost = simulated_annealing(initial_state)

    print("Final state:", solution)
    print("Final cost (number of attacking pairs):", cost)
    print_board(solution)
