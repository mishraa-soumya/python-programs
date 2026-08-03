# Program to multiply two matrices

# Using Numpy
import numpy as np

# Multiplying 2 matrices using Numpy. This method does "element-wise" multiplication
def multiplication_using_numpy(matrix1, matrix2):
    # result = matrix1*matrix2
    result = np.multiply(matrix1, matrix2) # The result from above line and this line would be same. "*" operator is the shortcut of "multiply" method of numpy
    print(f"The output of matrix multiplication using numpy is {result} and shape is {result.shape}")

def matrix_multiplication():
    mx1 = np.array([[2,2], [1,2]])
    mx2 = np.array([[2, 3], [1,4]])
    multiplication_using_numpy(mx1, mx2)

matrix_multiplication()
