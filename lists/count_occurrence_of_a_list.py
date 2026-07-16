# Program to count occurrence of an element in a list

import operator

def count_using_count_method(arr, elem):
    elemCount = 0
    try:
        if len(arr) == 0 or elem is None:
            raise TypeError("Invalid values for the argument")
        else:
            elemCount = arr.count(elem) # counting the occurrence using the count method
    except TypeError as error:
        print(f"Something went wrong! Please check the error! {error}")
    else:
        print(f"No. of occurrence of {elem}: {elemCount}")

# Program to count element using countof method of operator module
def count_using_operator(arr, elem):
    elemCount = None
    if arr and elem:
        elemCount = operator.countOf(arr, elem)
        print(f"Count for {elem} is : {elemCount}")

# Main Program

def count_occurrence_of_an_element(arr, elem):
    # Using count method
    count_using_count_method(arr, elem)

    # Using countof Operator
    count_using_operator(arr, elem)


count_occurrence_of_an_element([1, 3, 4, 2, 3, 5, 1, 1, 5], 2)
