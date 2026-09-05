-- Query 1: Top 5 funds by AUM
SELECT
    amfi_code,
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- Query 2: Average NAV by month
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date)
ORDER BY month;


-- Query 3: SIP transaction growth by year
SELECT
    strftime('%Y', transaction_date) AS year,
    COUNT(*) AS sip_transactions,
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY strftime('%Y', transaction_date)
ORDER BY year;


-- Query 4: Transactions by state
SELECT
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- Query 5: Funds with expense ratio below 1%
SELECT
    amfi_code,
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;

-- Query 6: Transaction count by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;


-- Query 7: Top 10 funds by 1-year return
SELECT
    amfi_code,
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;


-- Query 8: Average returns by fund category
SELECT
    category,
    ROUND(AVG(return_1yr_pct), 2) AS avg_1yr_return,
    ROUND(AVG(return_3yr_pct), 2) AS avg_3yr_return,
    ROUND(AVG(return_5yr_pct), 2) AS avg_5yr_return
FROM fact_performance
GROUP BY category
ORDER BY avg_1yr_return DESC;


-- Query 9: KYC status distribution
SELECT
    kyc_status,
    COUNT(*) AS investor_transactions
FROM fact_transactions
GROUP BY kyc_status
ORDER BY investor_transactions DESC;


-- Query 10: Top 10 cities by total transaction amount
SELECT
    city,
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY city, state
ORDER BY total_amount DESC
LIMIT 10;