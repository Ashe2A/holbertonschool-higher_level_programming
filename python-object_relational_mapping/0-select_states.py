#!/usr/bin/python3
"""Get all states"""

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
    c.execute("SELECT * FROM states ORDER BY states.id;")
    for i in c.fetchall():
        print(i)

    c.close()
    db.close()
