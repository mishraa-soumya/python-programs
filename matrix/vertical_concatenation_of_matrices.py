# Problem: Given a matrix containing strings, the task is to perform vertical concatenation where elements from each columnare joined together to form a single string for that column.

# Example:
# Input: [["Gfg", "good"], ["is", "for"]]
# Output: [["Gfgis", "goodfor"]]

import pandas as pd
import numpy as np
def vc_using_pandas(mat):
    # Create a data frame from the matrix using pandas
    data_frame = pd.DataFrame(mat)
    # Replace all the missing values with empty strings and join the strings of each column
    column_data = data_frame.fillna(" ").apply("".join)
    # Convert the column data back into a list form
    result = list(column_data)
    print(f"Result of vertical concatenation of a matrix: {result}")

# Using Numpy
def vc_using_numpy(mat):
    max_column = max(len(x) for x in mat) # Finds the maximum sublist or the max column
    p = [x + [''] * (max_column - len(x)) for x in mat]
    arr = np.array(p).T
    res = [''.join(r) for r in arr]
    print(f"Result of vertical concatenation using Numpy: {str(res)}")


def vertical_concatenation_of_matrix(mat):
    # Using Pandas to concatenation
    vc_using_pandas(mat)
    # Using Numpy for concatenation
    vc_using_numpy(mat)

# Main Program
mat = [["Python", "good"], ["is", "for"], ["Best"]]
vertical_concatenation_of_matrix(mat)
