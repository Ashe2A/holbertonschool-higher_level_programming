-- Number of shows by genre:
SELECT tvg.name AS genre, COUNT(tvs.id) AS number_of_shows
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tvsg ON tvg.id = tvsg.genre_id
INNER JOIN tv_shows AS tvs ON tvsg.show_id = tvs.id
GROUP BY genre
ORDER BY number_of_shows DESC;
