x = 10
y = 20       ## Comparison Operators: Used to compare values and return a boolean

print(x == y) # False, because 10 is not equal to 20
print(x != y) # True, because 10 is not equal to 20
print(x <= y) # True, because 10 is less than or equal to 20

              # Boolean (True or False)


a = True
b = False     ## Logical Operators: Used to combine conditional statements

print(a and b) # False, because both conditions are not true
print(a or b)  # True, because one of the conditions is true
print(not a)   # False, because 'not' reverse the condition


age = 18       ## Control Flow Statements: Allows code to make decisions and repeat actions

if age < 18:    # The if checks the first condition; if it's false
    print("Minor")
elif age == 18: # elif provides another option
    print("Just became an adult")
else:           # else covers any other cases
    print("Adult")        


count = 0       ## While Loop:
while count < 5: # Repeats code as long as condition is true
    print(count)
    count += 1   # This loop will print numbers from 0 to 4, 
                 # as count is incremented each time it reaches 5


for i in range(5): ## For Loop:
    print(i)        # Iterates over a sequence (like a list, tuple, or range)

#The modulus operator (%) gives you the remainder when you divide one number by another. So, i % 2 means "divide i by 2 and give me the remainder."

#Here's how it works in the context of even and odd numbers:

#Even numbers are exactly divisible by 2 (they leave no remainder). So, for even numbers, i % 2 will be 0.
#Odd numbers leave a remainder of 1 when divided by 2. So, for odd numbers, i % 2 will be 1.
#In our for loop example, if i % 2 == 0 checks if i is even:

#If i % 2 is 0, i is even, so we print it.
#If i % 2 is 1, i is odd, and we skip the print statement.

### File Handling

with open('your_file.txt', 'r') as file:  # Open the file in read mode
    lines = file.readlines()  # Read all lines into a list
    line_count = len(lines)  # Get the number of lines
    print("Number of lines:", line_count)  # Print the result

## Opening a File: Use open(filename, mode) to open a file. Common modes are:

#'r' for reading (default mode).
#'w' for writing (overwrites the file if it exists, creates a new one if it doesn’t).
#'a' for appending (adds to the file without overwriting).

## Closing a File: Always close a file after you’re done with it by using file.close() 
    # or, better yet, using a with statement that automatically closes the file.