-- Number by score:
SELECT st.score, COUNT(*) AS number
FROM second_table AS st
GROUP BY st.score
ORDER BY number DESC;
