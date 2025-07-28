-- Last updated: 7/28/2025, 12:51:24 PM
# Write your MySQL query statement below
SELECT * FROM Cinema WHERE (id%2 != 0) AND description NOT LIKE "Boring" ORDER BY rating DESC;