-- lists all genres of the show Dexter
SELECT g.name FROM tv_genres g INNER JOIN tv_show_genres AS s ON g.id = s.genre_id INNER JOIN tv_shows t ON t.id = s.show_id WHERE t.title = "Dexter" ORDER BY g.name;
