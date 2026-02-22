class BankAccount:
    bankName = "HDFC Bank"
    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.__balance = balance
    def show_details(self):
        print("Name: ", self.name)
        print("Account No.: ", self.accno)
        print("Balance: ", self.__balance)
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully.")
    def getBalance(self):
        return self.__balance
    
    def withdraw(self,amtWithdraw):
        if amtWithdraw >= self.__balance:
            print("No funds!")
        else:
            self.__balance -= amtWithdraw
 
class SavingsAccount(BankAccount):
    pass
class CurrentAccount(BankAccount):
    pass
class SalaryAccount(BankAccount):
    pass