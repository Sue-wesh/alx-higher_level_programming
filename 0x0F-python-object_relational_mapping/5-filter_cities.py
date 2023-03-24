#!/usr/bin/python3
# list all cities of a certain state from the database hbtn_0e_4_usa
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    [print(city) for city in c.fetchall()]

    c.close()
    db.close()
