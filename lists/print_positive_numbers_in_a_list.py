# Program to print positive numbers in a list

# Any number greater than or equal to Zero is a Positive number
def print_positive_number(arr):
    positiveNums = []
    try:
        if(len(arr)):
            for num in arr:
                if num >= 0:
                    positiveNums.append(num)
        else:
            raise RuntimeError("Can't proceed as length of list is ZERO")
    except TypeError:
        print("Invalid Parameters. Please pass a Valid List")
    except Exception as error:
        print(f"Something went wrong! Please check the error: \n{error}")
    else:
        if len(positiveNums):
            print(f"The positive numbers are as listed: {positiveNums}")
        else:
            print(f"There are no positive numbers")

print_positive_number([0, -10, 199, 555, -25, -13, -4, 1300])
# Negative Scenario
print_positive_number(["abc", "momo", "heena", "raj"])


