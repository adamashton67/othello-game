EMPTY = "."
BLACK = "B"
WHITE = "W"
BOARD_SIZE = 8

DIRECTIONS = [
    (-1, 0),   # up
    (1, 0),    # down
    (0, -1),   # left
    (0, 1),    # right
    (-1, -1),  # up left
    (-1, 1),   # up right
    (1, -1),   # down left
    (1, 1),    # down right
]

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

def is_on_board(row, column):
    return (
        0 <= row < BOARD_SIZE
        and
        0 <= column < BOARD_SIZE
    )

def get_opponent(player):
    if player == BLACK:
        return WHITE
    else:
        return BLACK
    
def find_flips_in_direction(board, row, column, player, row_change, column_change):
    opponent = get_opponent(player)

    row += row_change
    column += column_change

    flips = []
    while is_on_board(row, column):
        current_square = board[row][column]
        if current_square == opponent:
            flips.append((row, column))
            row += row_change
            column += column_change
            continue 
        elif current_square == player:
            return flips
        elif current_square == EMPTY:
            return []
        else:
            return []


if __name__ == "__main__":
    board = create_starting_board()

    print_board(board)

    print()
    print(is_empty_square(board, 0, 0))
    print(is_empty_square(board, 3, 3))
    print()
    print(is_on_board(0, 0))
    print(is_on_board(7, 7))
    print(is_on_board(8, 0))
    print(is_on_board(-1, 3))
