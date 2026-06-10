EMPTY = "."
BLACK = "B"
WHITE = "W"
BOARD_SIZE = 8

def create_starting_board():
    board = [[EMPTY for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE

    return board

def print_board(board):
    for row in board:
        print(" ".join(row))


def is_empty_square(board, row, column):
    return board[row][column] == EMPTY

if __name__ == "__main__":
    board = create_starting_board()

    print_board(board)

    print()
    print(is_empty_square(board, 0, 0))
    print(is_empty_square(board, 3, 3))
