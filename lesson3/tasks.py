import random

matr = [
    [1, 2, 3, 5],
    [1, 2, 3, -1],
    [1, 20, 4, 22],
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


def garmaev_glavinskaya_tumene2(matr):
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


def Marbaev_Hagoev_Panteleev(A):
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



def Marbaev_Hagoev_Panteleev_2(A):
    i1 = j1 = 0
    max_elem = A[i1][j1]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if max_elem < A[i][j]:
                max_elem = A[i][j]
                i1, j1 = i, j

    return i1 != 0 and A[i1 - 1][j1] == max_elem - 1



def lavrentev_buldaev(matr):
    import numpy as np
    matr = np.array(matr)
    (i, j) = np.unravel_index(np.argmax(matr), matr.shape)
    if matr[i][j] in matr[:, -1]:
        matr[matr > 0] = 0
    elif matr[i][j + 1] == -1 or matr[i][j + 1] > 1:
        matr[matr > 0] = 0
    elif (matr[i][j + 1]) == 0:
        temp = matr[i][j]
        matr[i][j] = matr[i][j + 1]
        matr[i][j + 1] = temp
        matr[matr > 0] -= 1
        matr[i][j + 1] += 1
    elif (matr[i][j + 1]) == -2:
        matr[i][j + 1] = matr[i][j] + 1
    return matr.tolist()


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

def Nikolaeva_Mordvin(matr):
    max=matr[0][0]
    xmax=0
    ymax=0
    for i in range(len(matr)):
         for j in range(len(matr[i])):
             if(max<=matr[i][j]):
                 max=matr[i][j]
                 xmax=i
                 ymax=j
    #print(xmax,ymax)
    #print(matr[xmax+1][ymax])
    if(matr[xmax+1][ymax]==max-1):
        return True
    else:
        return False

def dashieva(matr):
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

    return matr

print(matr)
