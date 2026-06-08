# Armstrong Number: It is a number whose sum of cubes of all the digits is equal to the number

import math

def check_armstrong_number(num):
    if (num <= 0):
        print("Invalid number")
        return
    
    # Convert number into String to extract each digit
        
    numberToString = str(num)
    output = 0
    for i in numberToString:
        output += pow(int(i), 3)

    if (output == num):
        return True 
    else:
        return False


def find_armstrong_number():
    armstrong_numbers = []
    num_list = [786, 371, 225, 407, 87, 370, 32, 153, 13, 9, 1634]
    
    for i in num_list:
        result =check_armstrong_number(i)
        if result == True:
            armstrong_numbers.append(i)
            print(f"The num {i} is an Armstrong number")

    print(f"List of Armstrong No. {armstrong_numbers}")    

find_armstrong_number()