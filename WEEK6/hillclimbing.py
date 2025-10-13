print("Shrinanda Dinde")
print("1BM23CS324")

def calculate_cost(state):
    """Calculate the number of attacking pairs of queens."""
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def generate_neighbors(state):
    """Generate neighbors by swapping the row positions of two queens."""
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            neighbor = state.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_state):
    current = initial_state
    current_cost = calculate_cost(current)
    step = 0

    print(f"Step {step}: State = {current}, Cost = {current_cost}")
    print_board(current)

    while True:
        neighbors = generate_neighbors(current)
        costs = [calculate_cost(n) for n in neighbors]

        min_cost = min(costs)
        if min_cost >= current_cost:
            # No better neighbor found, return current state
            print("No better neighbor found. Stopping.")
            break

        # Choose neighbor with minimum cost
        best_index = costs.index(min_cost)
        current = neighbors[best_index]
        current_cost = min_cost
        step += 1

        print(f"Step {step}: State = {current}, Cost = {current_cost}")
        print_board(current)

        if current_cost == 0:
            print("Goal reached!")
            break

    return current, current_cost

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

if __name__ == "__main__":
    import random

    initial_state = random.sample(range(4), 4)  # Random initial state
    print("Initial state:", initial_state)
    print_board(initial_state)

    solution, cost = hill_climbing(initial_state)

    print("Final state:", solution)
    print("Final cost:", cost)
    print_board(solution)
