-- Cities of California:
SELECT c.id, c.name
FROM (
    SELECT *
    FROM states AS s
    WHERE s.name = "California"
    ) AS s, cities AS c
WHERE c.state_id = s.id
ORDER BY c.id;
