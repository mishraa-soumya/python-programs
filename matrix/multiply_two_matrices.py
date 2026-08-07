# Program to multiply two matrices

# Using Numpy
import numpy as np

# Multiplying 2 matrices using Numpy. This method does "element-wise" multiplication
def multiplication_using_multiply(matrix1, matrix2):
    # result = matrix1*matrix2
    result = np.multiply(matrix1, matrix2) # The result from above line and this line would be same. "*" operator is the shortcut of "multiply" # method of numpy
    print(f"The output of matrix multiplication using 'numpy.multiply' is {result} and it's shape is {result.shape}")

def matrix_multiplication():
    mx1 = np.array([[2,2], [1,2]])
    mx2 = np.array([[2, 3], [1,4]])
    multiplication_using_multiply(mx1, mx2)
    # Multiplication using Dot Product
    multiplication_using_dot(mx1, mx2)

def multiplication_using_dot(mx1, mx2):
    # result = mx1@mx2
    result = np.dot(mx1, mx2)
    print(f"Matrix Multiplication using 'numpy.dot' is {result}")

matrix_multiplication()
