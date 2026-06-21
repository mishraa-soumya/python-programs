# Program to sum up all the elements in a list

def sum_of_lists():
    scores = [88, 75, 69, 90, 77, 85]
    sum = 0
    for score in scores:
        sum += score

    print(f"Sum of all the elements of a list are: {sum}")

sum_of_lists()