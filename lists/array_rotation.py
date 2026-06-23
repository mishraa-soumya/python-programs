# Program to rotate an array with specific elements

"""
{arr} an array to be rotated
{r} no. of elements by which an array to be rotated to the left
"""

def lists_rotation(arr, r):
    arr[:] = arr[r:] + arr[:r]               # Slicing the array from position "r" to the end and
    print(f"The rotated array is : {arr}")   # joining it with array elements starting from "0" index until "r"

r_arr = [1,2,3,4,5,6, 7]
r = 2

lists_rotation(r_arr, r)
