# Program to clone a list

def clone_using_slicing(arr):
    new_list = arr[:]
    print(f"The Old list is {arr}")
    print(f"The cloned list is {new_list}")

def clone_using_assignment(arr):
      new_list = arr
      print(f"The Old list using assignment is : {arr}")
      print(f"The cloned list using assignment is : {new_list}")


def clone_a_list(arr = ["heena", "gunnu", "sugam", "viraj", "alka"]):
    # Clone a List Using the Slicing Method
        clone_using_slicing(arr)
    # Clone using Assignment
        clone_using_assignment(arr)

# Calling Main Program
clone_a_list()
