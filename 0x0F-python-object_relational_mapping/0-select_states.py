#!/usr/bin/python3
""" 
list all states from the database hbtn_0e_0_usa
take 3 arquments ie mysql username, mysql password and database name
"""
from sys import argv
from MySQLdb import connect

if __name__ == "__main__":
    db = connect(user=argv[1], passwd=argv[2], 
                 db=argv[3], host="localhost", port=3306)
    query = db.cursor()
    query.execute("SELECT * FROM  states ORDER BY states.id")
    results = query.fetchall()
    for state in results:
        print(state)
    query.close()
    db.close()
