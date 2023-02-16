-- list all shows without genre Comedy
SELECT DISTINCT title FROM tv_shows t LEFT JOIN tv_show_genres s ON s.show_id = t.id LEFT JOIN tv_genres g ON g.id = s.genre_id WHERE t.title NOT IN (SELECT title FROM tv_shows t INNER JOIN tv_show_genres s ON s.show_id = t.id INNER JOIN tv_genres g ON g.id = s.genre_id WHERE g.name = "Comedy") ORDER BY title;
