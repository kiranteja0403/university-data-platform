import pandas as pd

avg_gpa = pd.read_csv("data/avg_gpa_by_department.csv")
staff_count = pd.read_csv("data/staff_count_by_department.csv")
budget = pd.read_csv("data/budget_utilization.csv")

print("=== University Summary Report ===")

print("\nAverage GPA by Department:")
print(avg_gpa)

print("\nStaff Count by Department:")
print(staff_count)

print("\nBudget Utilization:")
print(budget[["department", "utilization_percent"]])
