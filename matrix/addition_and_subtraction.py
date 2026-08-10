# Problem: Adding 2 Matrices using "numpy.add".

import numpy as np

def adding_two_matrices(mtr1, mtr2):
    # add method add the elements of 2 matrices which results to a third matrix
    result = np.add(mtr1, mtr2)
    print(f"The matrix addition using 'numpy.add': {result}")

adding_two_matrices([[1, 2], [3, 4]], [[4, 5], [6, 7]])
