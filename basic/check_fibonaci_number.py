# Check if a number is Fibonaci Number

def check_fibonaci_number(num):
    if (num == 0):
       print("Number Zero is a Fibonaci Number")
       return
    elif (num == 1):
        print("Number One is a Fibonaci Number")
        return
    else:
        fibonaci_list = [0,1]
        for n in range(2, num+1):
            nMinusOne = n - 1
            nMinusTwo = n - 2
            print(f"nMinusOne: {nMinusOne}")
            next_num = fibonaci_list[nMinusTwo] + fibonaci_list[nMinusOne]
            
            if (next_num == num):
                print(f"The number {num} is a Fibonaci Number")
                break
            else:
                fibonaci_list.append(next_num)
                continue
        else:
            print(f"The number {num} is not a Fibonaci Number")

def get_user_input():
    print("Input any number and check if it is fibonaci or not!")
    userInput = input("Enter the number!")
    fibonaci_num = int(userInput)

    check_fibonaci_number(int(fibonaci_num))

get_user_input()
