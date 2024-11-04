# Bank Account class (deposit, withdrawl, check_balance)
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance # Set initial balance

    def deposit(self, amount):
        self.balance += amount # Add amount to balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount # Subtract amount if balance is sufficient
        else:
            print("Insufficient funds")            

    def check_balance(self):
        print(f"Current balance: ${self.balance}")     

account = BankAccount(100)  # Start with a balance of 100
account.deposit(50)          # Add 50 to balance
account.withdraw(30)         # Subtract 30 from balance
account.check_balance()       # Should print: Current balance: $120