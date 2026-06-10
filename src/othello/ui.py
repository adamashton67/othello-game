import pygame
from othello.game import Game
from othello.board import BLACK, WHITE, count_pieces

pygame.init()
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 48)

BOARD_SIZE = 8
SQUARE_SIZE = 80
BOARD_PIXELS = BOARD_SIZE * SQUARE_SIZE
INFO_PANEL_HEIGHT = 100
WINDOW_WIDTH = BOARD_PIXELS
WINDOW_HEIGHT = BOARD_PIXELS + INFO_PANEL_HEIGHT

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Othello")

game = Game()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
            mouse_x, mouse_y = event.pos

            if mouse_y < BOARD_PIXELS:
                row = mouse_y // SQUARE_SIZE
                column = mouse_x // SQUARE_SIZE

                game.make_move(row, column)
                game.update_game_over()

    screen.fill((0, 128, 0))

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            rect = pygame.Rect(
                column * SQUARE_SIZE,
                row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE,
            )

            pygame.draw.rect(
                screen,
                (0, 0, 0),
                rect,
                1,
            )

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            square = game.board[row][column]

            if square == BLACK:
                colour = (0, 0, 0)

            elif square == WHITE:
                colour = (255, 255, 255)

            else:
                continue

            centre_x = column * SQUARE_SIZE + SQUARE_SIZE // 2
            centre_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

            pygame.draw.circle(
                screen,
                colour,
                (centre_x, centre_y),
                32,
            )

    pygame.draw.rect(
        screen,
        (200, 200, 200),
        pygame.Rect(0, BOARD_PIXELS, WINDOW_WIDTH, INFO_PANEL_HEIGHT),
    )

    black_count, white_count = count_pieces(game.board)

    if game.current_player == BLACK:
        current_player_name = "Black"
    else:
        current_player_name = "White"

    if game.game_over:
        winner = game.get_winner()

        if winner == BLACK:
            winner_text = "Winner: Black"
        elif winner == WHITE:
            winner_text = "Winner: White"
        else:
            winner_text = "Draw"

        status_text = large_font.render(
            "Game Over",
            True,
            (0, 0, 0),
        )

        winner_surface = font.render(
            winner_text,
            True,
            (0, 0, 0),
        )

        final_score_text = font.render(
            f"Final Score - Black: {black_count}  White: {white_count}",
            True,
            (0, 0, 0),
        )

        screen.blit(status_text, (20, BOARD_PIXELS + 5))
        screen.blit(winner_surface, (20, BOARD_PIXELS + 45))
        screen.blit(final_score_text, (20, BOARD_PIXELS + 72))

    else:
        turn_text = font.render(
            f"Turn: {current_player_name}",
            True,
            (0, 0, 0),
        )

        score_text = font.render(
            f"Black: {black_count}  White: {white_count}",
            True,
            (0, 0, 0),
        )

        screen.blit(turn_text, (20, BOARD_PIXELS + 15))
        screen.blit(score_text, (20, BOARD_PIXELS + 55))

    pygame.display.flip()

pygame.quit()