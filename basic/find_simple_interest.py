# Find the Simple Interest

# Simple Interest Formula

# SI = Prinicpal * Rate * Time / 100

def find_simple_interest(prinicpal, rate, time):
    # Error Handling
    try:
        if (prinicpal <=0 or rate <=0 or time <=0):
            print("Invalid or Missing Principal, Rate Or Time")
    except SyntaxError:
        print(f"Error: Please check Syntax Error")
        # return
    else:
        # Find the Simple Interest
        simple_interest = prinicpal * rate * time / 100
        # Turn Simple Interest to Integer
        si = int(simple_interest)
        print(f"The Simple Interest is {si}")

def calc_simple_interest():
    try:
        find_simple_interest(0, 5, 10)
    except Exception as e:
        print(f"Error: {e}")

calc_simple_interest()