-- list all genres and display number of shows linked to each other.
SELECT tv_genres.name AS genre, COUNT(show_id) AS number_shows
FROM tv_genres 
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;
