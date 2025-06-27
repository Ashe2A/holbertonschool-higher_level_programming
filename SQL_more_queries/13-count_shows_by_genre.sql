-- Number of shows by genre

SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY number_of_shows DESC;
