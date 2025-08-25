def vacuum_cleaner():
    try:
        state_A = int(input("Enter state of A (0 for clean, 1 for dirty): "))
        state_B = int(input("Enter state of B (0 for clean, 1 for dirty): "))
        location = input("Enter location (A or B): ").upper()

        if state_A not in (0, 1) or state_B not in (0, 1) or location not in ('A', 'B'):
            raise ValueError("Invalid input! Please enter correctly.")
    except ValueError as e:
        print("Error:", e)
        return

    environment = {'A': state_A, 'B': state_B}
    cost = 0

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

        if environment['A'] == 0 and environment['B'] == 0:
            print("\nBoth rooms are clean. Turning vacuum off.")
            break

        move = input("Enter action (LEFT / RIGHT / STAY / EXIT): ").upper()

        if move == "LEFT":
            if location == 'A':
                print("Already at A. Can't move LEFT.")
            else:
                location = 'A'
                print("Moving vacuum LEFT to A.")
            cost += 1

        elif move == "RIGHT":
            if location == 'B':
                print("Already at B. Can't move RIGHT.")
            else:
                location = 'B'
                print("Moving vacuum RIGHT to B.")
            cost += 1

        elif move == "STAY":
            print("Staying in the same room.")

        elif move == "EXIT":
            print("Exiting manually.")
            break

        else:
            print("Invalid action! Please enter LEFT, RIGHT, STAY, or EXIT.")

    print("\nFinal Environment:", environment)
    print("Total Cost:", cost)

vacuum_cleaner()
