-- Last updated: 11/06/2026, 21:31:33
# Write your MySQL query statement below
SELECT 
    e.name AS Employee
FROM 
    Employee e
JOIN 
    Employee m ON e.managerId = m.id
WHERE 
    e.salary > m.salary;