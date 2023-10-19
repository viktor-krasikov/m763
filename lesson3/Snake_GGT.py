import time
import tasks
import numpy as np
import pygame

pygame.init()
board = np.zeros((30, 40))
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
while not game_over:
    tasks.create_snake_if_need(board)
    tasks.create_food_if_need(board)
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
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
    elif direction == 'D':
        tasks.step_down(board)
    elif direction == 'L':
        tasks.step_left(board)
    elif direction == 'U':
        tasks.step_up(board)

    time.sleep(0.1)
pygame.quit()
quit()
