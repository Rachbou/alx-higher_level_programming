-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.
SELECT DISTINCT name FROM tv_genres AS genre
INNER JOIN tv_show_genres AS s ON genre.id = s.genre_id
INNER JOIN tv_shows AS t ON s.show_id = t.id
WHERE genre.name NOT IN (SELECT name FROM tv_genres AS genre
INNER JOIN tv_show_genres AS s ON genre.id = s.genre_id
INNER JOIN tv_shows AS t ON s.show_id = t.id
WHERE t.title = "Dexter")
ORDER BY genre.name;
