#!/usr/bin/python3
"""Filter states"""

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
        if i[1][0] == "N":
            print(i)

    c.close()
    db.close()
