# Given an array of numbers and an integer n, the task is to find the remainder when all numbers in the array are multiplied and divided by n.

def multiply_lists_element(scores):
    product = 1 # default or initial product
    for value in scores:
        product *= value

    return product

def division_by_n(n, scores):
    lists_product = multiply_lists_element(scores)

    if lists_product is not None or lists_product != 1:
        try:
            remainder = lists_product % n
            print(f"Remainder for list product {lists_product} divided by {n}: {remainder}")
        except ZeroDivisionError:
            print(f"ZeroDivisionError for {n}. Please enter a number greater than zero")

def find_remainder_for_lists_element(n, scores):
    division_by_n(n, scores)



find_remainder_for_lists_element(n = 13, scores = [2, 3, 4, 5, 6, 7, 9])