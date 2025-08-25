def vacuum_cleaner_4_rooms_grid():
   
    try:
        state_A = int(input("Enter state of A (0 for clean, 1 for dirty): "))
        state_B = int(input("Enter state of B (0 for clean, 1 for dirty): "))
        state_C = int(input("Enter state of C (0 for clean, 1 for dirty): "))
        state_D = int(input("Enter state of D (0 for clean, 1 for dirty): "))
        location = input("Enter location (A, B, C, D): ").upper()

        if (state_A not in (0, 1) or state_B not in (0, 1) or 
            state_C not in (0, 1) or state_D not in (0, 1) or
            location not in ('A', 'B', 'C', 'D')):
            raise ValueError("Invalid input! Enter 0 or 1 for states, and location as A/B/C/D.")
    except ValueError as e:
        print("Error:", e)
        return

 
    environment = {'A': state_A, 'B': state_B, 'C': state_C, 'D': state_D}
    cost = 0

  
    moves = {
        'A': {'RIGHT': 'B', 'DOWN': 'C'},
        'B': {'LEFT': 'A', 'DOWN': 'D'},
        'C': {'UP': 'A', 'RIGHT': 'D'},
        'D': {'UP': 'B', 'LEFT': 'C'}
    }

    while True:
        print("\nCurrent Environment:", environment)
        print("Vacuum is at Room", location)

  
        if environment[location] == 1:
            print(f"{location} is dirty. Cleaning...")
            environment[location] = 0
            cost += 1
            print(f"{location} is now clean.")
        else:
            print(f"{location} is already clean.")

        if all(state == 0 for state in environment.values()):
            print("\nAll rooms are clean. Turning vacuum off.")
            break

        move = input("Enter action (LEFT / RIGHT / UP / DOWN / STAY / EXIT): ").upper()

        if move in moves[location]:
            new_location = moves[location][move]
            print(f"Moving vacuum {move} to {new_location}.")
            location = new_location
            cost += 1

        elif move == "STAY":
            print("Staying in the same room. (No cost)")

        elif move == "EXIT":
            print("Exiting manually.")
            break

        else:
            print("Invalid move from this room! Try again.")

    print("\nFinal Environment:", environment)
    print("Total Cost:", cost)

vacuum_cleaner_4_rooms_grid()
