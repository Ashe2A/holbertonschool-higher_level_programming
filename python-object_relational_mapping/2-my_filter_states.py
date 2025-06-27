#!/usr/bin/python3
"""Filter states by user input"""

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
    c.execute("SELECT * FROM states WHERE BINARY states.name = \"{}\"\
ORDER BY states.id;".format(argv[4]))
    for i in c.fetchall():
        print("{}".format(i))

    c.close()
    db.close()
