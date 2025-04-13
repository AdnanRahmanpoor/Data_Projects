import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

n_employees = 500

# Create department list
departments = ['HR', 'Engineering', 'Product', 'Sales', 'Marketing', 'Finance']
job_titles = ['Analyst', 'Senior Analyst', 'Manager', 'Director']

# Create Employees table
employees = []
for emp_id in range(1, n_employees + 1):
    join_date = fake.date_between(start_date='-10y', end_date='-1y')
    employees.append({
        'EmployeeID': emp_id,
        'Name': fake.name(),
        'Gender': random.choice(['Male', 'Female']),
        'Age': random.randint(24, 60),
        'JoinDate': join_date,
        'DepartmentID': random.randint(1, len(departments)),
        'Location': fake.city()
    })

df_employees = pd.DataFrame(employees)
df_departments = pd.DataFrame({'DepartmentID': range(1, len(departments)+1), 'DepartmentName': departments})

# Job History: Each person has 1–3 roles
job_history = []
for emp in df_employees.itertuples():
    num_roles = random.randint(1, 3)
    base_date = datetime.strptime(str(emp.JoinDate), '%Y-%m-%d')
    for i in range(num_roles):
        role_date = base_date + timedelta(days=365*i)
        if role_date >= datetime.today():
            break
        job_history.append({
            'EmployeeID': emp.EmployeeID,
            'RoleStartDate': role_date.date(),
            'JobTitle': random.choice(job_titles)
        })

df_job_history = pd.DataFrame(job_history)

# Performance Reviews
performance = []
for emp in df_employees.itertuples():
    for year in range(2020, 2024):
        performance.append({
            'EmployeeID': emp.EmployeeID,
            'ReviewYear': year,
            'Score': random.randint(1, 5)
        })

df_performance = pd.DataFrame(performance)

# Transfers
transfers = []
for emp in df_employees.itertuples():
    if random.random() < 0.3:
        transfers.append({
            'EmployeeID': emp.EmployeeID,
            'TransferDate': fake.date_between(start_date='-5y', end_date='-1y'),
            'FromDepartmentID': random.randint(1, len(departments)),
            'ToDepartmentID': random.randint(1, len(departments))
        })

df_transfers = pd.DataFrame(transfers)

# Save to CSV
df_employees.to_csv("employees.csv", index=False)
df_departments.to_csv("departments.csv", index=False)
df_job_history.to_csv("job_history.csv", index=False)
df_performance.to_csv("performance.csv", index=False)
df_transfers.to_csv("transfers.csv", index=False)
