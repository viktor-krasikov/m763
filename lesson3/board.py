import numpy as np
import random
import pygame
import time
from matplotlib import pyplot


class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols))
        pyplot.ion()
        self.fig, self.ax = pyplot.subplots()
        self.axim = pyplot.imshow(self.board)
        self.disp = pygame.display.set_mode((cols * 10, rows * 10))

    def get_color(self, value):
        if value == -2:
            return (180, 0, 0)
        elif value > 0:
            return (200, 200, 0)
        elif value == -1:
            return (150, 150, 150)
        return (0, 0, 100)

    def draw_board(self):
        self.axim.set_data(self.board)
        self.fig.canvas.flush_events()
        pygame.draw.rect(self.disp, (0, 0, 100), [0, 0, self.cols * 10, self.rows * 10])
        for i, row in enumerate(self.board):
            for j, elem in enumerate(row):
                if elem != 0:
                    pygame.draw.rect(self.disp, self.get_color(elem), [j * 10, i * 10, 10, 10])

        pygame.display.update()

    def step_down(self):
        print("step_down(self) - авторы: Гармаев Чимит, Главинская Арина, Тумэнэ Алексей")
        maximum = 0
        stroka = len(self.board)
        stolb = len(self.board[0])
        for i in range(stroka):
            for j in range(stolb):
                if self.board[i][j] > maximum:
                    maximum = self.board[i][j]
                    x = i
                    y = j
        if x == stroka - 1 or (x + 1 < stroka and (self.board[x + 1][y] == -1 or self.board[x + 1][y] > 1)):
            for i in range(stroka):
                for j in range(stolb):
                    if self.board[i][j] > 0:
                        self.board[i][j] = 0
        elif x + 1 < stroka and self.board[x + 1][y] == 0:
            for i in range(stroka):
                for j in range(stolb):
                    if self.board[i][j] > 0:
                        self.board[i][j] = self.board[i][j] - 1
            self.board[x + 1][y] = maximum
        elif x + 1 < stroka and self.board[x + 1][y] == -2:
            self.board[x + 1][y] = maximum + 1

    def create_snake_if_need(self):
        print("step_down(self) - авторы: Гармаев Чимит, Главинская Арина, Тумэнэ Алексей")
        positive = False
        stroka = len(self.board)
        stolb = len(self.board[0])
        for i in range(stroka):
            for j in range(stolb):
                if self.board[i][j] > 0:
                    positive = True
                    return False
        if positive == False:
            for i in range(stroka):
                for j in range(stolb - 3):
                    if (self.board[i][j] == 0 and self.board[i][j + 1] == 0 and self.board[i][j + 2] == 0 and
                            self.board[i][j + 3] == 0):
                        self.board[i][j] = 1
                        self.board[i][j + 1] = 2
                        self.board[i][j + 2] = 3
                        return True
        return False

    def step_up(self):
        print("Имя функции: step_up; Авторы: Марбаев, Пантелеев, Хагоев")
        i1 = j1 = 0
        max_elem = self.board[i1][j1]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if max_elem < self.board[i][j]:
                    max_elem = self.board[i][j]
                    i1, j1 = i, j

        if i1 == 0:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] > 0:
                        self.board[i][j] = 0

        elif self.board[i1 - 1][j1] == -1 or self.board[i1 - 1][j1] > 1:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] > 0:
                        self.board[i][j] = 0

        elif self.board[i1 - 1][j1] == 0:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] > 0:
                        self.board[i][j] -= 1
                    if i == i1 - 1 and j == j1:
                        self.board[i][j] = max_elem

        else:
            if self.board[i1 - 1][j1] == -2:
                self.board[i1 - 1][j1] = max_elem + 1

    def can_not_step_up(self):
        print("Имя функции: can_not_step_up; Авторы: Марбаев, Пантелеев, Хагоев")
        i1 = j1 = 0
        max_elem = self.board[i1][j1]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if max_elem < self.board[i][j]:
                    max_elem = self.board[i][j]
                    i1, j1 = i, j

        return i1 != 0 and self.board[i1 - 1][j1] == max_elem - 1

    def step_right(self):
        print("step_right Lavr_Buld")
        (i, j) = np.unravel_index(np.argmax(self.board), self.board.shape)
        if self.board[i][j] in self.board[:, -1]:
            self.board[self.board > 0] = 0
        elif self.board[i][j + 1] == -1 or self.board[i][j + 1] > 1:
            self.board[self.board > 0] = 0
        elif (self.board[i][j + 1]) == 0:
            self.board[i][j + 1] = self.board[i][j]
            self.board[self.board > 0] -= 1
            self.board[i][j + 1] += 1
        elif (self.board[i][j + 1]) == -2:
            self.board[i][j + 1] = self.board[i][j] + 1
        # return matr.tolist()

    def step_left(self):
        print("step_left Dashieva")
        maxElem, xMaxElem, yMaxElem = self.board[0][0], 0, 0

        for i, row in enumerate(self.board):
            for j, elem in enumerate(row):
                if elem > maxElem:
                    maxElem = elem
                    xMaxElem = i
                    yMaxElem = j

        leftElem = self.board[xMaxElem][yMaxElem - 1]

        if maxElem == self.board[xMaxElem][0] or leftElem == -1 or leftElem > 1:
            for i, row in enumerate(self.board):
                for j, elem in enumerate(row):
                    if elem > 0:
                        self.board[i][j] = 0

        elif leftElem == 0:
            for i, row in enumerate(self.board):
                for j, elem in enumerate(row):
                    if elem > 0:
                        self.board[i][j] -= 1
            self.board[xMaxElem][yMaxElem - 1] = maxElem

        elif leftElem == -2:
            self.board[xMaxElem][yMaxElem - 1] = maxElem + 1

    def can_not_step_down(self):
        print("can_not_step_down Mordvin Nikolaeva")
        max = self.board[0][0]
        xmax = 0
        ymax = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (max <= self.board[i][j]):
                    max = self.board[i][j]
                    xmax = i
                    ymax = j
        if (self.board[xmax + 1][ymax] == max - 1):
            return True
        else:
            return False

    def create_food_if_need(self):
        print("create_food_if_need Dashieva")
        isMinusTwo = False
        x, y = [], []

        for i, row in enumerate(self.board):
            for j, elem in enumerate(row):
                if elem == -2:
                    isMinusTwo = True
                if elem == 0:
                    x.append(i)
                    y.append(j)

        if isMinusTwo == False and len(x) > 0:
            rand = random.randint(0, len(x) - 1)
            self.board[x[rand]][y[rand]] = -2

    def can_not_step_right(self):
        print("can_not_step_right_Lavr")
        (i, j) = np.unravel_index(np.argmax(self.board), self.board.shape)
        if self.board[i][j] in self.board[:, -1]:
            return False
        elif self.board[i][j + 1] == self.board[i][j] - 1:
            return True
        else:
            return False

    def can_not_step_left(self):
        print("can_not_step_left(self) - авторы: Гармаев Чимит, Главинская Арина, Тумэнэ Алексей")
        i1 = j1 = 0
        max_elem = self.board[i1][j1]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if max_elem < self.board[i][j]:
                    max_elem = self.board[i][j]
                    i1, j1 = i, j

        return i1 != 0 and self.board[i1][j1 - 1] == max_elem - 1

    def create_vertical_wall(self):
        print("create_vertical_wall Dashieva")
        randCol = random.randint(0, len(self.board[0]) - 1)
        randRow = random.randint(0, len(self.board) - 5)

        for k in range(5):
            self.board[randRow + k][randCol] = -1

    def create_horizontal_wall(self):
        print("create_horizontal_wall_Lavr_Marb_Hag")
        y = random.randint(0, len(self.board) - 1)
        x = random.randint(0, len(self.board[0]) - 7)
        for i in range(0, 7):
            self.board[y][x + i] = -1
