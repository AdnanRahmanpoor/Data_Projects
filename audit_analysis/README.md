---
 
---
# 🧾 End-to-End Audit Analytics Project 
This project simulates the role of a **Auditor Data Analyst** and walks through a complete **end-to-end audit analytics workflow** using synthetic financial data.

We identify fraud, policy violations, and financial anomalies using **Python, SQL, and Excel**, and generate a full audit report/dashboard in Excel for stakeholders.

## 🚀 Project Overview

This project covers:

1. **General Ledger Analysis**
2. **Vendor Payment Analysis**
3. **Employee Expense Reimbursement Analysis**
4. **Audit Dashboard & Reporting in Excel** *(INCOMPLETE)*

Each section uses synthetic data generated using the [`Faker`](https://faker.readthedocs.io/en/master/) library and applies common audit checks performed during external or internal audits.

---

## 🛠️ Tools & Technologies

| Tool         | Purpose                               |
|--------------|----------------------------------------|
| **Python (Pandas, Faker)** | Data generation, cleaning, audit logic |
| **SQLite (via pandas/sqlite3)** | Run SQL queries and filters       |
| **Excel**     | Final dashboard, pivot tables, formatting |
| **OpenPyXL**  | Export DataFrames to multi-tab Excel   |
| **Jupyter Notebook** | Interactive data exploration/reporting |

---

## ✅ Audit Checks Performed

### 📘 General Ledger
- Round-value entries (estimates/manual)
- Weekend entries (outside normal ops)
- Suspicious descriptions (misc, test, etc.)
- High-value journal entries
- Unusual accounts usage

### 💸 Vendor Payments
- Duplicate payments (vendor + date + amount)
- Large one-off payments (potential fraud)
- Payments made outside working days
- Top vendors by spend
- Descriptive anomalies

### 🧾 Employee Expenses
- Duplicate claims (employee + date + amount)
- Policy violations (meals > 100, etc.)
- Weekend or late-night claims
- Round amounts (fabrication risks)
- Vague descriptions
- Frequent small claims (threshold abuse)
- Top spenders by amount

---

## 📊 Deliverables

- ✅ Cleaned datasets (Ledger, Payments, Expenses)
- ✅ Flagged risk entries with Boolean indicators
- ❌ Summary Dashboard (Excel) with (INCOMPLETE):
  - Key metric tables
  - Pivot tables
  - Charts (Top vendors, category distribution)
  - Conditional formatting to highlight red flags

---

## 📂 Project Structure

```
audit_analysis/
│
├── data/
│   ├── general_ledger.csv
│   ├── vendors.csv
│   ├── vendor_payments.csv
│   ├── employee_expenses.csv
│
├── notebooks/
│   ├── audit_checks.ipynb   <-- core project work
│
├── scripts/
│   ├── generate_data.py     <-- Faker scripts
│
├── audit_report/
│   ├── audit_report.xlsx
└── README.md

```

---

## 📎 Use Cases

- ✅ Resume & Portfolio project for Data Analyst / Audit Analyst roles  
- ✅ Client work showcase for data services agencies  
- ✅ Practice case for audit interview prep  
- ✅ Internal training tool for audit/data teams

---

## 📌 How to Run

1. Clone the repo  
2. Install dependencies  
   ```bash
   pip install pandas faker openpyxl
   ```
3. Run `generate_data.py` or use `audit_checks.ipynb` step by step  
4. Open `audit_report/audit_analysis_report.xlsx` for full dashboard

---

## 👨‍💼 Author

Built by a solo data analyst simulating audit fieldwork for portfolio and job-readiness.

Connect on [LinkedIn](https://www.linkedin.com/in/adnanrahmanpoor) | Explore more at [Al Hilal Data Services](https://www.alhilaldataservices.com)

---

## 📘 License

This project is for **educational & portfolio use only**. You are free to reuse or modify for personal use or job applications.
```
