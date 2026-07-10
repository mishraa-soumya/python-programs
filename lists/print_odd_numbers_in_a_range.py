# Program to print odd numbers in a range

def print_odd_numbers_in_range(start, stop, step):
    oddNums = []
    try:
        for num in range(start, stop, step):
            if (num % 2 != 0):
                oddNums.append(num)
    except Exception as error:
        raise RuntimeError("Something went Wrong. Please check the error: {error}")
    else:
        if len(oddNums):
            print(f"The list of odd numbers between {start} and {stop} are {oddNums}")
        else:
            print(f"There are no Odd numbers b/w {start} and {stop}")

print_odd_numbers_in_range(1, 20, 2)
