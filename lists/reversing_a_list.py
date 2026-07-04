# Program to reverse a list

def reversing_a_list_using_loop(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j -= 1

    print(f"The reverse list is {arr}")

def reversing_a_list_using_reverse_method():
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr.reverse()
    print(f"The reverse array using reverse method: {arr}")

def reverse_using_list_slicing():
    arr = [2, 3, 4, 5, 6, 7]
    rev_arr = arr[::-1] # double colon with negative Index reverse the list
    print(f"The reverse array using list slicing: {rev_arr}")

def reversing_a_list(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]):
    # Using a loop
    reversing_a_list_using_loop(arr)
    # Using the reverse method
    reversing_a_list_using_reverse_method()
    # Using list slicing
    reverse_using_list_slicing()

reversing_a_list()
