# Program to read a text file word by word

# Approach 1: Using the split method to read a file

def read_file_using_split(file_name):
    try:
        with open(file_name, "r") as file: # opening a file in "read" mode and stored it in "file"
            for line in file: # Iterating over each line from the file
                print(f"Reading the file {file_name} word by word:")
                for word in line.split(): # split method is used to break the line by word
                    print(word)
    except Exception as error:
        print(f"Error: {error}")



def read_file():
    # Reading using split method
    read_file_using_split("/Library/WebServer/Documents/projects/python-projects/python-programs/file-handling/test_file.txt")

#Calling the Main Program
read_file()