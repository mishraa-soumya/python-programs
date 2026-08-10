# Problem: Adding 2 Matrices using "numpy.add".

import numpy as np

def adding_two_matrices(mtr1, mtr2):
    # add method add the elements of 2 matrices which results to a third matrix
    result = np.add(mtr1, mtr2)
    print(f"The matrix addition using 'numpy.add': {result}")

adding_two_matrices([[1, 2], [3, 4]], [[4, 5], [6, 7]])

def subtract_two_matrices(mx1, mx2):
    # subtract method performs subtraction of matrices element wise
    finalMatrix = np.subtract(mx1, mx2)
    print(f"Result of matrix subtraction using 'numpy.subtract': {finalMatrix}")

subtract_two_matrices([[9, 7], [8, 12]], [[4, 5], [6, 7]])
