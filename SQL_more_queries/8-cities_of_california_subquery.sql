-- Cities by States

USE hbtn_0d_usa;

SELECT cities.id AS id, cities.name AS name
FROM cities, states
WHERE cities.state_id = state.id AND states.name = "California"
ORDER BY cities.id;
