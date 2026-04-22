# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 06:18:41 2026

@author: indrajeet
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        grade = self.calculate_grade()
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {grade}")


# Example usage
stu1 = Student("indrajeet", 82.40)
stu1.display()
