# Line Writer
lines_to_write = ["Hello, World!", "Welcome to file handling.", "This is a test."]

with open('output_file.txt', 'w') as file: # Open the file in write mode
    for line in lines_to_write: # Loop through each string in the list
        file.write(line + '\n') # Write the string with a newline