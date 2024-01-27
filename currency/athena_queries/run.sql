-- get data for current day
SELECT *
FROM currency_data
WHERE year = CAST(DATE_FORMAT(CURRENT_DATE, '%Y') AS INTEGER)
  AND month = CAST(DATE_FORMAT(CURRENT_DATE, '%m') AS INTEGER)
  AND day = CAST(DATE_FORMAT(CURRENT_DATE, '%d') AS INTEGER);

-- get max currencies for current month
SELECT 
    target_currency,
    MAX(usd) AS max_usd,
    MAX(eur) AS max_eur,
    MAX(gbp) AS max_gbp
FROM currency_data
WHERE 
    year = CAST(DATE_FORMAT(CURRENT_DATE, '%Y') AS INTEGER)
    AND month = CAST(DATE_FORMAT(CURRENT_DATE, '%m') AS INTEGER)
    AND day IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
                24, 25, 26, 27, 28, 29, 30, 31)
GROUP BY target_currency;