import tasks
import numpy as np
import pygame
import time

pygame.init()

board = np.zeros((40, 30))
disp = pygame.display.set_mode((400, 300))
# board[15][15] = 1
# board[15][16] = 2
# board[20][10] = -2

print(board.shape)

def get_color(value):
    if value == -2:
        return (180, 0, 0)
    elif value > 0:
        return (200, 200, 0)
    elif value == -1:
        return (150, 150, 150)


def draw_board():
    pygame.draw.rect(disp, (0, 0, 100), [0, 0, 400, 300])
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem != 0:
                pygame.draw.rect(disp, get_color(elem), [j * 10, i * 10, 10, 10])
    pygame.display.update()


direction = 'R'
game_over = False

while not game_over:
    tasks.garmaev_glavinskaya_tumene2(board)
    tasks.dashieva(board)
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'L'
            if event.key == pygame.K_UP:
                direction = 'U'
            if event.key == pygame.K_DOWN:
                direction = 'D'
            if event.key == pygame.K_RIGHT:
                direction = 'R'
    if direction == 'R':
        tasks.lavrentev_buldaev(board)
    if direction == 'D':
        tasks.garmaev_glavinskaya_tumene(board)
    if direction == 'L':
        tasks.dashieva_Ykehev_mansheev(board)
    if direction == 'U':
        tasks.Marbaev_Hagoev_Panteleev(board)

    draw_board()
    time.sleep(0.5)
pygame.quit()
quit()
