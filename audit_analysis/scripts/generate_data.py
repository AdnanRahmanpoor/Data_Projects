from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)

# --- Create data directory ---
os.makedirs("data", exist_ok=True)

# --- General Ledger ---
def generate_general_ledger(n=1000):
    data = []
    for _ in range(n):
        date = fake.date_between(start_date='-6M', end_date='today')
        time = fake.time()
        user = fake.user_name()
        account = random.choice(['1001-Cash', '4001-Revenue', '5001-COGS', '2001-AP', '3001-Equity'])
        amount = round(random.uniform(-50000, 50000), 2)
        desc = fake.sentence(nb_words=6)
        data.append([date, time, user, account, amount, desc])
    df = pd.DataFrame(data, columns=['date', 'time', 'user', 'account', 'amount', 'description'])
    df.to_csv("data/general_ledger.csv", index=False)

# --- Vendor Master ---
def generate_vendors(n=50):
    data = []
    for _ in range(n):
        name = fake.company()
        vendor_id = fake.uuid4()
        data.append([vendor_id, name])
    df = pd.DataFrame(data, columns=['vendor_id', 'vendor_name'])
    df.to_csv("data/vendors.csv", index=False)

# --- Vendor Payments ---
def generate_vendor_payments(n=500):
    vendors = pd.read_csv("data/vendors.csv")
    data = []
    for _ in range(n):
        vendor = vendors.sample(1).iloc[0]
        date = fake.date_between(start_date='-6M', end_date='today')
        amount = round(random.uniform(100, 10000), 2)
        invoice_no = fake.unique.bothify(text='INV-####')
        data.append([vendor['vendor_id'], vendor['vendor_name'], date, amount, invoice_no])
    df = pd.DataFrame(data, columns=['vendor_id', 'vendor_name', 'payment_date', 'amount', 'invoice_no'])
    df.to_csv("data/vendor_payments.csv", index=False)

# --- Employee Expenses ---
def generate_employee_expenses(n=300):
    data = []
    for _ in range(n):
        emp_id = fake.unique.random_int(min=1000, max=9999)
        name = fake.name()
        date = fake.date_between(start_date='-6M', end_date='today')
        category = random.choice(['Travel', 'Meals', 'Supplies', 'Entertainment'])
        amount = round(random.uniform(10, 2000), 2)
        reason = fake.sentence(nb_words=5)
        data.append([emp_id, name, date, category, amount, reason])
    df = pd.DataFrame(data, columns=['employee_id', 'employee_name', 'date', 'category', 'amount', 'description'])
    df.to_csv("data/employee_expenses.csv", index=False)

# --- Run all ---
generate_general_ledger()
generate_vendors()
generate_vendor_payments()
generate_employee_expenses()
