-- Last updated: 7/28/2025, 12:51:20 PM
# Write your MySQL query statement below
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years FROM Project 
    INNER JOIN Employee ON Project.employee_id = Employee.employee_id
    GROUP BY Project_id;