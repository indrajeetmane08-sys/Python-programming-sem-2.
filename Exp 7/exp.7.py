# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:11:03 2026

@author: indra
"""
class Employee:
    def __init__(self, name, emp_id, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary

    def calculate_gross_salary(self):
        # Standard allowances
        hra = 0.2 * self.basic_salary # 20% HRA
        da = 0.1 * self.basic_salary # 10% DA
        gross_salary = self.basic_salary + hra + da
        return gross_salary

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Gross Salary: {self.calculate_gross_salary()}")


# Example usage
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary: "))

emp = Employee(name, emp_id, basic_salary)

print("\nEmployee Details:")
emp.display_details()

