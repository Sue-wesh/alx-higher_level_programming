-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT t.title AS title, g.genre_id AS genre_id FROM tv_shows t INNER JOIN tv_show_genres g ON t.id=g.show_id  ORDER BY t.title, g.genre_id
