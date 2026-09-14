USE uber_analytics;

-- 1. Top 10 start locations
SELECT
    START_LOCATION,
    COUNT(*) AS start_count
FROM uber_trips
GROUP BY START_LOCATION
ORDER BY start_count DESC
LIMIT 10;


-- 2. Top 10 stop locations
SELECT
    STOP_LOCATION,
    COUNT(*) AS stop_count
FROM uber_trips
GROUP BY STOP_LOCATION
ORDER BY stop_count DESC
LIMIT 10;


-- 3. Top locations by total activity
SELECT
    LOCATION,
    start_count,
    stop_count,
    (start_count + stop_count) AS total_activity
FROM (
    SELECT
        LOCATION,
        SUM(start_count) AS start_count,
        SUM(stop_count) AS stop_count
    FROM (
        SELECT
            START_LOCATION AS LOCATION,
            COUNT(*) AS start_count,
            0 AS stop_count
        FROM uber_trips
        GROUP BY START_LOCATION

        UNION ALL

        SELECT
            STOP_LOCATION AS LOCATION,
            0 AS start_count,
            COUNT(*) AS stop_count
        FROM uber_trips
        GROUP BY STOP_LOCATION
    ) AS location_data
    GROUP BY LOCATION
) AS location_summary
ORDER BY total_activity DESC
LIMIT 10;


-- 4. Most common known routes
SELECT
    START_LOCATION,
    STOP_LOCATION,
    COUNT(*) AS trip_count
FROM uber_trips
WHERE START_LOCATION <> 'Unknown Location'
  AND STOP_LOCATION <> 'Unknown Location'
GROUP BY START_LOCATION, STOP_LOCATION
ORDER BY trip_count DESC
LIMIT 10;