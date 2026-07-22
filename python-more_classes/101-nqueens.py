#!/usr/bin/python3
"""Solves the N queens puzzle.

Usage: nqueens N

Prints every possible solution to placing N non-attacking queens on
an N x N chessboard, one solution per line, formatted as a list of
[row, column] pairs.
"""
import sys


def print_usage_and_exit():
    """Print the usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def parse_n(args):
    """Parse and validate the N argument.

    Args:
        args (list): The command-line arguments (excluding the script name).

    Returns:
        int: The validated board size N.
    """
    if len(args) != 1:
        print_usage_and_exit()

    try:
        n = int(args[0])
    except (ValueError, TypeError):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def solve(n):
    """Find and print every solution to the N queens puzzle.

    Args:
        n (int): The size of the board (N x N) and number of queens.
    """
    columns = set()
    diagonals = set()
    anti_diagonals = set()
    board = []

    def backtrack(row):
        if row == n:
            print(board_to_solution(board))
            return
        for col in range(n):
            if (col in columns or
                    (row - col) in diagonals or
                    (row + col) in anti_diagonals):
                continue
            columns.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)
            board.append(col)

            backtrack(row + 1)

            columns.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)
            board.pop()

    def board_to_solution(board):
        return str([[row, col] for row, col in enumerate(board)])

    backtrack(0)


if __name__ == "__main__":
    n = parse_n(sys.argv[1:])
    solve(n)
