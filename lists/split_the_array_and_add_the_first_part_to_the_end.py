# Program to split the array into 2 parts and then add the first part at the end of the array

"""
{n} The no. of elements in the array which needs to be splitted
"""

def split_array_into_two_parts(n):
    arr = [2,5,7,9,11,13,15,17,19,21,23]

    # Split the array into two parts
    first_part = arr[ :n] # slice the array upto n elements
    second_part = arr[n+1:] # n+1 upto end element

    final_arr = second_part + first_part

    print(f"The final array is {final_arr}")

# split_array_into_two_parts(3)

"""
{n}: The Index in the array before which the array needsto be splitted
"""

def split_using_extend_method(n):
    arr = [2,5,7,9,11,13,15,17,19,21,23]

    # Split the array into two parts
    first_part = arr[ :n]
    second_part = arr[n:]

    # extend() the second part to the first part
    second_part.extend(first_part)

    print(f"The final array is: {second_part}")

split_using_extend_method(2)
