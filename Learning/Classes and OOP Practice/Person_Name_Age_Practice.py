# Person class (name & age)
class Person:
    def __init__(self, name, age): # Initialize with name and age
        self.name = name # Assign name to the instance
        self.age = age # Assign age to the instance

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}") # Print details of the person        

person1 = Person("Alice", 30)
person1.print_details()  # Should print: Name: Alice, Age: 30
