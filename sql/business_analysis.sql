USE uber_analytics;

-- 1. Trips by category
SELECT
    CATEGORY,
    COUNT(*) AS total_trips
FROM uber_trips
GROUP BY CATEGORY
ORDER BY total_trips DESC;


-- 2. Percentage of trips by category
SELECT
    CATEGORY,
    COUNT(*) AS total_trips,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM uber_trips),
        2
    ) AS percentage
FROM uber_trips
GROUP BY CATEGORY
ORDER BY total_trips DESC;