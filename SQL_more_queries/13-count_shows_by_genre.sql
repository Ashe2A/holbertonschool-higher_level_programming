-- no genre

SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.id) AS number_of_shows
FROM tv_show_genres
RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY number_of_shows DESC;
