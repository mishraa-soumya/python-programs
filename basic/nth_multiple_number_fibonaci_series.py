# Find the Nth Multiple of number in Fibonaci Series
# Suppose n is a number and m is also a number. Find a number in Fibonaci Series divisible by "m" and which is "nth" multiple

""" 
# {n} Parameter representing nth multiple 
# {m} Parameter representing divisible number
"""

def find_n_multiple_in_fibonaci(n, m):
    fibonaci_list = [0, 1]
    count = 0

    # Run a while loop until the nth multiple is found
    while True:
        # for num in range(2, n+1): # Running a for loop from 2 to n+1, so that loop iterates until nth times
        next_num = fibonaci_list[-2] + fibonaci_list[-1]
        fibonaci_list.append(next_num) 
        if (next_num % m == 0):
            count +=1
            
            if (count == n):
                print(f"The number {next_num} in Fibonaci Series is divisible by {m} and is {n}th multiple of {m}")
                break
    else:
        print(f"Fibonaci Series has no {n} multiple of {m}. Below is the Fibonaci Series:")
        fibonaci_series = " ".join(str(item) for item in fibonaci_list)
        print(f"Fibonaci Series: {fibonaci_series}")          
    

find_n_multiple_in_fibonaci(2, 5)
