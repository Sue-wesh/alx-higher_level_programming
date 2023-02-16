-- lists all Comedy shows in the database hbtn_0d_tvshow
SELECT tv_shows.title AS title FROM tv_shows INNER JOIN tv_show_genres s ON tv_shows.id = s.show_id INNER JOIN tv_genres g ON g.id = s.genre_id WHERE g.name = "Comedy" ORDER BY tv_shows.title;
