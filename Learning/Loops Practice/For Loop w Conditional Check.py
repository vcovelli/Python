# For Loop
for i in range(1,11):
    if i % 2 == 0:  # modulus operator % 
        print(i)

        #The modulus operator (%) gives you the remainder when you divide one number by another. So, i % 2 means "divide i by 2 and give me the remainder."

        #Here's how it works in the context of even and odd numbers:

        #Even numbers are exactly divisible by 2 (they leave no remainder). So, for even numbers, i % 2 will be 0.
        #Odd numbers leave a remainder of 1 when divided by 2. So, for odd numbers, i % 2 will be 1.
        #In our for loop example, if i % 2 == 0 checks if i is even:

        #If i % 2 is 0, i is even, so we print it.
        #If i % 2 is 1, i is odd, and we skip the print statement.