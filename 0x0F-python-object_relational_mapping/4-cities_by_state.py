#!/usr/bin/python3
# list all cities from the database hbtn_0e_4_usa
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3], host="localhost", port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `c`.`id`, `c`.`name`, `s`.`name` FROM `cities` AS `c` INNER JOIN `states` AS `s` ON `c`.`state_id` = `s`.`id` ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
