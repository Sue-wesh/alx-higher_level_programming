#!/usr/bin/python3
"""
list all cities of a certain state from the database hbtn_0e_4_usa
"""
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    db = connect(user=argv[1], passwd=argv[2],
                 db=argv[3], host="localhost", port=3306)
    c = db.cursor()
    state = argv[4]
    search = "SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC"
    c.execute(search, (state,))
    reslt = c.fetchall()
    print(', '.join([city[0] for city in reslt]))

    c.close()
    db.close()
