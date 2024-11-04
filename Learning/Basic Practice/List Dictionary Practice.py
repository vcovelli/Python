# List & Sum of list
numbers = [2,4,6,15,67,50] # Name the variable *don't use list
total = sum(numbers)
print(total)


# Dictionary with items & prices
items = {
    "Apples": 5,
    "Oranges": 6,
    "Pears": 4,
    "Plums": 2,
}

total_cost = 0 # Start with a total of 0

for price in items.values():    # Loop through the prices in the dictionary
    total_cost += price     # Add each price to total_cost

print(total_cost)    # Print the final total after the Loop