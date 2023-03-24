#!/usr/bin/python3
"""
list all cities from the database hbtn_0e_4_usa
"""
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    db = connect(user=argv[1], passwd=argv[2],
                 db=argv[3], host="localhost", port=3306)
    c = db.cursor()
    search = "SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states
    ON cities.states_id = states.id
    ORDER BY cities.id ASC"
    c.execute(search)
    for city in c.fetchall():
        print(city)

    c.close()
    db.close()
