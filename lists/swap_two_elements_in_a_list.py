# Program to Swap 2 Elements from a list

# Using Direct Assignment

def swap_using_direct_assignment(arr_list, swapIndex, swapWithIndex):
    # check for empty List
    if not arr_list:
        print("List is Empty")
        return

    if not swapIndex or not swapWithIndex:
        print("Invalid or Empty Parameters. Please pass values for swapIndex or swapWithIndex")
        return

    arr_list[swapWithIndex], arr_list[swapIndex] = arr_list[swapIndex], arr_list[swapWithIndex]

    print(f"The swapped array list for Index {swapIndex} and {swapWithIndex} is {arr_list}")

def swap_list_elements():
    arr_list = [2,5,7,9,11,13,19,20,21]
    swap_using_direct_assignment(arr_list, 3, 6)

swap_list_elements()


