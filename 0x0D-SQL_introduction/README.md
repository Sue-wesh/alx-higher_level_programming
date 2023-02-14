0x0D. SQL - Introduction

0. List databases
script that lists all databases of your MySQL server

1. Create a database
script that creates the database hbtn-0c-0 in your MySQL server.

If the database hbtn-0c-0 already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

2. Delete a database
delete database hbtn-0c-0
if it doesn’t exist, your script should not fail

3. List tables
script that lists all the tables of a database in your MySQL server

4. First table
script that creates a table called first-table in the current database in your MySQL server.
first-table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table first-table already exists, your script should not fail

5. Full description
script that prints the full description of the table first-table from the database hbtn-0c-0 in your MySQL server

6. List all in table
all rows of the table first-table
All fields should be printed

7. First add
insert a a new row in the table first-table

8. Count 89
number of records with id = 89 in the table first-table

9. Full creation
create a table second-_table in the database hbtn-_0c-_0
If the table second_table already exists, your script should not fail

10. List by best
script that lists all records of the table second-table
Results should display both the score and the name (in this order)
Records should be ordered by score (top first)

11. Select the best
script that lists all records with a score >= 10 in the table secondtable

12. Cheating is bad
script that updates the score of Bob to 10 in the table secondtable

13. Score too low
script that removes all records with a score <= 5 in the table second_-table

14. Average
script that computes the score average of all records in the table

15. Number by score
script that lists the number of records with the same score in the table

16. Say my name
script that lists all records of the table

17. Go to UTF8
script that converts hbtn-0c-0 database to UTF8
You need to convert all of the following to UTF8:

Database  hbtn-0c-0
Table first-table
field name in first-table

18. Temperatures #0
Import in hbtn-0c-0 database this table dump: download

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

19. Temperatures #1
Import in hbtn-0c-0 database this table dump: download (same as Temperatures #0)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

20. Temperatures #2
Import in hbtn-0c-0 database this table dump: download (same as Temperatures #0)

Write a script that displays the max temperature of each state (ordered by State name)
