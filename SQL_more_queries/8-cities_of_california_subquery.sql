-- Cities of California:
SELECT c.*
FROM states AS s, cities AS c
WHERE c.state_id = s.id AND s.name = "California"
ORDER BY c.id;
