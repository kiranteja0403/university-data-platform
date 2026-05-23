import pandas as pd

students = pd.read_csv("data/students.csv")
staff = pd.read_csv("data/staff.csv")
budget = pd.read_csv("data/budget.csv")

print("Students missing values:")
print(students.isnull().sum())

print("\nStaff missing values:")
print(staff.isnull().sum())

print("\nBudget missing values:")
print(budget.isnull().sum())

print("\nStudents duplicate rows:", students.duplicated().sum())
print("Staff duplicate rows:", staff.duplicated().sum())
print("Budget duplicate rows:", budget.duplicated().sum())
