# Program : Given a number n, the task is to create a n*n matrix in python.

import numpy as np
def create_zero_matrix(n):
    result = np.zeros((n,n), dtype=int)
    print(f"The final matrix of dimension {n} is {result}")

def create_custom_matrix(n, val):
    result = np.full((n,n), val)
    print(f"\n ======= \n The custom matrix of value: {val} and dimension: {n} is: {result}")

def create_matrix(n, type = 'zero', val=6):
    if type == "zero":
        create_zero_matrix(n)
    elif type == "full":
        create_custom_matrix(n, val)

# Calling the program to create Zero matrix
create_matrix(4)
# Calling the program to create a full matrix
create_matrix(3, 'full',8)
