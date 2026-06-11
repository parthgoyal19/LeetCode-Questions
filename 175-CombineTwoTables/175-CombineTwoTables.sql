-- Last updated: 11/06/2026, 21:31:35
# Write your MySQL query statement below
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM 
    Person p
LEFT JOIN 
    Address a ON p.personId = a.personId;