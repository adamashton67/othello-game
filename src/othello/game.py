from othello.board import BLACK, WHITE, count_pieces, create_starting_board, apply_move, get_opponent, get_valid_moves

class Game:
    def __init__(self):
        self.board = create_starting_board()
        self.current_player = BLACK
        self.game_over = False

    def make_move(self, row, column):
        move_was_applied = apply_move(self.board, row, column, self.current_player)

        if not move_was_applied:
            return False

        next_player = get_opponent(self.current_player)

        if self.player_has_moves(next_player):
            self.current_player = next_player

        elif self.player_has_moves(self.current_player):
            pass

        else:
            self.game_over = True

        return True
    
    def player_has_moves(self, player):
        valid_moves = get_valid_moves(self.board, player)

        return len(valid_moves) > 0
    
    def update_game_over(self):
        if (
            not self.player_has_moves(BLACK)
            and not self.player_has_moves(WHITE)
        ):
            self.game_over = True

    def get_winner(self):
        black_count, white_count = count_pieces(self.board)

        if black_count > white_count:
            return BLACK

        elif white_count > black_count:
            return WHITE

        else:
            return "DRAW"
