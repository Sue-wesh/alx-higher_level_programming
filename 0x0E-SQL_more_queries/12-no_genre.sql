-- list all shows without a genre
SELECT t.title AS title, g.genre_id AS genre_id FROM tv_shows t LEFT JOIN tv_show_genres g ON t.id = g.show_id WHERe g.genre_id IS NULL ORDER BY t.title, g.genre_id;
