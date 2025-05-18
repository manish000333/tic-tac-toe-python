def print_board(board):
    print("\nCurrent board:")
    print("-------------")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print("-------------")
    print()


def player_move(icon, board):
    player = "1" if icon == "X" else "2"
    print(f"Player {player} ({icon}) turn")

    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("⚠️  Please enter a number between 1 and 9.")
                continue
            if board[choice - 1] == " ":
                board[choice - 1] = icon
                break
            else:
                print("⛔ That space is already taken!")
        except ValueError:
            print("⚠️  Invalid input! Please enter a number.")


def is_victory(icon, board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == icon for i in condition) for condition in win_conditions)


def is_draw(board):
    return " " not in board


def print_result(winner, board):
    print_board(board)
    if winner == "X":
        print("🎉 Player 1 (X) Wins! Congratulations!")
    elif winner == "O":
        print("🎉 Player 2 (O) Wins! Congratulations!")
    else:
        print(" It's a draw!")


def reset_board():
    return [" " for _ in range(9)]


def play_game():
    board = reset_board()
    winner = None

    while True:
        print_board(board)
        player_move("X", board)
        if is_victory("X", board):
            winner = "X"
            break
        if is_draw(board):
            break

        print_board(board)
        player_move("O", board)
        if is_victory("O", board):
            winner = "O"
            break
        if is_draw(board):
            break

    print_result(winner, board)


def ask_play_again():
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response in ("yes", "no"):
            return response == "yes"
        print("⚠️  Please type 'yes' or 'no'.")


def main():
    print(" Welcome to Tic-Tac-Toe!")
    while True:
        play_game()
        if not ask_play_again():
            print("👋 Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
