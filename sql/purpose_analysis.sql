USE uber_analytics;

-- 1. Trips by purpose
SELECT
    PURPOSE,
    COUNT(*) AS total_trips
FROM uber_trips
GROUP BY PURPOSE
ORDER BY total_trips DESC;


-- 2. Percentage of trips by purpose
SELECT
    PURPOSE,
    COUNT(*) AS total_trips,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM uber_trips),
        2
    ) AS percentage
FROM uber_trips
GROUP BY PURPOSE
ORDER BY total_trips DESC;


-- 3. Distance analysis by purpose
SELECT
    PURPOSE,
    COUNT(*) AS total_trips,
    ROUND(SUM(MILES), 2) AS total_miles,
    ROUND(AVG(MILES), 2) AS average_miles
FROM uber_trips
GROUP BY PURPOSE
ORDER BY total_trips DESC;