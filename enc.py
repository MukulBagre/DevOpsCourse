class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid amount!")

    @property
    def balance(self):
        """Getter method to access the private balance."""
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(200)      
print(account.balance)     

account.__balance = 0

print(account.__balance)

print(account.__dict__)