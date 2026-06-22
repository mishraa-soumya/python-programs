# Program to find the largest element of the lists

def find_largest_element():
    scores = [89, 68, 72, 97, 108, 55]
    largest_element = scores[0]

    for index, value in enumerate(scores):
        if (index == 0):
            continue
        element = scores[index] # starting the comparison from 2nd number

        if (element > largest_element):
            largest_element = element
            continue
        else:
            continue
    else:
        print(f"The largest element is {largest_element}")


find_largest_element()

