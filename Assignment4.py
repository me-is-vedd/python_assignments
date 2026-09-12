#LIST MATRIX ADDITION------------
empty_list=[[0,0,0],[0,0,0],[0,0,0]]
listmatrix1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listmatrix2=[[9, 8, 7], [6, 5, 4], [3, 2, 1]]
for i in range(len(listmatrix1)):
    for j in range(len(listmatrix1[0])):
        empty_list[i][j] = listmatrix1[i][j] + listmatrix2[i][j]

print("List Matrix 1:")
for row in listmatrix1: #For printing one row below the other
    print(row)

print("List Matrix 2:")
for row in listmatrix2: #For printing one row below the other
    print(row)

print("Addition of List Matrices:")
for row in empty_list: #For printing one row below the other
    print(row)

#NUMPY MATRIX ADDITION------------
import numpy as np
numpy_matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
numpy_matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
numpy_matrix_sum = np.add(numpy_matrix1, numpy_matrix2)
print("Numpy Matrix 1:\n", numpy_matrix1)
print("Numpy Matrix 2:\n", numpy_matrix2)
print("Addition of Numpy Matrices:\n", numpy_matrix_sum)