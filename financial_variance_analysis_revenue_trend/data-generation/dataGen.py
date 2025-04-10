import pandas as pd
import numpy as np
from faker import Faker
import sqlite3

fake = Faker()
np.random.seed(42)

months = pd.date_range(start='2024-01-01', end='2024-12-01', freq='MS')
product_lines = ['Property Listings', 'Premium Ads', 'Memberships']

data = []
for month in months:
    for product in product_lines:
        budget = np.random.randint(50000, 120000)
        actual = budget + np.random.randint(-15000, 15000)
        cost = actual * np.random.uniform(0.4, 0.7)
        data.append([month.strftime('%Y-%m'), product, budget, actual, round(cost)])

df = pd.DataFrame(data, columns=['Month', 'Product', 'Budget_Revenue', 'Actual_Revenue', 'Cost'])

# Save to SQLite
conn = sqlite3.connect("../data/finance_data.db")
df.to_sql("financials", conn, if_exists="replace", index=False)
conn.close()
