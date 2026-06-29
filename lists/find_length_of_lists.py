# Program to find length of lists through different ways

# Using len()
def length_of_lists_using_len(arr_list):
    print(f"Length of Lists using len(): {len(arr_list)}")

# Using loop (Naive method)
def find_length_using_loop(arr_list):
    count = 0
    for elem in arr_list:
        count += 1

    print(f"The length of lists using loop method: {count}")

# Using length_hint() from operator Module
from operator import length_hint

def find_length_using_length_hint(arr):
    arr_length = length_hint(arr)
    print(f"The length of array using length hint function: {arr_length}")

# Main Program
def find_length_of_lists(arr):
    # Length of Lists using len()
    length_of_lists_using_len(arr)

    # Length of Lists using loop
    find_length_using_loop(arr)

    # Length of Lists using length_hint
    find_length_using_length_hint(arr)

# Main Program
arr = [25, 26, 27, 28, 30, 0, 10, 12, 14, 66, 77, 99]
find_length_of_lists(arr)
