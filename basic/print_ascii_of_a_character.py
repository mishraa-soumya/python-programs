# Program to take user input for a character and print the ASCII code of the character

def get_ascii_code(char):
    return ord(char)

def print_ascii():
    userInput = input("Enter any character to print it's ASCII code ")
    if (userInput):
        try:
            char_code = get_ascii_code(str(userInput))
        except Exception as error:
            print(f"Exception: {error}")
            return
        else:
            print(f"ASCII Code for Char {userInput} = {char_code}")
            return

print_ascii()