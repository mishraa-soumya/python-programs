# Program to find if element exists in a lists

# Using in Statement
def element_exists(arr_lists, elem):
    # considering "0", and " " not part of this search
    if elem in arr_lists:
        print(f"{elem} exists in the {arr_lists}")
        return
    else:
        print(f"{elem} doesn't exists in the {arr_lists}")

# Using any() Function
# any() checks if a specific element exists in a list and returns True if found, otherwise False.
def check_using_any_function(arr_lists, elem):
    exists = any(el == elem for el in arr_lists)
    if (exists):
        print(f"{elem} exists in the list")
    else:
        print(f"{elem} doesn't exists in the list")

# Using count()
# count() function checks how many times a specific element appears in a list and returns the number of occurence.

def using_the_count_function(arr_lists, elem):
    exists = arr_lists.count(elem)
    if (exists):
        print(f"{elem} exists in the lists")
    else:
        print(f"{elem} doesn't exists in the lists")

def check_if_elements_exists(elem = "heena", arr = [10, 13, 52, 25, "Heena", 45, "soumya"], ):
    if elem and arr:
        # 1. Using in statement. Case Sensitive Search
        # element_exists(arr, elem)
        # 2. using any function. Case Sensitive Search
        # check_using_any_function(arr, elem)
        # 3. using the count function. Case Sensitive Search
            using_the_count_function(arr, elem)
    else:
        print(f"Please pass valid element for search")
        return

check_if_elements_exists()
