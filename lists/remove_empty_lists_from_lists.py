# Program to remove Empty Lists from a List

def remove_empty_lists(arr):
    newArr = []
    try:
        if len(arr):
            for val in arr:
                if len(val):
                    newArr.append(val)
    except Exception as error:
        print(f"Something went wrong! Please check below error \n {error}")
    else:
        print(f"Lists after removing empty lists: {newArr}")

def using_list_comprehension(arr):
    result = [val for val in arr if val]
    print(f"The result is: {result}")

def remove_empty_lists_from_lists(arr):
    # Using loop to remove lists
    remove_empty_lists(arr)

    # Using List Comprehensions
    using_list_comprehension(arr)

remove_empty_lists_from_lists([[12, 7], [34, 8], [], [65, 87]])
