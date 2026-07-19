# Program to print duplicates from a list of integers

def print_duplicates_from_a_list_of_integers(Int_list):
    duplicates = []
    for inum in Int_list:
        current = inum
        count = Int_list.count(current)
        # push the elements whose count is more than 1 in another list 'duplicates'
        # only if it is not already present
        if (count > 1 and current not in duplicates):
            duplicates.append(current)
    else:
        print(f"The duplicates are : {duplicates}")

print_duplicates_from_a_list_of_integers(Int_list=[1,2,2,3,3,4,5,5])