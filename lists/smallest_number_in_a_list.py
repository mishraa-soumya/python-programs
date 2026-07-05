# Program to fnd the smallest number in a list

# arr = [15, 77, 62, 9, 83]

def using_loop(arr):
    smallest = arr[0]
    for val in arr:
        if (val < smallest):
            smallest = val
    print(f"The smallest number in the list {smallest}")

def using_min(arr):
    smallest = min(arr)
    print(f"The smallest no. using 'min()': {smallest}")

def using_sorting(arr):
    arr.sort()
    smallest = arr[0]
    print(f"The smallest number in the array is: {smallest}")

def find_smallest_number(arr):
    # Using a for loop
    using_loop(arr)

    # using min
    using_min(arr)

    # using Sorting
    using_sorting(arr)

find_smallest_number(arr = [10, 77, 62, 19, 83])
