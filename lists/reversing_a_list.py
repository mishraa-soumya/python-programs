# Program to reverse a list

def reversing_a_list_using_loop(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j -= 1

    print(f"The reverse list is {arr}")

def reversing_a_list(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]):
    # Using a loop
    reversing_a_list_using_loop(arr)
