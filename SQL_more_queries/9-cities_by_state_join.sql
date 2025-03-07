-- cities by state join query

SELECT c.id AS id, c.name AS name, states.name AS name
FROM cities AS c
INNER JOIN states ON c.state_id = states.id
ORDER BY c.id
