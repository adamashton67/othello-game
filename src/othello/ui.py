

import pygame
from othello.game import Game
from othello.board import BLACK, WHITE

pygame.init()

BOARD_SIZE = 8
SQUARE_SIZE = 100

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Othello")

game = Game()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            row = mouse_y // SQUARE_SIZE
            column = mouse_x // SQUARE_SIZE

            game.make_move(row, column)

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
                40,
            )

    pygame.display.flip()

pygame.quit()