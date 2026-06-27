# Program to interchange the first and last elements in a list

def interchange_elements(arr_list):
    temp = arr_list[0]
    arr_list[0] = arr_list[-1]
    arr_list[-1] = temp

    print(f"The updated array list is {arr_list}")

interchange_elements(arr_list = [2,5,7,9,11,13,19,20,21])
