from tasks import SnakeData
import pygame
import time
from keras.models import load_model
import numpy as np
import autokeras
model = load_model('snake_ns.h5',compile=False)
model.compile() #Paste it here

sd = SnakeData(10, 10)
cell_size = 20
pygame.init()
disp = pygame.display.set_mode((sd.cols_count * cell_size, sd.rows_count * cell_size))


def get_color(value):
    if value == -2:
        return 180, 0, 0
    elif value > 0:
        return 200, 200, 0
    elif value == -1:
        return 150, 150, 150


def draw_board():
    disp.fill((0, 0, 100))
    for i in range(sd.rows_count):
        for j in range(sd.cols_count):
            if sd[(i, j)] != 0:
                pygame.draw.rect(disp, get_color(sd[(i, j)]),
                                 [j * cell_size, i * cell_size, cell_size, cell_size])

    pygame.display.update()


direction = 'R'
game_over = False

# for _ in range(4):
#     sd.create_horizontal_wall()
#     sd.create_vertical_wall()

sd.create_snake_if_need()
sd.create_food_if_need()

# while not game_over:
#     sd.create_snake_if_need()
#     sd.create_food_if_need()
#     draw_board()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 sd.turn_left()
#             elif event.key == pygame.K_UP:
#                 sd.turn_up()
#             elif event.key == pygame.K_DOWN:
#                 sd.turn_down()
#             elif event.key == pygame.K_RIGHT:
#                 sd.turn_right()
#             elif event.key == pygame.K_ESCAPE:
#                 pygame.quit()
#                 quit()
#     sd.step()
#     draw_board()
#     time.sleep(0.5)

while not game_over:
    sd.create_snake_if_need()
    sd.create_food_if_need()
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pred = model.predict(sd.get_matr())
    print(sd.get_matr())
    print(np.argmax(pred))
    if np.argmax(pred) == 2:
        sd.turn_left()
    if np.argmax(pred) == 3:
        sd.turn_up()
    if np.argmax(pred) == 1:
        sd.turn_down()
    if np.argmax(pred) == 0:
        sd.turn_right()
    sd.step()
    draw_board()
    time.sleep(1)
pygame.quit()
quit()
