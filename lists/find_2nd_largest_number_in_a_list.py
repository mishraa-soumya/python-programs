# program to find the 2nd largest number in a list

def using_sort(arr):
    # Sorting the list in ascending order
    arr.sort()
    second_largest = arr[-2]
    print(f"The 2nd largest number is: {second_largest}")

def using_sort_in_descending(arr):
    # Sorting the list in descending order
        arr.sort(reverse=True)
        second_largest = arr[1]
        print(f"The 2nd largest number is {arr[1]}")

def find_2nd_largest_number_in_a_list():
    arr = [100, 500, 800, 1200, 300]
    using_sort(arr)
    # Using Sorting in Descending Order
    using_sort_in_descending(arr)

find_2nd_largest_number_in_a_list()