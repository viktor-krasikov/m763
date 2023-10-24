import pygame
import numpy as np
import time
import tasks

pygame.init()
board = np.zeros((30, 40))
disp = pygame.display.set_mode((400, 300))


def get_color(value):
    if value == -2:
        return (180, 0, 0)
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

for i in range(4):
    tasks.create_horizontal_wall(board)
    tasks.create_vertical_wall(board)

tasks.create_snake_if_need(board)
tasks.create_food_if_need(board)

direction = 'R'
game_over = False
while not game_over:
    tasks.create_food_if_need(board)
    draw_board()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:  # Добавить проверку на то, можно ли поворачивать
            if event.key == pygame.K_LEFT and not tasks.can_not_step_left(board):
                direction = 'L'
            elif event.key == pygame.K_UP and not tasks.can_not_step_up(board):
                direction = 'U'
            elif event.key == pygame.K_RIGHT and not tasks.can_not_step_right(board):
                direction = 'R'
            elif event.key == pygame.K_DOWN and not tasks.can_not_step_down(board):
                direction = 'D'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if direction == 'R':
        tasks.step_right(board)
    if direction == 'D':
        tasks.step_down(board)
    if direction == 'L':
        tasks.step_left(board)
    if direction == 'U':
        tasks.step_up(board)

    draw_board()

    time.sleep(0.1)

pygame.quit()
quit()
