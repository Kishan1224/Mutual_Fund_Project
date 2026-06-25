SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
strftime('%m', nav_date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

SELECT
strftime('%Y', transaction_date) AS year,
COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='Sip'
GROUP BY year;

SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state;

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

SELECT
AVG(expense_ratio_pct)
FROM fact_performance;

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;

SELECT
transaction_type,
AVG(amount)
FROM fact_transactions
GROUP BY transaction_type;