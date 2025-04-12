import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

n = 5000
departments = ['Engineering', 'HR', 'Marketing', 'Sales', 'Product']
locations = ['Dubai', 'New York', 'Berlin', 'Remote']
genders = ['Male', 'Female', 'Other']
attrition_reasons = ['Better offer', 'Lack of growth', 'Manager conflict', 'Relocation', 'Retired']

data = []

for i in range(n):
    join_year = random.randint(2012, 2022)
    join_date = pd.Timestamp(f"{join_year}-{random.randint(1,12)}-{random.randint(1,28)}")
    today = pd.Timestamp("2025-04-01")
    tenure_years = (today - join_date).days // 365
    
    last_promotion = join_date + pd.Timedelta(days=365*random.randint(0, tenure_years if tenure_years > 0 else 1))
    
    left = np.random.choice([0, 1], p=[0.7, 0.3])  # 30% attrition
    attrition_reason = np.random.choice(attrition_reasons) if left else None

    data.append({
        'EmployeeID': i+1,
        'JoinDate': join_date,
        'LastPromotionDate': last_promotion,
        'Age': random.randint(22, 55),
        'Gender': random.choice(genders),
        'Department': random.choice(departments),
        'Location': random.choice(locations),
        'JobLevel': random.randint(1, 5),
        'EngagementScore': np.clip(np.random.normal(6.5, 2), 1, 10),
        'PerformanceScore': np.clip(np.random.normal(3.5, 1), 1, 5),
        'ManagerSatisfaction': np.clip(np.random.normal(3.5, 1.2), 1, 5),
        'NumTrainingsCompleted': random.randint(0, 10),
        'TenureYears': tenure_years,
        'LeftCompany': left,
        'AttritionReason': attrition_reason
    })

df = pd.DataFrame(data)
df.to_csv("employee_metrics.csv", index=False)
