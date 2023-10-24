import pygame
import numpy as np
import time
import tasks
from matplotlib import pyplot

from lesson3.board import Board

pygame.init()

board = Board(30, 40)

# disp = pygame.display.set_mode((400, 300))
for _ in range(4):
    # tasks.create_vertical_wall(board)
    # tasks.create_horizontal_wall(board)
    board.create_vertical_wall()
    board.create_horizontal_wall()

# tasks.create_snake_if_need(board)
# tasks.create_food_if_need(board)
board.create_snake_if_need()
board.create_food_if_need()

# pyplot.ion()
# fig, ax = pyplot.subplots()
# axim = pyplot.imshow(board)
#
#
# def get_color(value):
#     if value == -2:
#         return (180, 0, 0)
#     elif value > 0:
#         return (200, 200, 0)
#     elif value == -1:
#         return (150, 150, 150)
#     return (0, 0, 100)
#
#
# def draw_board():
#     axim.set_data(board)
#     fig.canvas.flush_events()
#     pygame.draw.rect(disp, (0, 0, 100), [0, 0, 400, 300])
#     for i, row in enumerate(board):
#         for j, elem in enumerate(row):
#             if elem != 0:
#                 pygame.draw.rect(disp, get_color(elem), [j * 10, i * 10, 10, 10])
#
#     pygame.display.update()


direction = 'R'
game_over = False
while not game_over:
    # tasks.create_snake_if_need(board)
    # tasks.create_food_if_need(board)
    board.create_snake_if_need()
    board.create_food_if_need()

    # draw_board()
    board.draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT and not tasks.can_not_step_left(board):
            #     direction = 'L'
            # elif event.key == pygame.K_UP and not tasks.can_not_step_up(board):
            #     direction = 'U'
            # elif event.key == pygame.K_DOWN and not tasks.can_not_step_down(board):
            #     direction = 'D'
            # elif event.key == pygame.K_RIGHT and not tasks.can_not_step_right(board):
            #     direction = 'R'
            if event.key == pygame.K_LEFT and not board.can_not_step_left():
                direction = 'L'
            elif event.key == pygame.K_UP and not board.can_not_step_up():
                direction = 'U'
            elif event.key == pygame.K_DOWN and not board.can_not_step_down():
                direction = 'D'
            elif event.key == pygame.K_RIGHT and not board.can_not_step_right():
                direction = 'R'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    # if direction == 'R':
    #     tasks.step_right(board)
    # elif direction == 'D':
    #     tasks.step_down(board)
    # elif direction == 'L':
    #     tasks.step_left(board)
    # elif direction == 'U':
    #     tasks.step_up(board)
    if direction == 'R':
        board.step_right()
    elif direction == 'D':
        board.step_down()
    elif direction == 'L':
        board.step_left()
    elif direction == 'U':
        board.step_up()

    # draw_board()
    board.draw_board()
    time.sleep(0.05)

pygame.quit()
quit()
