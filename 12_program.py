# Q13 (7.5 Marks): Write a Python program using OOP to create a BankAccount class with:
# • deposit()
# • withdraw()
# • display_balance()
# Ensure withdraw doesn't allow balance to go negative.
# Create an object and demonstrate all methods.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current balance: ${self.balance:.2f}")     
# Demonstration of the BankAccount class
account = BankAccount(100)  # Create an account with an initial balance of $100
account.display_balance()    # Display the current balance
account.deposit(50)         # Deposit $50
account.display_balance()    # Display the current balance
account.withdraw(30)        # Withdraw $30
account.display_balance()    # Display the current balance
account.withdraw(150)       # Attempt to withdraw $150 (should fail)
account.display_balance()    # Display the current balance
