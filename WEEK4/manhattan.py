import heapq
print("Shrinanda Dinde")
print("1BM23CS324")

def manhattan_distance(state, goal):
    """Calculate total Manhattan distance of all tiles from their goal positions."""
    goal_positions = {}
    for i in range(3):
        for j in range(3):
            goal_positions[goal[i][j]] = (i, j)

    dist = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = goal_positions[tile]
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def print_state(state):
    for row in state:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

def get_user_state(prompt):
    print(prompt)
    print("Enter 9 numbers separated by space, use 0 for blank tile (e.g. '2 8 3 1 6 4 7 0 5'):")
    while True:
        try:
            entries = list(map(int, input().strip().split()))
            if len(entries) != 9 or set(entries) != set(range(9)):
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Enter exactly 9 unique digits from 0 to 8 separated by spaces.")
    return tuple(tuple(entries[i*3:(i+1)*3]) for i in range(3))

def a_star_verbose(start_state, goal_state):
    open_set = []
    start_h = manhattan_distance(start_state, goal_state)
    heapq.heappush(open_set, (start_h, 0, start_state, []))  # (f, g, state, path)
   
    closed_set = set()
    step_counter = 0

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        step_counter += 1
       
        print(f"Step {step_counter}:")
        print(f"Current state with f = g + h = {g} + {f - g} = {f}")
        print_state(current)
       
        if current == goal_state:
            print("Goal reached!")
            return path + [current]

        if current in closed_set:
            print("This state has already been visited. Skipping.\n")
            continue
        closed_set.add(current)

        neighbors = get_neighbors(current)
        print(f"Expanding neighbors ({len(neighbors)}):")
        for n in neighbors:
            if n not in closed_set:
                h = manhattan_distance(n, goal_state)
                new_g = g + 1
                new_f = new_g + h
                print(f"Neighbor state with g={new_g}, h={h}, f={new_f}:")
                print_state(n)
                heapq.heappush(open_set, (new_f, new_g, n, path + [current]))
            else:
                print("Neighbor already visited, skipping.")
        print("-----\n")
    return None

if __name__ == "__main__":
    start = get_user_state("Enter the START state:")
    goal = get_user_state("Enter the GOAL state:")
    print("\nStarting A* search with Manhattan distance heuristic...\n")
    solution = a_star_verbose(start, goal)

    if solution:
        print(f"\nSolution found in {len(solution)-1} moves:\n")
        for step_num, step in enumerate(solution):
            print(f"Step {step_num}:")
            print_state(step)
    else:
        print("No solution found.")
