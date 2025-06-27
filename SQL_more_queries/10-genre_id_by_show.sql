-- Genre ID by show

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
