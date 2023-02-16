-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT g.name AS name, SUM(rate) AS rating FROM tv_genres g INNER JOIN tv_show_genres s ON s.genre_id = g.id INNER JOIN tv_show_ratings r ON r.show_id = s.show_id GROUP BY g.name ORDER BY rating DESC;
