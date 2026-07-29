# Program to add 2 matrices using the Numpy Module

import numpy as np

def matrix_addition_using_numpy(mx1, mx2):
    matrix1 = np.array(mx1)
    matrix2 = np.array(mx2)
    result = matrix1 + matrix2

    print(f"The matrix addition result is : {result}")

def matrix_addition_using_list_comprehension(matrix1, matrix2):
    # matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    output = []
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    for res in result:
        output.append(res)
    print(f"The result of matrix addition through list comprehensions is: {output}")


def matrix_addition(mx1, mx2):
    # Using Numpy
    matrix_addition_using_numpy(mx1, mx2)
    # Using List Comprehensions
    matrix_addition_using_list_comprehension(mx1, mx2)

# Main Program Calling
matrix_addition([[9,2,5], [2, 4, 7], [3, 6, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
