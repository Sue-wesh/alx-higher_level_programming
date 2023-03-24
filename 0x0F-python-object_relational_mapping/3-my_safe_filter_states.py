#!/usr/bin/python3
"""
display all values in the states table where name 
matches the argument and is safe from MySQL injections
takes 4 arguments <mysql username> \
                  <mysql password> \
                  <database name> \
                  <state name searched>
"""
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    db = connect(user=argv[1], passwd=argv[2], 
                 db=argv[3], host="localhost", port=3306)
    query = db.cursor()
    state = argv[4]
    search = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    query.execute(search, [state])
    [print(state) for state in query.fetchall()]
    
    query.close()
    db.close()
