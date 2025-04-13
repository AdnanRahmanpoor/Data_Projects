# 🧠 **Insight Summaries**

#### **Query 1: Employees with 2+ Job Title Changes (Promotions)**  
**SQL Purpose:** Identify employees who have held 2+ roles (indicating promotions).  
**Key Findings:**  
- 117 employees have 3 roles (2 promotions), while 125 employees have 2 roles (1 promotion).  
- Frequent promotions are concentrated in departments like **Sales** and **Product** (visible in cross-referenced department data).  
- Top promotable employees: **Anthony Li**, **Joshua Lozano**, and **Lorraine Turner** (3 roles each).  
📊 *Example Data:*

| EmployeeID | Name             | NumRoles |  
|------------|------------------|----------|  
| 493        | Anthony Li       | 3        |  
| 490        | Joshua Lozano    | 3        |  

---

#### **Query 2: Average Time Between Promotions**  
**SQL Purpose:** Calculate the average time employees wait between promotions.  
**Key Findings:**  
- **Avg time between promotions: 1.0 years.**  
- Rapid promotion cycles suggest a culture prioritizing internal mobility but may risk burnout if not managed.  

---

#### **Query 3: Average Performance Score by Department**  
**SQL Purpose:** Measure department performance based on 2023 review scores.  
**Key Findings:**  
- **Top Performers:** Sales (3.21), Finance (3.2), HR (3.06).  
- **Lowest Performance:** Engineering (2.83).  
- High-performing departments (Sales/Finance) correlate with frequent promotions and transfers.  
📊 *Performance Rankings:*  

| Department   | AvgPerformance2023 |  
|--------------|--------------------|  
| Sales        | 3.21               |  
| Engineering  | 2.83               |  

---

#### **Query 4: Most Transferred Departments**  
**SQL Purpose:** Identify departments with the highest internal transfers.  
**Key Findings:**  
- **Product (26 transfers)** and **Finance (25 transfers)** lead in movement.  
- High transfers may indicate dynamic teams or instability.  
- Engineering has the fewest transfers (17), suggesting stagnation.  

---

#### **Query 5: Top Performers (All Scores = 5)**  
**SQL Purpose:** Find employees with consistently perfect performance scores.  
**Key Findings:**  
- **10 employees** achieved max scores (5/5) across all reviews.  
- Example: **Sheila Evans**, **Nathan Freeman**, and **Kyle Phillips** (4 reviews each).  
📊 *Example Data:*  

| EmployeeID | Name            | NumReviews |  
|------------|-----------------|------------|  
| 18         | Sheila Evans    | 4          |  

---

#### **Query 6: Promotion Lag Risk (5+ Years in Role)**  
**SQL Purpose:** Flag employees stagnant in the same role for 5+ years.  
**Key Findings:**  
- **64 employees** are retention risks, including **Donald Walker (8.1 years)** and **Amanda Davis (8.5 years)**.  
- Stagnation is most common in **HR** and **Engineering**.  

---

## 💡 **Final Recommendations**  
1. **Mitigate Retention Risks:** Initiate career path discussions for employees with 5+ years in the same role (e.g., Engineering’s Donald Walker).  
2. **Improve Engineering Performance:** Investigate low scores in Engineering—provide training or mentorship programs.  
3. **Leverage High Mobility in Product/Finance:** Use frequent transfers to foster cross-department collaboration and knowledge sharing.  
4. **Recognize Top Performers:** Reward employees like Sheila Evans (perfect scores) to maintain engagement.  
5. **Audit Promotion Pace:** Ensure 1-year promotion cycles are sustainable and tied to skill development.  

---
