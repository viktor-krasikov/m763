import random
import numpy as np


class SnakeData:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__matr = np.zeros((rows, cols))
        self.__direction = 'R'

    def get_matr(self):
        return self.__matr

    @property
    def rows_count(self):
        return self.__rows

    @property
    def cols_count(self):
        return self.__cols

    def __getitem__(self, indexes):
        return self.__matr[indexes[0]][indexes[1]]

    def __step_down(self):
        matr = self.__matr
        print("step_down(matr) - авторы: Гармаев Чимит, Главинская Арина, Тумэнэ Алексей")
        maximum = 0
        stroka = len(matr)
        stolb = len(matr[0])
        for i in range(stroka):
            for j in range(stolb):
                if matr[i][j] > maximum:
                    maximum = matr[i][j]
                    x = i
                    y = j
        if x == stroka - 1 or (x + 1 < stroka and (matr[x + 1][y] == -1 or matr[x + 1][y] > 1)):
            for i in range(stroka):
                for j in range(stolb):
                    if matr[i][j] > 0:
                        matr[i][j] = 0
        elif x + 1 < stroka and matr[x + 1][y] == 0:
            for i in range(stroka):
                for j in range(stolb):
                    if matr[i][j] > 0:
                        matr[i][j] = matr[i][j] - 1
            matr[x + 1][y] = maximum
        elif x + 1 < stroka and matr[x + 1][y] == -2:
            matr[x + 1][y] = maximum + 1

    def create_snake_if_need(self):
        matr = self.__matr
        print("step_down(matr) - авторы: Гармаев Чимит, Главинская Арина, Тумэнэ Алексей")
        positive = False
        stroka = len(matr)
        stolb = len(matr[0])
        for i in range(stroka):
            for j in range(stolb):
                if matr[i][j] > 0:
                    positive = True
                    return False
        if positive == False:
            for i in range(stroka):
                for j in range(stolb - 3):
                    if (matr[i][j] == 0 and matr[i][j + 1] == 0 and matr[i][j + 2] == 0 and matr[i][j + 3] == 0):
                        matr[i][j] = 1
                        matr[i][j + 1] = 2
                        matr[i][j + 2] = 3
                        return True
        return False

    def __step_up(self):
        A = self.__matr
        print("Имя функции: step_up; Авторы: Марбаев, Пантелеев, Хагоев")
        i1 = j1 = 0
        max_elem = A[i1][j1]

        for i in range(len(A)):
            for j in range(len(A[i])):
                if max_elem < A[i][j]:
                    max_elem = A[i][j]
                    i1, j1 = i, j

        if i1 == 0:
            for i in range(len(A)):
                for j in range(len(A[i])):
                    if A[i][j] > 0:
                        A[i][j] = 0

        elif A[i1 - 1][j1] == -1 or A[i1 - 1][j1] > 1:
            for i in range(len(A)):
                for j in range(len(A[i])):
                    if A[i][j] > 0:
                        A[i][j] = 0

        elif A[i1 - 1][j1] == 0:
            for i in range(len(A)):
                for j in range(len(A[i])):
                    if A[i][j] > 0:
                        A[i][j] -= 1
                    if i == i1 - 1 and j == j1:
                        A[i][j] = max_elem

        else:
            if A[i1 - 1][j1] == -2:
                A[i1 - 1][j1] = max_elem + 1

    def __can_not_step_up(self):
        A = self.__matr
        print("Имя функции: can_not_step_up; Авторы: Марбаев, Пантелеев, Хагоев")
        i1 = j1 = 0
        max_elem = A[i1][j1]

        for i in range(len(A)):
            for j in range(len(A[i])):
                if max_elem < A[i][j]:
                    max_elem = A[i][j]
                    i1, j1 = i, j

        return i1 != 0 and A[i1 - 1][j1] == max_elem - 1

    def __step_right(self):
        matr = self.__matr
        print("step_right Lavr_Buld")
        (i, j) = np.unravel_index(np.argmax(matr), matr.shape)
        if matr[i][j] in matr[:, -1]:
            matr[matr > 0] = 0
        elif matr[i][j + 1] == -1 or matr[i][j + 1] > 1:
            matr[matr > 0] = 0
        elif (matr[i][j + 1]) == 0:
            matr[i][j + 1] = matr[i][j]
            matr[matr > 0] -= 1
            matr[i][j + 1] += 1
        elif (matr[i][j + 1]) == -2:
            matr[i][j + 1] = matr[i][j] + 1
        # return matr.tolist()

    def __step_left(self):
        matr = self.__matr
        print("step_left Dashieva")
        maxElem, xMaxElem, yMaxElem = matr[0][0], 0, 0

        for i, row in enumerate(matr):
            for j, elem in enumerate(row):
                if elem > maxElem:
                    maxElem = elem
                    xMaxElem = i
                    yMaxElem = j

        leftElem = matr[xMaxElem][yMaxElem - 1]

        if maxElem == matr[xMaxElem][0] or leftElem == -1 or leftElem > 1:
            for i, row in enumerate(matr):
                for j, elem in enumerate(row):
                    if elem > 0:
                        matr[i][j] = 0

        elif leftElem == 0:
            for i, row in enumerate(matr):
                for j, elem in enumerate(row):
                    if elem > 0:
                        matr[i][j] -= 1
            matr[xMaxElem][yMaxElem - 1] = maxElem

        elif leftElem == -2:
            matr[xMaxElem][yMaxElem - 1] = maxElem + 1

    def __can_not_step_down(self):
        matr = self.__matr
        print("can_not_step_down Mordvin Nikolaeva")
        max = matr[0][0]
        xmax = 0
        ymax = 0
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                if max <= matr[i][j]:
                    max = matr[i][j]
                    xmax = i
                    ymax = j
        if (matr[xmax + 1][ymax] == max - 1):
            return True
        else:
            return False

    def create_food_if_need(self):
        matr = self.__matr
        print("create_food_if_need Dashieva")
        isMinusTwo = False
        x, y = [], []

        for i, row in enumerate(matr):
            for j, elem in enumerate(row):
                if elem == -2:
                    isMinusTwo = True
                if elem == 0:
                    x.append(i)
                    y.append(j)

        if isMinusTwo == False and len(x) > 0:
            rand = random.randint(0, len(x) - 1)
            matr[x[rand]][y[rand]] = -2

    def __can_not_step_right(self):
        matr = self.__matr
        print("can_not_step_right_Lavr")
        (i, j) = np.unravel_index(np.argmax(matr), matr.shape)
        if matr[i][j] in matr[:, -1]:
            return False
        elif matr[i][j + 1] == matr[i][j] - 1:
            return True
        else:
            return False

    def __can_not_step_left(self):
        A = self.__matr
        print("can_not_step_left(matr) - авторы: Гармаев Чимит, Главинская Арина, Тумэнэ Алексей")
        i1 = j1 = 0
        max_elem = A[i1][j1]

        for i in range(len(A)):
            for j in range(len(A[i])):
                if max_elem < A[i][j]:
                    max_elem = A[i][j]
                    i1, j1 = i, j

        return i1 != 0 and A[i1][j1 - 1] == max_elem - 1

    def create_vertical_wall(self):
        matr = self.__matr
        print("create_vertical_wall Dashieva")
        randCol = random.randint(0, len(matr[0]) - 1)
        randRow = random.randint(0, len(matr) - 5)

        for k in range(5):
            matr[randRow + k][randCol] = -1

    def create_horizontal_wall(self):
        matr = self.__matr
        print("create_horizontal_wall_Lavr_Marb_Hag")
        y = random.randint(0, len(matr) - 1)
        x = random.randint(0, len(matr[0]) - 7)
        for i in range(0, 7):
            matr[y][x + i] = -1

    def step(self):
        self.save()
        if self.__direction == 'R':
            self.__step_right()
        elif self.__direction == 'D':
            self.__step_down()
        elif self.__direction == 'L':
            self.__step_left()
        elif self.__direction == 'U':
            self.__step_up()

    def save(self):
        f = open('snake_dat.txt', 'a')
        for i in range(self.__rows):
            for j in range(self.__cols):
                f.write(str(int(self.__matr[i][j])) + ' ')
            f.write('\n')
        f.write(self.__direction + '\n')
        f.close()

    def turn_left(self):
        if not self.__can_not_step_left():
            self.__direction = 'L'

    def turn_up(self):
        if not self.__can_not_step_up():
            self.__direction = 'U'

    def turn_down(self):
        if not self.__can_not_step_down():
            self.__direction = 'D'

    def turn_right(self):
        if not self.__can_not_step_right():
            self.__direction = 'R'
