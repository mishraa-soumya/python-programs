# Print Prime Numbers between Intervals

# Prime Number: Divisible by 1 or the number itself

def print_prime_numbers(min, max):
    primeRange = range(min, max+1)

    for num in primeRange:
        if (num <= 1):
            continue

        for i in range(2, num):
            if (num % i == 0):
                # print(f"The number {num} is not a Prime Number")
                break # if num is divisible by any no. starting from 2, then it is not a prime number
        else:
            print(f"The number {num} is a Prime Number")

print_prime_numbers(900, 1000)