#!/usr/bin/python3
# list of all states with a name starting with N from the database
# takes 3 arguments mysql username, mysql password and database name
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3], host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
