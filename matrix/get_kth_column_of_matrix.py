# Problem: Get the Kth Column of a matrix

import numpy as np

def find_kth_column_matrix(matriqs, k):
    # Using Numpy
    get_kth_column_using_numpy(matriqs, k)
    # Using List Comprehension
    get_kth_column_element_using_list_c(matriqs, k)
    # Using map() and Lambda function
    get_kth_element_using_lambda_function(matriqs, k)

# Using Numpy
def get_kth_column_using_numpy(matriqs, k):
    result = np.array(matriqs)[:,k]
    print(f"The {k} column element using Numpy: {result}")

# Using List Comprehension
def get_kth_column_element_using_list_c(matriqs, k):
    kth_column = [row[k] for row in matriqs]
    print(f"The {k} column element using list comprehension: {kth_column}")

# Using Lambda Function
def get_kth_element_using_lambda_function(matriqs, k):
    kth_column = map(lambda row: row[k], matriqs)
    print(f"The kth element: {kth_column}")

# Calling Main Program
mat = [[4,5,6], [8,1,10], [7, 12, 5]]
find_kth_column_matrix(mat, 1)
