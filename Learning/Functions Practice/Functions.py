# Function to Add Two Numbers
def add_numbers( num1, num2):
    return num1 + num2      # Return the sum of num1 and num2

print(add_numbers(4,6))


# Function to Check if a Number is Prime
def is_prime(number):
    if number < 2 : 
        return 'Not Prime' # Early exit for numbers less than 2
    
    for i in range(2, int(number**0.5) + 1): # Loop from 2 to square root of number
        if number % i == 0: # Check if 'number' is divisible by 'i'
            return 'Not Prime' # If it is, return 'Not Prime' immediately
        
    return 'Prime'  # If no divisors found, number is prime

print(is_prime(7)) # Replace 7 with any number to check