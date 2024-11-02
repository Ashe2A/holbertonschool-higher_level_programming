-- Cheating is bad:
UPDATE second_table AS st
SET st.score = 10
WHERE st.name = "Bob";
