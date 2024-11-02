-- Say my name:
SELECT st.score, st.name
FROM second_table AS st
WHERE st.name IS NOT NULL
ORDER BY st.score DESC;
