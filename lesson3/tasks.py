matr = [
    [1, 2, 3, 5],
    [1, 2, 3, 5],
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
    ...


def dashieva_Ykehev_mansheev(matr):
    ...


print(matr)
