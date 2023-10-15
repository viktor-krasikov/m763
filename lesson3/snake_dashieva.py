import pygame
import numpy as np
import time
import tasks

pygame.init()

board = np.zeros((30, 30))

tasks.garmaev_glavinskaya_tumene2(board)

disp = pygame.display.set_mode((300, 300))


def get_color(value):
    if value == -2:
        return (180, 0, 0)
    elif value > 0:
        return (200, 200, 0)
    elif value == -1:
        return (150, 150, 150)
    return (0, 0, 100)


def draw_board():
    pygame.draw.rect(disp, (0, 0, 100), [0, 0, 300, 300])
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

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:  # Добавить проверку на то, можно ли поворачивать
            if event.key == pygame.K_LEFT:
                direction = 'L'
            if event.key == pygame.K_UP:
                direction = 'U'
            if event.key == pygame.K_DOWN:
                direction = 'D'
            if event.key == pygame.K_RIGHT:
                direction = 'R'
    if direction == 'R':
        board = tasks.lavrentev_buldaev(board)
    if direction == 'D':
        tasks.garmaev_glavinskaya_tumene(board)
    if direction == 'L':
        tasks.dashieva_Ykehev_mansheev(board)
    if direction == 'U':
        tasks.Marbaev_Hagoev_Panteleev(board)

    draw_board()

    time.sleep(0.1)

pygame.quit()
quit()
