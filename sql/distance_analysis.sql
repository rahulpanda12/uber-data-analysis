USE uber_analytics;

-- 1. Distance statistics by category
SELECT
    CATEGORY,
    COUNT(*) AS total_trips,
    ROUND(SUM(MILES), 2) AS total_miles,
    ROUND(AVG(MILES), 2) AS average_miles
FROM uber_trips
GROUP BY CATEGORY
ORDER BY total_miles DESC;


-- 2. Trips by distance type
SELECT
    DISTANCE_TYPE,
    COUNT(*) AS total_trips,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM uber_trips), 2) AS percentage
FROM uber_trips
GROUP BY DISTANCE_TYPE
ORDER BY total_trips DESC;


-- 3. Overall distance statistics
SELECT
    COUNT(*) AS total_trips,
    ROUND(SUM(MILES), 2) AS total_miles,
    ROUND(AVG(MILES), 2) AS average_miles,
    ROUND(MIN(MILES), 2) AS minimum_miles,
    ROUND(MAX(MILES), 2) AS maximum_miles
FROM uber_trips;