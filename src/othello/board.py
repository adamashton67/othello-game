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
    return (0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE)

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
    return []

def find_all_flips(board, row, column, player):
    all_flips = []

    for row_change, column_change in DIRECTIONS:
        flips = find_flips_in_direction(board, row, column, player, row_change, column_change)
        all_flips.extend(flips)

    return all_flips

def is_valid_move(board, row, column, player):
    # if square is not empty
    if not is_empty_square(board, row, column):
        return False
    # if square is empty
    flips = find_all_flips(board, row, column, player)
    return len(flips) > 0

def get_valid_moves(board, player):
    valid_moves = []

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if is_valid_move(board, row, column, player):
                valid_moves.append((row, column))

    return valid_moves

def apply_move(board, row, column, player):
    # if not a valid move
    if not is_valid_move(board, row, column, player):
        return False
    # if valid move
    flips = find_all_flips(board, row, column, player)

    board[row][column] = player

    for flip_row, flip_column in flips:
        board[flip_row][flip_column] = player

    return True

def count_pieces(board):
    black_count = 0
    white_count = 0

    for row in board:
        for square in row:

            if square == BLACK:
                black_count += 1

            elif square == WHITE:
                white_count += 1

    return black_count, white_count

if __name__ == "__main__":
    board = create_starting_board()

    apply_move(board, 2, 3, BLACK)

    print(count_pieces(board))