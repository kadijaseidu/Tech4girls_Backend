#!/usr/bin/python3
class BankAccount:
    """class variable for the bank name"""
    bank_name = "Tech4Girls Bank"

    def __init__(self, account_holder,):
        """instance variables for the account holder's name and balance initialized to 0"""
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self,amount):
        """add money to the account"""
        self.balance += amount
        print(f"{amount} has been deposited into your account\nCurrent balance: {self.balance}")
        
    def withdraw(self, amount):
        """deduct money from the account and ensuring balance doesn't go negative"""
        if self.balance < amount:
            print("Insufficient funds for this withdrawal")
        else:
           self.balance -= amount
           print(f"You have withdrawn {amount} from your account\nCurrent balance: {self.balance}")


    @staticmethod
    def bank_policy():
        """print a generic policy message"""
        print("Welcome to Tech4Girls Bank. We are committed to providing a safe and secure banking experience for all our customers.")

    @classmethod
    def get_bank_name(cls,):
        """return the bank name"""
        return cls.bank_name
    
"""Demostrating instances for the BankAccount class"""
bankaccount1 = BankAccount("Linda")

"""call static method to print the bank policy"""
bankaccount1.bank_policy()
bankaccount1.deposit(1000)
bankaccount1.withdraw(500)

"""withdrawing more than the amount"""
bankaccount1.withdraw(1500)
print(bankaccount1.get_bank_name())

"""create an instance for Alex"""
bankaccount2 = BankAccount("Alex")
bankaccount2.bank_policy()
bankaccount2.deposit(800)
bankaccount2.withdraw(300)
"""printing and calling the class method to get the bank name"""
print(bankaccount2.get_bank_name())