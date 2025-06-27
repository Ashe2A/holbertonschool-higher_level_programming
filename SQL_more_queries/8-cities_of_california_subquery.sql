-- Cities by States

USE hbtn_0d_usa;

SELECT cities.id AS id, cities.name AS name
FROM cities, states
WHERE states.name = "California"
ORDER BY cities.id;
