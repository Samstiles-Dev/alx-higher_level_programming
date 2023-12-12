-- Script that shows the max temperature of each state
-- Query to shows the max temp of each state

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC
LIMIT 3;
