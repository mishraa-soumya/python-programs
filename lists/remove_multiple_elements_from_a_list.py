# Program to remove multiple elements from a list

def remove_multiple_elements_from_list(arr, removeElem):
    try:
        if len(arr) > 0 and len(removeElem) > 0:
            for rElem in removeElem:
                arr.remove(rElem)
        else:
            raise RuntimeError("Please check if both the arguments lists are valid and not empty")
    except Exception as error:
        print(f"Something went error! Please check below error: \n{error}")
    else:
        print(f"Lists after removing elements: {arr}")

def remove_elements_using_not_in(arr, removeElem):
    newArr = []
    try:
        for val in arr:
            if val not in removeElem:
                newArr.append(val)
    except Exception as error:
        print(f"Something went error! Please check below error \n {error}")
    else:
        print(f"Lists after removing the element is: {newArr}")

def remove_elements_from_lists(arr = [23, 20, 35, 66, 97, 13], removeElem = [20, 35]):
    # Removing Element using 'remove' method
    remove_multiple_elements_from_list([23, 20, 35, 66, 97, 13], [20, 35])

    # Remove Elements using Not In
    remove_elements_using_not_in(arr, removeElem)

remove_elements_from_lists()
