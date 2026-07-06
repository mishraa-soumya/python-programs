# Program to find largest number in a list

from functools import reduce

# Find largest using loop
def largest_using_loop(arr):
    largest = arr[0]
    for val in arr:
        if (val > largest):
            largest = val
    else:
        print(f"The largest number in the list is: {largest}")

# find largest using sorting method
def largest_using_sort_method(arr):
    arr.sort() # sort method sorts the lists ascending
    largest = arr[-1]
    print(f"The largest number using 'sort()' in the list is: {largest}")

# find largest using max() function
def largest_using_max(arr):
    largest = max(arr)
    print(f"The largest number in the list using 'max()' is: {largest}")

def largest_using_reduce(arr):
    largest = reduce(lambda x, y: x if x > y else y, arr) # compares each pair of elements in the list arr and keeps the larger one, cumulatively returning the maximum value.
    print(f"The largest number using 'reduce' method: {largest}")

def find_largest_number():
    arr = [178, 666, 1231, 5432, 9999]
    # find largest using loop
    largest_using_loop(arr)
    # largest using sort method
    largest_using_sort_method(arr)
    # find largest using max() method
    largest_using_max(arr)
    # find largest using reduce method
    largest_using_reduce(arr)

find_largest_number()
