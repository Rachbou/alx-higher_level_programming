-- Lists all genres in the database hbtn_0d_tvshows_rate by their ratingenre.
-- Records are ordered by descending ratingenre.
SELECT name, SUM(rate) AS rating FROM tv_genres AS genre
INNER JOIN tv_show_genres AS show ON show.genre_id = genre.id
INNER JOIN tv_show_ratings AS r ON r.show_id = show.show_id
GROUP BY name
ORDER BY rating DESC;
