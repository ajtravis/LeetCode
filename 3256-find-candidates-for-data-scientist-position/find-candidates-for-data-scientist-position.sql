# Write your MySQL query statement below
SELECT candidate_id FROM Candidates
GROUP BY candidate_id
HAVING SUM(skill='Python' OR skill='Tableau' OR skill='PostgreSQL')=3
ORDER BY candidate_id;