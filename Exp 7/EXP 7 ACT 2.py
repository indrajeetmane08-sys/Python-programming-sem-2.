# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:15:02 2026

@author: indrajeet
"""

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self, bonus):
        if bonus < 0:
            print("Invalid bonus amount")
            return self.basic_salary
        total_salary = self.basic_salary + bonus
        return total_salary

    def display(self, bonus):
        total = self.calculate_salary(bonus)
        print(f"Employee Name: {self.name}")
        print(f"Basic Salary: ₹{self.basic_salary}")
        print(f"Bonus: ₹{bonus}")
        print(f"Total Salary: ₹{total}")


# Example usage
emp1 = Employee("indrajeet", 20000)
emp1.display(10000)
