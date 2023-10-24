from tasks import SnakeData
import pygame
import time

pygame.init()

disp = pygame.display.set_mode((400, 300))

sd = SnakeData(30, 40)


def get_color(value):
    if value == -2:
        return (180, 0, 0)
    elif value > 0:
        return (200, 200, 0)
    elif value == -1:
        return (150, 150, 150)


def draw_board():
    pygame.draw.rect(disp, (0, 0, 100), [0, 0, 400, 300])
    for i, row in enumerate(sd.matr):
        for j, elem in enumerate(row):
            if elem != 0:
                pygame.draw.rect(disp, get_color(elem), [j * 10, i * 10, 10, 10])
    pygame.display.update()


direction = 'R'
game_over = False

for _ in range(4):
    sd.create_horizontal_wall()
    sd.create_vertical_wall()

sd.create_snake_if_need()
sd.create_food_if_need()

while not game_over:
    sd.create_snake_if_need()
    sd.create_food_if_need()
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
        sd.step_right()
    if direction == 'D':
        sd.step_down()
    if direction == 'L':
        sd.step_left()
    if direction == 'U':
        sd.step_up()

    draw_board()
    time.sleep(0.2)
pygame.quit()
quit()
