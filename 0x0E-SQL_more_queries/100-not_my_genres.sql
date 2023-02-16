-- list genres not linked to show Dexter
SELECT name FROM tv_genres g INNER JOIN tv_show_genres s ON g.id = s.genre_id INNER JOIN tv_shows t ON s.show_id = t.id WHERE g.name NOT IN (SELECT name FROM tv_genres AS g INNER JOIN tv_show_genres AS s ON g.id = s.genre_id INNER JOIN tv_shows AS t ON s.show_id = t.id WHERE t.title = "Dexter") ORDER BY g.name;
