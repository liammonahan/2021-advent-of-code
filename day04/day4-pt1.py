import sys

from utils import *

boards = readgroups('input.txt')
draws = boards.pop(0)[0]
draws = to_ints(draws.split(','))

boards = [[[int(cell) for cell in row.split()] for row in board] for board in boards]

MARKED = None


def mark_number(number, board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == number:
                board[i][j] = MARKED
    return board


def get_columns(board):
    return zip(*board)


def row_wins(board):
    return [all(cell == MARKED for cell in row) for row in board]


def column_wins(board):
    return [all(cell == MARKED for cell in column) for column in get_columns(board)]


def winning_board():
    for board in boards:
        if any(row_wins(board)) or any(column_wins(board)):
            return board
    return None


def board_score(board):
    return sum(sum(cell for cell in row if cell) for row in board)


def print_board(board):
    for row in board:
        print(' '.join(str(c).rjust(2) if c else ' X' for c in row))


def print_boards():
    for board in boards:
        print_board(board)
        print()


for draw in draws:
    for i, board in enumerate(boards):
        mark_number(draw, board)
    winner = winning_board()
    if winner:
        print(board_score(winner) * draw)
        sys.exit()
