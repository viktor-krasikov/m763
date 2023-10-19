import time
import tasks
import numpy as np
import pygame

pygame.init()
board = np.zeros((40, 30))
disp = pygame.display.set_mode((400, 300))


def get_color(value):
    if value == -2:
        return (0, 128, 0)
    elif value > 0:
        return (200, 200, 0)
    elif value == -1:
        return (150, 150, 150)
    return (0, 0, 100)


def draw_board():
    pygame.draw.rect(disp, (0, 0, 100), [0, 0, 400, 300])
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem != 0:
                pygame.draw.rect(disp, get_color(elem), [j * 10, i * 10, 10, 10])
    pygame.display.update()


game_over = False
direction = 'R'
tasks.garmaev_glavinskaya_tumene2(board)
tasks.dashieva(board)
while not game_over:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'L'
            elif event.key == pygame.K_UP:
                direction = 'U'
            elif event.key == pygame.K_RIGHT:
                direction = 'R'
            elif event.key == pygame.K_DOWN:
                direction = 'D'
    if direction == 'R':
        board = tasks.lavrentev_buldaev(board)
    elif direction == 'D':
        tasks.garmaev_glavinskaya_tumene(board)
    elif direction == 'L':
        tasks.dashieva_Ykehev_mansheev(board)
    elif direction == 'U':
        tasks.Marbaev_Hagoev_Panteleev(board)

    time.sleep(0.1)
pygame.quit()
quit()
