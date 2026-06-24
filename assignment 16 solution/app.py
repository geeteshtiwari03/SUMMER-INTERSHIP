from pyspark import SparkContext
import os

sc = SparkContext("local[*]", "EmployeeAssignment")
sc.setLogLevel("ERROR")

# Read CSV
rdd = sc.textFile("data/employees.csv")

# Remove header
header = rdd.first()
data = rdd.filter(lambda row: row != header)

# Convert each row into list
employees = data.map(lambda x: x.split(","))

# --------------------------------------------------
# TASK 1
# Sort employees by salary descending
# --------------------------------------------------

sorted_employees = employees.sortBy(
    lambda x: int(x[3]),
    ascending=False
)

print("\n===== Employees Sorted By Salary =====")

for emp in sorted_employees.collect():
    print(emp)

# --------------------------------------------------
# TASK 2
# Department Wise Salary Total
# --------------------------------------------------

dept_salary = employees.map(
    lambda x: (x[2], int(x[3]))
)

dept_total = dept_salary.reduceByKey(
    lambda a, b: a + b
)

print("\n===== Department Salary Totals =====")

for dept in dept_total.collect():
    print(dept)

# --------------------------------------------------
# TASK 3
# Top 3 Highest Paid Employees
# --------------------------------------------------

top3 = sorted_employees.take(3)

os.makedirs("output", exist_ok=True)

with open("output/top3_employees.txt", "w") as f:
    for emp in top3:
        f.write(",".join(emp) + "\n")

print("\nTop 3 employees saved to output/top3_employees.txt")

sc.stop()