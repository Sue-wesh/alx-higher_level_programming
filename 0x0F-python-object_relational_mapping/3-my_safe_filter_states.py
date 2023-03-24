#!/usr/bin/python3
# display all values in the states table where name 
# matches the argument and is safe from MySQL injections
# takes 4 arguments <mysql username> \
#                   <mysql password> \
#                   <database name> \
#                   <state name searched>
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], 
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    query = db.cursor()
    state = sys.argv[4]
    search = "SELECT * FROM states WHERE name='{}' ORDER BY states.id ASC".format(state)
    query.execute(search)
    [print(state) for state in query.fetchall()]
    
    query.close()
    db.close()
