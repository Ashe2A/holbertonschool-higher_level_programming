#!/usr/bin/python3
"""Cities by states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
        )

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
        FROM cities\
        INNER JOIN states ON states.id = cities.state_id\
        ORDER BY cities.id;")
    for i in c.fetchall():
        print(i)

    c.close()
    db.close()
