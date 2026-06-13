# Print a N-th Fibonaci Number

def print_fibonaci_number(num):
    fibonaci_num_list = [0, 1]
    
    try:
        for n in range(2, num):
            print(f"n: {n}")
            nMinusOne = n-1
            nMinusTwo = n-2
            
            next_num = fibonaci_num_list[nMinusTwo] + fibonaci_num_list[nMinusOne]
              
            if next_num:
                fibonaci_num_list.append(int(next_num))
                print(f"Fibonaci List: {fibonaci_num_list}")
    except Exception as e:
        print(f"Error while calculating fibonaci number {e}")
    else:
        # Print the nth Fibonaci number from the list
        nth_fibo = fibonaci_num_list[num - 1]
        print(f"The {num} Fibonaci Number in the Series is {nth_fibo}")

print_fibonaci_number(5)