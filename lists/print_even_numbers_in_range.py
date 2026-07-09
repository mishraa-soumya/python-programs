# Program to print all even numbers in a range

def print_even_numbers(rangeStart, rangeStop, step=0):
    evenNums = []
    try:
        for num in range(rangeStart, rangeStop, step):
            if (num % 2 == 0):
                evenNums.append(num)

    except Exception as error:
        print(f"Error: {error}")
    else:
        if len(evenNums):
            print(f"List of even numbers between {rangeStart} and {rangeStop} is {evenNums}")
        else:
            print(f"No Even Numbers found between {rangeStart} and {rangeStop}")


# Calling the Function
print_even_numbers(12, 30, 2)

