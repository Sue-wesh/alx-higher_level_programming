#!/usr/bin/python3
"""
list of all states with a name starting with N from the database
takes 3 arguments mysql username, mysql password and database name
"""
from sys import argv
from MySQLdb import connect

if __name__ == "__main__":
    db = connect(user=argv[1], passwd=argv[2],
                 db=argv[3], host="localhost", port=3306)
    query = db.cursor()
    query.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    for state in query.fetchall():
        print(state)

    c.close()
    db.close()
