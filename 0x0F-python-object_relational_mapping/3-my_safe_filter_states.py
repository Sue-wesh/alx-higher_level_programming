#!/usr/bin/python3
# display all values in the states table where name 
# matches the argument and is safe from MySQL injections
# takes 4 arguments <mysql username> \
#                   <mysql password> \
#                   <database name> \
#                   <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
