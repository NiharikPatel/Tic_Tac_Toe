from colorama import init, Fore

init(autoreset=True)

def print_board(board):
    for i, row in enumerate(board):
        row_str = " | ".join(row)
        print(Fore.GREEN + row_str)
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print(Fore.CYAN + "Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        print(Fore.YELLOW + f"Player {current_player}'s turn")
        try:
            row = int(input("Enter the row (1, 2, 3): "))
            col = int(input("Enter the column (1, 2, 3): "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            continue

        # Convert 1-based input to 0-based index
        row -= 1
        col -= 1

        if row < 0 or row > 2 or col < 0 or col > 2:
            print(Fore.RED + "Invalid input. Row and column should be between 1 and 3.")
            continue

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print(Fore.RED + "That cell is already occupied. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(Fore.GREEN + f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print(Fore.YELLOW + "It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
