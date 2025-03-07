-- genre id by show

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
