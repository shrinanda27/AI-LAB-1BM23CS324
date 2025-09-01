from collections import deque
print("Shrinanda Shivprasad Dinde")
print("USN:1BM23CS324")

# Directions: Up, Down, Left, Right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Convert flat list to 2D list
def to_matrix(state_list):
    return [state_list[i:i+3] for i in range(0, 9, 3)]

# Convert 2D list to tuple
def state_to_tuple(state):
    return tuple(num for row in state for num in row)

# Find blank (0)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1

# Check bounds
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Swap tiles
def swap(state, x1, y1, x2, y2):
    new_state = [row[:] for row in state]
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

# DFS algorithm with visited set and optional depth limit
def dfs(start_state, goal_state, max_depth=50):
    visited = set()
    stack = [(start_state, 0)]  # (state, depth)
    parent = {}

    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)

    parent[start_tuple] = None
    visited.add(start_tuple)

    total_visited = 0

    while stack:
        current_state, depth = stack.pop()
        current_tuple = state_to_tuple(current_state)
        total_visited += 1

        if current_tuple == goal_tuple:
            print(f"\n Goal reached in {depth} moves.")
            print(f"Total states visited: {total_visited}\n")
            print_path(parent, start_tuple, goal_tuple)
            return

        if depth >= max_depth:
            continue  # Skip if depth limit is hit

        x, y = find_zero(current_state)

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                new_state = swap(current_state, x, y, nx, ny)
                new_tuple = state_to_tuple(new_state)
                if new_tuple not in visited:
                    visited.add(new_tuple)
                    parent[new_tuple] = current_tuple
                    stack.append((new_state, depth + 1))

    print(" No solution found within depth limit.")
    print(f" Total states visited: {total_visited}")

# Reconstruct and print solution path
def print_path(parent, start_tuple, goal_tuple):
    path = []
    current = goal_tuple
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    print(" Solution Path:")
    for state in path:
        print_state(state)
        print()

# Pretty print state
def print_state(state_tuple):
    for i in range(0, 9, 3):
        row = state_tuple[i:i+3]
        print(" ".join(str(x) if x != 0 else " " for x in row))

# Get and validate user input
def read_state(prompt):
    while True:
        try:
            nums = list(map(int, input(prompt).strip().split()))
            if len(nums) != 9 or sorted(nums) != list(range(9)):
                raise ValueError
            return to_matrix(nums)
        except ValueError:
            print("Invalid input. Enter 9 numbers (0-8) with no duplicates.")

# Main function
if __name__ == "__main__":
    print(" 8 Puzzle Solver using DFS (Uninformed Search)\n")
    print("Enter the initial state (use 0 for the blank tile):")
    start_state = read_state("Initial (e.g., 1 2 3 4 5 6 7 8 0): ")

    print("\nEnter the goal state:")
    goal_state = read_state("Goal (e.g., 1 2 3 4 5 6 7 8 0): ")

    # Optional: change max_depth for deeper searches
    dfs(start_state, goal_state, max_depth=50)
