# Program to clear a list

def using_clear_method(arr):
    arr.clear()
    print(f"The empty list {arr} after applying 'clear' method.")

def using_del_method(arr):
    del arr[:]
    print(f"The empty list {arr} after using 'del' keyword and list slicing method")

def using_pop_method(arr):
    for val in arr:
        val.pop()

    print(f"The empty list {arr} after using 'pop' method")

def using_reassigment(arr):
    arr = []
    print(f"The empty list {arr} after reassignment")

def clearing_a_list_using_different_methods(arr):
    # Using Clear Method
    using_clear_method(arr)

    # Using del method
    using_del_method(arr)

    # Using pop method()
    using_pop_method(arr)

    # Using Reassignment
    using_reassigment(arr)




clearing_a_list_using_different_methods(arr = [1, 2, 3, 4, 5, 6, 7])
