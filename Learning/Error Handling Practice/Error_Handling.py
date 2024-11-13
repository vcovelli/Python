try:
    user_input = input("Please enter a number: ") # Ask for input
    number = float(user_input) # Try to convert to a number (you can use int() for whole numbers)
    print("You entered the number:", number) # Print the number if conversion succeeds
except ValueError:
    print("That's not a valid number! Please enter a numeric value.") # Error message if input is not a number  