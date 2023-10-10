matr = [
    [1, 2, 3, 5],
    [1, 2, 3, -5],
    [1, 20, 3, 5],
    [10, 2, 0, 5],
    [1, 2, 3, 5],
]


def garmaev_glavinskaya_tumene(matr):
    maximum = 0
    stroka = len(matr)
    stolb = len(matr[0])
    for i in range(stroka):
        for j in range(stolb):
            if matr[i][j] > maximum:
                maximum = matr[i][j]
                x = i
                y = j
    if x == stroka-1 or (x+1 < stroka and (matr[x+1][y] == -1 or matr[x+1][y] > 1)):
        for i in range(stroka):
            for j in range(stolb):
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                if matr[i][j] > 0:
                    matr[i][j] = 0
    elif x+1 < stroka and matr[x+1][y] == 0:
        for i in range(stroka):
            for j in range(stolb):
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                if matr[i][j] > 0:
                    matr[i][j] = matr[i][j] - 1
        matr[x+1][y] = maximum
    elif x+1 < stroka and matr[x+1][y] == -2:
    elif x+1 < len(matr) and matr[x+1][y] == -2:
        matr[x+1][y] = maximum + 1



def Marbaev_Hagoev_Panteleev(A):
    max_elem = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if (max_elem < A[i][j]):
                max_elem = A[i][j]
                i1 = i
                j1 = j

    if i1 == 0:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] > 0: A[i][j] = 0

    elif A[i1 - 1][j1] == -1:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] > 0: A[i][j] = 0

    elif A[i1 - 1][j1] == 0:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] > 0: A[i][j] = 0
                if i == i1 - 1 and j == j1: A[i][j] = max_elem

    else:
        if A[i1 - 1][j1] == -2:
            A[i1 - 1][j1] = max_elem + 1



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

    return matr


print(matr)
