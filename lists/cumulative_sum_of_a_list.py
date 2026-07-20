# program to print cumulative sum of a list

def cumulative_sum_of_a_list(InputList):
    OutputList = []
    for index, val in enumerate(InputList):
        current = index
        sum = 0
        for num in range(0, current+1):
            sum += InputList[num]
        else:
            OutputList.append(sum)
    else:
        print(f"The cumulative sum list is: {OutputList}")

cumulative_sum_of_a_list([1,2,3,4,5])
