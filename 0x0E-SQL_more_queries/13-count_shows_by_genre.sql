-- list all genres and display number of shows linked to each other.
-- first column must be genre
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
