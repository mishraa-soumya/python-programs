# Program to print Negative Numbers in a List

def print_negative_numbers(arr):
    negativeArrNums = []
    try:
        for num in arr:
            if (num < 0):
                negativeArrNums.append(num)
    except TypeError as error:
        print(f"Something went wrong! Please check below error \n {error}")
    else:
        if len(negativeArrNums):
            print(f"The list of negative numbers is {negativeArrNums}")
        else:
            print(f"No negative numbers in the list: {arr}")

print_negative_numbers([-12, -8, 0, 18, -21, 55, 87])
