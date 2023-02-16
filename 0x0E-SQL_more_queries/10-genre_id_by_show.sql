-- list all shows contained in hbtn_0d_tvshows with at least one genre linked
SELECT t.title AS title, g.genre_id AS genre_id FROM tv_shows t INNER JOIN tv_show_genres g ON t.id=g.show_id  ORDER BY t.title, g.genre_id
