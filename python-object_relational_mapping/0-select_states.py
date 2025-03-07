#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    server = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    c = server.cursor()
    numrows = c.execute("SELECT * FROM states ORDER BY states.id;")

    print(i for i in range(numrows))
    c.close()
    server.close()
