# Program to return 'N' largest elements from the list

def nth_largest_element(arr, n):
    # Sort the array in a descending order
    arr.sort(reverse=True)
    # Split the array starting from first element upto "Nth" element
    nth_largest = arr[:n]
    print(f"List of 'Nth' largest element: {nth_largest}")

nth_largest_element([775, 25, 33, 999, 87, 57], 5)
