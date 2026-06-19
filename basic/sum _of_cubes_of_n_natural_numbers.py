# Program to print the sum of cubes of natural numbers


# Program to print the cube of a number

def cube_of_number(num):
    return pow(num, 3)

def sum_of_natural_numbers(nn_limit):
    if (nn_limit < 0):
        print(f"{nn_limit} is not a Natural Number")
        return
    else:
        nn_sum = 0
        for n in range(1, nn_limit+1):
            cube = cube_of_number(n)
            nn_sum += cube
        else:
            print(f"The sum of {n} natural number is {nn_sum}")

sum_of_natural_numbers(10)
        