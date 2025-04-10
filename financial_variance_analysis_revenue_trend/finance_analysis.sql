SELECT 
  Month,
  Product,
  Budget_Revenue,
  Actual_Revenue,
  ROUND(Actual_Revenue - Budget_Revenue, 2) AS Revenue_Variance,
  ROUND((Actual_Revenue - Budget_Revenue) * 100.0 / Budget_Revenue, 2) AS Variance_Percentage,
  Cost,
  ROUND(Actual_Revenue - Cost, 2) AS Gross_Profit,
  ROUND((Actual_Revenue - Cost) * 100.0 / Actual_Revenue, 2) AS Gross_Margin_Percent
FROM financials
ORDER BY Month, Product;