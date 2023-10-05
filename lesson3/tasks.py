matr = [
    [1, 2, 3, 5],
    [1, 2, 3, 5],
    [1, 20, 3, 5],
    [10, 2, 0, 5],
    [1, 2, 3, 5],
]


def garmaev_glavinskaya_tumene(matr):
    print("Вывод матрицы:")
    for i in range(5):
        for j in range(4):
            print(matr[i][j], ' ', end='')
        print('')
    print('\n', "Найти максимальный элемент матрицы:")
    maximum = 0
    for i in range(5):
        for j in range(4):
            if matr[i][j] > maximum:
                maximum = matr[i][j]
                x = i
                y = j
    print(maximum, x, y)


    if x == 4 or (x+1 < 5 and matr[x+1][y] == -1):
        print('\n', "Если он является последним элементом в столбце или снизу от него находится ", '\n',
                    "число -1, то заменить все положительные числа матрицы на 0:")
        for i in range(5):
            for j in range(4):
                if matr[i][j] > 0:
                    matr[i][j] = 0


    elif x+1 < 5 and matr[x+1][y] == 0:
        print('\n', "Если снизу от него находится число 0, то записать этот максимальный элемент ", '\n',
                    "вместо данного нуля, а все остальные положительные числа матрицы уменьшить на 1")
        for i in range(5):
            for j in range(4):
                if matr[i][j] > 0:
                    matr[i][j] = matr[i][j] - 1
        matr[x+1][y] = maximum

    elif x+1 < 5 and matr[x+1][y] == -2:
        print('\n', "Если снизу от него находится число -2, то вместо -2 записать значение ", '\n',
                    "= (максимальный элемент + 1)")
        matr[x+1][y] = maximum + 1
    print("Вывод матрицы:")
    for i in range(5):
        for j in range(4):
            print(matr[i][j], ' ', end='')
        print('')

def Marbaev_Hagoev(A):
    ...


def lavrentev_buldaev(matr):
    ...


def dashieva_Ykehev_mansheev(matr):
    ...


print(matr)
