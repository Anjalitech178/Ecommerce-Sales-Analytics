USE ecommerce_analytics;

-- 1. Total Sales, Profit and Quantity
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM sales_data;

-- 2. Sales by Category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 3. Profit by Region
SELECT
    Region,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales_data
GROUP BY Region
ORDER BY Total_Profit DESC;

-- 4. Sales by Customer Segment
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales_data
GROUP BY Segment
ORDER BY Total_Sales DESC;