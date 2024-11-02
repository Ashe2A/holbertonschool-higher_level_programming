-- My genres:
SELECT tvg.name
FROM tv_genres AS tvg
INNER JOIN tv_show_genres AS tvsg ON tvg.id = tvsg.genre_id
INNER JOIN tv_shows AS tvs ON tvsg.show_id = tvs.id
WHERE tvs.title = "Dexter"
ORDER BY tvg.name;
