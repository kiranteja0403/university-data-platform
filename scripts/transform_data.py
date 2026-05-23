import pandas as pd

students = pd.read_csv("data/students.csv")
staff = pd.read_csv("data/staff.csv")
budget = pd.read_csv("data/budget.csv")

avg_gpa = students.groupby("department")["gpa"].mean().reset_index()
avg_gpa.rename(columns={"gpa": "average_gpa"}, inplace=True)

staff_count = staff.groupby("department").size().reset_index(name="staff_count")

budget["utilization_percent"] = (budget["spent_budget"] / budget["allocated_budget"]) * 100

print("Average GPA by department:")
print(avg_gpa)

print("\nStaff count by department:")
print(staff_count)

print("\nBudget utilization by department:")
print(budget)

avg_gpa.to_csv("data/avg_gpa_by_department.csv", index=False)
staff_count.to_csv("data/staff_count_by_department.csv", index=False)
budget.to_csv("data/budget_utilization.csv", index=False)

print("\nTransformed files saved successfully.")
