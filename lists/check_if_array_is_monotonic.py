# Program to check if array is monotonic

# Monotonic : Given an array, check if elements of the array are in Increasing Order or Decreasing Order


def check_array_as_monotonic():
    array_list = [75,62,54,45,33,25,11,5]
    array_order = "None"
    firstElem = array_list[0]
    secondElem = array_list[1]

    if (firstElem > secondElem):
        array_order = "Decreasing"
    elif (firstElem < secondElem):
        array_order = "Increasing"

    for index, val in enumerate(array_list):
        # find if array needs to be checked for Increasing Order or Decreasing Order
        print(f"index: {index}")

        nextElem = int(index+1)
        print(f"length of array: {len(array_list)}")
        if (nextElem >= len(array_list)):
            if (array_order == "Increasing"):
                print(f"Array Elements are in Increasing Order")
                break
            else:
                print(f"Array Elements are in Decreasing Order")
                break

        nextArrayElement = array_list[nextElem]

        if (array_order == "Increasing"):
            if (array_list[index] > nextArrayElement):
                print(f"Array is not Monotonic")
                break
            else:
                continue
        elif (array_order == "Decreasing"):
            if (array_list[index] < nextArrayElement):
                print(f"Array is not Monotonic")
                break
            else:
                continue
    else:
        if (array_order == "Increasing"):
            print(f"Array Elements are in Increasing Order")
        else:
            print(f"Array Elements are in Decreasing Order")

check_array_as_monotonic()
