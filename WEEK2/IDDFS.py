from collections import deque

print("Shrinanda Shivprasad Dinde")
print("1BM23CS324")
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def to_matrix(state_list):
    return [state_list[i:i+3] for i in range(0, 9, 3)]

def state_to_tuple(state):
    return tuple(num for row in state for num in row)

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def swap(state, x1, y1, x2, y2):
    new_state = [row[:] for row in state]
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def dls(current_state, goal_tuple, depth_limit, visited, parent, depth):
    """
    Depth-Limited Search:
    Returns True if goal found within depth_limit, else False.
    """
    current_tuple = state_to_tuple(current_state)
    if current_tuple == goal_tuple:
        return True

    if depth >= depth_limit:
        return False

    x, y = find_zero(current_state)

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny):
            new_state = swap(current_state, x, y, nx, ny)
            new_tuple = state_to_tuple(new_state)
            if new_tuple not in visited:
                visited.add(new_tuple)
                parent[new_tuple] = current_tuple
                found = dls(new_state, goal_tuple, depth_limit, visited, parent, depth + 1)
                if found:
                    return True
          
                visited.remove(new_tuple)
    return False

def iddfs(start_state, goal_state, max_depth=50):
    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)
    parent = {start_tuple: None}

    for depth_limit in range(max_depth + 1):
        visited = set([start_tuple])
        print(f"Searching with depth limit = {depth_limit} ...")
        found = dls(start_state, goal_tuple, depth_limit, visited, parent, 0)
        if found:
            print(f"\n Goal found at depth {depth_limit}!\n")
            print_path(parent, start_tuple, goal_tuple)
            return
    print(" No solution found within max depth.")

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

def print_state(state_tuple):
    for i in range(0, 9, 3):
        row = state_tuple[i:i+3]
        print(" ".join(str(x) if x != 0 else " " for x in row))

def read_state(prompt):
    while True:
        try:
            nums = list(map(int, input(prompt).strip().split()))
            if len(nums) != 9 or sorted(nums) != list(range(9)):
                raise ValueError
            return to_matrix(nums)
        except ValueError:
            print("Invalid input. Enter 9 numbers (0-8) with no duplicates.")

if __name__ == "__main__":
    print(" 8 Puzzle Solver using IDDFS\n")
    print("Enter the initial state (use 0 for the blank tile):")
    start_state = read_state("Initial (e.g., 1 2 3 4 5 6 7 8 0): ")

    print("\nEnter the goal state:")
    goal_state = read_state("Goal (e.g., 1 2 3 4 5 6 7 8 0): ")

    iddfs(start_state, goal_state, max_depth=30)
