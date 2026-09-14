USE uber_analytics;

-- 1. Trips by hour
SELECT
    HOUR,
    COUNT(*) AS total_trips
FROM uber_trips
GROUP BY HOUR
ORDER BY HOUR;


-- 2. Trips by day of week
SELECT
    DAY_OF_WEEK,
    COUNT(*) AS total_trips
FROM uber_trips
GROUP BY DAY_OF_WEEK
ORDER BY total_trips DESC;


-- 3. Average distance by hour
SELECT
    HOUR,
    ROUND(AVG(MILES), 2) AS average_miles
FROM uber_trips
GROUP BY HOUR
ORDER BY HOUR;