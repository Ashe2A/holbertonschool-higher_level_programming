-- Select the best:
SELECT st.score, st.name
FROM second_table AS st
WHERE st.score >= 10
ORDER BY st.score DESC;
