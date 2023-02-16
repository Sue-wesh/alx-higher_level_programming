-- displays the number of shows linked to each genre
SELECT g.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres g INNER JOIN tv_show_genres t ON g.id = t.genre_id GROUP BY g.name ORDER BY number_of_shows DESC; 
