# Problem: Get the Kth Column of a matrix

import numpy as np
def get_kth_column_using_numpy(matriqs, k):
    result = np.array(matriqs)[:,k]
    print(f"The {k} column element: {result}")

def find_kth_column_matrix(matriqs, k):
    # Using Numpy
    get_kth_column_using_numpy(matriqs, k)

mat = [[4,5,6], [8,1,10], [7, 12, 5]]

find_kth_column_matrix(mat, 2)
