# Program to break a list into chunks of lists of size "N"

def break_a_list_using_loop(input_list, n):
    output_list = []
    start_counter = 0
    end_counter = n
    while start_counter < len(input_list):
        new_list = input_list[start_counter:end_counter] # Using Slicing to create new lists
        output_list.append(new_list)
        start_counter = end_counter
        end_counter = start_counter + n
    else:
        print(f"The output list is: {output_list}")

def breaking_a_list_using_list_comprehension(input_list, n):
    output_list = [input_list[counter: counter+n] for counter in range(0, len(input_list), n)]
    print(f"The output list using List Comprehension is {output_list}")

def break_a_list_into_n_chunks(input_list, n):
    # Breaking a List using loop
    break_a_list_using_loop(input_list, n)

    # Breaking a list using List Conprehension
    breaking_a_list_using_list_comprehension(input_list, n)

break_a_list_into_n_chunks([1, 4, 6, 8, 10, 12, 13, 15], 3)
