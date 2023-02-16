-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT t.title AS title, SUM(rate) AS rating FROM tv_shows t INNER JOIN tv_show_ratings r ON t.id = r.show_id GROUP BY t.title ORDER BY rating DESC;
