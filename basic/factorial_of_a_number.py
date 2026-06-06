# Factorial of a number

def factorial_of_a_number(num):
    factorial = 1
    # check if number is Zero or Greater than Zero
    if (num == 0):
        return factorial
    else:
        
        for i in range(1, num+1):
            factorial = i * factorial
        
    if (factorial > 1):
        print(f"factorial: {factorial}")
    else:
        print("Error in finding Factorial")

factorial_of_a_number(5)