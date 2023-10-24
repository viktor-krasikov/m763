import pygame
import time
from tasks import SnakeData

snake_data = SnakeData(30, 40)

cell_size = 10

pygame.init()
disp = pygame.display.set_mode(
    (snake_data.cols_count * cell_size,
     snake_data.rows_count * cell_size)
)

for _ in range(4):
    snake_data.create_vertical_wall()
    snake_data.create_horizontal_wall()

snake_data.create_snake_if_need()
snake_data.create_food_if_need()


def get_color(value):
    if value == -2:
        return (180, 0, 0)
    elif value > 0:
        return (200, 200, 0)
    elif value == -1:
        return (150, 150, 150)
    return (0, 0, 100)


def draw_board():
    disp.fill((0, 0, 100))

    for i in range(snake_data.rows_count):
        for j in range(snake_data.cols_count):
            if snake_data[(i, j)] != 0:
                pygame.draw.rect(disp, get_color(snake_data[(i, j)]),
                                 [j * cell_size, i * cell_size, cell_size, cell_size])

    pygame.display.update()


game_over = False
while not game_over:
    snake_data.create_snake_if_need()
    snake_data.create_food_if_need()
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_data.turn_left()
            elif event.key == pygame.K_UP:
                snake_data.turn_up()
            elif event.key == pygame.K_DOWN:
                snake_data.turn_down()
            elif event.key == pygame.K_RIGHT:
                snake_data.turn_right()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    snake_data.step()
    draw_board()
    time.sleep(0.1)

pygame.quit()
