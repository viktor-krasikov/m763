from tasks import SnakeData
import pygame
import time

sd = SnakeData(20, 20)
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
                sd.turn_left()
            if event.key == pygame.K_UP:
                sd.turn_up()
            if event.key == pygame.K_DOWN:
                sd.turn_down()
            if event.key == pygame.K_RIGHT:
                sd.turn_right()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
    sd.step()
    draw_board()
    time.sleep(0.2)
pygame.quit()
quit()
