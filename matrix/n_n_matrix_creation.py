# Program : Given a number n, the task is to create a n*n matrix in python.

import numpy as np
def create_zero_matrix(n):
    result = np.zeros((n,n), dtype=int)
    print(f"The final matrix of dimension {n} is {result}")

def create_matrix(n, type = 'zero'):
    if type == "zero":
        create_zero_matrix(n)

create_matrix(4)
