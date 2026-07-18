# Program to remove Tuples from a list

def remove_empty_tuples_using_filter_method(tuple_list):
   final_list = list(filter(None, tuple_list)) # filter object is converted into a python list
   print(f"The {tuple_list} after removing empty tuples is {final_list}")

def using_for_loop(tuple_list):
    new_tuple_list = []
    for lst in tuple_list:
        if lst:
            new_tuple_list.append(lst)
    print(f"The new list is: {new_tuple_list}")


# Main Program
def remove_empty_tuples_from_list(t_list=[(1,2), (), (4,5), (7,8)]):
    remove_empty_tuples_using_filter_method(t_list)
    using_for_loop(t_list)

remove_empty_tuples_from_list()
