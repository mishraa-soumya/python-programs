# Program to read a text file word by word

# Approach 1: Using the split method to read a file

def read_file_using_split(file_name):
    try:
        with open(file_name, "r") as file: # opening a file in "read" mode and stored it in "file"
            print(f"Reading the file {file_name} word by word:")
            for line in file: # Iterating over each line from the file
                for word in line.split(): # split method is used to break the line by word
                    print(word)
    except Exception as error:
        print(f"Error: {error}")

# Approach 2: Using the Generators

def read_file_using_generators(file_name):
    try:
        with open(file_name, "r") as file:
            print(f"Reading file {file_name} using generators: \n")
            for line in file:
                for word in line.split():
                    yield word
    except Exception as error:
        print(f"Error while reading file: {error}")

def read_file():
    read_txt_file = "/Library/WebServer/Documents/projects/python-projects/python-programs/file-handling/test_file.txt"
    # Reading using split method
    read_file_using_split("/Library/WebServer/Documents/projects/python-projects/python-programs/file-handling/test_file.txt")
    # Reading using Generators
    for w in read_file_using_generators(read_txt_file):
        print(w)

#Calling the Main Program
read_file()