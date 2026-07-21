# Program to find sum of digits for each number in a list

def sum_of_digits_for_number_in_list(numList):
    output = []
    for num in numList:
        sum = 0
        print(f"num: {str(num)}")
        for i  in str(num):
            print(f"i = {i}")
            sum += int(i)
        output.append(sum)
    else:
        print(f"The output list is: {output}")

sum_of_digits_for_number_in_list([123, 999, 15, 77, 23, 8])
