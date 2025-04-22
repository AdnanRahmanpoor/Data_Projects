# 📊 Client Acquisition, Retention & LTV Analysis

This project explores key business metrics—Customer Acquisition Cost (CAC), Client Retention, and Lifetime Value (LTV)—using simulated data to mimic a real-world customer lifecycle. It’s designed to demonstrate data analysis skills relevant for roles in marketing analytics, business intelligence, and customer lifecycle management.

> ✅ Built in Python using pandas, matplotlib, seaborn, and Plotly.

---

## 🔍 Objective

Analyze how marketing spend, acquisition channels, and customer behavior influence revenue outcomes and client value. This is especially aligned with roles involving:

- Customer retention and churn analysis  
- Marketing performance evaluation  
- LTV vs CAC strategy  
- Monthly revenue tracking  

---

## 📂 Datasets

The project uses three synthetic datasets:

- `campaigns.csv`: Marketing spend by acquisition channel  
- `clients.csv`: Client info including acquisition channel and signup date  
- `transactions.csv`: Transaction history per client  

---

## 💡 Key Business Questions

1. **What is the Customer Acquisition Cost (CAC) by channel?**
2. **How does Lifetime Value (LTV) vary across acquisition channels?**
3. **What is the monthly client retention rate by signup cohort?**
4. **How does revenue trend over time?**

---

## 🧪 Analysis Overview

### 📉 Customer Acquisition Cost (CAC)

Calculated as:

CAC = Total Cost per Channel / Number of Clients Acquired


> 📌 **Insight:** Helps evaluate channel efficiency.

### 💰 Client Lifetime Value (LTV)

Total value of all transactions per client, merged with acquisition channel.

> 📌 **Insight:** Highlights the most profitable channels based on average LTV.

### 🔁 Retention Analysis

Built a retention matrix by comparing clients' transaction months to their signup month.

> 📌 **Insight:** Visualized with a heatmap to identify how long clients remain active.

### 📈 Monthly Revenue Trend

Tracked revenue over time by aggregating transaction values monthly.

---

## 📊 Visualizations

- [x] CAC by Channel (Bar Chart – Plotly)
- [x] Distribution of LTV (Histogram – Seaborn)
- [x] Avg LTV by Channel (Bar Chart – Plotly)
- [x] Client Retention Heatmap (Cohort Analysis – Seaborn)
- [x] Monthly Revenue Trend (Line Chart – Plotly)

> You can preview these visualizations directly in the [notebook](./client_ltv_retention_analysis.ipynb)

---

## 🛠️ Tools & Technologies

- Python 3.10  
- pandas, numpy  
- seaborn, matplotlib, plotly.express  
- Jupyter Notebook  

---

## 📥 How to Use

1. Clone the repo or download the notebook:
   ```bash
   git clone https://github.com/adnanrahmanpoor/Data_Projects.git

   cd Data_Projects

2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```
3. Open `client_ltv_retention_analysis.ipynb` in Jupyter or VSCode.

## 📌 Results Summary

- **Channel C had the lowest CAC and highest average LTV** → Most efficient.
- **Client retention dropped sharply after the first 2 months**, indicating potential churn issues.
- **Monthly revenue showed steady growth**, likely driven by new acquisitions.

---

## 🧠 Skills Demonstrated

✅ Data Cleaning & Transformation  
✅ Business Metrics Calculation (CAC, LTV)  
✅ Cohort Retention Analysis  
✅ Data Visualization  
✅ Insight Communication for Business Impact

---

## 📄 License

MIT License  
© 2025 [Adnan Rahmanpoor](https://www.github.com/adnanrahmanpoor)

---

## 🙋‍♂️ Let's Connect

If you're hiring for data roles or want to collaborate on analytics projects:

- 💼 [LinkedIn](https://linkedin.com/in/adnanrahmanpoor)
- 🌐 [alhilaldataservices.com](https://www.alhilaldataservices.com)

---
