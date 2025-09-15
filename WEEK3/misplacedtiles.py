from heapq import heappush, heappop
print("Shrinanda Dinde")
print("1BM23CS324")



GOAL_STATE = ((1, 2, 3),
              (8, 0, 4),
              (7, 6 , 5))

def misplaced_tiles(state):
    """Heuristic: count of misplaced tiles compared to the goal."""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                count += 1
    return count

def get_neighbors(state):
    """Generate possible moves by sliding the empty tile (0) up/down/left/right."""
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

def a_star(start_state):
    """A* search using misplaced tile heuristic."""
    open_set = []
    heappush(open_set, (misplaced_tiles(start_state), 0, start_state, []))  
    closed_set = set()

    while open_set:
        f, g, current, path = heappop(open_set)

        if current == GOAL_STATE:
            return path + [current]

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_set:
                continue
            new_g = g + 1
            new_f = new_g + misplaced_tiles(neighbor)
            heappush(open_set, (new_f, new_g, neighbor, path + [current]))

    return None  


start = ((2, 8, 3),
         (1, 6, 4),
         (7, 0, 5))

solution_path = a_star(start)
if solution_path:
    print(f"Solution found in {len(solution_path) - 1} moves:")
    for state in solution_path:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
