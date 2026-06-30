# Program to find if element exists in a lists

def element_exists(arr_lists, elem):
    # considering "0", and " " not part of this search
    if elem in arr_lists:
        print(f"{elem} exists in the {arr_lists}")
        return
    else:
        print(f"{elem} doesn't exists in the {arr_lists}")

def check_if_elements_exists(elem = "Heena", arr = [10, 13, 52, 25, "Heena", 45, "soumya"], ):
    if elem and arr:
        element_exists(arr, elem)
    else:
        print(f"Please pass valid element for search")
        return

check_if_elements_exists()