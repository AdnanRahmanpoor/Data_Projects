-- ---------------------------
-- 🎯 DEPARTMENTS TABLE
-- ---------------------------
CREATE TABLE departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
);

-- Stores department lookup data.
-- Referenced in `employees` and `transfers`.

-- ---------------------------
-- 🧍 EMPLOYEES TABLE
-- ---------------------------
CREATE TABLE employees (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT,
    Gender TEXT,
    Age INTEGER,
    JoinDate DATE,
    DepartmentID INTEGER,
    Location TEXT,
    FOREIGN KEY (DepartmentID) REFERENCES departments(DepartmentID)
);

-- Stores personal employee data + current department.
-- Will join with job_history, performance, transfers.

-- ---------------------------
-- 🧾 JOB HISTORY TABLE
-- ---------------------------
CREATE TABLE job_history (
    EmployeeID INTEGER,
    RoleStartDate DATE,
    JobTitle TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID)
);

-- Tracks all roles an employee had over time.
-- Used to infer promotions & tenure-based movements.

-- ---------------------------
-- 🏆 PERFORMANCE REVIEWS
-- ---------------------------
CREATE TABLE performance (
    EmployeeID INTEGER,
    ReviewYear INTEGER,
    Score INTEGER,
    FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID)
);

-- Annual performance review data from 2020–2023.

-- ---------------------------
-- 🔁 TRANSFERS TABLE
-- ---------------------------
CREATE TABLE transfers (
    EmployeeID INTEGER,
    TransferDate DATE,
    FromDepartmentID INTEGER,
    ToDepartmentID INTEGER,
    FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID),
    FOREIGN KEY (FromDepartmentID) REFERENCES departments(DepartmentID),
    FOREIGN KEY (ToDepartmentID) REFERENCES departments(DepartmentID)
);

-- Tracks when employees switched departments.
-- Useful for analyzing department movement trends.

-- Analysis Queries

-- Employees with 2+ Job Title Changes (i.e. Promotions)
SELECT 
    e.EmployeeID,
    e.Name,
    COUNT(j.JobTitle) AS NumRoles,
    MIN(j.RoleStartDate) AS FirstRoleDate,
    MAX(j.RoleStartDate) AS LastRoleDate
FROM employees e
JOIN job_history j ON e.EmployeeID = j.EmployeeID
GROUP BY e.EmployeeID
HAVING COUNT(j.JobTitle) >= 2
ORDER BY NumRoles DESC;

-- 2: Average Time Between Promotions (Using Window Functions)
WITH ranked_roles AS (
  SELECT 
    EmployeeID,
    RoleStartDate,
    ROW_NUMBER() OVER (PARTITION BY EmployeeID ORDER BY RoleStartDate) AS rn
  FROM job_history
),
role_diffs AS (
  SELECT 
    r1.EmployeeID,
    julianday(r2.RoleStartDate) - julianday(r1.RoleStartDate) AS DaysBetween
  FROM ranked_roles r1
  JOIN ranked_roles r2 
    ON r1.EmployeeID = r2.EmployeeID AND r1.rn = r2.rn - 1
)
SELECT 
  AVG(DaysBetween)/365.0 AS AvgYearsBetweenPromotions
FROM role_diffs;

-- 3: Average Performance Score by Department (Latest Year)
SELECT 
    d.DepartmentName,
    ROUND(AVG(p.Score), 2) AS AvgPerformance2023
FROM employees e
JOIN departments d ON e.DepartmentID = d.DepartmentID
JOIN performance p ON e.EmployeeID = p.EmployeeID
WHERE p.ReviewYear = 2023
GROUP BY d.DepartmentName
ORDER BY AvgPerformance2023 DESC;

-- 4: Most Transferred Departments

SELECT 
    d.DepartmentName,
    COUNT(*) AS TransfersOut
FROM transfers t
JOIN departments d ON t.FromDepartmentID = d.DepartmentID
GROUP BY d.DepartmentName
ORDER BY TransfersOut DESC;


-- 5: Top Performers: Employees with all scores = 5
SELECT 
    e.EmployeeID,
    e.Name,
    COUNT(*) AS NumReviews
FROM performance p
JOIN employees e ON e.EmployeeID = p.EmployeeID
GROUP BY p.EmployeeID
HAVING MIN(p.Score) = 5 AND MAX(p.Score) = 5;

-- 6: Promotion Lag Risk: 5+ Years in Same Role

WITH role_span AS (
  SELECT 
    EmployeeID,
    MIN(RoleStartDate) AS FirstRoleDate,
    MAX(RoleStartDate) AS LastRoleDate,
    COUNT(*) AS RoleCount
  FROM job_history
  GROUP BY EmployeeID
)
SELECT 
  e.EmployeeID,
  e.Name,
  ROUND((julianday('now') - julianday(r.FirstRoleDate)) / 365.0, 1) AS YearsInRole
FROM role_span r
JOIN employees e ON e.EmployeeID = r.EmployeeID
WHERE r.RoleCount = 1 AND (julianday('now') - julianday(r.FirstRoleDate)) > (5 * 365);