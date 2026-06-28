# Program to interchange the first and last elements in a list

def interchange_elements(arr_list):
    # Using Temporary Variable
    # temp = arr_list[0]
    # arr_list[0] = arr_list[-1]
    # arr_list[-1] = temp
    # print(f"The updated array list using Temporary Variable {arr_list}")

    # Using Direct Assignment
    arr_list[0], arr_list[-1] = arr_list[-1], arr_list[0]
    print(f"The updated array list using Direct Assignment method {arr_list}")

    # Using Tuple Variable
    # pair = arr_list[-1], arr_list[0] # pair = (21,2)
    # arr_list[0], arr_list[-1] = pair
    # print(f"The updated array list using Tuple Variable {arr_list}")

    # Using Slicing
    firstElem = arr_list[:1]
    lastElem = arr_list[-1:]
    midElements = arr_list[1:-1] # elements between first and last
    arr_list = lastElem + midElements + firstElem
    # print(f"The updated array list through slicing is {arr_list}")

interchange_elements(arr_list = [2,5,7,9,11,13,19,20,21])
