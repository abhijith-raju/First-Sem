import numpy as np


def multiplication(A, B) :
    Result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for m in range(len(A)) :
        for n in range(len(B[0])) :
            for o in range(len(B)) :
                Result[m][n] = Result[m][n] + A[m][o] * B[o][n]

    return Result


def createidentity(rows, col) :
    result = []
    for i in range(rows) :
        row = []
        for j in range(col) :
            if i == j :
                element = 1
            else :
                element = 0
            row.append(element)
        result.append(row)
    return np.array(result)


def transpose(matrix) :
    result = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row) :
        rowoft = []
        for j in range(col) :
            element = matrix[j][i]
            rowoft.append(element)
        result.append(rowoft)

    return result


matrix = np.array([
    [1 / 3, 2 / 3, -2 / 3],
    [-2 / 3, 2 / 3, 1 / 3],
    [2 / 3, 1 / 3, 2 / 3]])

print("\nMatrix (Q) = :")
for row in matrix :
    print(row)

transpose = np.array(transpose(matrix))

print("\nTranspose Matrix (QT) = :")
for row in transpose :
    print(row)

rows = len(matrix)
cols = len(matrix[0])
identitymatrix = createidentity(rows, cols)

QQT = multiplication(matrix, transpose)
print(f"\nQ QT = :")

for row in QQT :
    print(row)

QTQ = multiplication(transpose, matrix)
print(f"\nQT Q = :")

for row in QTQ :
    print(row)

print("\nQ QT = QT Q = I =: ")
for row in identitymatrix :
    print(row)








