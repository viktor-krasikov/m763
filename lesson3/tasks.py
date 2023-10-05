matr = [
    [1, 2, 3, 5],
    [1, 2, 3, -5],
    [1, 20, 3, 5],
    [10, 2, 0, 5],
    [1, 2, 3, 5],
]


def garmaev_glavinskaya_tumene(matr):
    maximum = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] > maximum:
                maximum = matr[i][j]
                x = i
                y = j


    if x == len(matr)-1 or (x+1 < len(matr) and matr[x+1][y] == -1):
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                if matr[i][j] > 0:
                    matr[i][j] = 0


    elif x+1 < len(matr) and matr[x+1][y] == 0:
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                if matr[i][j] > 0:
                    matr[i][j] = matr[i][j] - 1
        matr[x+1][y] = maximum

    elif x+1 < len(matr) and matr[x+1][y] == -2:
        matr[x+1][y] = maximum + 1


def Marbaev_Hagoev(A):
    ...


def lavrentev_buldaev(matr):
    import numpy as np
    matr = np.array(matr)
    (i, j) = np.unravel_index(np.argmax(matr), matr.shape)
    max_index = np.argmax(matr)
    if (max_index + 1) % 4 == 0:
        matr[matr > 0] = 0
    elif (max_index + 1) == -1:
        matr[matr > 0] = 0
    elif (matr[i][j + 1]) == 0:
        temp = matr[i][j]
        matr[i][j] = matr[i][j + 1]
        matr[i][j + 1] = temp
        matr[matr > 0] -= 1
        matr[i][j + 1] += 1
    elif (matr[i][j + 1]) == -2:
        matr[i][j + 1] = matr[i][j] + 1
    return matr


def dashieva_Ykehev_mansheev(matr):
    ...


print(matr)
