# Program 2: Read a file character by character

# Approach1: Manual read char by char

def read_by_char(file_name):
    # Read 1 character at a time
    read_single_character(file_name)

    # Read Multi Character
    read_multiple_character(file_name, char_num = 4)


def read_single_character(file_name):
    # Using for loop
    with open(file_name, "r") as file: # reading a file
        for line in file:
            for char in line: # reads 1 character at a time from the line.
                print(f"char: {char}")

def read_multiple_character(file_name, char_num):
    file = open(file_name, "r")
    print(f"Reading {char_num} character at a time from file: {file_name}")
    while 1:
        char = file.read(char_num) # Includes spaces and special chracters
        if not char:
            break
        print(char)

    print("Closing the file")
    file.close()

def read_file():
    file_name = "/Library/WebServer/Documents/projects/python-projects/python-programs/file-handling/test_file.txt"
    # read char by char
    read_by_char(file_name)

read_file()
