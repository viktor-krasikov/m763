import pygame
import time
from tasks import SnakeData

pygame.init()

disp = pygame.display.set_mode((400, 300))

snake_data = SnakeData(30, 40)


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
    for i, row in enumerate(snake_data.board):
        for j, elem in enumerate(row):
            if elem != 0:
                pygame.draw.rect(disp, get_color(elem), [j * 10, i * 10, 10, 10])

    pygame.display.update()


for i in range(4):
    snake_data.create_horizontal_wall()
    snake_data.create_vertical_wall()

snake_data.create_snake_if_need()
snake_data.create_food_if_need()

direction = 'R'
game_over = False
while not game_over:
    snake_data.create_food_if_need()
    draw_board()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:  # Добавить проверку на то, можно ли поворачивать
            if event.key == pygame.K_LEFT and not snake_data.can_not_step_left():
                direction = 'L'
            elif event.key == pygame.K_UP and not snake_data.can_not_step_up():
                direction = 'U'
            elif event.key == pygame.K_RIGHT and not snake_data.can_not_step_right():
                direction = 'R'
            elif event.key == pygame.K_DOWN and not snake_data.can_not_step_down():
                direction = 'D'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if direction == 'R':
        snake_data.step_right()
    if direction == 'D':
        snake_data.step_down()
    if direction == 'L':
        snake_data.step_left()
    if direction == 'U':
        snake_data.step_up()

    draw_board()

    time.sleep(0.1)

pygame.quit()
quit()
