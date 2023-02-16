0x0E. SQL - More queries

0. My privileges!
script that lists all privileges of the MySQL users user-_0d-_1 and user-_0d-_2 on your server (in localhost)

1. Root user
script that creates the MySQL server user user-_0d-_1
user-_0d-_1 should have all privileges on your MySQL server
The user-_0d-_1 password should be set to user-_0d_-1-_pwd
If the user user-_0d-_1 already exists, your script should not fail

2. Read user
script that creates the database hbtn-0d-2 and the user user-0d-2.

user-0d-2 should have only SELECT privilege in the database hbtn-0d-2
The user-0d-2 password should be set to user-0d-2-pwd
If the database hbtn-0d-2 already exists, your script should not fail
If the user user-0d-2 already exists, your script should not fail

3. Always a name
script that creates the table force-name on your MySQL server.

force-name description:
id INT
name VARCHAR(256) can’t be null
The database name will be passed as an argument of the mysql command
If the table force-name already exists, your script should not fail

4. ID can't be null
script that creates the table id-not-null 
id INT with the default value 1
name VARCHAR(256)
if already exists, your script should not fail

5. Unique ID
script that creates the table unique-id
description:
id INT with the default value 1 and must be unique
name VARCHAR(256)
already exists, your script should not fail

6. States table
creates the database hbtn-0d-usa and the table states
description:
id INT unique, auto generated, can’t be null and is a primary key
name VARCHAR(256) can’t be null

7. Cities table
creates the database hbtn-od-usa and table cities
 description:
id INT unique, auto generated, can’t be null and is a primary key
state-id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
name VARCHAR(256) can’t be null

8. Cities of California
lists all the cities of California that can be found in the database
The states table contains only one record where name = California
Results must be sorted in ascending order by cities.id

9. Cities by States
lists all cities contained in the database
Each record should display: cities.id - cities.name - states.name
Results must be sorted in ascending order by cities.id
You can use only one SELECT statement

10. Genre ID by show
Import the database dump from hbtn-0d-tvshows to your MySQL server:
script that lists all shows contained in hbtn-0d-tvshows that have at least one genre linked
Each record should display: tv-shows.title - tv-show-genres.genre-id
Results must be sorted in ascending order by tv-shows.title and tv-show-genre.genre-id

11. Genre ID for all shows
Import the database dump of hbtn-0d-tvshows to your MySQL server
script that lists all shows contained in the database hbtn-0d-tvshows
Each record should display: tv-show.title - tv-show-genres-id
Results must be sorted in ascending order by tv-show.title, tv-show-genres-id
If a show doesn’t have a genre, display NULL

12. No genre
Import the database dump of hbtn-0d-tvshows to your MySQL server
script that lists all genres contained in the database hbtn-0d-tvshows without a genre linked
Each record should display: tv-show.title - tv-show-genres-id
Results must be sorted in ascending order by tv-show.title, tv-show-genres-id

13. Number of shows by genre
Import the database dump of hbtn-0d-tvshows to your MySQL server
script that lists all genres contained in the database hbtn-0d-tvshows and the no of shows
Each record should display: <TV Show genre> - <Number of shows linked to this genre>
First column must be called genre
Second column must be called number-of-shows
Don’t display a genre that doesn’t have any shows linked
Results must be sorted in descending order by the number of shows linked

14. My genres
Import the database dump of hbtn-0d-tvshows to your MySQL server
script that uses hbtn-0d-tvshows database to list all genres of the show Dexter 
the t-show table contains only one record where title = Dexter
Each record should display: tv-genres.name
Results must be sorted in ascending order by the genre name


