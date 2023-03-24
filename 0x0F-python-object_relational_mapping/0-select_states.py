#!/usr/bin/python3
# list all states from the database hbtn_0e_0_usa
# take 3 arquments ie mysql username, mysql password and database name
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], 
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM  states ORDER BY states.id")
    results = c.fetchall()
    for state in results:
        print(state)
    c.close()
    db.close()
