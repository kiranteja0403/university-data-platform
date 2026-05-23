import pandas as pd

students = pd.read_csv("data/students.csv")
staff = pd.read_csv("data/staff.csv")
budget = pd.read_csv("data/budget.csv")

print("Students data:")
print(students.head())

print("\nStaff data:")
print(staff.head())

print("\nBudget data:")
print(budget.head())
