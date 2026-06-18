# Program to print the sum of squares of n natural numbers

def squares_of_number(num):
    return pow(num, 2)

def sum_of_natural_number(nn_limit):
    if (nn_limit < 0):
        print(f"The {nn_limit} is not a Natural Number")
        return
    else:
        nn_sum = 0
        try:
            for num in range(1, nn_limit+1):
                nn_square = squares_of_number(num)
                nn_sum += nn_square
            print(f"The sum of squares of {nn_limit} Natural Number: {nn_sum}")
        except Exception as err:
            print(f"Error in the program: {err}")



sum_of_natural_number(15)
