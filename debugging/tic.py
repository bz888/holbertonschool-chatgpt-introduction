#!/usr/bin/python3
"""
A simple command-line Tic-Tac-Toe game.

Two players take turns placing X and O on a 3x3 board.
The first player to get three marks in a row, column, or diagonal wins.
If the board fills up with no winner, the game ends in a draw.
"""


def print_board(board):
    """
    Print the current Tic-Tac-Toe board.

    Args:
        board (list): A 3x3 list representing the game board.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))

        if i < len(board) - 1:
            print("-" * 9)


def check_winner(board):
    """
    Check whether the current board has a winner.

    Args:
        board (list): A 3x3 list representing the game board.

    Returns:
        bool: True if a player has won, otherwise False.
    """
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    for col in range(3):
        if (
            board[0][col] != " "
            and board[0][col] == board[1][col] == board[2][col]
        ):
            return True

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def board_full(board):
    """
    Check whether the board is full.

    Args:
        board (list): A 3x3 list representing the game board.

    Returns:
        bool: True if there are no empty spaces, otherwise False.
    """
    for row in board:
        if " " in row:
            return False

    return True


def get_move(player):
    """
    Get a valid row and column from the current player.

    Args:
        player (str): The current player, either X or O.

    Returns:
        tuple: The row and column chosen by the player.
    """
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move. Row and column must be between 0 and 2.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")

        except EOFError:
            print()
            raise


def switch_player(player):
    """
    Switch from one player to the other.

    Args:
        player (str): The current player.

    Returns:
        str: The next player.
    """
    if player == "X":
        return "O"

    return "X"


def tic_tac_toe():
    """
    Run the Tic-Tac-Toe game loop.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row, col = get_move(player)
        except EOFError:
            break

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if board_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        player = switch_player(player)


if __name__ == "__main__":
    tic_tac_toe()