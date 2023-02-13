import numpy as np

r = int(input("Enter the rows of matrix :"))
c = int(input("Enter the columns of matrix:"))
matrix = []
print("Enter the matrix element in row ways : ")

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

met1 = np.array(matrix)
met1 = met1.reshape(r,c)
print(met1)

arr1_transpose = met1.transpose()
print(f'Transposed Array:\n{arr1_transpose}')