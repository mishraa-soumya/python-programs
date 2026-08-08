# Problem Statement: Given a matrix of numbers. Find out the product
# Example: [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

import numpy as np
def product_of_matrix_using_numpy(mx):
    # flatten the matrix to a 1-D List
    flattened_list = [ele for sub in mx for ele in sub] # Using List Compression to flattened the matrix before getting the product
    matrix_product = np.prod(flattened_list)

    print(f"The product of matrix is: {matrix_product}")

def product_of_matrix(matriqs):
    # Using numpy.prod to find out the product of the matrix
    product_of_matrix_using_numpy(matriqs)

# calling main program
matriqs = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
product_of_matrix(matriqs)
