import csv

# Sample data
data = [
    ["Name", "Age", "City", "Salary"],
    ["Alice", 30, "New York", 70000],
    ["Bob", 25, "Los Angeles", 50000],
    ["Charlie", 35, "Chicago", 80000],
    ["Diana", 28, "San Francisco", 65000],
    ["Evan", 40, "Seattle", 90000],
    ["Fiona", 29, "Boston", 60000],
    ["George", 33, "Austin", 75000],
    ["Hannah", 27, "Denver", 58000]
]

# Write to CSV
with open("sample_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("sample_data.csv created successfully!")    