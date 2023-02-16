-- lists all shows and genres linked to that showin DB btn_0d_tvshow
SELECT t.title AS title, g.name AS name FROM tv_shows t LEFT JOIN tv_show_genres s ON t.id = s.show_id LEFT JOIN tv_genres g ON s.genre_id = g.id ORDER BY t.title, g.name;
