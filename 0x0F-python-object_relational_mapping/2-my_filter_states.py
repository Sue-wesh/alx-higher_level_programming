#!/usr/bin/python3
# display all values in the states table where name matches the argument
# takes 4 arguments <mysql username> \
#                   <mysql password> \
#                   <database name> \
#                   <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    state_name = sys.argv[4]
    search = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
    search = search.format(state_name)
    c.execute(search)
    [print(state) for state in c.fetchall()]
