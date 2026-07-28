# Program to add 2 matrices using the Numpy Module

import numpy as np

def matrix_addition():
    matrix1 = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
    matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    result = matrix1 + matrix2

    print(f"The matrix addition result is : {result}")

# Main Program Calling
matrix_addition()
