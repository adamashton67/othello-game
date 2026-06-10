from othello.board import BLACK, WHITE, create_starting_board, apply_move, get_opponent


class Game:
    def __init__(self):
        self.board = create_starting_board()
        self.current_player = BLACK

    def make_move(self, row, column):
        move_was_applied = apply_move(self.board, row, column, self.current_player)

        if not move_was_applied:
            return False

        self.current_player = get_opponent(self.current_player)

        return True
    
if __name__ == "__main__":
    game = Game()

    print(game.current_player)

    print(game.make_move(2, 3))
    print(game.current_player)