def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def play_game(board):
    current_player = 'X' if sum(row.count('X') for row in board) <= sum(row.count('O') for row in board) else 'O'
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers 0–2.")
            continue
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid position. Try again.")
            continue
        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


initial_board = [
    ['X', 'O', 'X'],
    [' ', 'O', ' '],
    [' ', ' ', ' ']
]

for i in range(3):
    for j in range(3):
        if initial_board[i][j] not in ['X', 'O']:
            initial_board[i][j] = ' '

play_game(initial_board)
