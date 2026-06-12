# Program to check if the number is Prime or Not

def check_prime_number(num):
    if (num <= 0):
        print(f"The num {num} is Invalid")
        return

    if (num == 1):
        print("The number 1 is prime number")
        return
    
    primeRange = range(2, num)

    for i in primeRange:
        mod = num % i
        if mod == 0:
           # the num is divisible by the num {i}, which falls b/w 2 and 1 less than the num
           print(f"{num} is divisible by {i} and is not a Prime Number")
           break
    # The else block can be attached directly to a for loop. The code inside the else block only executes only if the loop completes the iteration naturally w/o a break statement. If the iteration is interupted with a break, then else block is not executed
    else:
        print(f"The number {num} is a Prime Number")
    
    return

check_prime_number(173)
    