# 🏙️ Dubai Real Estate Market Performance Dashboard (2023 vs 2024)

## 📌 Project Overview

This project analyzes and visualizes **Dubai real estate market performance** using real-world listing data from 2023 and 2024. The goal is to uncover trends in pricing, volume, and property types across time and regions, and to provide a comparative dashboard for stakeholders and investors.

> 📅 **Time Period Analyzed**: January 2023 – December 2024  
> 📍 **Location**: Dubai, UAE  
> 🧑‍💻 **Role**: Data Analyst (solo project)

---

## 🎯 Objectives

- Clean and preprocess real estate listings data
- Exclude incomplete years (2021, 2022) due to data sparsity
- Conduct year-over-year exploratory data analysis (EDA)
- Identify trends in property prices, volume, and types
- Build a Power BI dashboard for business users and real estate stakeholders *(INCOMPLETE)*

---

## 📂 Dataset Details

| Column Name                 | Description                                  |
|----------------------------|----------------------------------------------|
| `price`                    | Listing price in AED                         |
| `price_category`           | Binned pricing category                      |
| `type`                     | Property type (e.g., Apartment, Villa)       |
| `beds`, `baths`            | Number of bedrooms and bathrooms             |
| `address`, `building_name` | Property location details                    |
| `furnishing`               | Furnishing status (Furnished, Unfurnished)   |
| `completion_status`        | Off-plan or completed                        |
| `post_date`                | Listing post date                            |
| `year`                     | Extracted from post_date                     |
| `total_building_area_sqft`| Total built-up area                          |
| `area_name`, `city`        | Geolocation fields                           |
| `Latitude`, `Longitude`    | For geospatial mapping                       |

---

## 🧹 Data Cleaning Summary

- Removed listings from 2021 and 2022 due to insufficient volume
- Treated outliers in `price` and `price_per_sqft`
- Calculated monthly/yearly aggregates for trend analysis
- Exported a clean CSV for dashboarding

---

## 📊 EDA Highlights

- 📈 **Listing Volume**: 2024 had a significant increase in property listings compared to 2023.
- 💸 **Pricing Trends**: Average prices remained stable, but there was an uptick in ultra-high-value listings in 2024.
- 🏘️ **Property Type Shift**: Shift toward villas and townhouses in 2024.
- 🌍 **Top Areas**: Key areas like Palm Jumeirah and Downtown Dubai dominated both years but with shifting ranks.

---

## 📈 Power BI Dashboard (INCOMPLETE)

**Sections:**
- KPI Cards (Total Listings, Avg Price, Avg Price/SqFt)
- Year-over-Year Trend Charts
- Property Type Distribution
- Top 10 Areas by Avg Price
- (Optional) Geo Heatmap using Latitude/Longitude

➡️ Exported data: `real_estate_2023_2024_cleaned.csv`

---

## 🧠 Key Insights

- Dubai's property market is expanding rapidly post-COVID, with consistent demand in luxury segments.
- Emerging neighborhoods in 2024 indicate growing investor interest beyond traditional hotspots.
- Year-over-year comparisons enable stakeholders to make informed decisions on pricing strategy and location targeting.

---

## 🛠️ Tools & Tech

- **Python** (Pandas, Seaborn, Matplotlib)
- **Jupyter Notebook**
- **Power BI** (Dashboarding and interactive visuals)
- **VS Code / GitHub** for documentation and version control

---

## 📁 Folder Structure

```
dubai_real_estate_market_performance/
│
├── data/
│   └── dubai_real_estate_sales.csv
│   
├── real_estate_market_analysis.ipynb
│
├── real_estate_market_report.pdf
│
└── README.md

```
---

## 📬 Contact

**Author**: Adnan Rahmanpoor  
📧 [adnanrahmanpoor@gmail.com](mailto:adnanrahmanpoor@gmail.com)  
🌐 [www.alhilaldataservices.com](https://www.alhilaldataservices.com)

---

> ⭐ *If you found this project helpful, feel free to connect or share!*
