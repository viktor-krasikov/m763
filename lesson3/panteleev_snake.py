from tkinter import *
from threading import Thread
import time
import random


def pressed(event):
    global moveDirection, isPause, isMoveDirectionCanChange

    key = event.keysym.lower() if event.char == ' ' else event.char.lower()

    if isPause and key == 'space':
        isPause = False
    elif not isPause and key == 'space':
        isPause = True

    if isMoveDirectionCanChange:
        if moveDirection in list(Directions)[:2] and key in list(Directions)[2:]:
            moveDirection = key
            isMoveDirectionCanChange = False
        elif moveDirection in list(Directions)[2:] and key in list(Directions)[:2]:
            moveDirection = key
            isMoveDirectionCanChange = False


def GenerateSnake(root, snake_map, snake):
    global moveDirection

    moveDirection = list(Directions)[random.randint(0, 3)]

    x = random.randint(3, len(snake_map) - 3)
    y = random.randint(3, len(snake_map[0]) - 3)

    snake_map[x][y] = 1
    snake_position = [x, y]
    snake.append(snake_position.copy())

    UpdatePosition(root, snake_position, map_colors.get('1'))


def Generate(root, snake_map, generate_type):
    x = random.randint(0, len(snake_map) - 1)
    y = random.randint(0, len(snake_map[0]) - 1)

    while snake_map[x][y] != 0:
        x = random.randint(0, len(snake_map) - 1)
        y = random.randint(0, len(snake_map[0]) - 1)

    snake_map[x][y] = generate_type
    position = [x, y]

    UpdatePosition(root, position, map_colors.get(str(generate_type)))


def SnakeMove(root, snake_map, snake, apples):
    global isAlive, isPause, isMoveDirectionCanChange

    isApple = False
    while isAlive:
        while isPause:
            pass

        time.sleep(0.1)

        snakeX, snakeY = snake[0][0], snake[0][1]

        snake_map[snakeX][snakeY] = 0
        prev_pos = [snakeX, snakeY]

        if moveDirection in list(Directions)[:2]:
            snakeY += eval(Directions.get(moveDirection))
        elif moveDirection in list(Directions)[2:]:
            snakeX += eval(Directions.get(moveDirection))

        if snakeX == len(snake_map) or snakeY == len(snake_map[0]) or snakeX == -1 or snakeY == -1:
            print('GAME OVER')
            isAlive = False
            break

        if snake_map[snakeX][snakeY] == -2:
            apples += 1
            root.title(f'Яблок собрано: {apples}')
            Generate(root, snake_map, -2)

            snake.insert(1, prev_pos)
            isApple = True

        if snake_map[snakeX][snakeY] == -1 or snake_map[snakeX][snakeY] == 2:
            print('GAME OVER')
            isAlive = False
            break

        snake_map[snakeX][snakeY] = 1
        snake[0] = [snakeX, snakeY]

        if len(snake) == 1:
            snake.append(prev_pos.copy())
        elif len(snake) == 2:
            snake[-1] = prev_pos.copy()

        if not isApple and len(snake) > 2:
            snake[1], snake[2:] = prev_pos, snake[1:-1]

        for i in snake:
            if i == snake[0]:
                UpdatePosition(root, i, map_colors.get('1'))
                snake_map[i[0]][i[1]] = 1
            elif len(snake) > 1 and i != snake[-1]:
                UpdatePosition(root, i, map_colors.get('2'))
                snake_map[i[0]][i[1]] = 2
            elif i == snake[-1]:
                UpdatePosition(root, i, map_colors.get('0'))
                snake_map[i[0]][i[1]] = 0

        isApple = False
        isMoveDirectionCanChange = True
    root.destroy()


def UpdatePosition(root, position, color, prev_pos=None, prev_pos_color=None):
    if prev_pos is not None or prev_pos_color is not None:
        root.children[f'({prev_pos[0]}:{prev_pos[1]})'].configure(bg=prev_pos_color)
    root.children[f'({position[0]}:{position[1]})'].configure(bg=color)


def Initialisation(root, snake_map, snake, apples, wall_count):
    root.attributes('-fullscreen', True)
    root.bind("<KeyPress>", pressed)
    root.title(f'Яблок собрано: {apples}')

    UpdateMap(snake_map)

    Generate(root, snake_map, -2)
    GenerateSnake(root, snake_map, snake)

    for _ in range(wall_count):
        Generate(root, snake_map, -1)

    snake_move_thread = Thread(target=SnakeMove, args=(root, snake_map, snake, apples))
    snake_move_thread.start()


def UpdateMap(snake_map):
    for i in range(len(snake_map)):
        for j in range(len(snake_map[i])):
            color = map_colors.get(str(snake_map[i][j]))

            btn = Button(bd=0, name=f"({i}:{j})", bg=color, width=2, height=1, state=DISABLED)  # bd=0 убирает края
            btn.grid(row=i, column=j)


def Snake(map_width, map_height, wall_count):
    root = Tk()

    apples, snake = 0, []
    snake_map = [[0 for _ in range(map_width)] for _ in range(map_height)]

    Initialisation(root, snake_map, snake, apples, wall_count)
    root.mainloop()


Directions = {'d': '+ 1',
              'a': '- 1',
              's': '+ 1',
              'w': '- 1'}
moveDirection = ''

isMoveDirectionCanChange = isPause = isAlive = True

if __name__ == '__main__':
    WIDTH = 40
    HEIGHT = 20

    APPLE = 'FF0000'
    WALL  = 'FFFFFF'
    GRASS = '00AA00'
    SNAKE = '000000'
    TAIL  = '444444'

    WALL_COUNT = 50

    global map_colors
    map_colors = {'-2': f'#{APPLE}' ,
                  '-1': f'#{WALL}'  ,
                  '0' :  f'#{GRASS}',
                  '1' :  f'#{SNAKE}',
                  '2' :  f'#{TAIL}' }
    Snake(WIDTH, HEIGHT, WALL_COUNT)
    isAlive = False
