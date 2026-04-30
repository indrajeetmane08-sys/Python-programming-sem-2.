# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:12:29 2026

@author: indrajeet
"""

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")


# Example usage
acc1 = BankAccount("indrajeet", 1000)

acc1.deposit(500)
acc1.withdraw(300)
acc1.display_balance()
